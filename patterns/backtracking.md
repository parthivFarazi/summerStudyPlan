# Backtracking

**Status:** learning (started Day 28, 2026-07-22) · **Mastery: 3/5** · Block B
**Problems:** #78 Subsets, #39 Combination Sum (Day 28) · **#90 Subsets II, #46 Permutations (Day 29 — #46 derived cold from scratch)**.
**Interactive tools (artifacts):** `backtracking-stack-animator` (stack unwind), `subsets2-skip-copies-animator` + `subsets2-tree-animator` (the dedup skip + the decision tree drawing itself). Reopen whenever recursion feels fuzzy (rule 9).

## The three shapes so far
1. **Index take/skip** (#78 Subsets, #39 Comb Sum) — walk index `i`, TAKE (`i+1`, or stay on `i` for reuse) vs SKIP.
2. **Dedup take/skip** (#90 Subsets II) — sort, and in the SKIP branch **walk past all copies** of the value before recursing.
3. **For-loop + used-set** (#46 Permutations) — **no index**; at each slot loop over ALL nums, skip used ones, choose/recurse/un-choose. Use for orderings where every element is used and order matters.

## In one line
Build a solution **incrementally**; at each step try every choice, and **undo each choice before trying the next**. That undo — the *back* in backtracking — is the whole pattern.

## The three moves (memorize this shape)
```python
res, path = [], []
def backtrack(state):
    if <complete>:
        res.append(path.copy())   # SNAPSHOT — path is one shared list you keep mutating
        return
    for choice in choices:
        path.append(choice)       # 1. choose
        backtrack(advance)        # 2. explore
        path.pop()                # 3. un-choose   ← undo before the next branch
```

## The mental model that makes it click *(Day 28)*
Every answer is a sequence of **decisions**. For subsets of `[1,2]`, each element is "take it or skip it" → a binary **decision tree**; every leaf is one answer. Backtracking walks that tree depth-first; the `pop()` is what lets you back up and try the other branch.

**How a `return` unwinds** (the hard part): a return goes up **exactly one level**, to the line *after* the call. It *cascades* up only through frames with nothing left to do, and **stops at the first frame that still has a line to run**. (In the take/skip shape: a frame paused on the *last* line — the skip — falls straight through and returns; a frame paused on *take* still has its pop + skip to do, so the cascade halts there.)

## #78 Subsets — take/skip, each element used ONCE
```python
def subsets(self, nums):
    res, path = [], []
    def backtrack(i):
        if i == len(nums):
            res.append(path.copy()); return
        path.append(nums[i]); backtrack(i + 1); path.pop()   # TAKE → i+1
        backtrack(i + 1)                                       # SKIP → i+1
    backtrack(0)
    return res
# Time O(n·2^n) — 2^n subsets, each costs up to O(n) to copy.  Space O(n) — depth = n.
```

## #39 Combination Sum — reuse allowed, hunt a target
Three changes from subsets: (1) carry a running **total**; (2) success = `total == target` (not end-of-list); (3) **TAKE stays on `i`** (reuse), SKIP goes to `i+1`.
```python
def combinationSum(self, candidates, target):
    res, combo = [], []
    def backtrack(i, total):
        if total == target:                      # success — stands alone, records
            res.append(combo.copy()); return
        if total > target or i == len(candidates):  # dead ends — same action
            return
        combo.append(candidates[i])
        backtrack(i, total + candidates[i])      # TAKE → STAY on i (reuse)
        combo.pop()
        backtrack(i + 1, total)                  # SKIP → i+1
    backtrack(0, 0)
    return res
# Time O(N^(T/M+1)), Space O(T/M) — T=target, M=smallest candidate, N=#candidates.
```

## #90 Subsets II — dedup (sort + skip all copies)
Duplicates arise because two equal values are interchangeable: `[2]` can be made by "take the 1st 2, skip the 2nd" OR "skip the 1st, take the 2nd." **Fix: sort, and once you decide to SKIP a value, skip every copy of it** (the TAKE branch is untouched, so `[2,2]` still comes from take-take).
```python
nums.sort()
def backtrack(i):
    if i == len(nums): res.append(path.copy()); return
    path.append(nums[i]); backtrack(i+1); path.pop()      # TAKE (unchanged)
    while i+1 < len(nums) and nums[i+1] == nums[i]: i += 1 # SKIP: walk past all copies
    backtrack(i+1)
# O(n·2ⁿ)/O(n)  (worst case all-distinct = plain Subsets)
```

## #46 Permutations — for-loop + used-set (NO index)
Every element used, order matters → at each slot, try **any unused** number. `backtrack` takes **no index**; it loops over all nums.
```python
res, path, seen = [], [], set()
def backtrack():
    if len(path) == len(nums): res.append(path.copy()); return
    for num in nums:
        if num in seen: continue
        seen.add(num); path.append(num)      # choose — TWO things
        backtrack()                          # fill the next slot (no i+1)
        path.pop(); seen.remove(num)         # un-choose — undo BOTH
# O(n·n!)/O(n).  (value-set works because nums is distinct; with dups track INDICES)
```
The loop goes **sideways** (try each number for this slot); the recursion goes **down** (fill the next slot). That sideways loop is what the index-based take/skip can't do (it can only build in original order).

## 🔑 Two ideas worth banking
- **Carry mutable running state as a PARAMETER, not `self.x`.** `backtrack(i, total + c[i])` — the parent's `total` is untouched, so it auto-undoes on return. **No `-=` needed.** (Contrast `combo`, which you *do* undo by hand with `pop()`, because you want it to grow and shrink.) Passing state *down* via a parameter is the same tool as #98's bounds.
- **Reuse ⇒ depth decouples from n.** Subsets: one decision per element → depth exactly `n` → space O(n). Combination Sum: TAKE stays on `i`, so the deepest path is "take the smallest over and over" → depth `T/M`, unrelated to `n`. That's why the complexities differ.

## Complexity (say it out loud)
- The number of answers is usually **exponential**, and each answer costs its **length** to copy into `res` — that's where the extra factor comes from (subsets: `2^n` leaves × O(n) copy = **O(n·2^n)**).
- Space = **recursion depth** (the call stack) + the path. Depth = how deep the tree goes: `n` for one-use problems, `T/M` for reuse.

## Reach for it when
- "all subsets / combinations / permutations", "all ways to…", "return every…"
- Build-a-string / place-N-things (N-Queens), partition, target-sum enumerations
- The answer is a **set of sequences**, not a single value, and you must explore choices.

## Your gotchas *(Day 28 — first exposure)*
- **`res.append(path.copy())`, not `path`** — store the reference and every entry points at the same list, empty by the end. Snapshot at the leaf.
- **`append`/`pop` are a matched pair (M-027)** — drop the `pop` and the path never resets; every answer gets polluted.
- **Reuse = stay on `i`.** Writing `backtrack(i+1)` in the TAKE branch is the subsets rule and kills reuse. (First attempt on #39 did this.)
- **Don't fold success and overshoot together.** `total == target` records; `total > target` throws away. `>=` with one action is wrong.
- **`[]` is your stack, not `stack()`** (that isn't a thing in Python).
- **Recursion is his slowest area (rule 9)** — trace the stack by hand / use the animator before coding; don't just state the recursive idea and move on.
