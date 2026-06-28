# Big-O & complexity  (knowledge file)

**Status:** ongoing training · **Mastery: 3/5**

You state **time AND space before coding**, then we correct. Complexity = the work actually done, *including inside loops and hidden operations*.

## What you've internalized
- The ladder: O(1) < O(log n) < O(n) < O(n log n) < O(n²).
- **Amortized analysis** (Day 8): a forward-only pointer shared across iterations makes a nested-looking loop O(n), not O(n²) — each element enters/leaves once.
- **Space is not free** (Day 5): building a new string/list/dict that scales with input is **O(n) space**, even if you "only loop once."
- **Hidden costs** (Day 3): a `sorted()` inside the loop made Group Anagrams O(n·k log k), not O(n).

## Gotchas to keep correcting
- Guessing **O(1) space** when you actually allocate a structure that grows with input.
- Forgetting to count the cost of operations *inside* a loop.
- Confusing "values vs indexes" when reasoning about what the loop touches.
