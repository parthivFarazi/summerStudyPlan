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
| Add & Search Words (#211) | tries | **3d** | 2026-07-28 | 1 | (new)·F·F·**P** |
| Last Stone Weight (#1046) | heap | **3d** | 2026-07-28 | 1 | (new)·F·F·**P** |
| Right Side View (#199) | trees | **3d** | 2026-07-28 | 1 | (new)·P·F·F·**P** |
| **Subsets II (#90)** | backtracking | **1d (reset)** | 2026-07-27 | 0 | (new)·**F** |
| **Permutations (#46)** | backtracking | **1d (reset)** | 2026-07-27 | 0 | (new)·**F** |
| **Subsets (#78)** | backtracking | **1d (reset)** | 2026-07-27 | 0 | (new)·**F** |
| **Word Search (#79)** | backtracking (grid DFS) | **1d** | 2026-07-27 | 0 | (new) |
| **Combination Sum (#39)** | backtracking | **1d** | 2026-07-27 | 0 | (new) |
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

### Load after Day 30 fuzz *(cap ~8/day · 🗣 = verbal · ⚠️ Jul 26 = REST)*
Nominal: `Jul 27` (backtracking 1d cluster #90/#46/#78/#79/#39 — all reset/new, fragile → full-solve; drain first) · `Jul 28` heavy (3d passes #211/#1046/#199 back down + #110/#973/#215/#143/#146 + #100/#15/#20/#141/#875/#424/#543 + 7d/verbal layer) · then 7d/21d climb. **Jul 28 is over ~8** — apply the overflow rule: full-solve the fragile first, **verbal-tier the 21d items**, **roll the stable 3d/7d overflow forward 1–2 days.** The backtracking cluster is the priority — it's the youngest, most fragile pattern (3 resets Day 30).

**Day 27 (Jul 21):** #102/#208/#703→3d, #235→7d (**B-6 CLEARED**); #211/#1046/#110 reset; #973/#215 new.
**Day 28 (Jul 22):** #271/#226/#98→7d; #143/#199/#146 reset; #78/#39 new.
**Day 29 (Jul 23):** **5/8** — #110/#973/#215/#143/#146 **PASS→3d**; #211/#1046/#199 **reset** (fresh facets: #211 constructor/keys/return, #1046 return-negation *again*, #199 enqueue direction); new **#90/#46 backtracking→1d**. **Named checks HELD** (self./curr3/guard/space/box all correct first-draft). **B-7 held today → 1 clean session (clear after 1 more).**

**Day 30 (Jul 25 — interleave + new) — DONE.** 3/6 interleave: **#211/#1046/#199 PASS→3d** (every older named cause held — #1046 un-negate FINALLY, #211's 3 Day-29 facets, #199 enqueue direction); **#78/#90/#46 reset→1d** (all backtracking — the youngest pattern). **Block 2 new: #79 Word Search** ✅ (grid DFS, built cold w/ 2 M-027 nudges).

**Day 31 order (Jul 27 — drain the backtracking cluster + new):**
Fragile first: **#90 → #46 → #78 → #79 → #39** (backtracking 1d — the whole young cluster). Then new material (Intervals, or Backtracking cont. #40/#131). Roll any 3d overflow to Jul 28.

> **✅ B-7 (self./ownership) CLEARED Day 30** (2nd clean session) — no drill-now blocker; all of B-1…B-7 clear. Keep the ownership check as a standing habit.
> **👁 M-027 — the through-line, but the one *repeat* is CLOSED.** #1046's un-negate finally landed Day 30 after two identical misses. Keep the final read-through: the two #79 nudges (dropped left direction, `dfs(0,0,0)` vs `dfs(r,c,0)`) were this flavor.
> **👁 Backtracking fragility (Day 30):** #78/#90/#46 all reset — the pattern is <1 week old. Not a blocker; drain the 1d cluster on Jul 27. Every *older* named cause held first-draft.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
