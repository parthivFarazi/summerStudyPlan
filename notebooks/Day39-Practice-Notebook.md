# Day 39 — Wed Aug 5, 2026 — 1-D DP cont. (#322 Coin Change, #152 Maximum Product Subarray)

> **Block 2 first** (DP-heavy day, `COACHING.md` rule 17). **First session run under rules 20 and 21.**
> **STATUS: COMPLETE.** Block 2 ~2 h 18 m · Block 1 **6 of 7** in ~15 min.

| | |
|---|---|
| `#322` Coin Change | **1:14:00** ✅ |
| `#152` Maximum Product Subarray | **1:04:00** ✅ |
| **Block 2 total** | **~2 h 18 m** |
| **Block 1** | **6 of 7 · ~15 min** |

**Both `O(1)`-space-optimal where possible, both verified against INDEPENDENT oracles** (a BFS shortest-path for `#322`, an `O(n²)` brute force for `#152`) — never a second copy of his own algorithm.

---

# Block 2 · Problem 1 — #322 Coin Change (Medium)

## 🟢 He asked a clarifying question first
*"Will the coins given be sorted?"* — **the right instinct, and `GOALS.md` explicitly scores this.** Answer: not guaranteed; `coins.length ≤ 12` so sorting is free. *(It turns out not to help.)*

## Greedy proposed, and killed in ten seconds

His rule: take the largest coin that fits, subtract, repeat.

**Counter-example given, not explained: `coins = [1, 3, 4]`, `amount = 6`.**

He ran his rule correctly — `4 + 1 + 1` = **3 coins** — and then wrote *"this was the best way I would have done it by hand."*

> **🔴 That's his rule vouching for itself.** Asked flatly to *"make 6 out of [1,3,4] using exactly TWO coins,"* he had it instantly: **`3 + 3`.** **M-043's shape again — he asserts rather than tests — but this time one direct instruction was enough.**

> **🔑 Why greedy keeps dying on these:** taking the biggest coin **locks you out of combinations that use none of it**. `4` looks best locally and is exactly why `3+3` is unreachable. **A fixed local rule cannot search an exponential space of choices.** Same sentence that killed his even/odd idea on `#198`.

## Deriving the recurrence — split on the last move

Third use of the tool, and it's becoming automatic. Given the enumerated table:

| if the last coin is… | left over | need to know |
|---|---|---|
| `1` | `6 − 1 = 5` | `best(5)` |
| `3` | `3` | `best(3)` |
| `4` | `2` | `best(2)` |

**He produced `best(k) = 1 + min(best(k-1), best(k-3), best(k-4))` unaided**, and — importantly — **named his own remaining problem**: *"This is have to find way to generalize it for any number of coins."*

**Generalisation taught by pointing at his OWN code from `#121`, one day earlier:**

```python
profit = max(profit, num - minVal)      # a running best, updated inside a loop
```

Same move, so the answer was his: keep a running `least`, loop over `coins`.

## 🔑 dp[0] again — and the general rule

He proposed base cases `best(n) = 1` for every `n` in `coins`. **True, but a consequence, not the base.** Asked *"what is `best(0)`?"* he answered **`0`** immediately — 24 hours after losing an hour to the same slot on `#91`.

| | `dp[0]` | why |
|---|---|---|
| `#91` — counting **ways** | **1** | exactly one way to decode nothing: the empty way |
| `#322` — counting **coins** | **0** | it takes zero coins to make nothing |

> **Same slot, different value, because the quantity being counted is different.** `dp[0]` is always *"the answer for the empty case"* — **work out what it means, don't reach for 1 or 0 by habit.**

## New machinery — `float('inf')` (pre-taught in isolation, rule 2)

```python
min(float('inf'), 5)  ->  5      # inf never wins a min
1 + float('inf')      ->  inf    # inf stays inf when you build on it
```

Shown working on `coins=[2], amount=3`:

| | `dp` | |
|---|---|---|
| start | `[0, inf, inf, inf]` | `dp[0]=0`, rest unreachable |
| `k=1` | `[0, inf, inf, inf]` | `2` doesn't fit. Nothing updates. |
| `k=2` | `[0, inf, 1, inf]` | `1 + dp[0]` = 1 |
| `k=3` | `[0, inf, 1, inf]` | `1 + dp[1]` = `1 + inf` = inf |

