# Day 3 — Practice Notebook

**Week 1 · Day 3 — June 20, 2026**
**Topic:** Top K Frequent Elements + **bucket sort**; active time/space complexity
**Solved:** Top K Frequent Elements (Medium) via bucket sort

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Warm-up retrieval (cold)

### Valid Anagram
**My raw answer:**
```python
if len(s) != len(t):
    return False
return "".join(sorted(s)) == "".join(sorted(t))
```
**Correction:** ✅ Correct (sorting approach). Complexity note: this is **O(n log n)** (the sort), vs the **O(n)** counting-loop version. Both fine; keep the O(n) version in your back pocket for "can you do better?"

### Group Anagrams
**My raw answer:**
```python
guide = {}
for word in strs:
    key = "".join(sorted(word))
    if key in guide:
        guide[key].append(word)
    else:
        guide[key] = [word]
return list(guide.values())
```
**Correction:** ✅ Perfect.

---

## Block 2 — Top K Frequent Elements (Medium)

**Problem:** Return the `k` most frequent elements of `nums` (any order).
Example: `nums=[1,1,1,2,2,3], k=2` → `[1,2]`

### Attempt 1 (raw)
```python
aDict = {}
for num in nums:
    if num in aDict:
        aDict[num] += 1
    else:
        aDict[num] = 1
keyList = list(aDict.keys())
freqList = list(aDict.values())
reverse = {}
for i in range(len(keyList)):
    reverse[freqList[i]] = keyList[i]
freqListsorted = sorted(freqList)
finalList = []
for j in k:
    key = freqListsorted[j]
    finalList.append(reverse[key])
return finalList
# guessed O(n), then suspected O(n log n) because of sorted
```
**Correction:**
- 👏 Frequency counting is automatic now, and you **caught the hidden sort cost yourself** ("suspect O(n log n) because of sorted") — exactly the skill we're training. Correct: it's **O(n log n)**.
- **Fatal flaw:** `reverse[freq] = num` — two numbers with the same frequency collide and one is overwritten (inverting a dict only works when values are unique). `nums=[1,1,2,2,3]` would drop a number.
- **Bug:** `for j in k` — `k` is an int, can't loop it → `range(k)`.
- **Bug:** `sorted(...)` is ascending; you want the *largest* → would pull the least frequent.

### Attempt 2 (raw) — fixed the ties, two bugs left
```python
# ... counts dict same as before ...
reverse = {}
for i in range(len(freqList)):
    if freqList[i] in reverse:
        reverse[freqList[i]].append(keyList[i])
    else:
        reverse[freqList[i]] = [keyList[i]]
freqLista = sorted(freqList)
freqListsorted = freqLista[::-1]
final = []
for i in range(len(freqListsorted)):
    key = freqListsorted[i]
    aList = reverse[key]
    for j in aList:
        final.append(aList[j])     # bug
        if len(final) == k:
            return final
```
**Correction:**
- 👏 **You fixed the fatal flaw yourself** — mapping `freq → list of numbers`. That was the hard leap.
- **Bug (recurring values-vs-index):** `for j in aList` makes `j` a *number*, then `aList[j]` treats it as an index → wrong/crash. Should be `final.append(j)`.
- **Bug:** `freqList` has duplicate frequencies, so a frequency can be processed twice → duplicates in output. e.g. `nums=[1,1,2,2,3], k=3` → `[1,2,1]`. Fix: walk **unique** frequencies.

### ⚠️ Coaching reset (my mistake)
I then showed a "clean" version using `.get()`, `.items()` unpacking, `setdefault`, `sorted(reverse=True)`, and a list comprehension **all at once** — overload. New standing rule going forward: **teach each new Python concept on its own, one at a time, before it appears in a solution; default to your current toolkit.**

### Bucket sort — the version we built (in your toolkit)
**Idea:** use frequency as an *address*. Make bins where the bin's position = frequency; drop each number into `bins[its frequency]`; read bins from the right (highest) until you have `k`. No sorting → faster.

