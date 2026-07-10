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
| Valid Palindrome (#125) | two-pointers | 7d | 2026-07-12 | 2 | F·F·F·F·P·P |
| Binary Search (#704) | binary-search | 7d | 2026-07-12 | 2 | P·P |
| Search a 2D Matrix (#74) | binary-search | 7d | 2026-07-13 | 2 | P·P |
| Koko Eating Bananas (#875) | binary-search | 1d | 2026-07-11 | 0 | P·F·P·F |
| Find Min in Rotated Sorted Array (#153) | binary-search | 7d | 2026-07-17 | 2 | F·P·F·P·P |
| Search in Rotated Array (#33) | binary-search | 7d | 2026-07-16 | 2 | P·P |
| Valid Parentheses (#20) | stack | 3d | 2026-07-13 | 1 | P·F·P |
| Min Stack (#155) | stack | 7d | 2026-07-17 | 2 | P·P |
| Evaluate RPN (#150) | stack | 3d | 2026-07-11 | 1 | P |
| Daily Temperatures (#739) | stack | 3d | 2026-07-11 | 1 | P |
| 3Sum (#15) | two-pointers | 3d | 2026-07-12 | 1 | F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | 2026-07-13 | 1 | P |
| Longest Consecutive Sequence (#128) | arrays-hashing | 3d | 2026-07-12 | 1 | P |
| Encode/Decode Strings (#271) | arrays-hashing | 3d | 2026-07-12 | 1 | P |
| Longest Substring No Repeat (#3) | sliding-window | 21d | 2026-07-30 | 3 | P·P·P |
| Best Time to Buy/Sell (#121) | sliding-window | 21d | 2026-07-31 | 3 | P·P·P |
| Reverse Linked List (#206) | linked-list | 1d | 2026-07-12 | 0 | (new) |
| Merge Two Sorted Lists (#21) | linked-list | 1d | 2026-07-12 | 0 | (new) |
| Linked List Cycle (#141) | linked-list | 1d | 2026-07-13 | 0 | (new) |
| Two Sum II (#167) | two-pointers | 7d | 2026-07-11 | 2 | P·P |
| Container With Most Water (#11) | two-pointers | 7d | 2026-07-11 | 2 | P·P |
| Top K Frequent (#347) | arrays-hashing | 21d | 2026-07-21 | 3 | P·P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d | 2026-07-23 | 3 | P·P·P |
| Two Sum (#1) | arrays-hashing | 21d | 2026-07-14 | 3 | P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 21d | 2026-07-14 | 3 | P·P·P |
| Valid Anagram (#242) | arrays-hashing | 21d | 2026-07-11 | 3 | P·P·P |
| Group Anagrams (#49) | arrays-hashing | 21d | 2026-07-11 | 3 | P·P·P |

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
