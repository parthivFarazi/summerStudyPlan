# Day 37 — 2026-08-03 (Mon)
## FIRST CONTACT: 1-D Dynamic Programming — #70, #746, #198 · Block 1 partial

> **Longest session of the sprint, and correctly so. You didn't spend four hours solving Climbing Stairs — you spent them acquiring DP. `#70` was the vehicle; the pattern was the cargo.**

---

# Warm-up ✅ — B-10, from Saturday's mock

**One pass costs `O(m log m)` · passes `n − m + 1` · product `O(n·m log m)` → `O(n² log n)`.** Total correct.

*(One imprecision: you said one pass costs `O(n log n)`. It sorts `s1` and a window of length **`m`** — the window is never length `n`. **When a problem hands you `m` and `n`, using the wrong letter mid-analysis is how a bound quietly becomes wrong** — and here it's the difference between "fine" and "TLE".)*

---

# Block 2 — 1-D DP, first contact

## 🔑 The five steps (now in `patterns/dynamic-programming-1d.md`)

1. **What does `dp[i]` MEAN?** — a full sentence
2. **What are my choices at `i`?**
3. **Base cases**
4. **Loop upward**
5. **How far back does it reach?** ⇒ collapse the space

## #70 Climbing Stairs — ✅

**You derived the recurrence yourself.** Counted `n = 1..4` by hand → `1, 2, 3, 5`, then split the five `n=4` sequences by their **last move**:

```
3 end in "1"  ->  strip it, you're standing on step 3  ->  ways(3)
2 end in "2"  ->  strip it, you're standing on step 2  ->  ways(2)
```

**Two groups, no overlap, nothing missed** ⇒ `ways(n) = ways(n-1) + ways(n-2)`. That's Fibonacci, and you built it from the problem rather than recognising it.

### 🔴 The exponential — and your `O(n)` was wrong

You predicted the naive recursion was `O(n)`: *"it computes n, then n−1, then n−2…"* — **that describes a chain. It's a branching tree.** Instrumented:

| n | total calls | answer |
|---|---|---|
| 5 | 9 | 8 |
| 20 | 13,529 | 10,946 |
| **40** | **204,668,309** | 165,580,141 |

For `n = 5`, `ways(3)` is computed **twice** and `ways(2)` **three times** — each repeat re-expanding its whole subtree.

> **A recursion that calls itself twice is `O(2ⁿ)` unless something stops the repetition.** Same B-10 disease as the mock: **you priced one call, not the number of calls.**

### 💡 And then you named the fix before I did
> *"If it has been computed, store it somewhere and then just retrieve it from there — so use a dictionary."*

**That's memoization**, invented on the spot. `memo` is the same *"have I done this already?"* role as `visited` in `#207`.

### Memoization vs tabulation
Built **`viz/dp-memo-vs-tabulation.html`** — twice, because the first version didn't show the **call order**. The rebuild has a numbered call log, line numbers, and each frozen frame showing its half-finished expression (`memo[5] = 5 + …running…`).

**The thing that was confusing you:** every call comes from the one line containing both calls, and **Python evaluates the LEFT operand completely — its entire subtree — before touching the right one.**

**Stop on step 11:** `ways(5)` asks for `ways(3)`, reaches **line 4** instead of line 6, and returns 3 **with no frame pushed.** Without that lookup, everything in steps 3–8 happens again.

> **The recurrence is NOT recursion.** `dp[i] = dp[i-1] + dp[i-2]` is a **formula**; recursion is one way to evaluate it, a loop is another. **You can't tabulate without the recurrence** — the recursive thinking happens either way. *(This was the blocking confusion, and it's worth keeping.)*

### Step 5 — and the misconception underneath it
```python
a, b = b, a + b        # right side evaluated FIRST, then assigned
```
> **You thought this was a Fibonacci trick.** It isn't. **The collapse works with ANY recurrence that reaches back a fixed number of steps** — the `+` is incidental, it can be `min` or `max`. That realisation is what unblocked `#746`.

**Verified:** `n = 1…499`, zero mismatches. `n = 45` in **3 microseconds** against 204 million calls at `n = 40`.

---

## #746 Min Cost Climbing Stairs — ✅

The statement is genuinely badly worded, so: **you pay `cost[i]` to LEAVE step `i`** (a toll on departure), **standing is free**, you start on index `0` or `1` free, and **"the top" is index `len(cost)`**.

```
cost = [10,15,20]
start at 1 -> pay 15 -> a 2-step move lands on index 3 = the top.  Total 15.
```

**You defined `dp[i]` correctly first try** — *"the minimum cost to reach that level"* — and derived `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`.

**Verified: 7 named cases + 20,000 random.** Zero mismatches.

**One real issue:** `return dp[i]` uses the **loop variable**, which only equals `len(cost)` by accident and raises `UnboundLocalError` if the loop never runs. **Say what the answer *is*: `dp[len(cost)]`.** Same family as `#210`'s return placement — a conclusion, not a leftover.

> **🔴 And one of my "failures" was mine.** I hand-wrote `[10,1,1,1,10] → 3` into the test list without computing it. **Your code said 2, and 2 is right.** M-035.

