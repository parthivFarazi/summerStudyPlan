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
| **Lowest Common Ancestor BST (#235)** | binary-search-tree | **1d (reset)** | 2026-07-16 | 0 | (new)·**F** |
| **Reorder List (#143)** | linked-list | **1d (reset)** | 2026-07-16 | 0 | (new)·**F** |
| Remove Nth Node From End (#19) | linked-list | 1d | 2026-07-16 | 0 | (new) |
| Daily Temperatures (#739) | stack | 3d | 2026-07-16 | 1 | P·F·P |
| Reverse Linked List (#206) | linked-list | 3d | 2026-07-16 | 1 | P |
| Merge Two Sorted Lists (#21) | linked-list | 3d | 2026-07-16 | 1 | P |
| **Level Order Traversal (#102)** | trees | 1d | 2026-07-17 | 0 | (new) |
| **Right Side View (#199)** | trees | 1d | 2026-07-17 | 0 | (new) |
| **3Sum (#15)** | two-pointers | 3d | 2026-07-17 | 1 | F·P·F·P |
| **Invert Binary Tree (#226)** | trees | 3d | 2026-07-17 | 1 | P |
| **Maximum Depth of Binary Tree (#104)** | trees | 3d | 2026-07-17 | 1 | P |
| Valid Parentheses (#20) | stack | 3d | 2026-07-17 | 1 | P·F·P |
| **Balanced Binary Tree (#110)** | trees | 1d | 2026-07-18 | 0 | (new) |
| **Encode/Decode Strings (#271)** | arrays-hashing | **3d** | 2026-07-18 | 1 | P·F·F·**P** |
| **Diameter of Binary Tree (#543)** | trees | **3d** | 2026-07-18 | 1 | **P** |
| Koko Eating Bananas (#875) | binary-search | 3d | 2026-07-18 | 1 | P·F·P·F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | 2026-07-18 | 1 | P |
| Evaluate RPN (#150) | stack | 7d | 2026-07-18 | 2 | P·P |
| **Valid Anagram (#242)** | arrays-hashing | **3d** | 2026-07-19 | 1 | P·P·P·F·F·**P** |
| **Same Tree (#100)** | trees | **3d** | 2026-07-19 | 1 | **P** |
| Binary Search (#704) | binary-search | 7d | 2026-07-19 | 2 | P·P |
| Search a 2D Matrix (#74) | binary-search | 7d | 2026-07-19 | 2 | P·P |
| Min Stack (#155) | stack | 7d | 2026-07-19 | 2 | P·P |
| **Linked List Cycle (#141)** | linked-list | **3d** | 2026-07-20 | 1 | **P** |
| Search in Rotated Array (#33) | binary-search | 7d | 2026-07-20 | 2 | P·P |
| Find Min in Rotated Sorted Array (#153) | binary-search | 7d | 2026-07-20 | 2 | F·P·F·P·P |
| Longest Consecutive Sequence (#128) | arrays-hashing | 7d | 2026-07-20 | 2 | P·P |
| Top K Frequent (#347) | arrays-hashing | 21d | 2026-07-21 | 3 | P·P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d | 2026-07-23 | 3 | P·P·P |
| Longest Substring No Repeat (#3) | sliding-window | 21d | 2026-07-30 | 3 | P·P·P |
| Best Time to Buy/Sell (#121) | sliding-window | 21d | 2026-07-31 | 3 | P·P·P |
| Two Sum II (#167) | two-pointers | 21d | 2026-08-01 | 3 | P·P·P |
| Container With Most Water (#11) | two-pointers | 21d | 2026-08-01 | 3 | P·P·P |
| Valid Palindrome (#125) | two-pointers | 21d | 2026-08-04 | 3 | F·F·F·F·P·P·P |
| Group Anagrams (#49) | arrays-hashing | 60d | 2026-09-09 | 4 | P·P·P·P |
| Two Sum (#1) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |

### Load after Day 23 fuzz *(cap ~8/day)*
`Jul 16` **6** *(the #146 LRU + interleave day — held at 6 despite the two resets)* · `Jul 17` **6** · `Jul 18` **6** · `Jul 19` **5** · `Jul 20` **4** · `Jul 21` 1 · `Jul 23` 1. **No day over the cap.**

**Rebalance (Jul 16–18 were clustering — three days of 3d items converging):** kept the fragile items on their due dates (resets #235/#143 → Jul 16; new #102/#199 → Jul 17; new #110 → Jul 18), then fuzzed the stable 7d items forward: #704 → Jul 19, #74 → Jul 19, #33 → Jul 20, #153 → Jul 20, #875 → Jul 18. **Jul 16 (LRU day) protected at 6.**

**Day 24 order (interleave — mix unlabeled where you can):**
resets **#235 → #143** first *(full re-solve, fragile)* → **#19 → #739 → #206 → #21**. Then Block 2 = **LRU Cache (#146)**.

> **⚠️ #235 is now the canary.** Reset twice for the **same direction inversion** (B-6). Day 24: **do the target-first spelling** (`p.val > node.val → right`). If it inverts a 3rd time, stop and drill direction cold.

> **Standing note — not a queue item:** **LRU Cache (#146)** = **Day 24 (Jul 16)**, the last unplaced core problem. Jul 16 was held to 6 reviews to protect it. **Do not let it drift.**
> **#98 Validate BST** was deferred from Day 23 → **Day 25**, clustering with #230 (both BST). Enters the queue at 1d once solved.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
