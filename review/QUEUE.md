# Spaced-Repetition QUEUE — single source of truth for review state

> **Ladder:** `1d → 3d → 7d → 21d → 60d` → graduated. **Pass** = advance one rung. **Fail** (needed a hint, blanked, or a bug you couldn't self-fix) = **reset to 1d** + log the cause in `MISTAKES.md`. Re-solves are **from a blank screen**, never re-reading the solution.

## How to use each session
1. Pull rows with **Next due ≤ today**; order **resets → 1d → 3d → oldest**. Work a **budget of ~6–8, time-boxed ~30–40 min** — overflow rolls forward (don't clear everything).
2. **Full re-solve from a blank screen** for fragile items (reset / 1d / learned in the last ~week). **30-sec verbal recall** for mastered items (**21d rung**): say pattern + approach + complexity; full-solve only if you blank.
3. Update the row: new rung + new **fuzzed** due date (jitter ±1–2 days toward the lightest day; keep any day ≤ ~6–8 due) + append result to `Results` (`P`/`F`). One write, here only.

## Overflow rule
A wall of 12-due is a **scheduling** problem, not a work problem. If **due count > 8** after prioritizing: (a) full-solve the fragile ones + verbal the mastered ones within the ~6–8 budget, and (b) **roll the leftover stable/verbal items forward 1–2 days** (fuzz) so no day exceeds ~8. Only go reviews-only (skip new) if it's still > 8 fragile items. Interleave days (~every 5th session) also drain the queue. Decay is the enemy, not volume.

> **Steady-state note:** at 2-new/day on this ladder, ~10 reviews/day is the natural floor (each problem → reviews at +1/+4/+11/+32/+92 days). The fuzz + verbal tier keep that from *spiking* or *eating the clock*; it won't (and shouldn't) drop to zero.

## Due / Active
*(Seeded from Days 1–8. This is the live starting state — correct rungs as you actually re-solve.)*

| Problem | Pattern | Rung | Next due | Streak | Results |
|---|---|---|---|---|---|
| **Level Order Traversal (#102)** | trees | **1d (reset)** | 2026-07-20 | 0 | (new)·F·**F** |
| **Implement Trie (#208)** | tries | **1d (reset)** | 2026-07-20 | 0 | (new)·**F** |
| **Add & Search Words (#211)** | tries | 1d | 2026-07-20 | 0 | (new) |
| **Kth Largest in Stream (#703)** | heap | 1d | 2026-07-20 | 0 | (new) |
| **Last Stone Weight (#1046)** | heap | 1d | 2026-07-20 | 0 | (new) |
| Lowest Common Ancestor BST (#235) | binary-search-tree | 3d | 2026-07-20 | 1 | (new)·F·P |
| **LRU Cache (#146)** | design / linked-list | **3d** | 2026-07-21 | 1 | (new)·F·**P** |
| **Invert Binary Tree (#226)** | trees | **3d** | 2026-07-21 | 1 | P·F·**P** |
| **Validate BST (#98)** | binary-search-tree | **3d** | 2026-07-21 | 1 | (new)·**P** |
| **Kth Smallest in BST (#230)** | binary-search-tree | **3d** | 2026-07-21 | 1 | (new)·**P** |
| Balanced Binary Tree (#110) | trees | 1d | 2026-07-21 | 0 | (new) |
| Encode/Decode Strings (#271) | arrays-hashing | 3d | 2026-07-21 | 1 | P·F·F·P |
| Right Side View (#199) | trees | 3d | 2026-07-21 | 1 | (new)·P |
| Reorder List (#143) | linked-list | 3d | 2026-07-22 | 1 | (new)·F·P |
| Remove Nth Node From End (#19) | linked-list | 3d | 2026-07-22 | 1 | (new)·P |
| Valid Anagram (#242) | arrays-hashing | 3d | 2026-07-22 | 1 | P·P·P·F·F·P |
| Same Tree (#100) | trees | 3d | 2026-07-22 | 1 | P |
| 3Sum (#15) | two-pointers | 3d | 2026-07-22 | 1 | F·P·F·P |
| Valid Parentheses (#20) | stack | 3d | 2026-07-22 | 1 | P·F·P |
| Linked List Cycle (#141) | linked-list | 3d | 2026-07-22 | 1 | P |
| Binary Search (#704) | binary-search | 7d | 2026-07-23 | 2 | P·P |
| Search in Rotated Array (#33) | binary-search | 7d | 2026-07-23 | 2 | P·P |
| Min Stack (#155) | stack | 7d | 2026-07-23 | 2 | P·P |
| Search a 2D Matrix (#74) | binary-search | 7d | 2026-07-23 | 2 | P·P |
| Koko Eating Bananas (#875) | binary-search | 3d | 2026-07-23 | 1 | P·F·P·F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | 2026-07-23 | 1 | P |
| Diameter of Binary Tree (#543) | trees | 3d | 2026-07-23 | 1 | P |
| Evaluate RPN (#150) | stack | 7d | 2026-07-23 | 2 | P·P |
| Top K Frequent (#347) | arrays-hashing | 21d | 2026-07-24 | 3 | P·P·P |
| Find Min in Rotated Sorted Array (#153) | binary-search | 7d | 2026-07-24 | 2 | F·P·F·P·P |
| Longest Consecutive Sequence (#128) | arrays-hashing | 7d | 2026-07-24 | 2 | P·P |
| Daily Temperatures (#739) | stack | 7d | 2026-07-24 | 2 | P·F·P·P |
| Reverse Linked List (#206) | linked-list | 7d | 2026-07-24 | 2 | P·P |
| Merge Two Sorted Lists (#21) | linked-list | 7d | 2026-07-25 | 2 | P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d | 2026-07-25 | 3 | P·P·P |
| Maximum Depth of Binary Tree (#104) | trees | 7d | 2026-07-25 | 2 | P·P |
| Longest Substring No Repeat (#3) | sliding-window | 21d | 2026-07-30 | 3 | P·P·P |
| Best Time to Buy/Sell (#121) | sliding-window | 21d | 2026-07-31 | 3 | P·P·P |
| Two Sum II (#167) | two-pointers | 21d | 2026-08-01 | 3 | P·P·P |
| Container With Most Water (#11) | two-pointers | 21d | 2026-08-01 | 3 | P·P·P |
| Valid Palindrome (#125) | two-pointers | 21d | 2026-08-04 | 3 | F·F·F·F·P·P·P |
| Group Anagrams (#49) | arrays-hashing | 60d | 2026-09-09 | 4 | P·P·P·P |
| Two Sum (#1) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |

### Load after Day 26 fuzz *(cap ~8/day · ⚠️ Jul 19 = REST DAY, nothing scheduled)*
`Jul 20` **6** · `Jul 21` **7** · `Jul 22` **7** · `Jul 23` **8** *(interleave — drains the 3d/7d backlog)* · `Jul 24` **5** · `Jul 25` **3**. **No day over the cap; Jul 19 empty.**

**Day 26 processed all 6 due Jul 18:** #146→3d, #226→3d, #98→3d, #230→3d (Jul 21); #102 & #208 **failed → stay reset 1d** (Jul 20). **3 new (#211/#703/#1046) enter at 1d → Jul 20.** **Big rebalance:** the prior schedule had wrongly put ~13 items across the Jul 19 **rest day** and Jul 20–21; spread them Jul 20→25, fragile items (resets #102/#208, new #211/#703/#1046, #235 canary) up front on Jul 20, stable 7d items drained into the **Jul 23 interleave** and Jul 24–25.

**Day 27 order (Jul 20 — 6 due):**
resets **#102 → #208** first (**#102: root-None guard + `if node.left/right` before enqueue; #208: `node.isEnd = True`**) → new **#211 → #703 → #1046** (1d) → **#235** (B-6 canary).

> **⚠️ #235 (B-6, search direction) is the pending canary** — its target-first re-solve on Jul 20 is the 2nd clean test needed to clear B-6, the last drill-now blocker.
> **⚠️ #102 & #208 reset twice now** — both on **dropped required lines** (guards / `isEnd`). Run the "walk the op to the end" scan out loud.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
