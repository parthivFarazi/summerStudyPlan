# Day 10 — Practice Notebook

**Week 2 · Day 10 — June 30, 2026**
**Topic:** Binary search **on the answer** (Koko #875); 5 spaced re-solves
**New:** Koko Eating Bananas (#875)

> Format: my **raw answers** verbatim, then the **correction / coaching notes**. (No `.py` files from Day 10 on — code lives here.)

---

## Block 1 — Due re-solves (cold)

### #125 Valid Palindrome — ❌ still fails (typo), but the recurring bug is FIXED
```python
clean = ""
for char in s:
    if char.isalum():        # TYPO: should be .isalnum()
        clean = clean + char.lower()
left = 0
right = len(clean) - 1
while left < right:
    if clean[left] != clean[right]:   # ✅ used `clean` (M-004 fix — the pre-empt worked!)
        return False
    else:
        left = left + 1
        right = right - 1
return True
```
**Correction:** **Win** — the wrong-variable bug (`s` vs `clean`, M-004) that haunted this problem is **gone**; the pre-empt drill worked. Remaining issue is a one-char typo: `.isalum()` → `.isalnum()` (crashes). Queue keeps it at 1d for one clean rep. Complexity O(n)/O(n).

### #704 Binary Search — ✅ PASS (advances 1d→3d)
Correct, **direction right** (`target > nums[mid]` → go right). M-012 reflex forming. O(log n)/O(1).

### #74 Search a 2D Matrix — ✅ PASS (advances 1d→3d)
Correct virtual-flatten + conversion. O(log(m·n))/O(1).

### #347 Top K Frequent — ✅ PASS (advances 7d→21d)
Clean bucket sort; `.append(num)` with parentheses (M-002 stayed away). O(n)/O(n).

### #121 Best Time to Buy/Sell — ✅ PASS (advances 3d→7d)
```python
minPrice = prices[0]
maxProfit = 0
for price in prices:
    if price < minPrice:
        minPrice = price
    if price - minPrice > maxProfit:
        maxProfit = price - minPrice
return maxProfit
```
Correct. Note: this is **pure running-state**, not a sliding window — no `left` pointer. O(n)/O(1).

---

## Block 2 — Koko Eating Bananas (#875): binary search ON THE ANSWER

**Problem:** `piles[i]` bananas in pile `i`; `h` hours; at speed `k`/hr Koko eats from **one** pile per hour, up to `k` (if the pile is smaller she finishes it and idles the rest of the hour). Return the **minimum** integer `k` to finish all within `h` hours.
`[3,6,7,11], h=8` → 4 · `[30,11,23,4,20], h=5` → 30

**New mental model:** don't search the array — search the **answer space**. Speed is in `[1, max(piles)]`; for a candidate `k`, hours needed = `sum(ceil(p/k))`. Monotonic (faster → fewer hours), so binary-search for the smallest `k` with `hours ≤ h`.
**New mechanics:** `import math` + `math.ceil(p/k)`; a **helper** loop summing hours over the piles (O(n) per call → overall O(n·log k)).

### Attempt 1 — returned only on `hours == h`
Returned `None` whenever the best speed finishes *early* (e.g. `[5], h=10` → answer 1, but `hours(1)=5 ≠ 10` → fell through to `None`).

### Attempt 2 — added `result` but kept `else: return mid`
Still returned on exact match too eagerly. **Failing case `[21], h=3`** (answer 7): hit `mid=8` (hours=3 `==` h) and returned **8**, never checking that 7 also ties.

### Attempt 3 — ✅ correct (passes all 6 tests incl. `[21],h=3→7`)
```python
import math
left = 1
right = max(piles)
result = 0
while left <= right:
    mid = (left + right) // 2
    midHours = 0
    for pile in piles:
        midHours = midHours + math.ceil(pile / mid)
    if h >= midHours:        # works (finishes in time, exactly counts) → record + go slower
        result = mid
        right = mid - 1
    else:                    # too slow → go faster
        left = mid + 1
return result
```
**Complexity:** O(n·log k) time (n piles × log of the speed range), O(1) space.

**THE lesson — boundary binary search:** when hunting "the smallest value that satisfies a condition," **record the candidate and keep shrinking; never return on an exact match.** A value that's *exactly* on the line is still just a candidate — a smaller one may tie it. Template (`result` + record-on-pass + return at end) reused for min-capacity / min-days / smallest-divisor problems.

---

## Takeaways
**New pattern:** **binary search on the answer** — when a value range is monotonic w.r.t. a yes/no check, binary-search the range, not the input. Plus the **boundary template** (record + shrink, return `result`).

**Wins:**
- **M-004 (wrong variable) did NOT recur** — the targeted pre-empt worked on #125.
- 4 clean review passes; bucket sort + running-min reproduced cold.

**Watch:** method-name typo `.isalum` → `.isalnum` (the only thing keeping #125 red). Pure-running-state vs sliding-window labels.

**Spaced-review queue (after today):**
- #125 Valid Palindrome → **Jul 1** (still 1d)
- Koko #875 → **Jul 1** (new)
- Two Sum II #167, Container #11 → **Jul 1**
- #3 Longest Substring → **Jul 2**
- #704, #74, Product #238 → **Jul 3**
- #121 Best Time → **Jul 7**
- #347 Top K → **Jul 21**

**Next session (Day 11):** review due recalls, then **Binary Search — Find Min in Rotated Sorted Array (#153)** (compare `mid` vs `right`; the rotated-array invariant).