---

## #198 House Robber — ✅

### 💡 You proposed even/odd — and killed it yourself

*"Iterate the even indices, iterate the odd indices, return the max."* Tested on **`[2,1,1,2]`**: even ⇒ 3, odd ⇒ 3, **actual answer 4** — rob index `0` and `3`, **skipping two houses**.

> **The rule is *no two adjacent*, not *alternate*.** And that's why greedy shortcuts die on DP generally: **the number of valid choice-patterns is exponential and no fixed rule enumerates them.**

### Step 1 mattered here
Your first definition — *"the cumulative amount after leaving this place"* — was too loose to build on. **Does it include house `i` or not?** Pinned to *"the maximum robbable from houses `0..i`"*, and then:

**rob it** ⇒ `nums[i] + dp[i-2]` (house `i−1` now banned) · **skip it** ⇒ `dp[i-1]` ⇒ **`max` of the two.**

**Verified: 9 named + 30,000 random against brute force + a 24,000-case sweep.** Zero mismatches.

### 🔴 `[5]` crashed — and I named that exact test case in the instruction
```
dp[1] = max(nums[0], nums[1])     # there is no index 1 on a one-house street
```
**2,007 of 20,000 random inputs crashed**, every one a single-element list. **The algorithm was already perfect.** B-4, dropped guard — and running the three cases I listed catches it in a second.

**Then you asked for the `O(1)` version and applied step 5 unprompted.** Better still:
```python
a, b = 0, 0
for n in nums:
    a, b = b, max(n + a, b)
return b
```
**The guard disappears.** *"Before any houses, the best is nothing"* is a base case true for every length.
> **When a guard exists to protect a base case, ask whether a more general base case removes the guard.**

---

# Block 1 — 27-min box, 2 of 8 reached

| # | Item | Result | → |
|---|---|---|---|
| 567 | Permutation in String | ✅ **`O(n)`, 0.0022 s** | 3d |
| 200 | Number of Islands | ❌ `==` for `=`, bounds off by one | **reset 1d** |
| 79 · 39 · 57 | ✍️ | box expired | **Aug 5** |
| 739 · 121 · 153 | 🗣 | box expired | **Aug 4** |

## #567 — the mock's TLE is dead

| | time at the constraint ceiling |
|---|---|
| Saturday's version | **5.67 s** ⛔ |
| today's | **0.0022 s** ✅ |

**A 2,600× speedup.** Verified on 50,000 random cases across two alphabets.

**Two bugs found on the way, and the second is the lesson:**
- `s2[right]` read one past the end after `right += 1`
- **`count == 0` was the wrong test.** `s1="ab"`, window `"aa"` ⇒ `adict['a'] = -1`, `adict['b'] = +1`, **sum = 0 ⇒ falsely `True`.** 2,929 of 20,000 cases wrong.

> **A sum of zero does not mean every value is zero.** A surplus in one character cancels a deficit in another. **When you need "all of these are true", don't reduce to a single number that can cancel.**

*(And a process note: you proposed patches for both bugs **before** doing the three-line arithmetic I asked for. **The arithmetic IS the way around** — once you see the cancellation the fix is obvious. Diagnosing first isn't a formality; it's what makes the fix the right one instead of a patch.)*

## 🔴 #200 — two single-character errors

```python
grid[row][col] == "0"                    # COMPARISON, not assignment - nothing is ever marked
if 0 < nr <= len(grid)                   # rejects row 0, accepts row len(grid)
```

**448 of 512 possible 3×3 grids crash; 43 more give the wrong answer.** You wrote the bounds check correctly on `#994` an hour earlier.

> **This was a ONE-DRAFT — the tier whose entire purpose is the self-audit before handing it over.** *"Does anything actually get marked?"* and *"is index 0 reachable?"* are exactly what that audit is for.

---

# Bank these

- **The five steps.** Define `dp[i]` as a sentence · choices at `i` · base cases · loop up · how far back ⇒ collapse.
- **A recursion that calls itself twice is `O(2ⁿ)`** unless something stops the repetition.
- **The recurrence is a formula, not recursion.** You need it either way.
- **The space collapse is general**, not a Fibonacci trick.
- **A sum of zero ≠ every value zero.**
- **When a guard protects a base case, look for a base case that needs no guard.**
- **Same skeleton, three operators:** *how many* ⇒ `+` · *cheapest* ⇒ `min` · *most* ⇒ `max`.

---

# Day 38 (Tue Aug 4) — 1-D DP continues

- **Block 2 — new:** **#5 Longest Palindromic Substring** and **#91 Decode Ways.** `#5` is the first one where `dp` is 2-D-ish in spirit (expand-around-centre is the expected answer); `#91` is the first where the recurrence has a *condition* on it.
- **Block 1 — 7 items, ~26 min:** full **#70 · #746 · #198** (yesterday's new) · **#200** (reset) → 🗣 **#739 · #121 · #153**.
- **⛔ B-10 — say both halves unprompted.** You needed three prompts today.
- **⛔ The twenty seconds.** `[5]` and `#200` both died to it, four hours deep. **That is an argument for the box, not against it.**
