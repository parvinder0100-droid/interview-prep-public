---
type: topic
topic: JVM & Garbage Collection
updated: 2026-07-10
status: not-started
---

# JVM Internals & Garbage Collection

## Subtopics

- JVM memory areas: heap (young/old gen), stack, metaspace, PC registers.
- Class loading: classloaders, linking, initialization order.
- Garbage collectors: Serial, Parallel, CMS, G1, ZGC — trade-offs and when each is used.
- GC mechanics: mark-sweep-compact, generational hypothesis, minor vs major/full GC.
- Memory leaks in Java despite GC (listener leaks, static references, ThreadLocal misuse).
- Reference types: strong, soft, weak, phantom — and their GC implications.
- JIT compilation basics, bytecode, `javap`/`jstack`/`jmap` awareness (conceptual).

## Problems/Questions Log

_Populated as topics are actually practiced/quizzed._

## Common Mistakes Seen in This Topic

_None yet — see [../mistakes/mistake_journal.md](../mistakes/mistake_journal.md)._
