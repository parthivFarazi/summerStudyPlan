# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-08-05 (Day 38 logged) · **`#5` derived unaided · `#91` in all three forms · Block 1 7/7 · pace decision made**
- **Phase:** Summer Sprint · Block C — **1-D DP consolidated**; `#5` derived unaided and correct on the first draft, `#91` written in all three forms, and **Block 1 hit 7 of 7 in 22 minutes** after 2-of-8 and 0-of-7. Core curriculum completes Day 46.
- **Sessions logged:** 38 · **Patterns learned:** 15 · **Mistakes tracked:** 44 · **Open blockers:** 3 (**B-5 fired hard**, B-10 moving fast, B-8) · ✅ B-9 cleared Day 36
- **Review queue:** **Day 39 (Wed Aug 5, later) — 7 items, ~15 min:** full **#5** (1d) · 🗣 **#347 · #238 · #150 · #21 · #104 · #206**. *(`#91` already advanced — see below.)*

## ✅ The pace decision — made Aug 5, his call

| | remaining | lands |
|---|---|---|
| **core** | **14** — `#322 #152 #139 #300 #62 #1143 #72 #53 #55 #134 #763 #136 #191 #338` | **Day 46 ≈ Aug 12** |
| depth | 13 — `#213 #647 #416 #309 #518 #494 #695 #417 #261 #131 #17 #110 #90` | Days 47–53 |

**`GOALS.md` targets "all 66 core + a head start on depth" — depth is fall material.** At 2/day the load-bearing curriculum finishes **with 7 sessions to spare.** And the intuitive option was the harmful one: **1/day now needs 16 sessions into 15 available and would push CORE past Aug 19.**

**Chosen: 2 new/day through Day 46, re-decide at Day 47.**

> ⛔ **Re-decide at Day 47 (≈ Aug 13), on a week of post-rule-20 session lengths. Do not let it lapse.**

## 🟢 `#5` — the best unaided work of the sprint

From *"I have no clue how to start"* to a correct first draft, **every step his**: substring-vs-subsequence · the triangular recurrence **`T(n) = T(n−1) + n`, written one day after learning what a recurrence is** · both palindrome parities by peeling `abcba` and `abba` by hand · expand-around-centre in his own words. **11,373 cases, zero failures.** And he reconstructed `s[left+1:right]` off-by-one correctly **in both directions, first try** — the day after `#200` failed on exactly that.

**Why `#5` sits in a DP block and isn't solved with DP:** his peeling *is* the recurrence `dp[i][j]`. The table is `O(n²)` time **and `O(n²)` space**; his two-pointer version is `O(n²)/O(1)`. **A recurrence existing does not make a table the right tool.** *(Roadmap corrected — `dp[i][j]` has two indices, so `#5`'s DP form is 2-D.)*

## 🟢 Block 1 — 7 of 7 in 22 minutes

| | tier | time | |
|---|---|---|---|
| `#200` | 🔴 reset → full | **7:59** | ✅ → 3d |
| `#70` | full | **2:03** | ✅ → 3d |
| `#746` | full | **3:39** | ✅ → 3d |
| `#198` | full | **3:53** | ✅ → 3d |
| `#739` · `#121` · `#153` | 🗣 | — | ✅ → 21d · 60d · 21d |

**Every full solve checked against an INDEPENDENT oracle** — union-find, path enumerator, subset enumerator — **48,000+ inputs, zero failures.**

**Two repairs landed unprompted:** `#200`'s `=`-for-`==` and both bounds; **`#198` guarded `[5]`**, the exact `IndexError` case named out loud before he wrote code the previous day.

**Rule 14, quantified:** he self-caught two `#746` bugs by running it. **The range off-by-one is wrong on 1,415 of 2,000 random arrays — 71%.**

> **⚠️ But Block 1 only got done because it ran as its own sitting with no Block 2 in front of it.** That is the finding, not the 7/7.

## 🟢 B-10 — moving fast. 🔴 One edge left, and it's the interview-grade one.

**Eight complexities volunteered unasked across seven review items, zero prompts** (Day 37: zero). Space correct every time, including `#200`'s `O(m·n)` recursion depth and `#91`'s *"O(n) space because of the recursion and dictionary"* — **both sources named, on his weak side.**

