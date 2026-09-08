---
type: topic
topic: Collections
updated: 2026-08-27
status: in-progress
---

# Collections Framework

## Subtopics

- Core interfaces: List, Set, Map, Queue/Deque — contracts and when to use each.
- Implementations: ArrayList vs LinkedList, HashMap vs TreeMap vs LinkedHashMap,
  HashSet vs TreeSet vs LinkedHashSet, ArrayDeque vs PriorityQueue.
- HashMap internals: hashing, buckets, treeification (Java 8+), load factor, resize.
- Iteration & fail-fast vs fail-safe iterators, ConcurrentModificationException.
- equals()/hashCode() contract and its effect on hash-based collections.
- Comparable vs Comparator, sorting collections.
- Immutable collections (List.of, Collections.unmodifiableList) and why they matter.
- Time/space complexity of common operations across implementations.

## Problems/Questions Log

_Populated as topics are actually practiced/quizzed._

## Common Mistakes Seen in This Topic

_None yet — see [../mistakes/mistake_journal.md](../mistakes/mistake_journal.md)._

## Log

- 2026-08-27 — **first live signal on this track in 49 days**, surfaced inside a
  DSA session (LC 84), not a Java block. Asked why `java.util.Stack` is
  discouraged: **unknown, answered "no idea"**, then requested the answer rather
  than take a hint.
  - `Stack extends Vector` — every method `synchronized`, so lock cost is paid on
    single-threaded `push`/`pop`/`peek`.
  - Its iterator walks **bottom-to-top** (Vector insertion order), the reverse of
    stack semantics — a real bug source.
  - JDK javadoc itself points to `Deque`. Use `Deque<Integer> s = new ArrayDeque<>()`
    — unsynchronized, array-backed, but rejects `null` elements.
  - Interview line: *"I'd use `ArrayDeque` over `Stack` — `Stack` extends `Vector`,
    so it's synchronized on every call and its iteration order is reversed."*
  - **Next on this track**: the legacy-vs-modern collection story more broadly
    (`Vector`/`Hashtable`/`Stack` vs `ArrayList`/`HashMap`/`ArrayDeque`), and
    `ArrayDeque` vs `LinkedList` as a `Deque`.
