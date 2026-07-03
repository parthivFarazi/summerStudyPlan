# Day 13 — Practice Notebook

**Week 2 · Day 13 — July 3, 2026**
**Topic:** Block 1 — 3 binary-search reviews (blank screen). Block 2 — NEW: Search in Rotated Array (#33) + first **Stack** problem, Valid Parentheses (#20).
**New patterns:** Stack (LIFO via list). **New syntax:** chained comparison `a <= x < b`; compound `and`/`or`.

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Warm-up — reflexes (2/2 correct)
1. Converging find-min: `return nums[left]` ✅ (the meeting point *is* the answer; no tracked candidate — M-015).
2. Target search loop → `while left <= right` ✅. Sharpened the *why*: target search moves `mid ± 1` so the pointers **cross** (`<=` lets you test the final lone element); converging moves `right = mid` so they **meet** (`<`). The loop condition follows from how you move.

---

## Block 1 — Due re-solves (all PASS)

### Review 1 — Binary Search (#704) ✅ PASS (3d → 7d)
Correct algorithm cold: right directions, `<=`, `return mid` / `return -1`. **Slip:** wrote `for left <= right:` instead of `while` (**M-016**, self-owned immediately). O(log n) / O(1).

### Review 2 — Search a 2D Matrix (#74) ✅ PASS (3d → 7d)
Clean first try. Virtual-flattened index `matrix[mid // cols][mid % cols]`, `while` loop, variable audit clean, complexity O(log(m·n)) / O(1) stated precisely. Nothing to fix.

### Review 3 — Find Min in Rotated (#153) ✅ PASS (1d → 3d) — **retest of the Day 12 fail**
```python
left = 0
right = len(nums) - 1
while left < right:
    mid = (left + right) // 2
    if nums[mid] <= nums[right]:
        right = mid
    else:
        left = mid + 1
return nums[left]
```
`return nums[left]`, **no tracked answer** — yesterday's M-015 bug gone. Verified `[2,1]→1`, `[5]→5`. (Comment said "mid = right"; code correctly does `right = mid` — verbal flip only.)

---

## Block 2 — NEW problems

### New 1 — Search in Rotated Sorted Array (#33)  ·  hardest yet
**Idea (built himself, with scaffolding):** still plain binary search (O(log n)); the twist is that at each `mid`, **one half is always sorted**. Detect it, then range-test:
- `nums[left] <= nums[mid]` → **left half sorted** → `nums[left] <= target < nums[mid]` decides direction.
- else → **right half sorted** → `nums[mid] < target <= nums[right]` decides direction.

Key sub-insight he flagged himself: the range-test is safe because it's **nested inside** the "which half is sorted" guard — the unsorted half never gets the wrong test.

**Bug — inverted ALL FOUR pointer updates (M-012 recurrence 2):** wrote `left = mid - 1` / `right = mid + 1` where it should be `right = mid - 1` / `left = mid + 1`. Fixed on the rule: **"the pointer you move is the *opposite* wall from the direction you're heading"** (go left → pull `right` in; go right → pull `left` in). He already does this correctly in #704 — the inversion only showed up under the harder nesting.

**Final (correct):**
```python
left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[left] <= nums[mid]:            # left half sorted
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:                                   # right half sorted
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
return -1
```
Verified `target=0→4`, `3→-1`, `6→2`. O(log n) / O(1).

### New 2 — Valid Parentheses (#20)  ·  first STACK problem
**Stack pre-taught first** (LIFO, list `.append`/`.pop`/`[-1]`). Approach: push openings; on a closing bracket the top must be its matching opening (via a **pair dict** closing→opening); at the end the stack must be **empty**.

**Three bugs, fixed by iteration:**
1. `stack.append()` — forgot the item → `stack.append(char)`.
2. Match looked up the wrong key: `aDict[x]` (x is the popped *opening* → KeyError; keys are *closings*) → fixed to `aDict[char] != x` (look up the current closing, compare to popped top).
3. Final `return True` ignored leftover openings. First tried a band-aid `if len(s) < 2: return False` (leaks on `"(("`) → corrected to `return len(stack) == 0` — the stack itself is what knows if anything's unclosed.

**Final (correct):**
```python
aDict = {")": "(", "]": "[", "}": "{"}
stack = []
for char in s:
    if char not in aDict.keys():      # opening
        stack.append(char)
    else:                             # closing
        if len(stack) > 0:
            x = stack.pop()
            if aDict[char] != x:
                return False
        else:
            return False
return len(stack) == 0
```
Verified `"()"`, `"()[]{}"`, `"(]"`, `"([)]"`, `"{[]}"`, `"("`, `"(("`, `")("`. O(n) time, O(n) stack space.

---

## Takeaways

**Biggest win:** built #33 — the hardest problem in the plan — mostly himself: which-half-is-sorted, the range test, and the nesting insight. Real progress on binary-search reasoning.

**Keeper #1 (M-012, 2nd time):** *the pointer you move is the opposite wall from the direction you go.* Go left → `right = mid - 1`; go right → `left = mid + 1`. Felt it twice now — should stick.

**Keeper #2 (new pattern — Stack):** LIFO via a list. Push opens, match closes against the top with a pair dict, and the **end-state check** (`stack` empty) is part of correctness, not an afterthought. Don't reach for a length/shape band-aid when the data structure already carries the answer.

**Precision watch:** `for`/`while` mix-up (M-016) and a couple of first-time stack slips (empty-arg `append`, dict direction). No classic wrong-*name* slip today — but keep running the variable audit (B-1 still active).

**Spaced-review queue (after today):**
- #125, #875, **#33 (new)**, **#20 (new)** → **Jul 4**
- #153 → Jul 6; #121 → Jul 7; #167, #11 → Jul 8; #3 → Jul 9
- #704, #74 → Jul 10; #1, #217 → Jul 10; #242, #49 → Jul 11; #347 → Jul 21; #238 → Jul 23

**Next session (Day 14):** Block 1 reviews (due: #125, #875, #33, #20); **new** — Min Stack (#155): a class holding two lists (value stack + running-min stack), O(1) per op.
