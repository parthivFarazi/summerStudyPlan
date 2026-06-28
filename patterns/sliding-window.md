# Sliding Window

**Status:** learned (Days 7–8) · **Mastery: 2/5** (still firming up) · Block A

## In one line
A moving window over a sequence that maintains *running state*; expand the right edge, shrink the left to keep the window valid.

## Reach for it when
- Contiguous subarray/substring with a constraint (longest/shortest/at-most-k distinct).
- A "running" max/min/sum as you scan.
- You'd otherwise recompute over overlapping ranges.

## Sub-techniques you've done
- Running-state form — Best Time to Buy/Sell Stock (#121): track running-min + best-profit (just 2 vars).
- Variable-size window — Longest Substring Without Repeating (#3): set + shrink-from-left.

## Template
```python
left = 0
state = ...                      # the minimum you need (a set, a count, a running min)
for right in range(len(s)):
    # include s[right] in state
    while not_valid(state):
        # remove s[left] from state
        left += 1
    answer = max(answer, right - left + 1)
```

## Complexity
O(n) by **amortized analysis** — each element is added once and removed at most once; forward-only pointers ⇒ not O(n²).

## Your gotchas (from the log)
- **Keep the minimum necessary state** — Day 7 you over-engineered with 4 vars + time-guards; the answer was 2 vars.
- Don't carry assumptions across problems — Day 8 you imported `k log k` from Group Anagrams (there's no sort here).
- **Read the spec/example** for work you must do (e.g., "alphanumeric only" = real work).
