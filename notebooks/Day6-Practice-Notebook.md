# Day 6 — Practice Notebook

**Week 1 · Day 6 — June 26, 2026**
**Topic:** First **interleaved review** + Container With Most Water (two pointers, greedy)
**Solved:** Contains Duplicate, Two Sum, Product (interleaved) + Container With Most Water

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Interleaved review (mixed patterns, no labels)

*New technique:* problems given mixed and unlabeled — I have to **recognize** the pattern myself (the real interview skill). All three correct, all complexity correct.

### Problem A → Contains Duplicate (set)
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    else:
        seen.add(num)
return False
# O(n) / O(n)
```
✅ Correct, `return False` present.

### Problem B → Two Sum, unsorted (hashmap)
```python
aDict = {}
for i in range(len(nums)):
    x = nums[i]
    y = target - x
    if y in aDict:
        return [aDict[y], i]
    else:
        aDict[x] = i
# O(n) / O(n)
```
✅ Correct, returns a **list** (old tuple slip fixed). **Key recognition:** array is *unsorted* → hashmap, NOT two pointers. (Sorted → two pointers for O(1) space.)

### Problem C → Product of Array Except Self (prefix/suffix)
```python
answer = []
leftRun = 1
for i in range(len(nums)):
    answer.append(leftRun)
    leftRun = leftRun * nums[i]
rightRun = 1
for j in range(len(nums) - 1, -1, -1):
    answer[j] = answer[j] * rightRun
    rightRun = rightRun * nums[j]
return answer
# O(n) time, O(1) space
```
✅ Correct (O(1)-space version).

**Coaching note:** I skipped the **"name the approach + why"** step and went straight to code. My choices were right, but *articulating the tell* is the muscle (you must say it out loud in interviews). The tells:
- A → set: "have I seen this value?" → O(1) membership.
- B → hashmap: "find a pair summing to target" on an *unsorted* array → store value→index.
- C → prefix/suffix: each answer is "everything except me," no division → running products both sides.

---

## Block 2 — Container With Most Water (Medium)

**Problem:** `height[i]` = height of a vertical line at `i`. Pick two lines forming the container with the most water. Area between `i,j` = `(j - i) * min(height[i], height[j])`.
Example: `[1,8,6,2,5,4,8,3,7]` → `49`

**My raw answer:**
```python
left = 0
right = len(height) - 1
maxArea = 0
while left < right:
    area = (right - left) * min(height[i], height[j])   # BUG: i, j undefined
    if area > maxArea:
        maxArea = area
    if height[left] <= height[right]:
        left = left + 1
    else:
        right = right - 1
return maxArea
# O(n) time, O(1) space
```

**Correction:**
- 👏 **Nailed the hard insight:** move the **shorter** wall (`if height[left] <= height[right]: move left, else move right`). That's the crux of the problem, and the complexity is right.
- **Bug (precision):** `min(height[i], height[j])` uses undefined `i`/`j`. The pointers are `left`/`right`:
  ```python
  area = (right - left) * min(height[left], height[right])
  ```
  With that fix it returns `49`.

**Why "move the shorter wall" is correct:** the area is capped by the shorter wall. Moving the *taller* wall in shrinks width while the cap stays the same → area can only drop. Moving the *shorter* wall is the only move that might raise the cap. (Greedy two-pointer.)

---

## Takeaways
**Patterns:** Two Pointers now includes a **greedy** variant (Container — move the shorter wall). Plus first rep of **interleaving** for pattern recognition.

**Recognition tells (say these out loud before coding):**
- "Seen it before / duplicates?" → **set**
- "Pair summing to target," unsorted → **hashmap**; sorted → **two pointers**
- "Everything except me," no division → **prefix/suffix**
- "Most/least over a window from both ends" → **two pointers**

**Precision habits:**
1. Use the problem's *actual* variable names — `left`/`right`, not `i`/`j`. (Today's bug.)
2. `.append(x)` parentheses; `()` = do, `[]` = grab.
3. Articulate the pattern *before* coding (skipped today).

**Win:** reasoned out the greedy "move the shorter wall" rule independently — the non-obvious heart of the problem.

**Spaced-review queue (re-solve cold):**
- Valid Anagram, Group Anagrams, Top K Frequent → **June 27**
- Palindrome, Valid Palindrome, Two Sum II → **June 27**, **July 1**
- Two Sum, Contains Duplicate, Product → next **~July 1–3**
- **Container With Most Water** → **June 29**, **July 3**

**Next session (Day 7):** warm-up, then likely a new sub-pattern (sliding window) or a Week-1 consolidation + timed mixed set.
