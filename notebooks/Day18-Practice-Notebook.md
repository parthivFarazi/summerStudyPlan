# Day 18 — Practice Notebook

**Week 2 · Day 18 — July 9, 2026**
**Topic:** **Interleave day** — mixed, UNLABELED review set (name the pattern first, state complexity incl. space). No new problem; clears the review backlog.

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Interleave set (6, unlabeled — I named the pattern each time before coding)

### 1 — 3Sum (#15) ✅ PASS (reset 1d → 3d)
Named it, sorted, pinned, two-pointer with **the `while left < right` wrapper present** (the Day-17 miss), both dedup levels. Called space **O(n)** (sorted copy) unprompted. `[-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]`. O(n²)/O(n). **Reset cleared.**

### 2 — Longest Consecutive Sequence (#128) ✅ PASS (1d → 3d)
"DO NOT SORT" → set + only-start gate (`num-1 not in seen`) + forward count with `in seen` (not the Day-17 inversion). Space O(n) (set) called right. → `4`. O(n) amortized / O(n).

### 3 — Valid Parentheses (#20) ❌ FAIL → reset 1d  *(M-011 — dropped a guard)*
Pattern + pair-dict right, but **dropped the empty-stack guard** — `stack.pop()` with no `len(stack) > 0` check → crashes on `")("`. Fixed on a nudge (it's in his own `stack.md` gotchas). Needs a rep.

### 4 — Longest Substring No Repeat (#3) ✅ PASS (7d → 21d)
Sliding window: expand-right / shrink-left with a set. Amortized O(n), O(n) space. → `"abcabcbb"=3`. Clean.

### 5 — Encode/Decode Strings (#271) ✅ PASS (1d → 3d)
Length-prefix (`len#word`), decode-by-count with `i`/`j` pointers + slice. **Slip:** `while n in range(l)` → should be `for n in range(l)` (**M-016 for/while, recurrence 2**); fixed on a nudge. Space O(n). → `["abc","de"]`.

### 6 — Search in Rotated Array (#33) ✅ PASS (3d → 7d)
Used **`nums[mid] > nums[right]`** to pick the sorted half (valid alternative to the left-end check); all four branches correct. Traced `target=0→4`, `3→-1`. O(log n)/O(1).

---

## Takeaways

**🎉 B-2 blocker CLEARED.** Two consecutive sessions with zero range/len scrambles (Day 17 + Day 18). M-003 → dormant. **Both blockers (B-1, B-2) now clear.**

**Space-complexity reflex held all day** — called O(n) correctly for every scaling structure (set, sorted copy, stack), zero "O(1)" slips. Yesterday's M-005 correction is sticking.

**Pattern recognition strong:** named all 6 cold on an unlabeled set. That's the interleave payoff.

**Two slips to watch (both recurrence 2 → watchlist):**
- **M-016** (for/while): `while n in range(l)` on #271.
- **M-011** (dropped a required guard): empty-stack check on #20.

**Interleave scorecard:** #15 ✅ · #128 ✅ · #20 reset · #3 ✅ · #271 ✅ · #33 ✅ (5 pass, 1 reset).

**Spaced-review queue (after today):**
- #15, #128, #271 → Jul 12; #33 → Jul 16; #20 (reset) → Jul 10; #3 → Jul 30
- #875, #153, #739, #704, #74, #1, #217 → Jul 10; #121, #167, #11 (rolled, still due) → do Day 19; #242, #49 → Jul 11; #150, #424 → Jul 11; #125 → Jul 12

**Next session (Day 19):** back to new material — **Linked Lists**: Reverse Linked List (#206), Merge Two Sorted Lists (#21), Linked List Cycle (#141). Plus rolled reviews (#121, #167, #11).
