# Day 38 — Tue Aug 4, 2026 — 1-D DP cont. (#5 Longest Palindromic Substring, #91 Decode Ways)

> **Block 2 first** (first-contact DP day, `COACHING.md` rule 17).
> **STATUS: COMPLETE.** Block 2 ran Tue Aug 4 evening (~2 h 43 m). **Block 1 ran Wed Aug 5 morning as the Day 38 tail — 7 of 7 in ~22 min.** Full Block 1 write-up at the bottom of this file.

| | |
|---|---|
| `#5` Longest Palindromic Substring | **61:25** ✅ approach derived entirely by him |
| `#91` Decode Ways | **1:42:00** ✅ recurrence handed to him · **tabulation + O(1)-space added Aug 5** |
| **Block 2 total** | **~2 h 43 m** |
| **Block 1** (Aug 5 morning) | **7 of 7 · ~22 min** ✅ — see the section at the bottom |

---

## Housekeeping — the working folder was not connected

Session opened with only the **tracker** folder mounted. He asked *"do you have access to all appropriate folders?"* — he was right to. `job-search/LeetCode Practice` was **not** connected; requested and granted mid-session. **Check both mounts at session start, not after.**

---

# Block 2 · Problem 1 — #5 Longest Palindromic Substring (Medium)

**Opening state: *"I have no clue how to start on this question."***

## The unblocking move (worth more than the problem)

> **When stuck: ask what the dumbest possible thing is that would definitely work.**
> Get *any* correct solution, price it, then attack whatever makes it expensive. **The clever solution is almost always the dumb one with one specific waste removed.**

## Deriving the brute force

**Step 1 — how many substrings?** He answered **`2ⁿ`**. Asked to *list* every substring of `"abc"`, he wrote seven and left out `[ac]`, correctly explaining: *"because there is always b in the middle and it could never be formed."*

> **He derived substring-vs-subsequence himself.** `2ⁿ` is the **#78 Subsets** number — he reached for it because it was the counting problem he'd drilled most recently. **Subsets can skip elements; substrings cannot.**

| | contiguous? | count for `"abc"` |
|---|---|---|
| subsequence | no | `2ⁿ` = 8 |
| **substring** | **yes** | **6** non-empty |

**Step 2 — the count.** Grouped by starting letter: `3, 2, 1`. He answered **`n!`**.

> **`n = 3` cannot distinguish `3+2+1 = 6` from `3! = 6`.** Sent to `n = 4`: he listed all ten by hand and killed `n!` himself (10 ≠ 24), then produced **`T(n) = T(n−1) + n`** unprompted.
>
> [INSIGHT] **He wrote a recurrence, one day after learning what a recurrence is, without the word "DP" anywhere near it.** Closed form `n(n+1)/2` → **`O(n²)`**.

> **A recurrence is not a bound.** It describes the work; you have to *solve* it to get a bound. `n(n+1)/2` → `(n²+n)/2` → drop constant and lower-order term → `O(n²)`.

**Step 3 — B-10.** *"There are `O(n²)` substrings"* (his) + *"checking one costs `O(n)`"* (prompted) ⇒ **`O(n³)`**, and **he multiplied the halves together without being asked.** At `n ≤ 1000` that's `10⁹` — a TLE. **The dumb solution works and is unusable, which is exactly the right place to be.**

## Deriving expand-around-centre

Peeling, by hand:

```
abcba          abba
bcb            bb
c              (empty)
```

*"Yes every intermediate is a palindrome."* Then, on `"abba"`: *"Still a palindrome but the last one is empty."*

| | peels down to | centre is |
|---|---|---|
| odd length | one character | **on a letter** |
| even length | **nothing** | **the gap between two letters** |

Run backwards, in his words:

> ***"You take a letter, expand it outwards like a two-pointer, expand it until the letters each pointer is at isn't the same."***

**[STRUGGLE]** *"You can't really apply the centre solution here cause there is no specific centre."* — he was hunting for **the** centre. **You don't know which centre wins, so you try every one and keep the longest. That's the loop.** And *"you can see it's the right place because n = 4 and you're a human looking at four letters. At n = 1000 your eye is not an algorithm."*

**Centres: `n` letters + `n−1` gaps = `2n − 1` = `O(n)`** — and **he volunteered the Big-O unasked.**

