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
| **Add & Search Words (#211)** | tries | **1d (reset)** | 2026-07-23 | 0 | (new)·**F** |
| **Last Stone Weight (#1046)** | heap | **1d (reset)** | 2026-07-23 | 0 | (new)·**F** |
| **Balanced Binary Tree (#110)** | trees | **1d (reset)** | 2026-07-23 | 0 | (new)·**F** |
| **K Closest Points (#973)** | heap | **1d** | 2026-07-23 | 0 | (new) |
| **Kth Largest in Array (#215)** | heap | **1d** | 2026-07-23 | 0 | (new) |
| **Reorder List (#143)** | linked-list | **1d (reset)** | 2026-07-23 | 0 | (new)·F·P·**F** |
| **Right Side View (#199)** | trees | **1d (reset)** | 2026-07-23 | 0 | (new)·P·**F** |
| **LRU Cache (#146)** | design / linked-list | **1d (reset)** | 2026-07-23 | 0 | (new)·F·P·**F** |
| **Subsets (#78)** | backtracking | **1d** | 2026-07-24 | 0 | (new) |
| **Combination Sum (#39)** | backtracking | **1d** | 2026-07-24 | 0 | (new) |
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

### Load after Day 28 fuzz *(cap ~8/day · 🗣 = verbal 30-sec tier · ⚠️ Jul 26 = REST, nothing scheduled)*
`Jul 23` **8** · `Jul 24` **8** · `Jul 25` **8** · `Jul 26` **REST** · `Jul 27` **8** · `Jul 28` **8** (6 full + 2 verbal). **No day over cap.** *(Heavy backlog — the double session + the skipped Jul 20 stacked the fragile/3d layers. Rides the cap ~a week, then eases as items climb to 7d/21d.)*

**Day 27 (Jul 21):** #102/#208/#703 PASS→3d, #235 PASS→7d (**B-6 CLEARED**); #211/#1046/#110 FAIL→reset; #973/#215 new→1d. (5 stable 3d rolled forward.)
**Day 28 (Jul 22 — 2nd session):** worked genuinely-due reviews only (skipped the 5 items done hours earlier, no spacing value). #271 PASS→7d, #226 PASS→7d, #98 PASS→7d; **#143/#199/#146 FAIL→reset** (all one-site final-pass slips). New backtracking #78/#39→1d. The **deferred 5** (#211/#1046/#110/#973/#215) now sit due Jul 23 — properly spaced.

**Day 29 order (Jul 23 — 8 due, all fragile):**
resets/deferred first: **#211 → #1046 → #110 → #973 → #215** (the Day-27 batch, now spaced) → **#143 → #199 → #146** (Day-28 resets). Then Block 2 new: **Backtracking cont.** (#90 Subsets II / #40 Combination Sum II, or #46 Permutations).

> **⚠️ B-7 (self./ownership) is RE-ESCALATED to drill-now** — fired Day 27 (#211) AND Day 28 (#146), two days running. Micro-drill at the start of the next 2–3 sessions.
> **⚠️ Every Day-28 reset was a single site missed on the final pass** (`curr`/`curr3`, dropped root guard, missing `self.`). The fix is a deliberate final read-through: guard present? every name real & owned? multi-site change complete (M-027)?
> **#199 also mis-stated BFS space as O(1)** — it's **O(n)** (queue holds a full level). #146: `self.remove` not `remove`.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
