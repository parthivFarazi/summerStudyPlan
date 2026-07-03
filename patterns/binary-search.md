# Binary Search

**Status:** learned (Day 9–13) · **Mastery: 3/5** · Block A

## In one line
Halve a sorted / monotonic search space each step → O(log n). Three shapes: **index-search**, **answer-search**, **converge-to-a-boundary**.

## Reach for it when
- Sorted input; "find min / first / last that satisfies…"; a monotonic **answer** space; the **pivot/min of a rotated** array; need better than O(n).

## Template 1 — classic index search (#704)
```python
left, right = 0, len(nums) - 1
while left <= right:                  # target search → <=
    mid = (left + right) // 2
    if nums[mid] < target:            # too SMALL → go RIGHT
        left = mid + 1
    elif nums[mid] > target:          # too BIG → go LEFT
        right = mid - 1
    else:
        return mid
return -1
```
### Variant — 2D matrix (#74)
Search the virtual flattened index `0…rows*cols-1`; `val = matrix[mid // cols][mid % cols]`.

## Template 2 — binary search ON THE ANSWER + boundary (Koko #875)
Search a **value range**, not the array; for "smallest value that satisfies X":
```python
left, right, result = 1, max(piles), max(piles)
while left <= right:
    mid = (left + right) // 2
    if hours_needed(mid) <= h:   # works → record + shrink for a smaller one
        result = mid
        right = mid - 1
    else:
        left = mid + 1
return result
```
- **Never `return mid` on an exact match** in a find-minimum search (M-013).

## Template 3 — CONVERGING search / find-min in rotated array (#153)
No explicit target — converge two pointers onto the answer:
```python
left, right = 0, len(nums) - 1
while left < right:                # STRICT < (converging), NOT <=
    mid = (left + right) // 2
    if nums[mid] <= nums[right]:   # mid in the lower run → min is mid or left
        right = mid                # keep mid — it might BE the min (NOT mid-1)
    else:                          # mid in the higher run → min is to the right
        left = mid + 1
return nums[left]                  # they meet ON the answer
```
- Compare `mid` to an **end** (`nums[right]`), not a target.
- **`<=` + `right = mid` → infinite loop (M-014).**

## Template 4 — search a ROTATED array for a target (#33)
Target search (`while left <= right`, `mid ± 1`), but pick the side by which half is **sorted**:
```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[left] <= nums[mid]:                 # LEFT half sorted
        if nums[left] <= target < nums[mid]:
            right = mid - 1                     # go left
        else:
            left = mid + 1                      # go right
    else:                                        # RIGHT half sorted
        if nums[mid] < target <= nums[right]:
            left = mid + 1                      # go right
        else:
            right = mid - 1                     # go left
return -1
```
- One half is **always** sorted; the range-test lives **nested inside** its "this half is sorted" guard, so the unsorted half never gets the wrong test.
- **Pointer = the OPPOSITE wall from where you go** (go left → `right = mid - 1`; go right → `left = mid + 1`). Inverting these = **M-012** (Day 9, again Day 13).

## Complexity
- Index / 2D / converging: **O(log n)** / **O(log(m·n))** / **O(log n)** time, **O(1)** space.
- Answer-search: **O(n · log(range))**, O(1) space.

## Your gotchas
- Direction (M-012): small mid → right, big mid → left. Boundary (M-013): record + shrink, never return on `==`. Converge (M-014): strict `<` + `right = mid`.
- **Rule of thumb:** *has a target →* `<=`, `mid ± 1`. *Converging to a spot →* `<`, `right = mid`, `return nums[left]`.
- **Converge-return (M-015):** the loop-exit index IS the answer — `return nums[left]`. Don't reintroduce a tracked `answer`; a default (`answer = 0`) leaks on `[2,1]` / single-element `[5]`. (Had it right Day 11, regressed Day 12.)
- `math.ceil(a / b)` rounds up (`import math`).
