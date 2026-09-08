---
type: note
problem: Alien Dictionary (LC 269)
updated: 2026-09-05
---

Adjacent-word comparison for edges (first differing char gives an edge;
non-adjacent pairs are redundant since the list is already sorted, so
transitivity covers them), then Kahn's BFS over 26 letter-nodes.

**Approach recall**: named "topological sort" cold but couldn't rebuild the
edge-extraction step despite a prior "I've solved this before" claim — closed
via concrete instantiation (`"ba"` vs `"a"`) rather than re-explaining the
abstract rule.

**Bug 1 — cast precedence**: `sb.append((char)cur+'a')`. `(char)` is unary,
binds to `cur` alone — `((char)cur) + 'a'` is `char+char=int`, and
`StringBuilder.append(int)` writes the digits, not a letter. Fix:
`(char)(cur+'a')`.

**Bug 2 — prefix-check order**: `compareWords` checked `if(slen<flen) return
invalid` *before* scanning for a differing character. For `first="ba",
sec="a"`, this short-circuits to "invalid" even though index 0 differs
(`b` vs `a`), a real edge. The prefix-invalid case only applies when the scan
reaches the end of the shorter word with **no** difference found — the
length check has to run after the loop, not before it. Same family as
"abc"/"ab": a proper prefix appearing *after* the longer word is invalid, but
only when no differing character exists at all.

**Bug 3 — cycle-check counter**: `cntr` was incremented once per character
occurrence across all words (`for(char c: word.toCharArray()) cntr++`),
not once per distinct letter — so it almost never reached 0 even on valid,
acyclic input. Fix: count `indegree[i]==0` across the 26 slots *after* marking
present letters but *before* adding any edges — that's a clean snapshot of
distinct-letter count, independent of how many times each letter appears.
