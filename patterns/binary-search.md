# Binary Search

**Status:** learned (Day 9) · **Mastery: 2/5** · Block A

## In one line
Halve a sorted search space (or a monotonic answer range) each step → O(log n).

## Reach for it when
- Input is sorted (or you can sort it cheaply)
- "Find min / first / last that satisfies…"
- Searching a monotonic **answer** space (e.g., min eating speed — Day 10)
- You need better than O(n) on a sorted array

## Template (classic — index search)
```python
left, right = 0, len(nums) - 1
while left <= right:                 # <= : the single-element case is still checked
    mid = (left + right) // 2        # // = integer (floor) division
    if nums[mid] < target:           # middle too SMALL → answer is to the RIGHT
        left = mid + 1
    elif nums[mid] > target:         # middle too BIG → answer is to the LEFT
        right = mid - 1
    else:
        return mid
return -1
```

### Variant — search a 2D matrix (#74, row-by-row sorted)
Binary-search the **virtual flattened index** `0 … rows*cols-1` (never built); convert `mid` → cell:
```python
cols = len(matrix[0])
val = matrix[mid // cols][mid % cols]    # row = mid // cols, col = mid % cols
```

## Complexity
- Classic: **O(log n)** time, **O(1)** space.
- 2D matrix: **O(log(m·n))** time, **O(1)** space.

## Your gotchas
- **Direction (M-012):** small middle → `left = mid + 1` (go right); big middle → `right = mid - 1` (go left). Inverted these on the first #704 try — *re-reason it, don't memorize symbols.*
- **`<=` not `<`** in the loop condition — otherwise you miss the last element when `left == right`.
- **±1 on the bounds** after checking `mid` — excludes the already-checked `mid` and guarantees the loop ends.
- Next: **binary search on the answer** (Koko, Day 10) — you don't search the array, you search a value range and ask "does this value work?"
