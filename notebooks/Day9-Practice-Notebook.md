# Day 9 — Practice Notebook

**Week 2 · Day 9 — June 29, 2026**
**Topic:** New pattern — **Binary Search** (#704 + #74); spaced re-solves
**Solved:** Valid Palindrome (review), Longest Substring (review), Binary Search #704, Search a 2D Matrix #74

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Due re-solves (cold)

### #125 Valid Palindrome — ❌ FAIL (3rd time) → queue resets to 1d
**My raw answer (bug):**
```python
clean = ""
for char in s:
    if char.isalnum():
        clean = clean + char.lower()
left = 0
right = len(clean) - 1
while left < right:
    if s[left] != s[right]:      # BUG: compared s, not clean
        return False
    else:
        left = left + 1
        right = right - 1
return True
```
**Correction:** built `clean`, then compared the **original `s`**. The pointers walk `0…len(clean)-1` but index into `s` → wrong chars (caps/spaces). Fix: `clean[left] != clean[right]`.
**Root cause:** referencing the **wrong variable/container** — same family as `nums.add` vs `seen.add` (**M-004**, now recurrence 2 → watchlist). Every #125 miss has been a small precision slip, never the algorithm.
**Complexity:** O(n) time, O(n) space (the `clean` string).

### #3 Longest Substring Without Repeating — ✅ PASS → advances 1d→3d
```python
seen = set()
left = 0
maxLen = 0
for right in range(len(s)):
    if s[right] not in seen:
        seen.add(s[right])
    else:
        while s[right] in seen:
            seen.remove(s[left])
            left = left + 1
        seen.add(s[right])
    maxLen = max(maxLen, right - left + 1)
return maxLen
```
**Correction:** correct, clean. And the complexity reasoning was unprompted + right: **"O(n) because it's O(2n) — right adds to the set, left removes"** (amortized analysis from Day 8, applied perfectly). O(n) time, O(n) space.

---

## Block 2 — Binary Search (new pattern)

**Concept:** on a **sorted** array, look at the middle and eliminate **half** each step → **O(log n)**. Mechanics taught:
- `mid = (left + right) // 2` — `//` is integer (floor) division.
- `while left <= right:` — `<=` (not `<`), since `left`/`right` are the bounds of the region still being searched; when `left == right` there's still one element to check.
- After checking `mid`: go right `left = mid + 1`, or left `right = mid - 1` (the **±1** excludes the already-checked `mid` and guarantees termination).
- Direction: `nums[mid] < target` → go **right**; `nums[mid] > target` → go **left**.

### #704 Binary Search — attempt 1 inverted, then ✅
**Raw attempt 1 (branches swapped):**
```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] > target:
        left = mid + 1        # BUG: too-big middle → should go LEFT
    elif nums[mid] < target:
        right = mid - 1       # BUG: too-small → should go RIGHT
    else:
        return mid
return -1
```
**Corrected:**
```python
left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1
    else:
        return mid
return -1
```
**Root cause of the bug:** inverted the discard direction (**M-012**, new). Reasoning to keep: *middle too small ⇒ go right; middle too big ⇒ go left.*
**Complexity:** O(log n) time (halving), O(1) space (just pointers).

### #74 Search a 2D Matrix — ✅ correct first try
**Idea taught — virtual flattening:** the matrix reads row-by-row as one sorted list of `rows*cols` elements. Binary-search the *virtual* index `0 … rows*cols-1` (never built), converting each `mid` to a real cell: `row = mid // cols`, `col = mid % cols` (`%` = remainder; `divmod(mid, cols)` gives both).
**My raw answer (correct):**
```python
left = 0
right = (len(matrix) * len(matrix[0])) - 1
while left <= right:
    mid = (right + left) // 2
    midVal = matrix[mid // len(matrix[0])][mid % len(matrix[0])]  # cols = len(matrix[0])
    if midVal < target:
        left = mid + 1
    elif midVal > target:
        right = mid - 1
    else:
        return True
return False
```
**Correction:** none — correct on the first attempt, right direction (carried over from #704), and **complexity stated unprompted**: O(log(m·n)) time, O(1) space. 👏

---

## Takeaways
**Pattern learned:** **Binary Search** — halve a sorted space each step (O(log n)). Variant: search a 2D matrix by binary-searching the virtual flattened index and converting with `// cols` and `% cols`.

**New syntax:** `//` (integer division), `%` (remainder) / `divmod`, 2D indexing `matrix[r][c]`, `while left <= right`.

**Mastery notes:** mechanics are solid; the one reflex still to build is the **discard direction** (small→right, big→left).

**Precision habit (escalating):** wrong-variable references — `s` vs `clean` today (M-004, now 2). One more and it becomes a drilled blocker. Pre-flight check: before running, scan each variable name — "is this the exact one I meant?"

**Spaced-review queue (after today):**
- #125 Valid Palindrome → **Jun 30** (reset to 1d, F·F·F)
- #704 Binary Search, #74 Search a 2D Matrix → **Jun 30** (new, rung 1d)
- Best Time to Buy/Sell #121 → Jun 30
- #3 Longest Substring → **Jul 2** (advanced to 3d)
- Two Sum II #167, Container #11 → Jul 1; Top K #347 → Jul 1; Product #238 → Jul 3

**Next session (Day 10):** review due recalls, then **Binary Search — Koko Eating Bananas (#875)** = "binary search on the *answer*" (pre-teach `math.ceil` + a helper function).
