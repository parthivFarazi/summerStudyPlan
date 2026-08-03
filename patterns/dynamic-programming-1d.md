# Dynamic Programming — 1-D

**Status:** **learned Day 37** (#70 Climbing Stairs, #746 Min Cost Climbing Stairs, #198 House Robber) · **Mastery: 2/5** · Block C
*(All three built, every recurrence derived unaided. 2/5 because it was a ~4-hour first-contact session with heavy scaffolding. The 1d/3d reps decide the number.)*

## In one line
**A problem whose answer is built from smaller versions of itself, where the same smaller versions keep coming back.** Find the recurrence, then stop recomputing.

---

## 🔑 The five steps — every 1-D DP problem, in this order

1. **What does `dp[i]` MEAN?** Say it as a full sentence. Vague here ⇒ no recurrence.
2. **What are my choices at `i`?** Usually two. Write each as an expression in earlier `dp` values.
3. **Base cases** — the smallest `i` where the recurrence can't apply and you just have to know.
4. **Loop upward** from the base cases.
5. **How far back does the recurrence reach?** Reaches back `k` ⇒ keep `k` variables ⇒ space collapses.

> **Step 1 is where the problems die.** *"`dp[i]` is the cumulative amount"* is not a definition — does it include `i` or not? Two different quantities, and only one gives a clean recurrence. *(Day 37, #198.)*

---

## Why any of this is needed: the exponential

`ways(n) = ways(n-1) + ways(n-2)` written as a plain recursion **calls itself twice**, so the work **doubles per level**. Measured:

| n | total calls | answer |
|---|---|---|
| 5 | 9 | 8 |
| 20 | 13,529 | 10,946 |
| 30 | 1,664,079 | 1,346,269 |
| **40** | **204,668,309** | 165,580,141 |

**Two hundred million calls for a number smaller than the call count.** For `n = 5`, `ways(3)` is computed **twice** and `ways(2)` **three times** — and each repeat re-expands its whole subtree.

> **`O(2ⁿ)`, not `O(n)`. A recursion that calls itself twice is exponential unless something stops the repetition.** Describing it as *"n, then n−1, then n−2"* describes a **chain**; it's a branching tree. *(Day 37 misconception, B-10 flavour: he priced one call, not the number of calls.)*

---

## Two ways to stop recomputing

Stepper built Day 37: **`viz/dp-memo-vs-tabulation.html`** — call log, stack frames with half-finished expressions, and the ⚡ cache-hit frame.

### Memoization (top-down) — recursion + a cache
```python
memo = {}
def ways(n):
    if n == 1: return 1
    if n == 2: return 2
    if n in memo: return memo[n]           # ⚡ already solved
    memo[n] = ways(n-1) + ways(n-2)
    return memo[n]
```
Starts at `n` and asks its way **down**. `memo` is the same *"have I done this already?"* role as `visited` in `#207`.

**⚠️ Every call comes from the one line with the two calls in it — and Python evaluates the LEFT operand completely (its entire subtree) before touching the right one.** That's why the stack goes all the way to the base cases before anything returns.

### Tabulation (bottom-up) — no recursion at all
```python
dp = [0] * (n + 1)
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
return dp[n]
```
Starts at the base cases and walks **up**. Every value it needs is already behind it, so **nothing is ever called.**

| | Memoization | Tabulation |
|---|---|---|
| Direction | n → base → back up | base → n |
| Shape | recursion + dict | a loop |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` cache **+ `O(n)` call stack** | `O(n)` table → **`O(1)` rolling** |
| Risk | recursion-limit crash | none |

**Working rule: derive the recurrence, then — fill order obvious ⇒ bottom-up; fill order not obvious ⇒ memoize.** (`#139 Word Break`, tree DP and `#494` are where top-down earns its keep.)

> **The recurrence is NOT recursion.** `dp[i] = dp[i-1] + dp[i-2]` is a **formula**. Recursion is one way to evaluate it; a loop is another. **You cannot tabulate without the recurrence, so the recursive thinking happens either way.** *(Day 37 — this was the blocking confusion.)*

---

## Step 5 — the space collapse, and it is NOT a Fibonacci trick

```python
a, b = 1, 2
for i in range(3, n + 1):
    a, b = b, a + b          # a = dp[i-2], b = dp[i-1]
return b
```

**`a, b = b, a + b` evaluates the whole right-hand side FIRST, then assigns** — which is why no temp variable is needed.

| | a | b |
|---|---|---|
| start | 1 | 2 |
| i=3 | 2 | **3** |
| i=4 | 3 | **5** |
| i=5 | 5 | **8** |

> **The collapse works with ANY recurrence that reaches back a fixed number of steps.** The `+` is incidental — it can be `min`, `max`, anything. *(Day 37: he believed it was arithmetic special to Fibonacci. It isn't.)*

---

## The three problems — one skeleton, three operators

| problem | `dp[i]` means | recurrence | operator |
|---|---|---|---|
| **#70** Climbing Stairs | ways to reach step `i` | `dp[i-1] + dp[i-2]` | *how many* ⇒ `+` |
| **#746** Min Cost | min cost to **reach** `i` *(not incl. its toll)* | `min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])` | *cheapest* ⇒ `min` |
| **#198** House Robber | max robbable from houses `0..i` | `max(nums[i]+dp[i-2], dp[i-1])` | *most* ⇒ `max` |

### #70 — derive the recurrence by splitting on the LAST move
Count the `n = 4` sequences (there are 5) and split them by whether they end in `1` or `2`:
**3 end in `1`** ⇒ strip it, you're standing on `3` ⇒ those are `ways(3)`.
**2 end in `2`** ⇒ strip it, you're standing on `2` ⇒ those are `ways(2)`.
**Two groups, no overlap, nothing missed.** Base: `ways(1)=1`, `ways(2)=2`.

### #746 — read the rules carefully, they're badly worded
**You pay `cost[i]` to LEAVE step `i`** — a toll on departure. **Standing is free**, and you start on index `0` or `1` for free. **"The top" is index `len(cost)`**, one past the last step.
`cost = [10,15,20]` → **15**: start on index 1, pay 15, a 2-step move lands on index 3 = the top.
**Base:** `dp[0] = dp[1] = 0`. **Answer: `dp[len(cost)]`**, not `dp[len(cost)-1]` — the single most common wrong submission.

### #198 — the one where the recurrence isn't obvious
**⚠️ "Rob the even indices or the odd indices, take the max" is WRONG.** Killed by `[2,1,1,2]`: even ⇒ 3, odd ⇒ 3, **actual answer 4** (rob index 0 and 3, **skipping two houses**). The rule is *no two adjacent*, **not** *alternate*.
> **That's why greedy shortcuts die on DP: the number of valid choice-patterns is exponential and no fixed rule enumerates them.** DP works by asking a local question at each position and letting the answer accumulate.

At house `i`: **rob it** ⇒ `nums[i] + dp[i-2]` (house `i-1` is now banned) · **skip it** ⇒ `dp[i-1]`.
**Base:** `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])` — with one house behind you, take the bigger.

**⚠️ `[5]` crashes** the array version — `dp[1]` doesn't exist for a one-house street. **Better: start both rolling variables at `0`:**
```python
a, b = 0, 0
for n in nums:
    a, b = b, max(n + a, b)
return b
```
**No guard needed, and `[]` returns `0`.** *"Before any houses, the best is nothing"* is a base case true for **every** length.
> **When a guard exists to protect a base case, ask whether a more general base case removes the guard.**

## Your gotchas
- **Define `dp[i]` as a sentence before anything else.** Inclusive or exclusive of `i`? Say which.
- **Price the loop body** (B-10): `one pass costs ___ × ___ passes`.
- **The array is a scaffold.** Write it first, collapse it after — never collapse before the indices are right.
- **`dp[len(cost)]` vs `dp[-1]`** — say what the answer *is*, don't return whatever the counter last happened to be.

## Still to come
#5 Longest Palindromic Substring · #91 Decode Ways · #322 Coin Change · #152 Max Product Subarray · #139 Word Break · #300 LIS · #213 House Robber II (the circular variant — two runs of this exact function).