**Full complexity, his sentence:** *"One pass will cost `O(n)` and there are `O(n)` passes therefore it will be `O(n²)`."* Space **`O(1)` auxiliary** — sharpened to *"a fixed number of variables regardless of `n`"*, not "nothing"; the returned string is **output**, not workspace.

## 🔑 Why #5 is on a DP list and isn't solved with DP

He asked directly: *"how was problem 1 a dynamic programming problem?"* **It wasn't.**

His peeling **is** the DP recurrence:

```python
dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i+1][j-1])
```

| | uses the recurrence by | time | space |
|---|---|---|---|
| DP table | storing every `dp[i][j]` | `O(n²)` | **`O(n²)`** |
| **his expand-around-centre** | re-walking outward, storing nothing | `O(n²)` | **`O(1)`** |

> **Same time, `n²` worse space. A recurrence existing does not make a table the right tool.** He had `O(1)` space in hand before DP was ever mentioned, because he attacked the *waste* instead of reaching for the pattern learned most recently. **Inverse of Mock #1's M-040.**
>
> **📌 Coach error, to fix:** the roadmap files `#5` under *"1-D DP."* That `dp[i][j]` has **two** indices — the DP solution to `#5` is 2-D, which isn't until Day 41. Right technique, wrong heading.

## His code — first draft, correct

```python
def longestPalindrome(self, s: str) -> str:
    left = 0
    right = 0
    answer = ""
    for i in range((2 * len(s)) - 1):
        if i % 2 == 0:
            left = i // 2
            right = i // 2
        else:
            left = (i - 1) // 2
            right = (i + 1) // 2
        count = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            else:
                break
        if len(s[left + 1: right]) > len(answer):
            answer = s[left + 1: right]
    return answer
```

**✅ Verified: 8,325 cases, zero failures** — every binary string ≤ len 10, every ternary ≤ len 7, 3,000 random over `abcd`; each answer checked three ways (is it a palindrome · is it a substring of `s` · does its length match an `O(n³)` oracle).

> [INSIGHT] **`answer = s[left + 1: right]`** — when the `while` exits, both pointers have stepped **one past** the valid palindrome. **He reconstructed the boundary correctly in both directions, first try.** Yesterday `#200` failed on a bounds check off by one in *both* directions. Today he got the harder version right.

**Dead code:** `count` incremented and never read; `left = 0` / `right = 0` overwritten before use.

## ⛔ B-10 — the slice inside the loop

```python
if len(s[left + 1: right]) > len(answer):
```

He guessed *"len() costs O(n)."*

> **`len()` on a Python `str` is `O(1)`** — the object stores its own length. **Slicing is the cost: `s[a:b]` allocates and copies, `O(k)` in the slice width.**

**The same line, in Mock #1's 5.67 s TLE:**

```python
key2 = "".join(sorted(s2[left:right]))
                      ^^^^^^^^^^^^^^ O(m) slice, inside an O(n) loop
```

**Measured, honestly:**

| input, `n = 1000` | his | without the slice | |
|---|---|---|---|
| `"a" * 1000` | 0.0469 s | 0.0365 s | **1.3×** |
| random `abcd` | 0.0006 s | 0.0004 s | **1.5×** |

**1.3×, not 2,600×. He was right that the bound doesn't move — a constant-factor waste, not a TLE.** The point is seeing it, because *the version that mattered looked identical*.

## 🔴 M-043 — three formulas, none tested

| he asserted | died to | seconds |
|---|---|---|
| `2ⁿ` substrings | listing `"abc"` — six, not eight | 20 |
| `n!` | trying `n = 4` — ten, not twenty-four | 30 |
| `right - left + 1` | substituting `left=−1, right=3` — five, not three | 5 |

**On the third, the trace with both numbers was on screen and he replied *"right - left + 1 is the right answer"* — without substituting.** Only on a flat *"do the arithmetic, don't assert it"* did he produce **`right - (left + 1)`**.

> **His reasoning is strong; his verification is the gap. One concrete case, plugged in, before believing his own formula.** Five seconds, and it caught all three.
>
> **Best form: for any `s[a:b]`, length is `b − a`.** Read it off the bounds — don't memorise an off-by-one.

## Final #5

