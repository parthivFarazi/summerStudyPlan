# Mistake Database

> Append-only registry of mistakes with root-cause analysis. Same root cause again ⇒ increment recurrence. **Recurrence ≥ 3 ⇒ escalate to `BLOCKERS.md`** (drill now). Mistakes are never deleted — they are data. Status: active / dormant (≥30d clean).

**Format:** `M-NNN | date | type | what happened | root cause | recurrence | sessions | status`
**Type:** `impl` (implementation/syntax) · `strategy` (wrong/unrecognized pattern, complexity, spec-reading).

## Mistakes

| ID | Date | Type | What happened | Root cause | Recur | Sessions | Status |
|---|---|---|---|---|---|---|---|
| M-001 | 2026-06-22 | impl | Wrote the logic but forgot to `return` the value | Conflating *computing* a value with *returning* it (`return` vs `print`) | 2 | Day 4, Day 6 | active |
| M-002 | 2026-06-24 | impl | `.append[x]` with brackets instead of `.append(x)` | Method **calls** use `()`; `[]` is indexing | 2 | Day 5, Day 8 | active |
| M-003 | 2026-06-19 | impl | `range(x)` instead of `range(len(x))` when looping indexes | Iterating the value vs the index range | 2 | Day 1, Day 4 | active |
| M-004 | 2026-06-19 | impl | Called `nums.add(...)` instead of `seen.add(...)` | Losing track of which container holds what | 1 | Day 1 | active |
| M-005 | 2026-06-24 | strategy | Called Valid Palindrome O(1) space while building a cleaned string | A new structure that scales with input = **O(n) space** | 1 | Day 5 | active |
| M-006 | 2026-06-20 | strategy | Called Group Anagrams O(n) — missed the hidden `sorted()` | Not counting the cost of operations *inside* the loop | 2 | Day 3, Day 8 | active |
| M-007 | 2026-06-26 | strategy | Over-engineered sliding window (4 vars + time guards, buggy) | Not reducing to the **minimum necessary state** | 1 | Day 7 | active |
| M-008 | 2026-06-26 | strategy | Jumped to code; used `i`/`j`; skipped naming the approach | Coding before verbalizing the pattern | 1 | Day 6 | active |
| M-009 | 2026-06-28 | strategy | Imported `k log k` from Group Anagrams into Longest Substring (no sort) | Carrying complexity assumptions across problems without re-deriving | 1 | Day 8 | active |
| M-010 | 2026-06-28 | strategy | Missed "alphanumeric only" in the spec = real work to do | Under-reading the problem statement / examples | 1 | Day 8 | active |
| M-011 | 2026-06-26 | impl | Dropped the anagram length check (then re-added) | Incomplete validation in a warm-up re-solve | 1 | Day 7 | active |

## Recurrence Watchlist (count ≥ 2 — one rep from escalating)

| ID | Type | Root cause | Count |
|---|---|---|---|
| M-001 | impl | Forgetting `return` | 2 |
| M-002 | impl | `()` call vs `[]` index | 2 |
| M-003 | impl | `range(len(x))` for index loops | 2 |
| M-006 | strategy | Counting hidden in-loop cost in Big-O | 2 |

*Pre-empt these four at the start of each session — they're the ones about to become blockers.*
