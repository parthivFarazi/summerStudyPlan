# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-13 (Day 21 logged)
- **Phase:** Summer Sprint · Block B — *Recursion learned from scratch; **Trees** open (#226, #104). Day 22 = Diameter (#543), Same Tree (#100), LCA BST (#235).*
- **Sessions logged:** 21 · **Patterns learned:** 8 · **Mistakes tracked:** 22 · **Open blockers:** 1 (B-4 edge-guards — B-3 cleared ✅)
- **Review queue:** Day 22 (Jul 14) ≈ **8 due** (~6 effective — #1/#217 are verbal tier); two resets up front (#15, #271)

## ⚠️ Standing schedule note
**LRU Cache (#146) is rescheduled from Day 21 → Day 24 (Jul 16).** Day 21's hour went to teaching recursion (load-bearing for Trees, Backtracking, Graphs, DP). Day 24 was the only day with no Block-2 problems, so #146 lands there. **It is the last unplaced core problem — do not let it drift.** Days 22, 23, 25, 26 unchanged; Aug 20 target unaffected.

## Pace Health
*(🟡 = off the sprint target · 🔴 = at risk. Refreshed each session.)*

| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 38 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 21 = 2 (#226, #104) + recursion taught | 🟢 on plan (#146 → Day 24) |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 days) | ~14 raw (~11 effective) | 🟡 fragile cluster — resets first |
| **Open blockers** | 1 (B-4 edge-guards) | 🟡 pre-submit edge scan |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | **self-corrected O(1)→O(h) on the call stack, unprompted** — space reflex now includes recursion |
| Arrays & Hashing | 3/5 | #271 reset (index-vs-char); #128 clean, with the reason |
| Two Pointers | 3/5 | **#15 reset** — dedup `if` should be `while` |
| Sliding Window | 3/5 | solid |
| Binary Search | 3/5 | stable |
| Stack | 3/5 | **#739 reset cleared** — the guard was back |
| Linked List | 3/5 | #206 (2:03) and #21 fluent; mediums held |
| **Trees** | **2/5** | **new** — recursion learned from zero; #226 + #104 off the template |

## 🟡 Open Blocker — the "first-draft precision" gap
- **B-4 (M-011, dropping edge-guards)** — 0 of 2 clean. Day 21: `node.left.val` on #226 would crash on every leaf. Pre-submit edge scan: *"empty? single? none-found? lengths equal? **is this None?**"*
- **Watchlist (recurrence 2):** **M-021 container-vs-contents** (index vs. value, node vs. `.val` — hit twice on Day 21), M-020 missing `self.`, M-005 space, M-012 BS direction.

*(B-1 names, B-2 range/len, and now **B-3 `return`** all cleared — keep as standing habits.)*

## Next Session Focus  → **Day 22**
1. **Block 1 — review (~8 due, protocol):** resets first (**#15**, **#271**), then #242, the new trees #226/#104 (1d), #125, #875. **Verbal tier:** #1, #217. Time-box 30–40 min.
2. **Block 2 — new:** **Trees** — Diameter of Binary Tree (#543), Same Tree (#100), Lowest Common Ancestor in a BST (#235). All three run off the Day-21 recursion template; #543 introduces *helper returns height, answer tracked outside*.
3. **Habits (standing):** **B-4 "edges guarded / is it None?"** · **node vs. value, index vs. value** · dedup is a `while` · `self.` inside classes · space reflex includes the call stack · does it return?

---
*Weekly snapshots can be appended below as the sprint progresses.*
