#!/usr/bin/env python3
"""Local semantic search over the InterviewPrep markdown tracker.

Everything runs offline on CPU after the first model download:
  - sentence-transformers loads a small Hugging Face embedding model
  - chunks are embedded once and cached in .embcache/ (incremental by mtime)
  - search is a cosine similarity over a numpy matrix (no vector DB needed
    at this corpus size: ~135 files / ~90k words)

Usage:
    python tools/semantic_search.py "why did merge intervals need a hint"
    python tools/semantic_search.py -k 10 --path DSA "monotonic stack"
    python tools/semantic_search.py --rebuild            # force re-embed all
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".embcache"
VEC_FILE = CACHE_DIR / "vectors.npy"
META_FILE = CACHE_DIR / "chunks.json"

# Small, fast, strong on retrieval. 384-dim, ~130MB.
MODEL_NAME = "BAAI/bge-small-en-v1.5"
# bge models are trained with an asymmetric query prefix; passages get none.
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

MAX_CHARS = 1200  # a section longer than this gets split
OVERLAP = 150

SKIP_DIRS = {".git", "__pycache__", ".embcache", "Archive", "node_modules"}


@dataclass
class Chunk:
    path: str  # repo-relative
    line: int  # 1-indexed start line
    heading: str  # breadcrumb of enclosing headings
    text: str
    mtime: float


def iter_markdown() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        out.append(p)
    return sorted(out)


def split_sections(path: Path) -> list[Chunk]:
    """Split a markdown file on ATX headings, keeping a heading breadcrumb."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    mtime = path.stat().st_mtime
    rel = str(path.relative_to(ROOT))

    stack: list[tuple[int, str]] = []  # (level, title)
    buf: list[str] = []
    buf_start = 1
    chunks: list[Chunk] = []

    def breadcrumb() -> str:
        return " > ".join(t for _, t in stack)

    def flush(crumb: str, start: int):
        body = "\n".join(buf).strip()
        if body:
            chunks.extend(_window(rel, start, crumb, body, mtime))
        buf.clear()

    for i, line in enumerate(lines, start=1):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush(breadcrumb(), buf_start)
            level, title = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            buf_start = i
        else:
            buf.append(line)

    flush(breadcrumb(), buf_start)
    return chunks


def _window(rel: str, start: int, crumb: str, body: str, mtime: float) -> list[Chunk]:
    """Sliding-window a long section so no single chunk blows past the model."""
    header = f"{rel} :: {crumb}\n" if crumb else f"{rel}\n"
    if len(body) <= MAX_CHARS:
        return [Chunk(rel, start, crumb, header + body, mtime)]

    out, pos = [], 0
    while pos < len(body):
        piece = body[pos : pos + MAX_CHARS]
        # approximate line offset so the reported line stays useful
        line_off = body[:pos].count("\n")
        out.append(Chunk(rel, start + line_off, crumb, header + piece, mtime))
        pos += MAX_CHARS - OVERLAP
    return out


def load_cache() -> tuple[np.ndarray | None, list[Chunk]]:
    if not VEC_FILE.exists() or not META_FILE.exists():
        return None, []
    vecs = np.load(VEC_FILE)
    meta = [Chunk(**d) for d in json.loads(META_FILE.read_text())]
    if len(meta) != vecs.shape[0]:
        return None, []  # cache torn; rebuild
    return vecs, meta


def save_cache(vecs: np.ndarray, chunks: list[Chunk]) -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    np.save(VEC_FILE, vecs)
    META_FILE.write_text(json.dumps([asdict(c) for c in chunks]))


def get_model():
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        sys.exit(
            "sentence-transformers not installed. Run:\n"
            "  python3 -m venv .venv && .venv/bin/pip install "
            "sentence-transformers"
        )
    return SentenceTransformer(MODEL_NAME)


def build_index(rebuild: bool = False) -> tuple[np.ndarray, list[Chunk]]:
    wanted: list[Chunk] = []
    for p in iter_markdown():
        wanted.extend(split_sections(p))

    old_vecs, old_chunks = (None, []) if rebuild else load_cache()
    # key a cached vector to its exact text + mtime, so an edited file re-embeds
    old_by_key = {}
    if old_vecs is not None:
        for vec, ch in zip(old_vecs, old_chunks):
            old_by_key[_key(ch)] = vec

    reuse = [old_by_key.get(_key(c)) for c in wanted]
    todo = [i for i, v in enumerate(reuse) if v is None]

    if todo:
        model = get_model()
        print(f"embedding {len(todo)} new/changed chunks "
              f"({len(wanted) - len(todo)} reused)...", file=sys.stderr)
        fresh = model.encode(
            [wanted[i].text for i in todo],
            batch_size=32,
            normalize_embeddings=True,
            show_progress_bar=len(todo) > 200,
        )
        for slot, vec in zip(todo, fresh):
            reuse[slot] = vec
    else:
        print(f"index up to date ({len(wanted)} chunks)", file=sys.stderr)

    vecs = np.vstack(reuse).astype("float32")
    save_cache(vecs, wanted)
    return vecs, wanted


def _key(c: Chunk) -> str:
    h = hashlib.sha1(c.text.encode()).hexdigest()[:16]
    return f"{c.path}:{c.mtime}:{h}"


def search(query: str, k: int, path_filter: str | None, rebuild: bool) -> None:
    vecs, chunks = build_index(rebuild)
    model = get_model()
    qv = model.encode([QUERY_PREFIX + query], normalize_embeddings=True)[0]

    scores = vecs @ qv  # both normalized -> cosine similarity

    if path_filter:
        mask = np.array([path_filter.lower() in c.path.lower() for c in chunks])
        scores = np.where(mask, scores, -1.0)

    top = np.argsort(-scores)[:k]
    for rank, i in enumerate(top, 1):
        if scores[i] < 0:
            break
        c = chunks[i]
        crumb = f"  [{c.heading}]" if c.heading else ""
        body = c.text.split("\n", 1)[1] if "\n" in c.text else c.text
        snippet = " ".join(body.split())[:220]
        print(f"\n{rank}. {scores[i]:.3f}  {c.path}:{c.line}{crumb}")
        print(f"   {snippet}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="*", help="natural-language query")
    ap.add_argument("-k", type=int, default=5, help="results to show")
    ap.add_argument("--path", help="only match files whose path contains this")
    ap.add_argument("--rebuild", action="store_true", help="re-embed everything")
    args = ap.parse_args()

    if not args.query:
        build_index(rebuild=args.rebuild)
        return
    search(" ".join(args.query), args.k, args.path, args.rebuild)


if __name__ == "__main__":
    main()