```python
def longestPalindrome(self, s: str) -> str:
    answer = ""
    for i in range((2 * len(s)) - 1):
        if i % 2 == 0:
            left = i // 2
            right = i // 2
        else:
            left = (i - 1) // 2
            right = (i + 1) // 2
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        if right - (left + 1) > len(answer):
            answer = s[left + 1: right]
    return answer
# O(n^2) time, O(1) auxiliary space
```

**✅ 11,373 cases, zero failures. 0.0413 s at the constraint ceiling.**

---

# Block 2 · Problem 2 — #91 Decode Ways (Medium)

**1:42:00. Almost none of it was DP** — the recurrence was written inside the first twenty minutes. **The rest was `ways(0) = 1`.**

## Deriving the recurrence

Stuck again, but **[INSIGHT] he produced the counter-example before the formula, unprompted** — *"this pattern doesn't really work if it is 246."* **That's the M-043 habit, applied ten minutes after being told about it.** *(Minor: wrote `[2, 64]` for `[2, 46]` — B-8, read digits off the string.)*

**Pointed at yesterday's tool — split on the LAST move.**

**[STRUGGLE]** *"the last chunk which is always 6 here"* — he assumed the last chunk was always the last *digit*. Asked what `[2, 26]`'s last chunk was: *"You take away the 26, it is [2]."* **Two cases, and every decoding falls into exactly one.**

**Notation:** `ways(i)` = decodings of the **first `i` characters** — a **count of characters, not an index**. He asked *"what is i in ways(i)?"*, which was the right question.

He produced **`ways(i) = ways(i-1) + ways(i-2)`**.

> [INSIGHT] **That is `#70` Climbing Stairs, letter for letter. He solved this problem yesterday and didn't know it.**

## The conditions

Broken on his own `"246"`: recurrence says 3, truth is 2. He named the fault — *"[2, 46] isn't true"* — and reached the right rule via *"we do not consider ways(i-2) if int(s[i-2:i]) > 26."*

**⚠️ First error worth keeping:** he first wrote **`ways(i-2) = 1`** when the chunk is invalid. `ways(2) + 1 = 3` **re-derives the original bug.** *"How many decodings of `"2"` with `"46"` on the end exist?"* → **zero, not one.**

**Final form:**

```
ways(i) =  ways(i-1)   if s[i-1]    is a valid 1-digit chunk (1–9),   else 0
         + ways(i-2)   if s[i-2:i]  is a valid 2-digit chunk (10–26), else 0
```

**`10–26`, not `1–26`** — below 10 means a leading zero, which is why `"06"` is 0.

## 🔴 THE HOUR — `ways(0) = 1`, and it is B-5

He would not accept the base case. Four prose explanations failed:

1. arithmetic — *if `ways(0) = 0`, `"10"`'s only answer `[10]` is unreachable*
2. `0` = **impossible**, `1` = **already done**
3. routes from your house to your house = one, stand still
4. same base as *one way to climb 0 stairs — don't climb*

**He kept writing `ways("") = 0`, three times, including immediately after being given `1`** — and on `"10"` **got the right answer from two cancelling errors**, crediting `[1, 0]` (not a decoding) and discarding `[10]` (the actual answer).

**The real fault, finally:**

> **He was counting LETTERS, not DECODINGS.**
>
> | question | answer |
> |---|---|
> | how many **letters** in the decoding of `""`? | **0** — he was right |
> | how many **decodings** does `""` have? | **1** |
>
> ```
> decodings of ""   =  { [] }    ONE element, which happens to be empty
> decodings of "0"  =  {   }     ZERO elements
> ```
>
> **`{ [] }` is not `{ }`.** A box containing an empty bag is not an empty box.
>
> **⛔ This is B-5 · M-036 — container vs contents.** The *decoding* is the container; the *letters* are the contents. Same failure as `#133`'s `node.neighbors` vs `clone.neighbors`, from a completely new direction. **It cost roughly an hour on a problem with no graphs in it.**

**Built `decode-ways-dp.html`** (rule 9 — when prose fails, visualise). Steps the dp table cell by cell showing **the actual set of decodings at every cell**, so `ways(0) = { [] }` sits next to `ways(1) = { }` for `"06"`. Recurrence checked against a brute-force enumerator on **1,111,110 strings**, zero mismatches. His verdict: *"it kinda makes sense."*