```python
def top_k_frequent(nums, k):
    # 1. count frequencies (your usual way)
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # 2. make empty bins, positions 0..len(nums)
    bins = []
    for _ in range(len(nums) + 1):
        bins.append([])

    # 3. drop each number into the bin matching its frequency
    for num in counts.keys():
        freq = counts[num]
        bins[freq].append(num)

    # 4. read bins from the highest position down, until we have k
    result = []
    for freq in range(len(bins) - 1, 0, -1):
        for num in bins[freq]:
            result.append(num)
            if len(result) == k:
                return result
```

**Why `len(nums) + 1` bins / why a bin 0?** Keep *position = frequency* so indexing is clean. Max frequency is `len(nums)`, so we need a valid `bins[len(nums)]` → that's the `+1`. Bin 0 stays empty (no number has frequency 0); we just never read it (`range(..., 0, -1)` stops before it).

### Complexity (my own derivation + corrections)
**My answer:** O(n) time. Reasoning: no sorting; count dict O(n), bins O(n) → O(2n) → O(n); filling buckets "less than O(n) so wouldn't consider."
**Corrections:**
- ✅ Answer correct, and the lead instinct ("no sort → no log n") is the key skill.
- Don't drop a step for being "smallish." Filling buckets is **O(m), m ≤ n → O(n)** — same order, kept, just doesn't grow the total. We only drop **constants and lower-order terms** (`O(4n)→O(n)`).
- Missed a step: reading bins back is also O(n). Full tally: count O(n) + make bins O(n) + fill O(n) + read O(n) = O(4n) → **O(n)**.
- **Space:** my answer **O(n)** (`counts` O(n) + `bins` O(n) → O(2n) → O(n)); `result` is O(k) ≤ n. ✅ Correct — and you applied the constant-drop rule cleanly.

---

## Python concepts that came up today (revisit slowly — not yet solid)
- `dict.get(key, default)` — read a key, or get `default` if missing (avoids KeyError). One-liner for the if/else count.
- `dict.items()` + **tuple unpacking** (`for num, freq in counts.items()`) — loops key+value together; each pair is a tuple `(key, value)`.
- `dict.setdefault(key, [])` — get the list at key, creating `[]` first if missing.
- `sorted(x, reverse=True)` — descending sort. (The `reverse` keyword is unrelated to any variable named `reverse`.)
- **list comprehension** `[[] for _ in range(n)]` — compact way to build a list; `_` = "loop variable I don't use."
- `range(start, stop, step)` incl. **negative step** to count down: `range(5, 0, -1)` → 5,4,3,2,1 (stop excluded).

*Solid toolkit so far:* if/else dict building, lists + `.append()`, `.keys()`/`.values()`, `range(len(x))`, basic `for`, `sorted()`, sets, slicing `[::-1]`, `"".join(sorted(word))`, list indexing.

---

## Takeaways
**Patterns learned:** **bucket sort** — when the values you rank by (here, frequency) are bounded by `n`, index into a list instead of sorting → O(n) selection.

**Precision habits still to automate:**
1. **Values vs. indexes** — `final.append(j)` not `aList[j]`. (Showed up again — still your #1 slip.)
2. Inverting a dict only works if values are unique.
3. In Big-O, keep all same-order terms; only drop constants + lower-order terms.

**Meta:** flagged (rightly) that I was overloading you with new syntax. Fixed the approach — one new concept at a time, taught first.

**Spaced-review queue (re-solve cold):**
- Two Sum, Contains Duplicate → **June 22**, **June 26**
- Valid Anagram, Group Anagrams → **June 23**, **June 27**
- **Top K Frequent (bucket sort)** → **June 23**, **June 27** *(also do as tomorrow's warm-up while fresh)*

**Next session (Day 4):** warm-up (reproduce bucket sort + the June 22 spaced re-solves), then **Product of Array Except Self**.
