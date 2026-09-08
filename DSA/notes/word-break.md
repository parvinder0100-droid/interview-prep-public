---
type: note
problem: Word Break (LC 139)
topic: Recursion / Backtracking + memoization
date: 2026-08-31
---

# LC 139 — Word Break

Accepted 2026-08-31, with-hints:5. Substituted for LC 131 on 2026-08-30 to test
the variable-length-piece move. It did bite — but not the way the 08-30 note
predicted.

## What actually blocked

Not string-index state, and not "choosing where a piece ends" either. The
opening algorithm was **greedy**: put the dictionary in a trie, walk the string,
take the first word that matches, advance. Two matches at index 0 ("cat" and
"cats") were noticed and the shorter one was committed to.

`"catsandog"` is a bad counterexample — greedy returns false and false is
correct. The one that works:

    s = "catsdog", wordDict = ["cat","cats","dog"]
    greedy: cat | "sdog" -> dead end -> false
    truth:  cats | dog -> true

Once that landed, "try all the combinations" came immediately. But the *first*
restatement of it silently reverted to greedy — "if it exists, move `start` to
`i+1`" — and needed one more pass over `"catsdog"` before the branch-and-continue
structure held.

## What was clean

- `f(start)` returns true if `s[start..]` can be segmented — stated cold.
- Base case `start == s.length()` -> true, justified cold: "empty string left,
  nothing to segment".
- **The memo went in unprompted**, which is why the exponential blowup that was
  flagged before coding never appeared.

## The two defects, both traced not told

    dfs(s, start, index)          both call sites pass (i+1, i+1)
                                  -> index is always == start, carries nothing

    top:      key = start + "-" + index      // always "k-k"
    success:  key = start + "-" + i          // REASSIGNED, i usually != start
              map.put(key, true)

Every `true` was stored under a key no lookup ever asks for. Only failures were
cached. Right answer, dead cache — **a cost bug**, and the user named it as such
unprompted, which is the same question shape as the Redundant Connection
`[leech]` item declined at the top of this session.

Rewrite: `Boolean[] cache = new Boolean[n]`, indexed by `start`. Drops the
parameter, the string concatenation per call, and the hashing.

## Complexity

`O(n³)` — n states, n split points each, and `s.substring(start,i+1)` plus its
hash costs `O(n)`. Space `O(n)` auxiliary (cache + recursion depth) plus
`O(sum of word lengths)` for the set; the dictionary term was volunteered.

## Open for review

1. Give an input where first-match-wins fails, cold, and name the line that
   prevents it.
2. Why is the mismatched memo key a cost bug and not a correctness bug?