## ⛔ B-10 — the fixed-width slice (he got this one)

Asked whether `s[i-2:i]` makes one pass `O(n)`, he first said **yes** — over-correcting from `#5` — then caught it:

> ***"it is always O(2) so essentially it is O(1) so a single pass costs O(1), and there are n passes."***

**Full drill sentence, correct, self-corrected.**

> **A slice costs `O(k)` where `k` is its WIDTH.** `s[i-2:i]` is width 2 no matter how long `s` is; `s[left+1:right]` on `#5` was width up to `n`. **Same syntax, different cost — read the indices, not the operator.**

## Draft 1 — crashes

```python
def numDecodings(self, s: str) -> int:
    def ways(i):
        if i == 0:
            return 1
        if 1 <= int(s[i - 1]) <= 9:
            a = ways(i - 1)
        else:
            a = 0
        if 10 <= int(s[i - 2: i]) <= 26:
            b = ways(i - 2)
        else:
            b = 0
        return a + b
    return ways(len(s))
```

```
"12"  -> ValueError: invalid literal for int() with base 10: ''   CRASH
"226" -> ValueError   CRASH
"06"  -> ValueError   CRASH
"10"  -> 1  OK
```

**🟢 He ran it. Three of four would have gone to a submit otherwise** — rule 14 working.

**🔴 But he could not instrument it:** *"I can't see, I don't know how to do it. I use the NeetCode testing always."* **He could not add a `print` and read a trace.** Coach ran it for him:

```
ways(3)  ->  s[1:3]  = '26'      ok
ways(2)  ->  s[0:2]  = '22'      ok
ways(1)  ->  s[-1:1] = ''        <-- here
```

**New machinery taught — negative indices:**

> **A negative index counts from the END.** For `"226"`, `s[-1]` is the last char. So `s[-1:1]` asks for *"index 2 up to index 1"* — backwards — and **Python silently returns `''` rather than erroring.** `int('')` then blows up **one line away from the actual bug.**

He produced the guard himself: **`if i > 1 and 10 <= int(s[i - 2: i]) <= 26:`** — `and` short-circuits, so `int()` never sees the bad slice. **✅ 1,115,110 strings, zero mismatches.**

## 🔴🔴 M-042 REPEAT — he priced a recursion as a loop

**He stated `O(n)` time, having said *"one pass costs `O(1)`, there are `n` passes."***

**He wrote a recursion. There are no passes.**

| `n` for `"1"*n` | calls | ×|
|---|---|---|
| 10 | 232 | 11.6× |
| 20 | 28,656 | 11.1× |
| 30 | **3,524,577** | 11.1× |

**Every 5 characters × 11 — `O(φⁿ)`, Fibonacci growth.** At `#91`'s ceiling `n = 100`: **1,146,295,688,027,637,940,224 calls ≈ 7.3 million years.**

> **Yesterday (M-042) he priced the naive `#70` recursion as `O(n)` — 204,668,309 calls at n=40. Today, one day later, same shape, same wrong answer.**
>
> 🔑 **The new and more valuable finding: he priced the algorithm IN HIS HEAD (a loop over `n`), not the code ON HIS SCREEN (a branching recursion).** `O(1)` per pass was even correct — *for the loop he never wrote.*
>
> **⛔ DRILL: price the code you wrote, not the approach you intended. Before any complexity — "is this a loop or a recursion?" If recursion, ask "how many CALLS," never "how many passes."**

## Final #91 — memoized

```python
def numDecodings(self, s: str) -> int:
    memory = {}
    def ways(i):
        if i == 0:
            return 1
        if i in memory:
            return memory[i]
        if 1 <= int(s[i - 1]) <= 9:
            a = ways(i - 1)
        else:
            a = 0
        if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
            b = ways(i - 2)
        else:
            b = 0
        memory[i] = a + b
        return memory[i]
    return ways(len(s))
# O(n) time, O(n) space (dictionary + call stack)
```

**Memo applied unaided** — he named it himself yesterday (*"if it has been computed, store it somewhere and retrieve it — so use a dictionary"*).

**✅ 1,116,110 strings, zero mismatches.**

| `n` | calls **now** | calls **before** |
|---|---|---|
| 10 | **20** | 232 |
| 20 | **40** | 28,656 |
| 30 | **60** | 3,524,577 |

