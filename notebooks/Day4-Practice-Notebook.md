# Day 4 — Practice Notebook

**Week 1 · Day 4 — June 22, 2026**
**Topic:** Product of Array Except Self — **prefix/suffix products**; first spaced re-solves
**Solved:** Product of Array Except Self (Medium)

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Warm-up (spaced re-solves + fresh reproduction)

### Two Sum (dict) — spaced re-solve (due June 22)
**Raw:**
```python
seen = {}
for index in range(len(nums)):
    x = nums[index]
    y = target - x
    if y in seen:
        return (seen[y], index)
    else:
        seen[nums[index]] = index
```
**Correction:** ✅ Correct logic. Two nits: return a **list** `[seen[y], index]` (LeetCode expects a list, not a tuple); and `seen[x] = index` is cleaner than `seen[nums[index]] = index`.

### Contains Duplicate (set) — spaced re-solve (due June 22)
**Raw:**
```python
seen = set()
for nums in num:          # bug: reversed
    if num in seen:
        return True
    else:
        seen.add(num)
# (no return False)
```
**Correction:** Two bugs.
1. `for nums in num` is **reversed** — should be `for num in nums` (walk each element `num` of the list `nums`). As written, `num` is undefined and `nums` gets clobbered.
2. Missing **`return False`** at the end (returns `None` when no duplicate).
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False
```
*Irony of the day: aced the hard problem, slipped on the easy one — autopilot. Precision matters even on Easies.*

### Top K Frequent (bucket sort) — fresh reproduction
**Raw:**
```python
aDict = {}
for num in nums:
    if num in aDict:
        aDict[num] += 1
    else:
        aDict[num] = 1
bucket = []
for i in range(len(nums) + 1):
    bucket.append([])
for key in aDict.keys():
    index = aDict[key]
    bucket[index].append(key)
final = []
for j in range(len(bucket) - 1, 0, -1):
    aList = bucket[j]
    for num in aList:
        final.append(num)
        if len(final) == k:
            return final
```
**Correction:** ✅✅ **Perfect** — full bucket sort reproduced from memory the day after learning it (during an overwhelming session, no less). This is the spaced-retrieval method working exactly as intended. Big win.

---

## Block 2 — Product of Array Except Self (Medium)

**Problem:** Return `answer` where `answer[i]` = product of every element **except** `nums[i]`. (Canonical constraints: no division, O(n).)
Example: `[1,2,3,4]` → `[24,12,8,6]`

### Attempt 1 (raw) — the division idea
```python
productOfAll = 1
for num in nums:
    productOfAll = productOfAll * num
final = []
for num in nums:
    value = productOfAll / num
    final.append[value]      # bug: brackets
return final
# O(n) time
```
**Correction:**
- 👏 Inventing the multiply-all-then-divide trick yourself is sharp.
- **Why division fails here:** zeros. `nums=[1,2,0,4]` → `productOfAll=0`, then `0/0` crashes, yet the correct answer `[0,0,8,0]` is well-defined. This is exactly why the problem **bans division**.
- **Bug:** `final.append[value]` → `.append(value)` ( `.append` is a method → parentheses, not brackets).

### The real technique — left × right (prefix/suffix products)
Key idea: `answer[i] = (product of everything LEFT of i) × (product of everything RIGHT of i)`. No division.

**One-pass trick (the new idea):** carry a running product; **append it BEFORE folding in `nums[i]`**, so position `i` excludes itself.

### Final solution (raw, assembled) — ✅ correct
```python
left = []
runningleft = 1
for i in range(len(nums)):
    left.append(runningleft)
    runningleft = runningleft * nums[i]

rightRev = []
runningright = 1
for j in range(len(nums) - 1, -1, -1):
    rightRev.append(runningright)
    runningright = runningright * nums[j]
right = rightRev[::-1]

final = []
for i in range(len(left)):
    final.append(left[i] * right[i])
return final           # <-- I forgot this line; remember to RETURN
```
- `left = [1,1,2,6]`, `right = [24,12,4,1]` → `final = [24,12,8,6]` ✓
- Bugs caught along the way: `runningright`/`runningRight` name mismatch (precision); `range(len-1, 0, -1)` missed index 0 → must be `range(len-1, -1, -1)` (stop is exclusive); forgot `return final`.

### Complexity (my derivation — ✅ correct)
- **Time O(n):** three separate loops → O(3n) → O(n).
- **Space O(n):** the `left` and `right` arrays. (Output array conventionally not counted as "extra.")

### Upgrade — O(1) extra space (drop the right array)
Carry a single `runningright` and multiply it straight into `answer` on the backward pass:
```python
answer = []
runningleft = 1
for i in range(len(nums)):
    answer.append(runningleft)
    runningleft = runningleft * nums[i]

runningright = 1
for i in range(len(nums) - 1, -1, -1):
    answer[i] = answer[i] * runningright   # overwrite in place
    runningright = runningright * nums[i]
return answer
```
Same O(n) time, but O(n) → **O(1) extra space**. Both versions are interview-fine.

---

## Takeaways
**Pattern learned:** **prefix/suffix products** — when each answer depends on "everything except me," precompute running products from the left and the right. (Generalizes: prefix sums, etc.)

**Precision habits:**
1. `for ITEM in LIST` ordering — *item* on the left, *list* on the right. (`for num in nums`, not `for nums in num`.)
2. **Always `return` the result** — happened twice today (Contains Duplicate, the combine loop). Make it a reflex.
3. Consistent variable spelling (`runningright` vs `runningRight`).
4. "stop is exclusive" in `range(start, stop, step)` — to include index 0 going down, stop at `-1`.

**Headline win:** reproduced bucket sort cold, and solved a Medium with a brand-new technique mostly self-driven.

**Spaced-review queue (re-solve cold):**
- Two Sum, Contains Duplicate → next: **June 26**
- Valid Anagram, Group Anagrams, Top K Frequent → **June 23**, **June 27**
- **Product of Array Except Self** → **June 25**, **June 29** *(also reproduce as tomorrow's warm-up)*

**Next session (Day 5):** warm-up (reproduce Product of Array Except Self), then continue Arrays & Hashing or start Two Pointers.
