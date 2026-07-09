# Spaced-Repetition QUEUE — single source of truth for review state

> **Ladder:** `1d → 3d → 7d → 21d → 60d` → graduated. **Pass** = advance one rung. **Fail** (needed a hint, blanked, or a bug you couldn't self-fix) = **reset to 1d** + log the cause in `MISTAKES.md`. Re-solves are **from a blank screen**, never re-reading the solution.

## How to use each session
1. At session start, pull rows with **Next due ≤ today**, oldest first (cap ~3 in the sprint).
2. Re-solve from scratch *before* opening the pattern file.
3. Update the row: new rung + new due date + append result to `Results` (`P`/`F`). One write, here only.

## Overflow rule
If **due count > 8**, do reviews only (no new problem) until it's back under control — decay is the enemy, not volume.

## Due / Active
*(Seeded from Days 1–8. This is the live starting state — correct rungs as you actually re-solve.)*

| Problem | Pattern | Rung | Next due | Streak | Results |
|---|---|---|---|---|---|
| Valid Palindrome (#125) | two-pointers | 7d | 2026-07-12 | 2 | F·F·F·F·P·P |
| Binary Search (#704) | binary-search | 7d | 2026-07-10 | 2 | P·P |
| Search a 2D Matrix (#74) | binary-search | 7d | 2026-07-10 | 2 | P·P |
| Koko Eating Bananas (#875) | binary-search | 3d | 2026-07-10 | 1 | P·F·P |
| Find Min in Rotated Sorted Array (#153) | binary-search | 3d | 2026-07-10 | 1 | F·P·F·P |
| Search in Rotated Array (#33) | binary-search | 7d | 2026-07-16 | 2 | P·P |
| Valid Parentheses (#20) | stack | 1d | 2026-07-10 | 0 | P·F |
| Min Stack (#155) | stack | 3d | 2026-07-09 | 1 | P |
| Evaluate RPN (#150) | stack | 3d | 2026-07-11 | 1 | P |
| Daily Temperatures (#739) | stack | 3d | 2026-07-10 | 1 | P |
| 3Sum (#15) | two-pointers | 3d | 2026-07-12 | 1 | F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | 2026-07-11 | 1 | P |
| Longest Consecutive Sequence (#128) | arrays-hashing | 3d | 2026-07-12 | 1 | P |
| Encode/Decode Strings (#271) | arrays-hashing | 3d | 2026-07-12 | 1 | P |
| Longest Substring No Repeat (#3) | sliding-window | 21d | 2026-07-30 | 3 | P·P·P |
| Best Time to Buy/Sell (#121) | sliding-window | 7d | 2026-07-07 | 2 | P·P |
| Two Sum II (#167) | two-pointers | 7d | 2026-07-08 | 2 | P·P |
| Container With Most Water (#11) | two-pointers | 7d | 2026-07-08 | 2 | P·P |
| Top K Frequent (#347) | arrays-hashing | 21d | 2026-07-21 | 3 | P·P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d | 2026-07-23 | 3 | P·P·P |
| Two Sum (#1) | arrays-hashing | 21d | 2026-07-10 | 3 | P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 21d | 2026-07-10 | 3 | P·P·P |
| Valid Anagram (#242) | arrays-hashing | 21d | 2026-07-11 | 3 | P·P·P |
| Group Anagrams (#49) | arrays-hashing | 21d | 2026-07-11 | 3 | P·P·P |

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