**Exactly `2n`. At `n = 100`: 200 calls, 0.000117 s — against 7.3 million years.** One dictionary.

**His complexity, unprompted and complete:** *"O(1) work for each and it has to do it n times so it is O(n) time but it requires O(n) space because of the recursion and dictionary."* **Both space sources named — his weak side, cleanest statement of the day.**

**🔸 OWED:** the `O(1)`-space rolling-variable collapse — the version an interviewer expects. He did exactly this unprompted on `#198` yesterday. **Build it cold when `#91` returns at 1d.**

---

# Blockers — Day 38

| | |
|---|---|
| **⛔ B-10** | **Mixed, first real movement.** Volunteered the halves **twice unasked** (`2n−1` centres; the memoized bound) and **self-corrected the fixed-width-slice trap** into the full drill sentence. **But** priced a Fibonacci recursion as `O(n)` (**M-042 second occurrence, one day apart**) and guessed `len()` was `O(n)`. **Not cleared.** |
| **⛔ B-5** | **FIRED HARD — the `ways(0)` hour.** Counted contents (letters) when asked for containers (decodings). Blocker's clean streak **reset to 0**. |
| **⛔ B-8** | One instance — `[2, 64]` for `[2, 46]`. Not cleared. |
| **🆕 M-043** | **States a formula without testing it on one concrete case.** Three today, plus re-asserting one *after* the disproving trace was on screen. |
| **🆕 M-044** | **Cannot instrument his own code.** No `print`-and-read-a-trace; relies entirely on NeetCode's runner. **In an interview nobody hands you a harness.** |
| **🟢 M-041** | **No instance.** He diagnosed `"246"` before proposing anything, unprompted. |

---

# Schedule — read this before Day 39

**Block 1 was NOT reached.** 7 items, 25-min box: **#200** (reset, full) · **#70 · #746 · #198** (1d, full) · 🗣 **#739 · #121 · #153**.

**It cannot roll into Day 39** — Aug 5 already carries 8, and 8 + 7 = 15 against a cap of 8.

**The plan: Block 1 runs on waking, Wed Aug 5, as the tail of Day 38.** Day 39 then runs later the same day. Aug 5 carries **25 min + 27 min of review across two sittings**, which is inside cap because they are separate sittings. Day 38 simply spans midnight.

## 🔴 The decision this session forces — raise it with him, do not absorb it

**Three hours of Block 2 for two new problems, with 15 sessions left and zero buffer.**

The DASHBOARD said to raise this after Day 39. **Day 38 makes it unavoidable now.** The `COACHING.md` rule 11 warning line — *"below ~55% pass rate, resets pile into 1d and Block 1 overruns on its own; the response is to slow new material, never to trim reviews"* — is now joined by a second failure mode: **Block 2 itself overrunning far enough to consume Block 1 entirely.** Block 1 has now under-delivered **two sessions running** (2 of 8 on Day 37, 0 of 7 on Day 38).

**His call, with the arithmetic in front of him. Not the coach's.**


---

# Block 1 — run Wed Aug 5 morning as the Day 38 tail · **7 of 7 in ~22 min** ✅

**Day 38 is CLOSED.** After 2-of-8 (Day 37) and 0-of-7 (Day 38 evening), a clean sweep — **but only because it ran as its own sitting with no Block 2 in front of it.** That is data for the capacity decision, not a refutation of it.

| # | item | tier | time | result |
|---|---|---|---|---|
| 1 | **#200** Number of Islands | 🔴 reset → full | **7:59** | ✅ → 3d |
| 2 | **#70** Climbing Stairs | 1d → full | **2:03** | ✅ → 3d |
| 3 | **#746** Min Cost Climbing Stairs | 1d → full | **3:39** | ✅ → 3d |
| 4 | **#198** House Robber | 1d → full | **3:53** | ✅ → 3d |
| 5 | **#739** Daily Temperatures | 🗣 verbal | — | ✅ → 21d |
| 6 | **#121** Best Time to Buy/Sell | 🗣 verbal | — | ✅ → 60d |
| 7 | **#153** Find Min in Rotated Array | 🗣 verbal | — | ✅ → 21d |

