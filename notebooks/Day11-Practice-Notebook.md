# Day 11 — Practice Notebook

**Week 2 · Day 11 — July 1, 2026**
**Topic:** Find Min in Rotated Sorted Array (#153); 4 reviews; **variable-audit drill (M-004 → blocker)**
**New:** Find Min in Rotated Sorted Array (#153)

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Due re-solves (4) + the variable-audit drill

**First pass — two wrong-variable slips (both M-004):**
- **#125 Valid Palindrome:** `for char in strs` — used `strs` (Group Anagrams' variable) instead of `s`. (Typo `.isalnum` was fixed ✅; `clean` used correctly ✅.)
- **#167 Two Sum II:** used `nums` instead of the given `numbers`.
- **#875 Koko:** ✅ clean — boundary template nailed (`midH <= h` → record + shrink, no return-on-`==`).
- **#11 Container:** ✅ clean — right variables, right formula.

**The pattern:** #125's *algorithm* has been correct for 5 sessions; it keeps failing on **variable-name precision**, a different mask each time (infinite loop → `s`/`clean` → `.isalum` typo → `strs`). That's **M-004 at recurrence 3 → escalated to a BLOCKER.**

**Drill introduced — "variable audit before every submit":** scan each variable against the names actually declared (params + your own vars) before sending. I ran it → fixed `strs → s` and `nums → numbers` in one pass → **all four clean, and #125 finally green.** ✅

---

## Block 2 — Find Min in Rotated Sorted Array (#153)

**Problem:** a sorted ascending array rotated at a pivot (e.g. `[4,5,6,7,0,1,2]`); return the minimum in O(log n).
**Idea:** rotated = two sorted runs with one "drop"; the min is at the drop. Compare `nums[mid]` to `nums[right]` to decide which half holds it. *(I derived the comparison logic myself.)*

**Attempt 1 — correct invariant, but infinite loop:**
```python
left = 0
right = len(nums) - 1
answer = 0
while left <= right:            # BUG: <= with right = mid → infinite loop
    mid = (right + left) // 2
    if nums[mid] <= nums[right]:
        answer = nums[mid]
        right = mid
    else:
        left = mid + 1
return answer
```
**Bug:** when `left == right`, `mid == left`, `nums[mid] <= nums[right]` is true → `right = mid` (no movement) → hangs. (Also `answer = 0` returns `0` for a single-element array.)

**Attempt 2 — ✅ correct (verified 7/7):**
```python
left = 0
right = len(nums) - 1
while left < right:             # converge: strict <
    mid = (right + left) // 2
    if nums[mid] <= nums[right]:
        right = mid             # keep mid — it might BE the min (not mid-1)
    else:
        left = mid + 1
return nums[left]               # they meet ON the answer
```
**Complexity:** O(log n) time, O(1) space. **M-014:** a *converging* binary search (two pointers → one spot) needs `while left < right` (strict), not `<=`.

---

## Takeaways
**New sub-pattern:** **converging binary search** — for "find the min / the boundary," use `while left < right`, move `right = mid` (keep the candidate) / `left = mid + 1`, and `return nums[left]` when they meet. Compare `mid` to an **end** (here `nums[right]`), not a target.

**Biggest win:** the **variable audit** turned 4 messy reviews into 4 clean passes and cleared #125 after 5 sessions. M-004 is now a tracked blocker — do the audit every submit until it goes dormant.

**Process note:** retired the roadmap's static "review" column — reviews now come only from the live `QUEUE.md` (no preemptive guesses).

**Spaced-review queue (after today):**
- Find Min Rotated #153 → **Jul 2** (new); Longest Substring #3 → **Jul 2**
- Product #238, #704, #74 → **Jul 3**
- #125, #875 → **Jul 4**; #121 → Jul 7; #167, #11 → Jul 8; #347 → Jul 21

**Next session (Day 12):** **Interleave day** — a mixed, *unlabeled* review set (name the pattern first, state complexity unprompted). No new problem.