**🔴 The remaining edge — AMORTIZED analysis.** On `#739` he said *"each iteration requires `O(1)` work."* It doesn't: the inner `while` can pop many times, so one pass can cost `O(n)`.

> **⛔ When a loop body contains its own loop, "one pass costs ___" is almost always FALSE.** Say instead: ***"each element enters and leaves once, so total work is `O(n)`."***

**🔴 Same family:** `#121`'s `minVal = max(nums)` is a wasted extra `O(n)` scan. **🔴 M-042 fired twice in two days** — he prices his **intent**, not his **code**: Day 37 the intent was a chain and the code branched; Day 38 the intent was a loop and the code recursed.

## 🔴 B-5 fired hard — the hour that wasn't DP

> *"if it's empty shouldn't it be 0 because there are 0 letters to it"*

**He counted the CONTENTS when asked for the CONTAINERS.** `decodings("") = { [] }` — one element, which happens to be empty — versus `decodings("0") = { }` — zero elements. **`{ [] }` is not `{ }`.** Four prose explanations failed; only `viz/decode-ways-dp.html`, printing the actual decoding **set** at each dp cell, landed it. **Clean streak reset to 0, and this blocker is no longer about graphs.**

## 🆕 M-043 · M-044

**M-043 — states a formula and never tests it.** Three in one hour: `2ⁿ`, `n!`, `right - left + 1`. Each died to **one** concrete case in under 30 seconds. **Corollary: never validate a formula on `n=3` — `3+2+1 = 6 = 3!`.** 🟢 He then applied the fix unprompted ten minutes later on `"246"`.

**M-044 — cannot instrument his own code.** *"I can't see, I don't know how to do it. I use the NeetCode testing always."* **Every crash from now on: HE adds the print and reads the trace first.**

## The slice rule — settled
**`len()` is always `O(1)`; a slice costs `O(k)` in its WIDTH.** `s[left+1:right]` on `#5` is width up to `n`; `s[i-2:i]` on `#91` is width **2** forever. **Same syntax, different cost — read the indices, not the operator.** This is the line that carried Mock #1's 5.67 s TLE.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · `=` or `==`? · Bounds `0 <= i < len`? · 🔴 Does any index go NEGATIVE at the boundary? · Terminal line written? · Every branch returns? · Did the function actually get CALLED? · What does the callee hand back, and where do I catch it? · 🔴 Am I counting the things, or what's INSIDE the things? · 🔴 Loop or recursion — and did I price the one I actually WROTE? · 🔴 Does this loop contain a loop? Then price it amortized. · Is anything in the body loop-invariant?**

## ⚠️ Standing schedule note
2-D DP and Greedy follow; **core completes Day 46**. **Aug 9 and Aug 16 are worked.** Block 2 runs first on first-contact days and **Block 1 is never dropped** (rule 17). Reviews run under a **30-min box measured in TIME** (full ≈ 6 min · one-draft ≈ 4, **6 if recursive** · verbal ≈ 0.5). **⚠️ Aug 7 currently sits at ~48 min against that box** — re-tier or re-spread before it arrives.