> **The sentinel does the `-1` logic for you.** Anything still `inf` at the end was never reachable — no separate feasibility check needed.

## ⛔ The negative-index trap, second day running

He proposed handling `i - c < 0` with `dp[i] = min(dp[i], float('inf'))`. **His reasoning was actually sound** — he was avoiding clobbering a value an earlier coin had set — but the real issue is that indexing at all is unsafe.

**Measured, on 3,000 random cases with the `i - c >= 0` guard removed:**

| | count |
|---|---|
| silently **WRONG** answer | **38** |
| **`IndexError`** crash | **1,301** |
| happened to be right | 1,661 |

Worked example: `coins=[5], amount=3` ⇒ `dp` has 4 entries; at `i=1`, `i-c = -4`; **Python reads `dp[-4]` = `dp[0]` = 0**, computes `1 + 0 = 1`, and returns **3** instead of `-1`.

> **`s[-1:1]` gave `''` on `#91`. `dp[-4]` gives `dp[0]` here. Neither one signals anything is wrong.**
> **⛔ Whenever you write `x[i - something]`, the guard is `i - something >= 0` and it belongs on the `if`, not folded into a `min`.**

## 🔴 M-041 — patched before diagnosing, and the patch was wrong

His code crashed on `coins=[1], amount=0`. He proposed: *"Do I just add a line saying, if amount == 0: return 0?"*

**The crash was not at `amount == 0`. It was this:**

```python
for n in coins:
    dp[n] = 1                  # dp has amount+1 entries; dp[n] is out of range when n > amount
```

```
coins=[1], amount=0  ->  dp has 1 entry (index 0 only).  dp[1] = 1  ->  IndexError
coins=[5], amount=3  ->  dp has 4 entries (0..3).        dp[5] = 1  ->  IndexError
```

**His proposed patch would not have fixed it** — `coins=[5], amount=3` has `amount != 0`, so the guard never fires and it still crashes. **He'd have watched one test go green and shipped the bug.**