**Every full solve verified against an INDEPENDENT oracle**, never a copy of his own algorithm: union-find for `#200` (5,706 grids — every 1×1–3×3, 2×4, 4×2, 1×8, 8×1, plus 4,000 random, plus empty/`[[]]`/all-water/50×50-all-land) · an enumerator for `#70` (n = 1..500) · a path enumerator for `#746` (27,840 arrays) · a subset enumerator for `#198` (14,840 arrays). **Zero failures anywhere.**

## 🟢 The two repairs that landed

**`#200` — both Day-37 single-character bugs are gone.** `grid[row][col] = "0"` is an assignment now, and the bounds read `0 <= nr < len(grid)`. Yesterday those cost 448 of 512 possible 3×3 grids.

**`#198` — he guarded `[5]` unprompted.**
```python
if len(nums) == 1:
    return nums[0]
```
**Yesterday `[5]` threw `IndexError` on a case named out loud before he wrote a line.** Today the guard was there without being asked. *(Confirmed: the same code minus that guard still throws.)*

## 🟢 Rule 14, in one number

He self-caught **two** bugs on `#746` by running it — `cost[i]` where `cost[i-1]`/`cost[i-2]` belonged, and `range(2, len(cost))` stopping one short. **I measured the second: wrong on 1,415 of 2,000 random arrays — 71%.** It returns `dp[n-1]` instead of `dp[n]`. He found it in three and a half minutes because he ran the code.

## ⛔ B-10 — eight for eight, and the remaining edge

**Every complexity today was volunteered unasked, both halves, zero prompts, across all seven items.** Day 37: zero. Day 38 Block 2: two. **This is the blocker moving.**

**Two precision gaps left, both handed over as facts:**

1. **`#739` is `O(n)` AMORTIZED, and he priced it as `O(1)` per iteration.** The inner `while` can pop many times in one pass — a single iteration can cost `O(n)`. **The bound comes from counting total pushes and pops over the whole run: each index enters once and leaves at most once.**
   > **This is B-10's next level.** When a loop body contains its own loop, *"one pass costs `O(1)`"* is almost always false. Say ***"each element enters and leaves the stack once, so total work is `O(n)`."***
2. **`#121`'s `minVal = max(nums)` is a full extra `O(n)` scan** before the loop begins. Doesn't move the bound; does walk the array twice to avoid choosing a starting value. `prices[0]` or `float('inf')` is free. **Same disease as Mock #1's un-hoisted `key1`.**

**B-8:** one narration slip — called the stack *"a stack called `answer`"* and then used `stack[-1]` and `answer[popped]` as two different objects. **The stack and the result array are separate; name them separately.**

## 🟢 M-015 held
`#153`'s convergence template came back clean — `while left < right` … `return nums[left]`, the convergence point rather than a tracked answer.


---

# `#91` follow-up — Aug 5 · tabulation → `O(1)` space *(the debt from Block 2, cleared)*

**Both written cold from a blank screen. This is a harder bar than a 1d re-solve, so `#91`'s 1d rep is met and it advances to 3d.**

## Tabulation — his, first draft, correct

```python
def numDecodings(self, s: str) -> int:

    dp = [0] * (len(s) + 1)

    dp[0] = 1

    for i in range(1, len(s) + 1):
        if 1 <= int(s[i - 1]) <= 9:
            a = dp[i - 1]
        else:
            a = 0

        if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
            b = dp[i - 2]
        else:
            b = 0

        dp[i] = a + b

    return dp[-1]
```

**✅ 1,116,110 strings vs brute force, zero mismatches.** `O(n)` time, `O(n)` space.

## The collapse — taught CONCRETELY, per rule 20

He asked *"I don't know what to do with it in order to make it space optimized. Especially the base case `dp[0] = 1`."* **No prose. Showed him his own loop's reads:**

| step | writes | reads | still needed after |
|---|---|---|---|
| — | `dp[0]=1` | *(base)* | `dp[0]` |
| `i=1` | `dp[1]=1` | `dp[0]` | `dp[0]`, `dp[1]` |
| `i=2` | `dp[2]=2` | `dp[1]` + `dp[0]` | `dp[1]`, `dp[2]` ← **`dp[0]` dead** |
| `i=3` | `dp[3]=3` | `dp[2]` + `dp[1]` | `dp[2]`, `dp[3]` ← **`dp[1]` dead** |

