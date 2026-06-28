# Two Pointers

**Status:** learned (Days 5–6) · **Mastery: 3/5** · Block A

## In one line
Two indices walking a (usually sorted) sequence to avoid an O(n²) scan.

## Reach for it when
- Sorted array + find a pair/triple hitting a target.
- Compare from both ends inward (palindrome, reverse).
- Partition / dedupe in place.
- A greedy "move the more constrained side" choice (water container).

## Sub-techniques you've done
- Both-ends symmetry — Valid Palindrome (#125)
- Sorted-pair search — Two Sum II (#167)
- Greedy move-the-shorter-wall — Container With Most Water (#11)

## Template
```python
left, right = 0, len(s) - 1
while left < right:
    # decide which side to move based on the comparison
    left += 1   # or right -= 1
```

## Complexity
O(n) time, **O(1) space** — *if* you work in place. (Cleaning a string into a new one = O(n) space.)

## Your gotchas (from the log)
- Name them `left`/`right`, not `i`/`j`.
- Building a cleaned string for Valid Palindrome is **O(n) space**, not O(1) (you guessed O(1) on Day 5 — corrected).
- **Say the pattern out loud before coding** (you skipped this Day 6).