> **🔑 And the loop was never needed.** `dp[c] = 1 + dp[c - c] = 1 + dp[0] = 1`. Deleting it makes every test pass:
> ```
> coins=[1,3,4], no seeding  ->  dp = [0, 1, 2, 1, 1, 2, 2, 2, 2]
>                                       ↑     ↑  ↑
>                                    dp[1]=1  dp[3]=1  dp[4]=1   fell out on their own
> ```
> **He wrote his base case correctly and then wrote it a second time by hand — and the hand-written copy is what broke.** *(Identical shape to `#91`'s redundant `if` the night before. **Twice in two days: once `dp[0]` is right, stop. The recurrence fills in the rest.**)*

## Final #322 — verified

**✅ 6,392 cases vs an INDEPENDENT BFS shortest-path oracle, zero failures.** `[186,419,83,408]` → 6249 gives 20. At the ceiling (12 coins, amount 10,000): **0.0147 s**, exactly the ~120,000 operations predicted.

**Complexity, his:** `O(k·n)` time, `O(k)` space, ***with `k` and `n` explicitly defined*** — the fix for his own earlier sentence in which `n` meant two different things at once. **That's the B-8 discipline arriving unprompted.**

---

# Block 2 · Problem 2 — #152 Maximum Product Subarray (Medium)

## Vocabulary — "contiguous"
He asked. **Handed over immediately (rule 20c), concretely:** every contiguous subarray of `[-2,0,-1]` listed, and `[-2,-1]` shown as the one that isn't allowed. **Connected to substring-vs-subsequence, which he derived himself on `#5`.**

## Three drafts, three distinct failure classes

**Draft 1** — running product, `maxCount = 0`, no reset. **Wrong on 1,928/5,000 random arrays.**

> **📌 Coach error worth recording: all three of my original examples PASSED his wrong rule.** A test set that agrees with a wrong answer is testing nothing. **Had to build a discriminating set: `[-2]` (all-negative init), `[0,2]` (zero kills the running product forever), `[2,-5,-2,-4,3]` (the real insight).**

**Draft 2** — `maxCount = nums[0]`, `max(num, maxCount*num)`. Fixed failures 1 and 2. **Wrong on 3,187/5,000 — worse than draft 1**, because it still carried one value and still had no separate answer.

## 🔑 The insight — and he had already said it

Asked what the running product was just before the winning subarray, he answered **"−10"** — and walked straight past it. **−10 is the SMALLEST product ending there, not the largest.**

Shown the actual subarrays rather than just numbers *(the second attempt at this table; the first showed only products and did not land — rule 20a)*:

```
i=1 (nums[1] = -5)
    BIGGEST  ending here:  [-5]    = -5
    SMALLEST ending here:  [2,-5]  = -10

i=2 (nums[2] = -2)  <-- a NEGATIVE
    [-5]     + (-2)  ->  [-5, -2]     =  -5 × -2  =  10
    [2, -5]  + (-2)  ->  [2, -5, -2]  = -10 × -2  =  20   <-- the winner
    start fresh      ->  [-2]         =            -2
```

> **The biggest subarray grew out of the SMALLEST one.** A negative `nums[i]` **swaps which end is best** — keep only the maximum and you discard the very number about to become the maximum.

**He then stated the rule himself, correctly and completely:** *"there are two decisions I can make: either multiply it by the biggest or the smallest and then record the output… to record the smallest I compare the minimum between (nums[i], a, b) and to record the biggest, I choose the maximum out of the three."*

**And it killed his `O(n²)` worry in the same breath** — he had believed he needed to look back over every combination. **Three candidates per index, `O(1)` each.**

## 🔴 The simultaneous-update bug — and a very sharp self-observation

```python
biggest  = max(nums[i], nums[i] * biggest, nums[i] * smallest)
smallest = min(nums[i], nums[i] * biggest, nums[i] * smallest)
                                  ^^^^^^^ already the NEW biggest
```

**Isolated by measurement:**

| version | wrong on |
|---|---|
| his | **2,825 / 5,000** |
| + fix the stale update only | 1,768 / 5,000 |
| + fix stale update **and** add a separate answer variable | **0 / 5,000** |

**Two independent bugs**, and the second — no separate answer variable — is the one he had **correctly diagnosed himself** two messages earlier (*"you do need two variables"*) and then not implemented.

**🔑 The keeper.** On `[-4,-3,-2]` his code returned **72** and he said: *"I am tracing it and it should be 12."*

> **He traced the algorithm he MEANT to write. The code on screen did something else.** *(Exact same disease as M-042 — pricing intent rather than code.)*

**What actually cracked it — checking achievability:**

```
nums = [-4,-3,-2]
every achievable product:  {-24, -4, -3, -2, 6, 12}
```

**`-36` is not on that list. Neither is `72`.** `smallest` became `-36` at `i=1` (`-3 × 12`, where `12` was the `biggest` computed one line above), and `72 = -2 × -36` is garbage built on garbage.

> **⛔ NEW REUSABLE MOVE: when a DP value looks wrong, ask whether it is even ACHIEVABLE.** A number corresponding to no real subarray means the state went corrupt **earlier than where you're looking.** It converts *"why is the answer wrong"* into *"which line first wrote an impossible value."*

**The fix pointed at a tool he already owns** — `a, b = b, a + b`, used four times this week on `#70`/`#746`/`#198`. **Python evaluates the whole right-hand side before assigning.** He got it at once: *"Oooooooh they are not doing it simultaneously."*

## Final #152 — verified

**✅ 133,178 arrays vs an `O(n²)` brute force, zero failures** — every array up to length 7 over `{-2,-1,0,1,2}`, every array up to length 9 over `{-3,0,3}`, 6,000 random over `[-10,10]`. **Every case that killed an earlier draft passes.** `n = 20,000` in **0.0065 s**.

**Complexity, volunteered:** `O(n)` time, `O(1)` space.

---

# Day 39 — running notes

## 🟢 B-10
Complexity volunteered unasked on **both** problems. On `#322` he initially overloaded `n` (coins in one clause, something else in another) and **fixed it by naming his variables explicitly** — the exact B-8 discipline, applied to a complexity statement.

## 🔴 M-041 — third instance in two days
Proposed `if amount == 0: return 0` before diagnosing; the patch would not have fixed the bug. **Diagnosing costs less than patching.**

## 🟢 M-043 improving
`"246"` on Day 38 was volunteered. Today, on `[1,3,4]`, he still wrote *"this was the best way I would have done it by hand"* — but **one direct instruction produced `3+3` immediately.** The gap is narrowing.

## Timing
| | time |
|---|---|
| `#91` (Day 38) | 1:42:00 |
| `#322` | **1:14:00** |
| `#152` | **1:04:00** |

**Three first-contact problems, monotonically faster.** Different problems of different difficulty, so not clean evidence — **but it is the data the Day 47 pace re-decision runs on. Keep recording it.**

## 📌 Coach errors
1. **My three `#152` examples all passed his wrong rule** — they discriminated nothing. **Build the failing set before presenting the problem, not after.**
2. **First `#152` table showed products without showing the subarrays behind them, and did not land.** The version with actual subarrays did. **Rule 20a means show the OBJECTS, not just their values** — the same lesson as `ways(0)`'s decoding sets.


---

# Block 1 — 6 of 7 · ~15 min

| # | item | tier | | |
|---|---|---|---|---|
| 1 | **#5** Longest Palindromic Substring | 1d → full | **7:32** | ✅ → 3d |
| 2 | **#347** Top K Frequent | 🗣 | — | ✅ → 60d |
| 3 | **#238** Product of Array Except Self | 🗣 | — | ✅ → 60d |
| 4 | **#150** Evaluate RPN | 🗣 | — | ✅ → 21d |
| 5 | **#21** Merge Two Sorted Lists | 🗣 | — | ❌ **reset → 1d** |
| 6 | **#104** Maximum Depth of Binary Tree | 🗣 | — | ✅ → 21d |
| 7 | **#206** Reverse Linked List | 🗣 | — | ✅ → 21d |

## 🟢 `#5` — M-043 closing, measured

He wrote **`right - left + 1`** again — *the exact expression that died to a trace yesterday* — and **caught it himself in his own test before sending.** Measured: that version is **wrong on 1,054 of 3,000 random strings (35%).**

> **Yesterday: the disproving trace was on screen and he replied *"that is the right answer"* without substituting. Today: same error, self-caught, no prompting.** The difference is that he ran it.

**✅ 11,373 cases, zero failures.** Complexity volunteered with **"auxiliary"** correctly qualified.

## ⛔ `#21` FAILED — and not by blanking

**His described approach contained no value comparison at all:**

```
while curr1 and curr2:
    curr.next = curr1;  curr1 = curr1.next;  curr = curr.next
    curr.next = curr2;  curr2 = curr2.next;  curr = curr.next
```

**That is interleaving, not merging.**

```
list1=[1,2,4]  list2=[1,3,4]   his -> [1,1,2,3,4,4]   correct -> [1,1,2,3,4,4]   ok (coincidence)
list1=[1,2,3]  list2=[7,8,9]   his -> [1,7,2,8,3,9]   correct -> [1,2,3,7,8,9]   ✗
list1=[1,5,9]  list2=[2,3,4]   his -> [1,2,5,3,9,4]   correct -> [1,2,3,4,5,9]   ✗
list1=[]       list2=[0]       his -> []              correct -> [0]             ✗
```

**Two things missing, not one:** the comparison (*"which head is smaller?"* — the entire problem) **and** the leftover-tail attach.

> **⛔ Graded FAIL, and the reason matters: he did not blank.** He gave a **confident, detailed, complete-sounding approach that does not solve the problem.** In an interview that is the worse failure mode, because nobody interrupts you.
>
> **📌 COACH ERROR, SECOND TIME TODAY: my example passed his wrong approach.** `1→2→4` and `1→3→4` happen to interleave into the correct order. **Build the discriminating case before presenting the problem, not after.** *(Same error as `#152`, four hours earlier.)*

## Precision notes handed over

| item | note |
|---|---|
| **#347** | narrated `bucket[freq] = key` (**assigns**) where `.append` belongs. `[1,1,2,2,3]` — two numbers tie at frequency 2 and one is lost. **He described the container as a list of lists and then used it as a scalar — B-5 in miniature. Self-caught in one line.** |
| **#150** | `#150` wants truncation **toward zero**; Python's `//` rounds **toward −inf**. `-7 // 2 = -4`, but the answer is `-3`. **Use `int(a / b)`.** Only bites on negatives — which is why it survives casual testing. |
| **#104** | space is `O(h)`: `O(n)` worst-case (skewed), `O(log n)` balanced. Saying it that way shows you know *why*. |

## 🟢 B-10
**Complexity volunteered on every item, unasked, both halves.** `#5`'s **"auxiliary"** qualifier held from yesterday. `#238`'s *"`O(2n)` iterations at `O(1)` each"* was precise. **No amortized cases arose today, so the `#739` gap is untested — watch for it.**
