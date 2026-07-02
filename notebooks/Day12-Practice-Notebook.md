# Day 12 — Practice Notebook

**Week 2 · Day 12 — July 2, 2026**
**Topic:** Interleave day — mixed, **unlabeled** review set (name the pattern first, state complexity unprompted). No new problem (per roadmap).

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Warm-up — variable-audit drill (B-1) + binary-search reflexes

Three from-memory reps, all correct:
1. Add 7 to a list `stack` → `stack.append(7)` ✅ (method call uses `()` — M-002 reflex)
2. Converging binary search loop → `while left < right` ✅ (M-014 reflex)
3. Find-minimum boundary, exact match → "record it and keep shrinking" ✅ (M-013 reflex)

Clean sweep — the two binary-search reflexes that tripped me last week are now automatic.

---

## Problem 1 (unlabeled) — Product of Array Except Self (#238)

**Naming:** described the mechanism (left-product pass, then right-product pass) correctly, but **named it "iteration of lists"** → corrected to **prefix & suffix products** (prefix-sum family). The name is the retrieval hook — "iteration of lists" fits every array problem.

**My solution (verbatim, first pass):**
```python
leftRun = 1
answer = []
for i in range(len(nums)):
    answer.appened(leftRun)          # typo: appened → append (caught on audit)
    leftRun = leftRun * nums[i]

rightRun = 1
for j in range(len(nums) - 1, -1, -1):
    answer[j] = answer[j] * rightRun
    rightRun = rightRun * nums[j]

return answer
```
**Result:** ✅ correct — traced `[1,2,3,4] → [24,12,8,6]`. **Time O(n)** (two linear passes). Reverse loop `range(len(nums)-1, -1, -1)` clean (no M-003 slip).
- **Variable audit** caught `appened → append` (B-1 slip — needed a nudge to spot).
- **Space:** O(1) **extra** — the `answer` array is the required return value, excluded by convention. Reasoning stated correctly; write the word "extra".

---

## Problem 2 (unlabeled) — Longest Substring Without Repeating Characters (#3)

**Naming:** **sliding window** ✅

**My solution (verbatim):**
```python
left = 0
maxLen = 0
seen = set()

for right in range(len(s)):
    if s[right] not in seen:
        seen.add(s[right])
    else:
        while s[right] in seen:
            seen.remove(s[left])
            left = left + 1
        seen.add(s[right])
    if right - left + 1 > maxLen:
        maxLen = right - left + 1
return maxLen
```
**Result:** ✅ correct — traced `"abcabcbb"→3`, `"bbbbb"→1`, `"pwwkew"→3`. **Variable audit clean** (no name slip).
- **Amortized O(n)** stated unprompted: each char added once (by `right`) and removed at most once (by `left`) → O(2n) = O(n), despite the `while` inside the `for`. **Space O(n)** for the set.
- **Verbal flip to fix:** narrated "left adds, right removes" — it's the reverse (**right** expands, **left** shrinks). Code was correct.
- **Optional tightening:** the `if s[right] not in seen` guard is redundant — `while s[right] in seen: shrink` then `seen.add(...)` unconditionally is identical with less state (Day-7 "minimum necessary state").

---

## Problem 3 (unlabeled) — Find Min in Rotated Sorted Array (#153)

**Naming:** **binary search** ✅ (give-away: O(log n)). Stated the full invariant — compare `nums[mid]` to `nums[right]`; `<=` → `right = mid`; else `left = mid + 1`; strict `while left < right`. All correct.

**Attempt 1 — correct invariant, but a tracking bug:**
```python
left = 0
right = len(nums) - 1
answer = 0
while left < right:
    mid = (left + right) // 2
    if nums[mid] <= nums[right]:
        answer = nums[mid]
        right = mid
    else:
        left = mid + 1
return answer
```
**Bug (found by tracing `[2,1]`):** returns `0`, not `1`. When the last move is the `else` branch (`left = mid + 1`), the convergence position is never recorded into `answer`, so the `answer = 0` default leaks out. Same failure on single-element `[5]` → returns `0`. **(M-015.)**

**Attempt 2 — ✅ fixed (self-corrected after a test-case nudge):**
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
Verified `[2,1]→1`, `[5]→5`, `[3,4,5,1,2]→1`, `[4,5,6,7,0,1,2]→0`, `[11,13,15,17]→11`. **O(log n) / O(1).** Deleted the now-dead `answer = nums[mid]` line.
- **Ladder:** needed a hint (the test case) to find the bug → **#153 resets to 1d.**

---

## Takeaways

**Keeper of the day:** in a **converging** binary search, the loop-exit position **is** the answer — `return nums[left]`. Don't reintroduce a tracked candidate; a default like `answer = 0` leaks on edge cases (`[2,1]`, `[5]`). Same "minimum necessary state" lesson as Day 7 — fewer variables, fewer places for a bug to hide. I had this right on Day 11 and regressed today by re-adding `answer`.

**Pattern-naming is the interleave skill:** the name is what lets you recognize a cold problem. Got 2/3 crisp (**sliding window**, **binary search**); #238 needed the label fixed to **prefix & suffix products**.

**Reflexes holding:** warm-up + all three solves kept the M-002 / M-013 / M-014 reflexes clean. Variable audit caught the one name slip (`appened`) — B-1 still active (needed a nudge), so the drill continues.

**Interleave scorecard:** #238 ✅ · #3 ✅ · #153 ✅ after a reset.

**Spaced-review queue (after today):**
- #153 → **Jul 3** (reset 1d); #704, #74 → **Jul 3**
- #125, #875 → **Jul 4**; #121 → Jul 7; #167, #11 → Jul 8; #3 → **Jul 9**
- #1, #217 → Jul 10; #242, #49 → Jul 11; #347 → Jul 21; #238 → **Jul 23** (advanced to 21d)

**Next session (Day 13):** Block 1 reviews (#11 Container, #875 Koko + due); **new** — Search in Rotated Array (#33, binary search) + Valid Parentheses (#20, stack: list as stack `.append`/`.pop`, pair dict).
