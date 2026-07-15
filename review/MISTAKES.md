# Mistake Database

> Append-only registry of mistakes with root-cause analysis. Same root cause again ⇒ increment recurrence. **Recurrence ≥ 3 ⇒ escalate to `BLOCKERS.md`** (drill now). Mistakes are never deleted — they are data. Status: active / dormant (≥30d clean).

**Format:** `M-NNN | date | type | what happened | root cause | recurrence | sessions | status`
**Type:** `impl` (implementation/syntax) · `strategy` (wrong/unrecognized pattern, complexity, spec-reading).

## Mistakes

| ID | Date | Type | What happened | Root cause | Recur | Sessions | Status |
|---|---|---|---|---|---|---|---|
| M-001 | 2026-06-22 | impl | Forgot to `return` the value — Day 4/6, and `return prev` on #206 (Day 19) | Conflating *computing* a value with *returning* it | 3 | Day 4, Day 6, Day 19 | dormant (B-3 cleared Day 21) |
| M-002 | 2026-06-24 | impl | `.append[x]` with brackets instead of `.append(x)` | Method **calls** use `()`; `[]` is indexing | 2 | Day 5, Day 8 | active |
| M-003 | 2026-06-19 | impl | `range(x)` / `len(range(x))` instead of `range(len(x))` when looping indexes | Scrambling the `range(len(x))` index-loop idiom | 3 | Day 1, Day 4, Day 16 | dormant (B-2 cleared Day 18) |
| M-004 | 2026-06-19 | impl | Wrong variable/container — `nums.add`/`seen.add`, `s`/`clean`, `strs`/`s` (#125), `nums`/`numbers` (#167), `appened`/`append` (#238), `self.stack`/`self.minStack` (#155) | Variable-name imprecision — losing track of which name holds what | 5 | Day 1, Day 9, Day 11, Day 12, Day 14 | dormant (B-1 cleared Day 16) |
| M-005 | 2026-06-24 | strategy | Called O(1) space for something O(n) — cleaned string (#125), RPN stack (#150), sorted copy (#15) | A new structure that scales with input = **O(n) space**; a bounded one (≤26) or the returned output does NOT count | 2 | Day 5, Day 17 | active |
| M-006 | 2026-06-20 | strategy | Called Group Anagrams O(n) — missed the hidden `sorted()` | Not counting the cost of operations *inside* the loop | 2 | Day 3, Day 8 | active |
| M-007 | 2026-06-26 | strategy | Over-engineered sliding window (4 vars + time guards, buggy) | Not reducing to the **minimum necessary state** | 1 | Day 7 | active |
| M-008 | 2026-06-26 | strategy | Jumped to code; used `i`/`j`; skipped naming the approach | Coding before verbalizing the pattern | 1 | Day 6 | active |
| M-009 | 2026-06-28 | strategy | Imported `k log k` from Group Anagrams into Longest Substring (Day 8); **imported #21 Merge's VALUE comparison (`if curr1.val <= curr2.val`) into #143 Reorder, which forbids touching values (Day 23)** | Carrying a template's BODY across problems without re-deriving. Pattern recognition gives the skeleton, not the body — ask "what decides the next step IN THIS problem?" The spec tell: "may not modify values" ⇒ a value comparison is a red flag | 2 | Day 8, **Day 23** | active (watchlist) |
| M-010 | 2026-06-28 | strategy | Missed "alphanumeric only" in the spec = real work to do | Under-reading the problem statement / examples | 1 | Day 8 | active |
| M-011 | 2026-06-26 | impl | Dropped a required guard — anagram length check (Day 7, #242 Day 20, #242 Day 22); empty-stack guard #20 (Day 18) & #739 (Day 20); `node.left.val` no None-check (#226, Day 21). **Day 23: CLEAN ✅ — #242 length guard present, #141 guarded the single-node `None==None`** | Incomplete validation — keep the edge-case guard | 6 | Day 7, Day 18, Day 20, Day 21, Day 22 | **→ BLOCKER (B-4, 1 of 2 clean)** |
| M-012 | 2026-06-29 | strategy | Inverted search direction — moved toward the half that CANNOT contain the target; #704 (Day 9); #33 all four pointer updates (Day 13); #235 BST descent (Day 22); **#235 AGAIN, same inversion, next day (Day 23)** | Not re-deriving which side can still contain the target. **FIX (Day 23): write the comparison TARGET-first** — `target > node → right`, `target < node → left` — so the direction word matches and there's nothing to mentally flip. The flip is where the inversion happens | 4 | Day 9, Day 13, Day 22, **Day 23** | **→ BLOCKER (B-6)** |
| M-013 | 2026-06-30 | strategy | Returned on exact match (`hours == h`) in a find-minimum binary search → returned a non-minimal value | In boundary search an exact hit is still just a *candidate* — record it and keep shrinking | 1 | Day 10 | active |
| M-014 | 2026-07-01 | impl | Converging binary search with `while left <= right` + `right = mid` → infinite loop | `<=` never terminates when two pointers converge to one spot; use strict `<` | 1 | Day 11 | active |
| M-015 | 2026-07-02 | strategy | Converging binary search: tracked a separate `answer` instead of returning the convergence point → returned 0 on `[2,1]`/`[5]` (#153) and on Koko `h=5` when answer = max(piles) (#875) | In a converge-to-boundary search the loop-exit index IS the answer (`return left`); a tracked candidate/default leaks on edge cases | 2 | Day 12, Day 15 | active |
| M-016 | 2026-07-03 | impl | for/while mix-up: `for left <= right` (#704, Day 13); `while n in range(l)` (#271, Day 18) | Pick the loop keyword: `for x in iterable` to iterate; `while cond` for a condition | 2 | Day 13, Day 18 | active |
| M-017 | 2026-07-06 | strategy | Converging find-min used `right = mid - 1` (discarded the candidate min) instead of `right = mid` → failed `[3,1,2]` | On the keep-candidate side of a converging search, `mid` might BE the answer — move `right = mid`, never `mid - 1` | 1 | Day 15 | active |
| M-018 | 2026-07-08 | strategy | Wrote a bare `if/elif` where the whole thing is a LOOP — 3Sum omitted the `while left < right` wrapper so the two-pointer never swept (Day 17); **#235 LCA reassigned `node = node.left` then fell off the bottom of the function → returned `None` (Day 22)** | A scan / a descent / a skip is a **LOOP**, not a single check. Moving a pointer once is not traversing | 2 | Day 17, **Day 22** | active (watchlist) |
| M-019 | 2026-07-10 | impl | Koko search used `left = 0` (min speed is 1) → `mid=0` → `math.ceil(p/0)` division by zero on `[1]` | Respect the valid LOWER bound of an answer-search range (eating speed ≥ 1) | 1 | Day 19 | active |
| M-020 | 2026-07-10 | impl | Dropped `self.` inside a class method — attribute (`minStack` vs `self.minStack`, #155) and AGAIN on the recursive **calls** in `invert` (`invert(...)` vs `self.invert(...)`, #226, Day 21) | Instance data AND sibling methods inside a method are ALWAYS `self.x` — new-to-classes slip; kin to M-004 | 2 | Day 19, Day 21 | active |
| M-021 | 2026-07-13 | impl | **Container vs. contents** — index vs. `"#"` instead of `s[j]` (#271, Day 21); `.val` vs the `.left`/`.right` pointers (#226, Day 21); #271 AGAIN identical index-vs-char (Day 22); `left`/`right` HEIGHTS to count NODES (Day 22). **Day 23: CLEAN ✅ — #271 re-solved with `s[j]` correct** | Reaching for the handle instead of the thing it points at: `i` is a position, `s[i]` is the char; `.left` is a NODE, `.val` is a number. **And: a variable being in scope does not make it relevant** | 4 | Day 21 (×2), Day 22 (×2) | **→ BLOCKER (B-5, 1 of 2 clean)** |
| M-022 | 2026-07-13 | impl | 3Sum dedup used `if nums[left] == nums[left+1]` instead of `while` → skipped only ONE duplicate, not a run of them | Skipping a **run** of equal values is a LOOP, not a single check | 1 | Day 21 | dormant (clean Day 22 ✅) |
| M-023 | 2026-07-14 | strategy | **Stated the algorithm in the wrong ORDER out loud** — verbal recall of #1/#217 as "add it to the set, then check" (which returns `True` on `[1,2,3,4]` and `[0,0]` on Two Sum). The mental model was right; the sentence was not | The map/set holds **only what you've already passed** — **check first, then insert**. And: in an interview the interviewer only has what you SAY — narrate the loop body in the order it executes | 1 | Day 22 | active |

## Recurrence Watchlist (count ≥ 2 — one rep from escalating)

| ID | Type | Root cause | Count |
|---|---|---|---|
| **M-018** | strategy | **A scan / descent / skip is a LOOP, not a single check** (`if` where `while` belongs) | **2** |
| **M-009** | strategy | **Importing a template's BODY across problems without re-deriving** ("what decides the next step HERE?") | **2** |
| M-002 | impl | `()` call vs `[]` index | 2 |
| M-006 | strategy | Counting hidden in-loop cost in Big-O | 2 |
| M-015 | strategy | Converging search — return convergence point, not a tracked answer | 2 |
| M-005 | strategy | Space complexity — a new structure that scales = O(n), not O(1) | 2 |
| M-016 | impl | for/while mix-up | 2 |
| M-020 | impl | Missing `self.` on an attribute or a method call inside a class | 2 |

*Pre-empt these at the start of each session. (M-004 → B-1 cleared Day 16; M-003 → B-2 cleared Day 18; **M-001 → B-3 cleared Day 21**.)*

**Active blockers: B-4 (M-011, dropped guards) · B-5 (M-021, container-vs-contents) · B-6 (M-012, search direction)** — see `BLOCKERS.md`.

> **Day 22 note — the shape of the problem.** M-011, M-021, M-018 and M-012 are **all the same failure mode wearing different clothes: first-draft precision.** Every one of them happened on a problem whose *algorithm he had already derived correctly*. The gap is not comprehension. **Three reflexes, said out loud before submitting: (1) box or contents? (2) is it guarded? (3) am I looping where I should loop?**
