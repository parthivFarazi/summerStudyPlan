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
| **LRU Cache (#146)** | design / linked-list | **1d (reset)** | 2026-07-18 | 0 | (new)·**F** |
| **Level Order Traversal (#102)** | trees | **1d (reset)** | 2026-07-18 | 0 | (new)·**F** |
| **Invert Binary Tree (#226)** | trees | **1d (reset)** | 2026-07-18 | 0 | P·**F** |
| **Validate BST (#98)** | binary-search-tree | 1d | 2026-07-18 | 0 | (new) |
| **Kth Smallest in BST (#230)** | binary-search-tree | 1d | 2026-07-18 | 0 | (new) |
| **Implement Trie (#208)** | tries | 1d | 2026-07-18 | 0 | (new) |
| Balanced Binary Tree (#110) | trees | 1d | 2026-07-19 | 0 | (new) |
| Encode/Decode Strings (#271) | arrays-hashing | 3d | 2026-07-19 | 1 | P·F·F·P |
| Lowest Common Ancestor BST (#235) | binary-search-tree | 3d | 2026-07-19 | 1 | (new)·F·P |
| Reorder List (#143) | linked-list | 3d | 2026-07-19 | 1 | (new)·F·P |
| Remove Nth Node From End (#19) | linked-list | 3d | 2026-07-19 | 1 | (new)·P |
| Valid Anagram (#242) | arrays-hashing | 3d | 2026-07-19 | 1 | P·P·P·F·F·P |
| Same Tree (#100) | trees | 3d | 2026-07-19 | 1 | P |
| **Right Side View (#199)** | trees | **3d** | 2026-07-20 | 1 | (new)·**P** |
| 3Sum (#15) | two-pointers | 3d | 2026-07-20 | 1 | F·P·F·P |
| Valid Parentheses (#20) | stack | 3d | 2026-07-20 | 1 | P·F·P |
| Linked List Cycle (#141) | linked-list | 3d | 2026-07-20 | 1 | P |
| Binary Search (#704) | binary-search | 7d | 2026-07-20 | 2 | P·P |
| Search in Rotated Array (#33) | binary-search | 7d | 2026-07-20 | 2 | P·P |
| Min Stack (#155) | stack | 7d | 2026-07-21 | 2 | P·P |
| Search a 2D Matrix (#74) | binary-search | 7d | 2026-07-21 | 2 | P·P |
| Top K Frequent (#347) | arrays-hashing | 21d | 2026-07-21 | 3 | P·P·P |
| Koko Eating Bananas (#875) | binary-search | 3d | 2026-07-21 | 1 | P·F·P·F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | 2026-07-21 | 1 | P |
| Diameter of Binary Tree (#543) | trees | 3d | 2026-07-21 | 1 | P |
| Evaluate RPN (#150) | stack | 7d | 2026-07-21 | 2 | P·P |
| Find Min in Rotated Sorted Array (#153) | binary-search | 7d | 2026-07-22 | 2 | F·P·F·P·P |
| Longest Consecutive Sequence (#128) | arrays-hashing | 7d | 2026-07-22 | 2 | P·P |
| Daily Temperatures (#739) | stack | 7d | 2026-07-23 | 2 | P·F·P·P |
| Reverse Linked List (#206) | linked-list | 7d | 2026-07-23 | 2 | P·P |
| Merge Two Sorted Lists (#21) | linked-list | 7d | 2026-07-23 | 2 | P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d | 2026-07-23 | 3 | P·P·P |
| **Maximum Depth of Binary Tree (#104)** | trees | **7d** | 2026-07-24 | 2 | P·**P** |
| Longest Substring No Repeat (#3) | sliding-window | 21d | 2026-07-30 | 3 | P·P·P |
| Best Time to Buy/Sell (#121) | sliding-window | 21d | 2026-07-31 | 3 | P·P·P |
| Two Sum II (#167) | two-pointers | 21d | 2026-08-01 | 3 | P·P·P |
| Container With Most Water (#11) | two-pointers | 21d | 2026-08-01 | 3 | P·P·P |
| Valid Palindrome (#125) | two-pointers | 21d | 2026-08-04 | 3 | F·F·F·F·P·P·P |
| Group Anagrams (#49) | arrays-hashing | 60d | 2026-09-09 | 4 | P·P·P·P |
| Two Sum (#1) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |

### Load after Day 25 fuzz *(cap ~8/day)*
`Jul 18` **6** *(3 resets + 3 new — all fragile 1d; Day 26 also has 3 new problems)* · `Jul 19` **7** · `Jul 20` **6** · `Jul 21` **7** · `Jul 22` **2** · `Jul 23` **4** · `Jul 24` **1**. **No day over the cap.**

**Day 25 processed all 5 due Jul 17:** #146 reset→1d (Jul 18), #102 reset→1d (Jul 18), #226 reset→1d (Jul 18), #199→3d (Jul 20), #104→7d (Jul 24). **3 new (#98/#230/#208) enter at 1d → Jul 18.** Jul 18 had 7 stale items pre-scheduled — **all 7 fuzzed forward** (#110→Jul19, #271→Jul19, #543→Jul21, #15→Jul20, #875→Jul21, #424→Jul21, #150→Jul21) to keep the fragile-heavy LRU-retry day at 6. Stable 7d items (#153, #128) pushed to the empty Jul 22.

**Day 26 order (6 due, all full re-solves — 3 are resets):**
**#146 → #102 → #226** *(resets — fragile; **#146: count the 4 pointers in `addFront`; #226: mutate `node.left/right`, not locals; #102: `from collections import deque`, `.popleft()`**)* → **#98 → #230 → #208** *(1d, learned yesterday)*.

> **⚠️ #146 and #226 are the canaries** — both reset on **pointer-surgery slips** (M-025). Day 26: run the "count the pointers / mutate the field not a local" check out loud.

> **Standing note:** #235 (B-6, search direction) is due **Jul 19** — its next re-solve is the pending test of whether the target-first fix holds a 2nd time.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
