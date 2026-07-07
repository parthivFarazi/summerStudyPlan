# Day 16 — Practice Notebook

**Week 2 · Day 16 — July 7, 2026**
**Topic:** Block 1 — 3 reviews (#875, #153, #739; the two converging retests). Block 2 — NEW: 3Sum (#15) + Longest Repeating Character Replacement (#424).
**Coaching shift:** first "less spoon-feeding" session — Parthiv derived both new problems; I guided with questions + minimal hints.

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Warm-up — recite the converging checklist (retrieval)
Got rules 1 and 3 solid (`while left < right`; `return nums[left]`). Rule 2 had a notation flip ("mid = right") → corrected to **`right = mid`, never `mid - 1`**.

---

## Block 1 — Due re-solves (all PASS — converging checklist stuck)

### #875 Koko ✅ PASS (1d → 3d)
`return left`, `right = mid`, no tracked answer. Traced `[30,11,23,4,20], h=5 → 30` (Day-15 breaker). O(n log m)/O(1).

### #153 Find Min ✅ PASS (1d → 3d)
`right = mid` (not mid-1), `return nums[left]`. Traced `[3,1,2] → 1`. O(log n)/O(1). **Both converging fails from Day 15 recovered.**

### #739 Daily Temperatures ✅ PASS (1d → 3d)
Guard-first monotonic stack, clean. O(n)/O(n).

---

## Block 2 — NEW

### #15 3Sum — derived mostly himself (with nudges)
**Approach he built:** sort → pin `i` as the first number → two-pointer the rest for target `-nums[i]` (recognized Two Sum II under it; realized "unsorted → sort it first" himself). 
**Bugs worked through:**
1. `==` branch didn't move the pointers → **infinite loop** (`if/elif` is exclusive, so a match with no movement locks in). Fix: move both pointers after appending.
2. `left = 0` → **`left = i + 1`** (only scan right of the pin) — he added this on his own.
3. **Dedup, two levels:** skip duplicate pin (`if i>0 and nums[i]==nums[i-1]: continue`) AND skip duplicate left after a match (`while left<right and nums[left]==nums[left-1]: left+=1`).
**Deep dive:** why the two skips aren't redundant (pin-skip = don't reuse the same *first* number across searches; left-skip = don't reuse the same *second* number within one search), and why left-skip **alone** suffices for correctness (a triplet is fixed by its first two numbers; `right` is forced). O(n²)/O(n).

**Final:**
```python
answer = []
aList = sorted(nums)
for i in range(len(aList)):
    if i > 0 and aList[i] == aList[i - 1]:
        continue
    target = 0 - aList[i]
    left = i + 1
    right = len(aList) - 1
    while left < right:
        if aList[left] + aList[right] == target:
            answer.append([aList[i], aList[left], aList[right]])
            left = left + 1
            right = right - 1
            while left < right and aList[left] == aList[left - 1]:
                left = left + 1
        elif aList[left] + aList[right] < target:
            left = left + 1
        elif aList[left] + aList[right] > target:
            right = right - 1
return answer
```

### #424 Longest Repeating Character Replacement — sliding window + freq map
**Key insight (his):** keep the most frequent letter, change the rest → window valid when **`L - maxFreq <= k`** (`L = right - left + 1`, `maxFreq = max(aDict.values())`).
**Bugs:**
1. `for right in len(range(s))` → **`range(len(s))`** (range/len order — **M-003 family, recurrence 3**).
2. `L` not updated inside the shrink `while` → stale → infinite loop. Fix: `L = L - 1` when sliding `left`.
3. Returned `right - left + 1` (last window) → should track **`answer = max(answer, L)`** across the loop.

**Final:**
```python
aDict = {}
left = 0
answer = 0
for right in range(len(s)):
    aDict[s[right]] = aDict.get(s[right], 0) + 1   # (his: if/else)
    maxFreq = max(aDict.values())
    L = right - left + 1
    while L - maxFreq > k:
        aDict[s[left]] -= 1
        left = left + 1
        L = L - 1
    answer = max(answer, L)
return answer
```
Verified `"ABAB",k=2 → 4`, `"AABABBA",k=1 → 4`. **O(n)** time (dict capped at 26 → `max()` is O(1)); **O(1)** space (dict ≤ 26 keys — corrected from his first "O(n)").

---

## Takeaways

**🎉 B-1 blocker CLEARED.** Two consecutive sessions clean on variable names (Day 15 + Day 16), including a clean #125 (Day 14) and clean 3Sum/#424 today. M-004 → dormant.

**New watch — B-2 (M-003, range/len order):** `len(range(s))` was the 3rd occurrence of the `range(len(x))` index-loop scramble (Day 1, Day 4, Day 16) → escalated to a **light** blocker (quick pre-empt at session start).

**Patterns:** 3Sum = *sort → pin → two-pointer `-nums[i]` → dedup pin + left*. #424 = *sliding window; window OK while `L - maxFreq <= k`; freq dict*.

**Coaching:** first less-spoon-feeding session went well — he derived both new problems' approaches and fixed his own bugs off nudges. Keep it up ([[coaching-less-spoonfeeding]]).

**Spaced-review queue (after today):**
- #150, #121 (carry-over from Jul 7); #33, #20, #167, #11, #15, #424 → **Jul 8**
- #875, #153, #739, #1, #217 → Jul 10; #155 → Jul 9; #3 → Jul 9; #242, #49 → Jul 11; #125 → Jul 12; #347 → Jul 21; #238 → Jul 23

**Next session (Day 17):** reviews due (heavy — #150, #121, #33, #20, #167, #11, #15, #424); **new** — Longest Consecutive Sequence (#128) + Encode and Decode Strings (#271), both Arrays & Hashing.
