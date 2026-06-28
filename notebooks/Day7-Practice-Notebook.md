# Day 7 — Practice Notebook

**Week 2 · Day 7 — June 26, 2026**
**Topic:** Start of Week 2 — **Sliding Window** (running-state form) + interleaved warm-up
**Solved:** Valid Anagram, Two Sum II (warm-up) + Best Time to Buy and Sell Stock

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Interleaved warm-up (named the pattern first ✅)

### Problem A → Valid Anagram (hashmap counting)
*My stated tell:* "length check, then count letters of s in a dict, then decrement for t."
- First pass **dropped the length check** (regression from Day 5). Failing case `s="aab", t="ab"` → returned `True` wrongly (shorter `t` not caught).
- Re-added `if len(s) != len(t): return False` → ✅ correct. O(n)/O(n).

### Problem B → Two Sum II (two pointers, sorted)
*My stated tell:* "sorted ascending → two pointers; sum<target move left, else right."
```python
left = 0
right = len(numbers) - 1
while left < right:
    total = numbers[left] + numbers[right]
    if total < target:
        left = left + 1
    elif total > target:
        right = right - 1
    else:
        return [left, right]
# O(n) time, O(1) space
```
✅ **Flawless** — cached `total`, clean branches, correct complexity.

> Win: I **verbalized the pattern + tell** before coding both — the step I skipped on Day 6.

---

## Block 2 — Best Time to Buy and Sell Stock (Sliding Window: running-state form)

**Problem:** `prices[i]` = price on day `i`. Buy once, sell later. Return max profit, or 0.
Example: `[7,1,5,3,6,4]` → `5` · `[7,6,4,3,1]` → `0`

**Attempt 1 (raw) — over-engineered, buggy:**
```python
minPrice = prices[0]; minTime = 0
maxPrice = 0; maxTime = len(prices) - 1
for i in range(len(prices)):
    if prices[i] < minPrice and i < maxTime:
        minTime = i; minPrice = prices[i]
    if prices[i] > maxPrice and i > minTime:
        maxTime = i; maxPrice = prices[i]
if maxPrice - minPrice < 0:
    return 0
else:
    return maxPrice - minPrice
```
**Correction:** Right instinct (need the min, and buy-before-sell), but tracking global min **and** max with `minTime`/`maxTime` guards gets tangled and breaks. Failing case `[2,4,1,7]` (answer 6): the `i < maxTime` guard blocks updating the min to `1`, so it returns `5`. ✗

**Reframe:** you don't need the max price at all. When selling on day `i`, the only thing you need is **the lowest price seen so far** — compare every day against the running min, and ordering is automatic.

**Attempt 2 (raw) — ✅ correct & clean:**
```python
minPrice = prices[0]
maxProfit = 0
for num in prices:
    if num < minPrice:
        minPrice = num
    if num - minPrice > maxProfit:
        maxProfit = num - minPrice
return maxProfit
# O(n) time, O(1) space
```
Checks out on `[2,4,1,7]` → 6, `[7,1,5,3,6,4]` → 5, `[7,6,4,3,1]` → 0.

---

## Takeaways
**Pattern:** **Sliding Window — running-state form**: sweep once, keep a running "best/min/max so far." (The variable-size expand/shrink window is next.)

**Biggest lesson today — simplify:** attempt 1 had 4 variables + ordering guards and broke; attempt 2 had 2 variables and worked. When ordering logic gets tangled, ask **"what's the minimum state I actually need?"** Comparing against a running min/max often makes ordering automatic.

**Recognition tells (said out loud today ✅):**
- "anagram / same letters & counts" → hashmap counting (+ length check!)
- "pair summing to target," sorted → two pointers
- "max profit / best over a sweep" → running-state one pass

**Precision habits:**
1. Don't drop the **length check** in anagram problems.
2. Keep the minimum necessary state — fewer variables, fewer bugs.

**Spaced-review queue (re-solve cold):**
- Valid Anagram, Group Anagrams, Top K Frequent → **June 27**
- Palindrome, Valid Palindrome, Two Sum II → **June 27**, **July 1**
- Container With Most Water → **June 29**, **July 3**
- **Best Time to Buy and Sell Stock** → **June 29**, **July 3**
- Two Sum, Contains Duplicate, Product → **~July 1–3**

**Next session (Day 8):** warm-up, then the **real sliding window** — variable-size window (Longest Substring Without Repeating Characters): expanding the right edge, shrinking the left on a duplicate.
