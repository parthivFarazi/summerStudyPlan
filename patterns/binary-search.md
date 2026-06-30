# Binary Search

**Status:** learned (Day 9–10) · **Mastery: 3/5** · Block A

## In one line
Halve a sorted search space — an **array index range** OR a **monotonic answer range** — each step → O(log n).

## Reach for it when
- Input is sorted (or you can sort it cheaply)
- "Find min / first / last that satisfies…"
- **Searching a monotonic answer space** (min speed, min capacity, smallest divisor) — Koko #875
- You need better than O(n) on a sorted array

## Template 1 — classic index search (#704)
```python
left, right = 0, len(nums) - 1
while left <= right:                  # <= : single-element case still checked
    mid = (left + right) // 2
    if nums[mid] < target:            # middle too SMALL → go RIGHT
        left = mid + 1
    elif nums[mid] > target:          # middle too BIG → go LEFT
        right = mid - 1
    else:
        return mid
return -1
```
### Variant — 2D matrix (#74)
Binary-search the virtual flattened index `0 … rows*cols-1`; `val = matrix[mid // cols][mid % cols]`.

## Template 2 — binary search ON THE ANSWER + boundary (Koko #875)
Search a **value range**, not the array — for "smallest value that satisfies a condition":
```python
import math
left, right = 1, max(piles)      # the ANSWER range, not indices
result = right                   # a known-valid fallback (max speed always works)
while left <= right:
    mid = (left + right) // 2
    if hours_needed(mid) <= h:   # works → record candidate...
        result = mid
        right = mid - 1          # ...and keep shrinking for a smaller one
    else:                        # too slow → go faster
        left = mid + 1
return result

def hours_needed(k):             # the O(n) "works?" check
    return sum(math.ceil(p / k) for p in piles)
```
- **Never `return mid` on an exact match** in a find-minimum search — an exact hit is still just a *candidate* (**M-013**). Record + shrink + return `result`.

## Complexity
- Classic / 2D: **O(log n)** / **O(log(m·n))** time, **O(1)** space.
- Answer-search: **O(n · log(range))** — `log(range)` search steps × an O(n) check each. O(1) space.

## Your gotchas
- **Direction (M-012):** small middle → go right; big middle → go left. *Re-reason it*, don't memorize symbols.
- **`<=` not `<`** in the loop condition; **±1** on the bound after checking `mid`.
- **Boundary search (M-013):** record candidate + keep shrinking; never bail out on `==`.
- `math.ceil(a / b)` rounds up (needs `import math`).
