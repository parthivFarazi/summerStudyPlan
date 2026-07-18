# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-17 (Day 25 logged)
- **Phase:** Summer Sprint · Block B — *Core done; now depth. **First Trie built clean (#208)**; Validate BST (#98) + Kth Smallest (#230) landed. Day 26 = Trie wildcard (#211) + first Heap (#703, #1046).*
- **Sessions logged:** 25 · **Patterns learned:** 10 · **Mistakes tracked:** 25 · **Open blockers:** 2 (B-6, B-7) + watches (M-025, B-5, B-3)
- **Review queue:** Day 26 (Jul 18) = **6 due**, all full re-solves — 3 are resets (#146, #102, #226).

## 🟡 The honest read

**Block 2 keeps getting stronger; Block 1 (reviews) is where the precision tax shows up.**

Day 25 Block 2 was **3 new, all correct** — including a **brand-new data structure (Trie) built clean cold**, plus Validate BST (bounds passed *down*) and Kth Smallest (in-order = sorted, with the call-stack "why"). He's absorbing new machinery fast and asking the exactly-right questions ("don't I need a `self.val`?" — which *is* the insight).

**Block 1 was rough — 3 of 5 reset — but every failure was surface, not comprehension:**
- **#102:** two API names (`from collections import deque`, `.popleft()`).
- **#146:** rebuilt end-to-end; **all three drilled behaviors held** (`self.` ✅, return ✅, dict-sync ✅). Bugs were an incomplete `addFront` + two syntax slips.
- **#226:** the one real slip — swapped local `left`/`right` instead of `node.left`/`node.right`.

**The precision drill is measurably working** (`self.`, return, dict-sync all clean → B-7 got its first clean rep, M-024 went dormant). **The live signal is a new facet: pointer-surgery** — #146's incomplete `addFront` and #226's local-vs-field are the same shape (**M-025**), and #226 also reopened the B-5 watch.

## The reflexes (say them OUT LOUD before submitting)
1. **Count the pointers · mutate the FIELD not a local** *(M-025 — new; #146, #226)*
2. **The `self.` test** *(B-7 — clean Day 25 ✅ 1/2)*
3. **Does it return?** *(B-3 — watch, clean)*
4. **Which side can contain the answer?** — target-first *(B-6 — awaiting #235 Jul 19)*
5. Both structures in sync? *(M-024 ✅)* · complexity time AND space *(the list-in-recursion is O(n) — M-005)*

## ⚠️ Standing schedule note
Core roadmap is complete. Remaining is depth: **Heap (Day 26), Backtracking, Intervals, Graphs, DP.** No unplaced core problems.

## Pace Health
*(🟡 = off the sprint target · 🔴 = at risk. Refreshed each session.)*

| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 34 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 25 = **3** (#98, #230, #208) | 🟢 ahead of plan |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 days) | 6 + 7 | 🟡 fragile cluster (3 resets Jul 18) |
| **Open blockers** | **2** (B-6, B-7) + watches B-3, B-5 | 🟡 B-7 1/2, B-6 pending #235 |
| Review pass rate (Day 25) | **2 / 5** | 🔴 3 resets — but all surface (API names, pointer slips) |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | re-derives per problem; #230 list O(n) self-corrected |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| Sliding Window | 3/5 | solid |
| Binary Search | 3/5 | stable |
| Stack | 3/5 | stable |
| Linked List | 4/5 | LRU verified; **#146 reset on `addFront` pointer count (execution)** |
| Trees & BFS/DFS | 3/5 | **#226 reset — swapped locals not fields** (execution, not concept) |
| **Binary Search Tree** | **3/5** | **#98 bounds-down + #230 in-order** both clean |
| **Tries** | **2/5** | **new — #208 built clean cold, verified** |

## 🟡 Open Blockers & watches

- **B-7 (M-020, the `self.` rule)** — 🟡 **1 of 2.** #146 rebuild + #104 both clean on `self.`. One more clean → drops.
- **B-6 (M-012, search direction)** — 🟡 **1 of 2.** No direction problem Day 25; the pending test is **#235 on Jul 19**.
- **M-025 (pointer surgery)** — 👁 **NEW watch, 1 rep from a blocker.** *Count the pointers; mutate the field not a local.* (#146 `addFront`, #226 locals.)
- **B-5 (M-021, container-vs-contents)** — 👁 **watch reopened Day 25** (#226 local-vs-field). Tracked with M-025.
- **B-3 (return)** — 👁 watch, clean Day 25.

*(Cleared & now standing habits: B-1 names, B-2 range/len, **B-4 guards**, **B-5 container-vs-contents [watch]**. M-024 dual-sync → dormant, clean Day 25.)*

## Next Session Focus  → **Day 26**
1. **Block 1 — review (6 due, full re-solves; 3 resets):** **#146 → #102 → #226** (resets — **count the pointers · `from collections import deque` / `.popleft()` · mutate `node.left/right` not locals**), then **#98 → #230 → #208** (1d).
2. **Block 2 — new:** **Design Add & Search Words (#211)** — Trie + `.` wildcard (DFS into all children at a `.`). **Heap** — Kth Largest in a Stream (#703), Last Stone Weight (#1046). **Pre-teach `heapq` in isolation:** min-heap by default, max-heap via negation, push/pop are O(log n).
3. **Habits (out loud before submit):** count the pointers / mutate the field not a local · the `self.` test · does it return? · complexity time AND space.

---
*Weekly snapshots can be appended below as the sprint progresses.*