## 🟡 Still owed
- **The slipped Jul 29 session** — one triple-new day, **still without a date**.
- **Delete the coach's stray file:** `Week 7/Day 38/block2LongestPalindromicSubstring.py`.
- **His `#5` note needs fixing** — `block2longestPalindrome.py` line 37 says *"use `right - left + 1`"*, which is the version that gave 5 instead of 3. The working code correctly uses `right - (left + 1)`. **His file, his edit.**

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | **15** | 🟡 runway exists, slack does not |
| **Sprint throughput** (new/day) | Day 38 = **2** (#5, #91) | 🟢 at the floor |
| **Core curriculum** | 14 left, **finishes Day 46 ≈ Aug 12** | 🟢 **7 sessions of margin** |
| **Schedule fit** (Days 39–53) | 15 sessions into 15 available days | 🟡 buffer owed — needs a date |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (Day 39) | **7** (~15 min) | 🟢 |
| Review backlog carried | dated through Aug 12, but **Aug 7 ≈ 48 min vs a 30-min box** | 🔴 **needs re-spreading before Aug 7** |
| **Open blockers** | **3 — B-5 (streak 0), B-10 (moving), B-8** | 🟡 |
| Review pass rate (Day 38 tail) | **7 / 7** | 🟢 **best session of the sprint** |
| **🎯 Unaided timed mediums** | **1 of 3 taken** · Mock #2 **Sat Aug 8** | 🟢 first data point beat expectation |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | **3/5** ↑ | 8 volunteered unasked in one session. **Held back by the amortized gap and by M-042 twice in two days** |
| Arrays & Hashing | 3/5 | stable |
| **Two Pointers** | **4/5** ↑ | **`#5` derived and written cold, first draft correct**, both-direction boundary reconstruction |
| Sliding Window | 3/5 | `#121` → 60d |
| Binary Search | 3/5 | `#153` convergence template clean (M-015 held) |
| Stack | 3/5 | `#739` → 21d, but priced non-amortized |
| Linked List | 4/5 | stable |
| Trees & BFS/DFS | 3/5 | stable |
| Binary Search Tree | 4/5 | stable |
| Tries | 3/5 | stable |
| Heap | 3/5 | stable |
| Backtracking | 3/5 | stable |
| Intervals | 3/5 | 4/5 needs a novel one cold (#253) |
| **Graphs (BFS/DFS)** | **3/5** | **`#200` reset cleared 7:59** — both Day-37 bugs fixed unprompted |
| **1-D DP** | **3/5** ↑ | **#70/#746/#198 all clean cold; `#91` written in all three forms — memo, tabulation, `O(1)` space.** Was 2/5 |
| **Greedy** *(previewed)* | **1/5** | Named block Aug 9–11 |

## Blockers

- **⛔ B-5 · M-036 — container vs contents. FIRED HARD Day 38, streak reset to 0.** The `ways(0) = 1` hour: counted letters when asked to count decodings. **`{ [] }` is not `{ }`.** Drill: before answering any count, say *"am I counting the things, or what's inside the things?"*
- **⛔ B-10 · M-006 — price the loop body. MOVING FAST, not cleared.** 8 volunteered unasked. **Remaining edge: amortized bounds** — when a loop contains a loop, per-pass pricing is the wrong instrument. Plus **M-042 twice in two days — he prices intent, not code.**
- **⛔ B-8 · M-029 — naming precision.** Two instances Day 38 (`[2, 64]` for `[2, 46]`; the stack narrated as `answer`). Not cleared.
- **✅ B-9 · M-001 — the recursive return channel. CLEARED Day 36.** Standing habit.
- **🆕 M-043 (formula stated, never tested) · 🆕 M-044 (cannot instrument his own code)** — both active.
- **M-042 · M-041 · M-040 · M-039 · M-034 · M-037 · M-038 · B-2 · B-4 · M-027 · M-005** — 👁 watch.

## Next Session Focus  → **Day 39** · DP heavy ⇒ **Block 2 first**

1. **Block 2 — new:** **`#322` Coin Change** and **`#152` Maximum Product Subarray** — `#322` is the first recurrence whose predecessors are a **loop over choices**, not a fixed 1-or-2 back.
2. **Block 1 — 7 items, ~15 min:** full **`#5`** (1d) → 🗣 **`#347` · `#238` · `#150` · `#21` · `#104` · `#206`**.
3. **⛔ B-10, amortized:** *"does this loop contain a loop?"* If yes, count total pushes/pops, not per-pass cost.
4. **⛔ B-10, M-042:** *"is what I wrote a loop or a recursion?"* — **before** pricing.
5. **⛔ B-5:** *"am I counting the things, or what's inside the things?"*
6. **⛔ M-044:** he adds the `print` and reads the trace. **The coach does not run it for him.**
7. **⛔ Rule 20:** concrete before abstract · two strikes then change modality · **facts get handed over, never withheld.**
8. **⛔ Rule 21:** the coach writes no `.py` into his tree. Ever.
9. **Re-spread the Aug 7 review load** (~48 min vs a 30-min box) before it arrives.
10. **The slipped session still needs a date**, and **Mock #2 is Sat Aug 8.**

---
*Weekly snapshots can be appended below as the sprint progresses.*
