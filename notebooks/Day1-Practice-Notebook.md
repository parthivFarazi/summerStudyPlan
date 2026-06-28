# Day 1 — Practice Notebook

**Week 1 · Day 1 — June 19, 2026**
**Topic:** Python on-ramp + Big-O foundations
**Goal:** Close the syntax gap; learn to read complexity; apply the hashmap/set pattern.

> Format: each block shows my **raw answer** exactly as I submitted it, then the **correction / coaching notes**.

---

## Block 1 — Retrieval rep: Two Sum (from memory)

**My raw answer:**
```python
def two_sums(nums, target):
    seen = {}
    for i in range(len(nums)):
        x = num[i]
        y = target - num[i]
        if y in seen:
            return[i, seen[y]]
        seen[x] = i
```

**Correction:**
- Logic is **correct** — near-perfect reproduction of the O(n) dict solution.
- **Bug:** `num[i]` should be `nums[i]` (twice). `num` is undefined → `NameError`. Use the *exact* declared name.
- Returning `[i, seen[y]]` is fine — pair order doesn't matter for Two Sum.

**Corrected:**
```python
def two_sum(nums, target):
    seen = {}                          # number -> index
    for i in range(len(nums)):
        x = nums[i]
        y = target - nums[i]           # partner that completes the pair
        if y in seen:
            return [seen[y], i]
        seen[x] = i
```

**Why it's O(n):** one pass over `n` elements, and each step (dict lookup + insert) is O(1) → `n × O(1)` = **O(n)**. Space is **O(n)** for the dict.

---

## Block 2 — Syntax drills

### #1 — Print 0 through 4
**My raw answer:**
```python
for i in range(5):
    print(i)
```
**Correction:** ✅ Correct.

### #2 — Print each element and its index
**My raw answer:**
```python
for i in range(len(nums)):
    print(i, num[i])
```
**Correction:** Logic correct. **Bug:** `num[i]` → `nums[i]` again.
```python
for i in range(len(nums)):
    print(i, nums[i])
```

### #3 — `total(nums)` without built-in `sum`
**My raw answer:**
```python
def total(nums):
    finalTotal = 0
    for i in range(nums):
        finalTotal += nums[i]
    return(finalTotal)
```
**Correction:** Accumulator pattern is correct. **Bug:** `range(nums)` → `range(len(nums))`. `range()` needs an integer (the length), not the list.
```python
def total(nums):
    finalTotal = 0
    for i in range(len(nums)):
        finalTotal += nums[i]
    return finalTotal
```
*(Note: I got `range(len(...))` right in #2, #4, #6 — so I know it; it's just not automatic yet.)*

### #4 — Build a dict mapping fruit → index
**My raw answer:**
```python
dict={}
for i in range(len(fruits)):
    dict[fruits[i]] = i
```
**Correction:** Logic correct. **Style:** don't name a variable `dict` — it shadows the built-in type. Rename it.
```python
fruit_index = {}
for i in range(len(fruits)):
    fruit_index[fruits[i]] = i
```

### #5 — Check if "banana" is a key, print its index
**My raw answer:**
```python
if "banana" in dict:
    print (dict["banana"])
```
**Correction:** ✅ Correct (just rename `dict`).

### #6 — Return a new list with each number doubled
**My raw answer:**
```python
doubleNums = []
for i in range(len(nums)):
    toAdd = nums[i] * 2
    doubleNums.append(toAdd)
return doubleNums
```
**Correction:** ✅ Correct. Clean build-a-new-list pattern with `.append()`.

---

## Block 3 — Big-O foundations

**Key ideas:**
- Big-O measures how runtime grows as input size `n` grows — the *shape*, not seconds.
- **O(1)** constant: dict lookup/insert, `nums[i]`.
- **O(n)** linear: one loop over `n` items.
- **O(n²)** quadratic: nested loop over `n` (loops *multiply*).
- **O(log n)** logarithmic: halving each step (binary search — Week 2).
- Rules: **drop constants and smaller terms** (O(2n) → O(n)); **nested loops multiply, separate loops add**.
- **Space complexity** = extra memory used (e.g., the dict in Two Sum is O(n) space).

### Quiz — my raw answers + corrections (scored 5/5 ✅)

**1. Why is the dict Two Sum O(n)?**
> My answer: "Because we have to iterate through the whole list once, which makes it n times. However since we are just using the dict to find whether the number exists or not, it is O(1) so the dominant Big (O) takes over, which is O(n)"

✅ Correct. Sharper wording: `n` iterations × O(1) work each = **O(n)**. The loop's O(n) dominates the constant work inside it.

**2. Time complexity of `total()`?**
> My answer: O(n)

✅ Correct — single loop.

**3. A loop nested inside another, each running `n` times?**
> My answer: O(n^2)

✅ Correct — nested loops multiply.

**4. One loop over `n`, then a *separate* second loop over `n`. Overall?**
> My answer: O(n)

✅ Correct (the tricky one). O(n) + O(n) = O(2n) → drop the constant → **O(n)**. (Separate loops add; nested loops multiply.)

**5. Space complexity of dict Two Sum, and why?**
> My answer: O(n) because it is using the space of n for the dictionary

✅ Correct.

---

## Block 4 — Contains Duplicate (full daily loop)

**Problem:** Return `True` if any value in `nums` appears at least twice, else `False`.
Example: `[1, 2, 3, 1]` → `True` · `[1, 2, 3, 4]` → `False`

### Brute force
**My raw answer:**
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if i == j:
            return True
return False
# O(n^2)
```
**Correction:** Structure is right (starting `j` at `i + 1` is correct). **Bug:** `if i == j` compares the *indexes* — and since `j` always starts at `i + 1`, they can never be equal, so it always returns `False`. Compare the **values**:
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:     # compare what's AT those positions
            return True
return False
# O(n^2) time, O(1) space
```

### Dict version
**My raw answer:**
```python
seen = {}
for i in range(len(nums)):
    if nums[i] in seen:
        return True
    seen[nums[i]] = i
return False
# O(n) time, O(n) space
```
**Correction:** ✅ Correct, and complexity is right.

**Upgrade — use a `set`:** I stored an index I never used. When I only need *"have I seen this?"*, a `set` is the cleaner tool:
```python
seen = set()
for num in nums:          # no index needed -> loop the values directly
    if num in seen:
        return True
    seen.add(num)
return False
# O(n) time, O(n) space
```

**Decision rule:** need the position/value back → **dict** (Two Sum). Only need presence → **set** (Contains Duplicate).

**Pattern tag:** same pattern as Two Sum → **"hashmap/set for O(1) lookup."**

---

## Takeaways

**Patterns learned:** Hashmap/set for O(1) lookup (Two Sum, Contains Duplicate).

**3 precision habits to keep tightening:**
1. Exact variable names — `nums`, not `num`.
2. `range(len(x))`, not `range(x)`.
3. Compare *values* vs *indexes* deliberately (`nums[i] == nums[j]`, not `i == j`).

> None are knowledge gaps — they're just not automatic yet. Week 1 makes them automatic.

**Spaced-review queue (re-solve cold, from a blank screen):**
- Two Sum → **Day 3 (June 22)**, **Day 7 (June 26)**
- Contains Duplicate → **Day 3 (June 22)**, **Day 7 (June 26)**

**Next session (Day 2):** warm-up retrieval first, then more Arrays & Hashing — Valid Anagram, Group Anagrams.
