# Day 2 — Practice Notebook

**Week 1 · Day 2 — June 20, 2026**
**Topic:** Arrays & Hashing — frequency counting + grouping by a canonical key
**Solved:** Valid Anagram (Easy), Group Anagrams (Medium — first Medium!)

> Format: each block shows my **raw answer** exactly as submitted, then the **correction / coaching notes**.

---

## Block 1 — Warm-up retrieval (yesterday's problems, cold)

### Two Sum (dict)
**My raw answer:**
```python
seen = {}
for i in range(len(nums)):
    x = nums[i]
    y = target - x
    if y in seen:
        return [seen[y], i]
    seen[x] = i
```
**Correction:** ✅ Perfect. `nums` correct throughout — yesterday's fix stuck.

### Contains Duplicate (set)
**My raw answer:**
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    nums.add(num)      # <-- bug
return False
```
**Correction:** **Bug:** `nums.add(num)` adds to the wrong container (and lists have no `.add()` → would crash). Should be `seen.add(num)`. Same theme: be precise about *which* thing you're touching.
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False
```

---

## Block 2 — Valid Anagram (Easy)

**Problem:** Return `True` if `t` is an anagram of `s`, else `False`.
Example: `s="anagram", t="nagaram"` → `True` · `s="rat", t="car"` → `False`

**My raw answer:**
```python
sdict = {}
for letter in s:
    if letter in sdict={}:        # bug 1
        sdict[letter] += 1
    else:
        sdict[letter] = 1

for letter in t:
    if letter in sdict:
        if sdict[letter] > 0:
            sdict[letter] -= 1
            continue
        else:
            return False
return True
# O(n) time, O(n) space
```

**Correction:** Core idea (frequency counting + decrement) is **correct** — that's the important part. Three holes:
1. **Typo:** `if letter in sdict={}:` → `={}` is an assignment, invalid. Should be `if letter in sdict:`.
2. **No length check.** `s="aab", t="ab"` would return `True` (wrong — different lengths).
3. **No `else` for a t-letter not in the dict.** `s="ab", t="ac"` → `c` is skipped, returns `True` (wrong).

**Corrected:**
```python
def is_anagram(s, t):
    if len(s) != len(t):          # kills length mismatches instantly
        return False
    counts = {}
    for letter in s:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    for letter in t:
        if letter not in counts or counts[letter] == 0:
            return False
        counts[letter] -= 1
    return True
```
**Complexity:** O(n) time, O(n) space ✅ (had this right).
**Alternatives:** `sorted(s) == sorted(t)` (O(n log n), one line); `Counter(s) == Counter(t)` (Pythonic shortcut). In an interview, write the manual count and mention `Counter`.
**Pattern:** *frequency counting with a hashmap*.

---

## Block 3 — Group Anagrams (Medium · first Medium)

**Problem:** Group anagrams together.
Example: `["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"],["tan","nat"],["bat"]]`

**My raw first attempt:**
```python
inDict = {}
finalList = []
count = 0
for word in strs:
    fixed = "".join(sorted(word))
    if fixed in inDict:
        finalList[inDict[fixed]].append(word)
    else:
        inDict[fixed] = count
        count += 1
return finalList
# (thought it was O(n))
```

**Correction:** Clever approach (map signature → index in `finalList`) and **95% correct**. One bug: the `else` branch records the index but never creates the group, so `finalList` stays empty and the next matching signature hits `finalList[...]` → **IndexError**.
One-line fix:
```python
else:
    inDict[fixed] = count
    finalList.append([word])   # create the group with its first word
    count += 1
```

**Upgrade (recommended):** keeping `inDict`, `finalList`, and `count` in sync is what caused the bug. Let the dict hold the lists directly:

**My retrieval rep (clean version) — ✅ correct:**
```python
groups = {}
for word in strs:
    key = "".join(sorted(word))
    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]
return list(groups.values())
```
Pro shortcut: `from collections import defaultdict; groups = defaultdict(list)` then `groups[key].append(word)`.

**Complexity correction — important:** NOT O(n). For each of `n` words you call `sorted(word)`, costing O(k log k) for a word of length `k`:
- **Time: O(n · k log k)** — account for work *inside* the loop (the hidden sort).
- **Space: O(n · k)**.

**Pattern:** *group by a canonical key* — map each item to a shared signature, bucket in a dict.

---

## Side questions answered today
- **Can strings be compared with `==`?** Yes — compares by value, character for character. (Use it on *signatures*, not raw words, for anagrams.)
- **Can a set hold strings?** Yes — any hashable type.
- **What does `groups.values()` return?** A `dict_values` view of just the values (the grouped lists), keys dropped. It's a view, not a list — wrap in `list(...)` to index it. Siblings: `.keys()`, `.items()`.

---

## Takeaways

**Patterns learned:** frequency counting with a hashmap (Valid Anagram); group by a canonical key (Group Anagrams). Both are Arrays & Hashing core.

**Precision habits still to automate:**
1. Touch the *right container* (`seen.add`, not `nums.add`).
2. Watch invalid syntax in conditionals (`if x in d:`, not `if x in d={}`).
3. Handle edge cases up front (length check; unknown/extra elements).
4. **Account for the cost of operations inside a loop** when computing Big-O (a hidden `sorted()` is not free).

**Big win:** first Medium solved, and the clean version reproduced from memory.

**Spaced-review queue (re-solve cold):**
- Two Sum, Contains Duplicate → **June 22** (Day 3), **June 26** (Day 7)
- Valid Anagram, Group Anagrams → **June 23**, **June 27**

**Next session (Day 3):** warm-up retrieval (incl. the June 22 spaced re-solves), then continue Arrays & Hashing (e.g., Top K Frequent Elements, Product of Array Except Self).