**Two questions off that table — "what's the oldest cell you ever read?" and "so how many are alive at once?" — and he had it immediately:** *"it is always i - 2 that is the oldest cell."*

> **Contrast with the `ways(0)` hour the night before: same student, same problem, ~2 minutes instead of ~60.** The difference was showing the objects instead of describing them. **This is the rule 20 evidence.**

## Space-optimised — his

```python
def numDecodings(self, s: str) -> int:

    iMinusTwo = 0

    if 1 <= int(s[0]) <= 9:
        iMinusOne = 1
    else:
        iMinusOne = 0


    for i in range(1, len(s) + 1):
        if 1 <= int(s[i - 1]) <= 9:
            a = iMinusOne
        else:
            a = 0

        if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
            b = iMinusTwo
        else:
            b = 0


        iMinusTwo = iMinusOne
        iMinusOne = a + b

    return iMinusOne
```

**✅ 1,119,110 strings vs brute force, zero mismatches.** `O(n)` time, **`O(1)` space.**

## 🔑 Correct — but right by unreachability, which is worth more than the pass

He said he'd *"use an if statement to set up `dp[1]`."* **His `if` actually lands in `dp[0]`'s slot:**

```
s = "226"
point            iMinusTwo   iMinusOne
before loop          0           1        <-- iMinusOne is dp[0], NOT dp[1]
after i=1            1           1            dp[0] and dp[1]
after i=2            1           2            dp[1] and dp[2]
after i=3            2           3            dp[2] and dp[3]
```

**His loop starts at `i = 1`, so it computes `dp[1]` itself** — the `if` is a leftover from the other structure he'd described. **And `dp[0]` is unconditionally 1**, so the conditional is wrong in principle.

**Measured: replacing the whole `if/else` with `iMinusTwo, iMinusOne = 0, 1` gives IDENTICAL output on all 1,119,110 strings.** Zero differences.

**Why the wrong value is never observable — he found the first half himself** (*"I am already calling `s[i - 1]` the first time already, and that guard is in the loop"*), coach gave the second:

| where `dp[0]` is read | the guard on that read | so `s[0]` is… |
|---|---|---|
| `i=1`, 1-digit branch | `1 <= int(s[i-1]) <= 9` | **valid** ⇒ his `if` said 1 |
| `i=2`, 2-digit branch | `10 <= int(s[0:2]) <= 26` | forced to `"1"` or `"2"` ⇒ **valid** ⇒ his `if` said 1 |

> **Both readers are guarded by conditions that already imply `s[0]` is valid, so the wrong value is unreachable.**
> **⛔ It is still wrong. Write `iMinusTwo, iMinusOne = 0, 1` and let `dp[0]` mean what it means. Code that is right by unreachability is one refactor away from being wrong.**

**🟢 And he got the better structure without meaning to:** starting the loop at `i = 1` means **no special `dp[1]` case is ever needed** — the exact gotcha flagged the night before (`ways(1)` is not always 1; it's 0 for `"06"`). He dodged it by construction.

---

# ✅ The pace decision — made Aug 5, his call

| | remaining | lands |
|---|---|---|
| **core** | **14** — `#322 #152 #139 #300 #62 #1143 #72 #53 #55 #134 #763 #136 #191 #338` | **Day 46 ≈ Aug 12** |
| depth | 13 — `#213 #647 #416 #309 #518 #494 #695 #417 #261 #131 #17 #110 #90` | Days 47–53 |

**`GOALS.md` targets "all 66 core + a head start on depth" — depth is fall material.** At 2/day the load-bearing curriculum finishes **with 7 sessions to spare.**

**And the intuitive option was the harmful one:** dropping to 1 new/day now needs **16 sessions into 15 available**, pushing **core** past Aug 19.

**His choice: 2/day through Day 46, re-decide at Day 47** on a week of post-rule-20 session lengths.

> **Stated before he chose, and it mattered:** Day 38's 2h43m was mostly `#91`, and ~1 hour of `#91` was the coach running the Socratic method on a base case — the failure rule 20 now forbids. **Block 1 took 22 minutes for 7 items once it ran on its own. He should not decide his schedule off a data point the coach caused.**

**⛔ Re-decide at Day 47 (≈ Aug 13). Do not let it lapse.**
