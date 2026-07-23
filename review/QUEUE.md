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
| **Add & Search Words (#211)** | tries | **1d (reset)** | 2026-07-24 | 0 | (new)·F·**F** |
| **Last Stone Weight (#1046)** | heap | **1d (reset)** | 2026-07-24 | 0 | (new)·F·**F** |
| **Right Side View (#199)** | trees | **1d (reset)** | 2026-07-24 | 0 | (new)·P·F·**F** |
| **Subsets II (#90)** | backtracking | **1d** | 2026-07-24 | 0 | (new) |
| **Permutations (#46)** | backtracking | **1d** | 2026-07-24 | 0 | (new) |
| **Subsets (#78)** | backtracking | **1d** | 2026-07-24 | 0 | (new) |
| **Combination Sum (#39)** | backtracking | **1d** | 2026-07-25 | 0 | (new) |
| Balanced Binary Tree (#110) | trees | 3d | 2026-07-25 | 1 | (new)·F·**P** |
| K Closest Points (#973) | heap | 3d | 2026-07-25 | 1 | (new)·**P** |
| Kth Largest in Array (#215) | heap | 3d | 2026-07-25 | 1 | (new)·**P** |
| Reorder List (#143) | linked-list | 3d | 2026-07-25 | 1 | (new)·F·P·F·**P** |
| LRU Cache (#146) | design / linked-list | 3d | 2026-07-27 | 1 | (new)·F·P·F·**P** |
| Level Order Traversal (#102) | trees | 3d | 2026-07-24 | 1 | (new)·F·F·P |
| Implement Trie (#208) | tries | 3d | 2026-07-24 | 1 | (new)·F·P |
| Kth Largest in Stream (#703) | heap | 3d | 2026-07-24 | 1 | (new)·P |
| Kth Smallest in BST (#230) | binary-search-tree | 3d | 2026-07-24 | 1 | (new)·P |
| Remove Nth Node From End (#19) | linked-list | 3d | 2026-07-24 | 1 | (new)·P |
| Valid Anagram (#242) | arrays-hashing | 3d | 2026-07-24 | 1 | P·P·P·F·F·P |
| Same Tree (#100) | trees | 3d | 2026-07-25 | 1 | P |
| 3Sum (#15) | two-pointers | 3d | 2026-07-25 | 1 | F·P·F·P |
| Valid Parentheses (#20) | stack | 3d | 2026-07-25 | 1 | P·F·P |
| Linked List Cycle (#141) | linked-list | 3d | 2026-07-25 | 1 | P |
| Koko Eating Bananas (#875) | binary-search | 3d | 2026-07-25 | 1 | P·F·P·F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | 2026-07-25 | 1 | P |
| Diameter of Binary Tree (#543) | trees | 3d | 2026-07-25 | 1 | P |
| Lowest Common Ancestor BST (#235) | binary-search-tree | **7d** | 2026-07-25 | 2 | (new)·F·P·**P** |
| Encode/Decode Strings (#271) | arrays-hashing | **7d** | 2026-07-27 | 2 | P·F·F·P·**P** |
| Invert Binary Tree (#226) | trees | **7d** | 2026-07-27 | 2 | P·F·P·**P** |
| Validate BST (#98) | binary-search-tree | **7d** | 2026-07-27 | 2 | (new)·P·**P** |
| Binary Search (#704) | binary-search | 7d | 2026-07-27 | 2 | P·P |
| Search in Rotated Array (#33) | binary-search | 7d | 2026-07-27 | 2 | P·P |
| Min Stack (#155) | stack | 7d | 2026-07-27 | 2 | P·P |
| Search a 2D Matrix (#74) | binary-search | 7d | 2026-07-27 | 2 | P·P |
| Evaluate RPN (#150) | stack | 7d | 2026-07-27 | 2 | P·P |
| Find Min in Rotated Sorted Array (#153) | binary-search | 7d | 2026-07-28 | 2 | F·P·F·P·P |
| Longest Consecutive Sequence (#128) | arrays-hashing | 7d | 2026-07-28 | 2 | P·P |
| Daily Temperatures (#739) | stack | 7d | 2026-07-28 | 2 | P·F·P·P |
| Reverse Linked List (#206) | linked-list | 7d | 2026-07-28 | 2 | P·P |
| Merge Two Sorted Lists (#21) | linked-list | 7d | 2026-07-28 | 2 | P·P |
| Maximum Depth of Binary Tree (#104) | trees | 7d | 2026-07-28 | 2 | P·P |
| Top K Frequent (#347) | arrays-hashing | 21d 🗣 | 2026-07-28 | 3 | P·P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d 🗣 | 2026-07-28 | 3 | P·P·P |
| Longest Substring No Repeat (#3) | sliding-window | 21d 🗣 | 2026-07-30 | 3 | P·P·P |
| Best Time to Buy/Sell (#121) | sliding-window | 21d 🗣 | 2026-07-31 | 3 | P·P·P |
| Two Sum II (#167) | two-pointers | 21d 🗣 | 2026-08-01 | 3 | P·P·P |
| Container With Most Water (#11) | two-pointers | 21d 🗣 | 2026-08-01 | 3 | P·P·P |
| Valid Palindrome (#125) | two-pointers | 21d 🗣 | 2026-08-04 | 3 | F·F·F·F·P·P·P |
| Group Anagrams (#49) | arrays-hashing | 60d | 2026-09-09 | 4 | P·P·P·P |
| Two Sum (#1) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 60d | 2026-09-12 | 4 | P·P·P·P |

### Load after Day 29 fuzz *(cap ~8/day · 🗣 = verbal · ⚠️ Jul 26 = REST · ⚠️ backlog EXCEEDS cap Jul 24–25 — apply overflow rule live)*
Nominal: `Jul 24` heavy (resets #211/#1046/#199 + new #90/#46/#78 + 3d cluster #102/#208/#703/#230/#19/#242) · `Jul 25` heavy (3d passes #110/#973/#215/#143/#39 + #100/#15/#20/#141/#875/#424/#543) · `Jul 26` REST · `Jul 27`–`Jul 28` 7d/verbal drain. **The fragile/3d layers are genuinely over ~8/day for Jul 24–25** (three straight big sessions stacked them). **Live overflow rule:** each day, full-solve the fragile (resets/1d) first, **verbal-tier the 21d items**, and **roll the stable 3d/7d overflow forward 1–2 days** so no day actually exceeds ~8. It eases after the Jul 26 rest as items climb to 7d/21d.

**Day 27 (Jul 21):** #102/#208/#703→3d, #235→7d (**B-6 CLEARED**); #211/#1046/#110 reset; #973/#215 new.
**Day 28 (Jul 22):** #271/#226/#98→7d; #143/#199/#146 reset; #78/#39 new.
**Day 29 (Jul 23):** **5/8** — #110/#973/#215/#143/#146 **PASS→3d**; #211/#1046/#199 **reset** (fresh facets: #211 constructor/keys/return, #1046 return-negation *again*, #199 enqueue direction); new **#90/#46 backtracking→1d**. **Named checks HELD** (self./curr3/guard/space/box all correct first-draft). **B-7 held today → 1 clean session (clear after 1 more).**

**Day 30 order (Jul 24 — interleave + new):**
Fragile first: **#211 → #1046 → #199** (resets) → new **#90 → #46 → #78** (backtracking 1d). **Block 2 new: #79 Word Search** (deferred from Day 29 — grid DFS + backtracking). Overflow the 3d cluster forward.

> **⚠️ B-7 (self./ownership) — drill-now, 1 clean session done** (held on #211 & #146 today). One more clean → clears. Keep the ownership check in the final read-through.
> **⚠️ M-027 — the through-line.** #1046's `return -maxHeap[0]` is now missed on Day 27 AND Day 29 (identical). Bank the rule: **negate in → un-negate at the return.** #199: flip the enqueue → flip the "keep."
> **The good news (Day 29):** every *previously-named* reset-cause was correct on the first draft. The resets are new facets, not old ones — the final read-through is closing the gaps one at a time.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
