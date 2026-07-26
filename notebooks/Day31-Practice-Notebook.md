# Day 31 — Practice Notebook
**Sunday, 2026-07-26** · Week 6 · *rest day converted to a working session* · **Block 1 reviews + Intervals (new pattern)**

> **Why today happened at all:** Jul 26 was a scheduled rest Sunday. The Days 31–53 calendar was **2 sessions short** of fitting before the Aug 20 deadline, so this Sunday and two more (Aug 9, 16) became working days. Working today recovered one of the two.

**Session shape as planned:** 93 min — warm-up 3 · backtracking drain 35 · pre-teach 10 · Intervals 40 · ingest 5.
**Actual:** ran well over, almost entirely in Block 3. Two unplanned full stops to build Python fundamentals from scratch (`sort(key=)`/`lambda`, then negative indexing). That was the right spend — see *Honest read* below.

---

## Scoreboard

| Target | Result |
|---|---|
| #90, #46, #78 re-solved from a blank screen | ✅ **3/3, all first-draft correct** |
| 2 new problems (#57, #56) | ✅ both built, both correct |
| Complexity stated **before** code | ✅ every problem (needed 3 asks on #57) |
| Ingest completed | ✅ |

**Times:** #90 **4:30** · #46 **4:28** · #78 **2:57** · #57 *untimed* · #56 **26:24**

---

# Block 1 — Backtracking drain (3 resets, ~12 min total)

All three **failed on Day 30** and sat at 1d. All three came back **correct on the first draft.** Twelve minutes for three Mediums.

## #90 Subsets II — ✅ PASS · 4:30

**Complexity stated first:** `O(n · 2ⁿ)` time, `O(n)` space — correct.

**What he missed on the first verbal answer:** the **sort**. He described the dedup while-loop correctly but omitted `nums.sort()`, which is the thing that makes adjacent-comparison dedup work at all. Found it himself after being asked to run his rule on `nums = [2,1,2]`.

```python
def subsetsWithDup(self, nums):
    nums.sort()
    path = []
    res = []

    def backtrack(i):
        if i == len(nums):
            res.append(path.copy())
            return

        path.append(nums[i])      # take branch
        backtrack(i + 1)
        path.pop()                # un-choose

        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i = i + 1             # skip all copies
        backtrack(i + 1)          # skip branch

    backtrack(0)
    return res
```

Traced on `[1,2,2]` → all six subsets, no duplicates. **The while loop's position is the whole trick:** after `path.pop()`, in front of the **skip** branch. Before the pop it would corrupt the take branch's state; guarding the take branch instead would lose valid subsets.

**Precision notes:**
- Wrote `self.path` / `self.res` — works (reset each call) but wrong ownership: these are scratch state for one call, not something the object owns. Forget the reset line and a second call returns the first call's results too. Plain closure variables are correct.
- Function named `subsetsTwo`; real name is `subsetsWithDup`. *"Every name real."*
- Called `nums.sort()` `O(n log n)` correctly, and correctly said it's **dominated** by `O(n · 2ⁿ)` so the total is unchanged. Say the dominated term out loud rather than dropping it.
- **Space convention:** `O(n)` = recursion stack + path, **excluding output**. Counting output it's `O(n · 2ⁿ)`. Always say which.

## #46 Permutations — ✅ PASS · 4:28

**Complexity stated first:** `O(n · n!)` time, `O(n)` space — correct.

**Why an index can't work here** (the shape difference, took two attempts): an index encodes *"how far along am I,"* which is enough when every element gets one yes/no decision in a fixed order (Subsets). **Permutations needs *"which elements have I used"* — a set, not a position** — because order is part of the answer and you must reach back for elements you've already passed. With an index from 0 you could only ever start with `nums[0]`; permutations beginning with 2 or 3 would be unreachable.

```python
def permute(self, nums):
    combo = []
    res = []
    seen = set()

    def backtrack():
        if len(combo) == len(nums):
            res.append(combo.copy())
            return
        for n in range(len(nums)):
            if nums[n] in seen:
                continue

            seen.add(nums[n])
            combo.append(nums[n])

            backtrack()

            popped = combo.pop()
            seen.remove(popped)

    backtrack()
    return res
```

**He dropped `self.` unprompted, same session.** [INSIGHT] Fastest correction turnaround so far.

**Better than the usual version:** `popped = combo.pop()` then `seen.remove(popped)` guarantees the value leaving the set is the one that left the path. The common `seen.remove(nums[n])` can drift out of sync. Keep it.

**The one fragility:** `seen` holds **values**, not indices. Correct here — #46 guarantees distinct integers. On `[1,1,2]` it would find `nums[1]` already in `seen` and skip it, producing too few permutations. **#47 Permutations II removes that guarantee and needs a used-set by index.**

Minor: `n` is only ever used as `nums[n]` — `for num in nums:` says the same with less to get wrong.

## #78 Subsets — ✅ PASS · 2:57

**Complexity stated first:** `O(n · 2ⁿ)` time, `O(n)` space — correct.

**Shape identified correctly:** index-based take/skip. **Deletions from #90:** the `while` loop is the one *required* deletion; the `sort` becomes *unnecessary* (harmless, since any subset order is accepted, but it's `O(n log n)` for nothing). He named the while loop but **missed the sort — five minutes after correctly identifying the sort as the thing he'd forgotten on #90.**

```python
def subsets(self, nums):
    path = []
    res = []

    def backtrack(i):
        if i == len(nums):
            res.append(path.copy())
            return

        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
        backtrack(i + 1)

    backtrack(0)
    return res
```

---

# Block 2 — Pre-teach

## `sort(key=...)` and `lambda` — stopped and rebuilt from zero [STRUGGLE] [NEEDS_RECALL]

He said *"I don't understand what that lambda is doing"*, then *"doesn't `data.sort()` just sort it? Why is there anything in the brackets?"* — so this went back further than planned. Rebuilt in four steps, `def` before `lambda`, one thing at a time:

**1. A function is a value.**
```python
def double(x):
    return x * 2

f = double        # no parentheses — f IS the function
f(5)              # 10
```
`double` vs `double(5)` — the tool vs the result of using it. Everything rests on this.

**2. So you can pass one to another function.**
```python
def apply_twice(fn, value):
    return fn(fn(value))

apply_twice(double, 3)    # 12
```

**3. Why `sort` needs an argument at all** — the motivating example that made it click:
```python
words = ["apple", "hi", "banana"]
words.sort()      # ['apple', 'banana', 'hi']   — alphabetical, the default
```
But "shortest first" is `['hi', 'apple', 'banana']` — an equally valid ordering of the same list that plain `.sort()` cannot produce. **Sort always needs a rule for "which comes first." For numbers and strings the rule is obvious, so he'd never had to think about it.** `key=` is how you name a different rule.
```python
def length_of(w):
    return len(w)

words.sort(key=length_of)      # ['hi', 'apple', 'banana']
```
Also connected `key=` to what he already writes: `path.append(nums[i])` puts input in the parentheses. Only two things are new — the input has a **name** (`key=`, optional), and the input **is a function**.

**4. `lambda` is only typing economy.** `lambda x: x[1]` is the same object as `def second(x): return x[1]`.

**Checks — all correct:**
- `pairs = [[5,1],[2,9],[8,4]]`, `key=second` → `[[5,1],[8,4],[2,9]]`, returns 1 / 9 / 4 in call order ✓
- `lambda x: x[0]` ✓
- `data.sort(key=lambda x: x[0])` → `[[1,30],[2,20],[3,10]]`, then `key=lambda x: x[1]` on **that** → `[[3,10],[2,20],[1,30]]` ✓ — including the trap that B runs on A's result

## Iterable unpacking

```python
for p in pairs:      print(p[0], p[1])
for a, b in pairs:   print(a, b)          # same output
a, b = [1, 30]                            # works outside loops too
```

**His question, and it was a good one:** *"Doesn't unpacking only work for tuples?"* — No. Lists, tuples, strings, any iterable of matching length. "Tuple unpacking" is a naming habit; the real name is **iterable unpacking**. Matters because LeetCode hands you **lists** of lists — filing it under "tuples only" would have shelved a tool he can use constantly.

**Checks:** `for x, y in [[7,8],[9,10]]: print(y, x)` → `8 7` / `10 9` ✓ · `for a, b in [[1,2,3]]` → `ValueError`, count mismatch ✓

**Sell for using it:** it lets you *name* the parts — `for start, end in pairs` tells a reader what the numbers mean; `p[1]` never will.

---

# Block 3 — NEW PATTERN: Intervals

## The primitive — derived, then improved

**First attempt (strict inequalities):** `c < a < d or c < b < d or a < c < b or a < d < b`.

Given three test rows to check by hand, **he diagnosed his own failures**: `[1,3]` vs `[3,5]` and `[1,3]` vs `[1,3]` both slip through. He also reasoned out the convention himself — **touching counts as overlapping**, because returning `[1,3]` and `[3,5]` separately would share the point 3 and the output wouldn't be non-overlapping.

**Patched to `<=`** — four clauses, and **verified correct** on all five cases. Worth recording precisely: he produced a *correct* condition unaided. The guidance was for the *shorter* one.

**The better move — count the failures, not the successes** [INSIGHT]. Needed a text number-line drawing before it landed:

```
   0   1   2   3   4   5   6   7   8   9
       |---------|           |---------|
       a         b           c         d      →  b < c
       c         d           a         b      →  d < a
```

Two segments that don't touch — one has to be on the left, and the only question is which. **Two cases, not four.**

```python
no_overlap = (b < c) or (d < a)
overlap    = (b >= c) and (d >= a)      # he wrote this himself
```

**Read as a sentence:** *"I reach at least as far as you start, and you reach at least as far as I start."*

## #57 Insert Interval — built, one self-found bug · *untimed*

**Complexity:** `O(n)` time — **input arrives sorted, so no sort at all** · `O(n)` output space, `O(1)` auxiliary.

**Derived the three buckets himself** once given the trace-table format. Filled 4/4 rows correctly on `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`:

| `[c,d]` | bucket | into result | `newInterval` after |
|---|---|---|---|
| `[1,2]` | before (`d < a`) | `[1,2]` | `[4,8]` |
| `[3,5]` | overlap | — | `[3,8]` |
| `[6,7]` | overlap | — | `[3,8]` |
| `[8,10]` | overlap | — | `[3,10]` |
| `[12,16]` | after | `newInterval`, **then** `[12,16]` | `[3,10]` |

**Got the ordering right** — `newInterval` before `[12,16]`, which is the step most people reverse. And worked out unaided that **one** post-loop guard suffices: the "before everything" case handles itself, because the "after" branch fires on the very first interval.

**First draft — real bug, found by him from a test case** [STRUGGLE]: `isMerged` was *set* in the "after" branch but never *gated* it, so on `intervals = [[1,2],[12,16],[20,25]]`, `newInterval = [4,8]` the branch re-fired on `[20,25]` and appended `newInterval` a second time → `[[1,2],[4,8],[12,16],[4,8],[20,25]]`.

**Fixed:**

```python
def insert(self, intervals, newInterval):
    answer = []
    isMerged = False

    for interval in intervals:
        c, d = interval
        a, b = newInterval          # re-read each pass — newInterval grows

        if d < a:
            answer.append(interval)

        elif d >= a and c <= b:
            newInterval = [min(a, c), max(b, d)]

        elif c > b:
            if not isMerged:
                answer.append(newInterval)
                isMerged = True
            answer.append(interval)

    if not isMerged:
        answer.append(newInterval)

    return answer
```

Verified on six cases: the example, the bug case, `newInterval` after everything, before everything, overlapping the last interval, and empty input. **All pass.** The flag-and-gate version is kept over the early-return version deliberately — the early return needs `enumerate` + slicing, which is new machinery for no real gain. One smell: `isMerged` is now read in two places for one fact (M-027 family).

Missing the `def insert(...)` signature line — wrote a bare body.

## #56 Merge Intervals — built · **26:24**

**The guarantee contrast is the entire problem.** He answered *"it is sorted but there are overlapping intervals"* — **wrong, and partly the notebook's fault**: the example I gave (`[[1,3],[2,6],[8,10],[15,18]]`) happens to be sorted by start, which made it look like a promise. **#56 gives neither promise.** #57 gave both. That's where the `O(n log n)` comes from.

**The representation was the sticking point** [STRUGGLE] — three rounds of "compare against the previous interval" before the fix. Shown by counter-example: on `[[1,10],[2,3],[4,5]]`, comparing `[4,5]` to the previous **input** interval `[2,3]` says no-overlap and wrongly appends it, but `[1,10]` had already absorbed `[2,3]`.

**Taught negative indexing** (`lst[-1]` = last element) and the unlock: **appending to `answer` does not finalise it.** The growing interval *is* `answer[-1]` — reach back and stretch its right edge. No separate variable.

```python
def merge(self, intervals):
    intervals.sort()
    answer = []

    for interval in intervals:
        if len(answer) == 0:
            answer.append(interval)
        else:
            c, d = interval
            a, b = answer[-1]

            if c > b:
                answer.append(interval)
            else:
                temp = [min(a, c), max(b, d)]
                answer.pop()
                answer.append(temp)

    return answer
```

Verified on five cases: the example, `[[1,10],[2,3],[4,5]]`, an unsorted input, touching `[[1,4],[4,5]]`, and empty. **All pass.** Used both pre-taught tools unprompted (unpacking, negative indexing).

**Corrections:**
1. **He stated `O(1)` space — wrong, and this is the lesson of the problem.** The sort costs *space* as well as time: Python's Timsort needs up to **`O(n)` auxiliary**. So space is `O(n)` under either convention. **When you add a sort, add its space too.**
2. `intervals.sort()` with no key **is** correct — Python compares lists element-wise, so it sorts by start (ties on end, harmless). Say *why* rather than looking lucky.
3. `answer[-1] = temp` replaces `pop()` + `append(temp)` — one site instead of two.
4. `min(a, c)`: sorted by start ⇒ `a <= c` always ⇒ it's always just `a`. **The sort is what buys you "the left edge never moves."** Harmless, but it was the question asked and not answered.

---

# The honest read

**Block 1 was gate-level.** Three Mediums that failed yesterday, all correct first-draft from a blank screen, 12 minutes total, complexity stated before code. `GOALS.md` asks for 4-of-5 unseen Mediums in ≤35 min; on *learned* patterns he is around there.

**Block 3 was first contact and should not be judged against Block 1.** Two different activities. Nobody derives a new pattern cold. He asked directly whether needing this much guidance was bad — the honest breakdown:

- **`lambda`/`sort(key=)`** — a **Python** hole, not an algorithms one. Six weeks from genuine beginner; expected, and exactly what the pre-teach slot exists for. Cost ~15 min once; won't recur.
- **The overlap condition** — he produced a **correct** condition unaided. Guidance got him the *shorter* one. Different problem.
- **The complement move** ("count the failures, not the successes") — a genuine, transferable gap. The real thing learned today; it recurs in graphs and DP.
- **The `answer[-1]` representation** — needed the drawing. But once framed, he filled every trace row correctly, including the orderings most people reverse.

**The two things worth more attention than any knowledge gap:**

**1. Confirm-seeking instead of self-testing** (M-030, 4× today). *"Am I right about this?"* on his four-clause condition — fifteen seconds on `[1,3]` vs `[3,5]` would have answered it. **In an interview the only verification available is the one you run yourself.**

**2. Vocabulary looseness** (M-029, 3× today). Called the `while` loop *"a guard before unchoose backtrack,"* then *"a guard with a while loop,"* then *"the if statement guard."* **His code was right every time; his language for it kept slipping.** `GOALS.md` flags that interviewers now probe *"what does this line do — remove it, what breaks?"* Also garbled the #56 sweep narration (`[4,5]` twice, dropped `[2,3]`).

Both are the same root: **outsourcing verification** — of his claims, and of his own words.

**One real cost:** Block 3 ran far over its 40 minutes, and Day 31's plan was already the trimmed one. The Aug 19 buffer is one day wide. Today didn't consume it — the session finished — but the pattern is worth watching: **first contact with Graphs (Jul 28) and DP (Aug 1) will need the pre-teach slot to actually hold.**

---

# Banked rules

1. **`overlap = (b >= c) and (d >= a)`** — *"I reach at least as far as you start, and you reach at least as far as I start."* `>=`, because touching merges.
2. **Count the ways a condition fails, not the ways it succeeds.** Four clauses → two.
3. **#57 vs #56 is entirely about the input guarantee.** Sorted + non-overlapping ⇒ `O(n)`. No promises ⇒ sort ⇒ `O(n log n)`.
4. **A sort costs space too.** `O(n)` auxiliary for Timsort. Never pair `O(n log n)` time with `O(1)` space.
5. **Appending doesn't finalise.** The growing interval is `answer[-1]`; reach back and stretch it.
6. **Compare against the growing one, not the previous input one.**
7. **The sort is what guarantees the left edge never moves.**
8. **Before asking "am I right" — run one case.**

# Next session — Day 32 (Mon Jul 27)

**Block 1 (~29 min):** #79 · #39 · **#57 · #56** (all 1d, full solve) · #146 LRU ✍️ **first one-draft — 4 min, no running, no debugging** · #704 🗣 · #33 🗣
**Block 2:** Intervals continued — **#435 Non-overlapping Intervals** (greedy by *end*), **#252 Meeting Rooms**. Light day, so heavy reviews sit here and reviews run first.
