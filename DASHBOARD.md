# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-08-03 (Day 37 logged) · **1-D DP acquired · #567 TLE fixed · B-10 no progress**
- **Phase:** Summer Sprint · Block C — ***1-D DP acquired** in a ~4-hour first-contact session — #70, #746, #198, every recurrence derived unaided. **The Mock #1 TLE is dead: 5.67 s → 0.0022 s.** But Block 1 reached only **2 of 8** items, and **at 3 new/day the review load is now the binding constraint**. B-10 made no progress — three prompts for a complexity, zero volunteered. Aug 9 and Aug 16 are working days.*
- **Sessions logged:** 37 · **Patterns learned:** 15 · **Mistakes tracked:** 42 · **Open blockers:** 3 (**B-10 price the loop body — no progress**, B-5 container/contents, B-8 naming) · ✅ B-9 cleared Day 36
- **Review queue:** **Day 38 (Tue Aug 4) — 7 items, ~25 min:** full **#70 · #746 · #198** (1d) · **#200** (reset) · 🗣 **#739 · #121 · #153**. Six unreached Day-37 items all landed on real dates; **drain extends to Aug 12**, every day Aug 4 – Aug 12 at 25–30 min.

## 🟢 1-D DP acquired — and the four hours were the right call

**#70 · #746 · #198 — one skeleton, three combining operators** (*how many* ⇒ `+`, *cheapest* ⇒ `min`, *most* ⇒ `max`). He didn't spend four hours solving Climbing Stairs; he spent them acquiring the pattern.

**What he produced unaided:** the `#70` recurrence, by splitting the `n=4` sequences on their **last move** · **memoization, named before I said the word** (*"if it has been computed, store it somewhere and retrieve it — so use a dictionary"*) · **his own even/odd idea for `#198`, killed by his own test case** `[2,1,1,2]` · and the `O(1)` collapse applied unprompted.

> **The two things actually blocking him were about the SHAPE of the tool, not the tool:**
> **(1) "the recurrence is recursion"** — it's a **formula**. Recursion evaluates it one way, a loop another, and **you cannot tabulate without it.**
> **(2) "`a, b = b, a + b` is Fibonacci arithmetic"** — the collapse works with **any** recurrence reaching back a fixed number of steps; the `+` is incidental.
> **Budget time for "what kind of thing is this" on 2-D DP, not just "how does it work".**

Built `viz/dp-memo-vs-tabulation.html` — **twice**, because the first version showed the stack and the cache but not the **call order**, which is what he actually needed.

## 🔴 The review load is now the binding constraint

Day 37's Block 2 carried **three** new problems ⇒ **three full solves arrive the next day** (18 min) on top of a reset. **Block 1 reached 2 of 8 items inside the 27-minute box.**

**That isn't a scheduling error — it's arithmetic.** Passes advance and stack, failures stay put, new problems keep arriving. Handled for now by spreading six items onto real dates and extending the drain to **Aug 12**.

> **If Block 1 under-delivers again this week, the choice is a longer box or fewer new problems — and that's his call, not mine. Raise it after Day 39.**

## 🔴 The honest read — Day 37

**🟢 `#567` — the mock's TLE is dead.** At the constraint ceiling: **5.67 s → 0.0022 s, a 2,600× speedup**, verified on 50,000 random cases across two alphabets.

Two bugs on the way, and the second is the keeper: **`count == 0` was the wrong test.** With `s1 = "ab"` and window `"aa"` the counters are `{'a': -1, 'b': +1}` — **sum zero, so it wrongly said `True`.** 2,929 of 20,000 cases wrong.

> **A sum of zero does not mean every value is zero.** A surplus in one character cancels a deficit in another. **When you need "all of these are true", don't reduce to a single number that can cancel.**

**🔴 The twenty seconds, at four hours deep.** `[5]` crashed `#198` — **on a test case I named in the instruction before he wrote the code** (2,007 of 20,000 random inputs crashed, every one a single-element list). And `#200`'s one-draft had **`==` where `=` belongs**, plus a bounds check off by one in **both** directions — 448 of 512 possible 3×3 grids crash. **He wrote that same bounds check correctly on `#994` an hour earlier.**

**Neither is knowledge. Both landed at the tail of the longest session of the sprint — which argues for the box, not against it.**

**🔴 B-10 made no progress.** Three prompts to get both halves of a complexity, **volunteered zero times across four problems.** He also priced the naive `#70` recursion as `O(n)` when it's `O(2ⁿ)` — *"n, then n−1, then n−2"* describes a **chain**, but each call makes **two** calls. **Same disease from the other side: pricing one call rather than the number of calls.** Measured for him: **204,668,309 calls at n=40.**

**🔴 M-035 fired twice — both mine.** Hand-written expected values in the `#746` and `#567` test lists, both wrong, his code right both times. **A hand-written expected value is a guess wearing a test's clothing.**

**⚠️ New watch — M-041.** Twice on `#567` he proposed a patch before finishing the diagnosis. **The arithmetic *is* the fix** — once the cancellation is visible the correct test is obvious; without it you get a plausible change that misses the cause.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · `=` or `==`? · Bounds `0 <= i < len`? · Terminal line written? · Every branch returns? · Did the function actually get CALLED? · What does the callee hand back, and where do I catch it? · Whose attribute is this — the original's or the copy's? · 🔴 What does ONE PASS of this loop cost, and is anything in it loop-invariant? · Is there a better approach I'm skipping because it's fiddlier?**

## ⚠️ Standing schedule note
Depth phase complete through Graphs; **1-D DP started Mon Aug 3**, 2-D DP and Greedy follow. **Aug 9 and Aug 16 are worked.** **2 new/day minimum stays and long sessions are accepted** (`COACHING.md` rule 17); Block 2 runs first on first-contact days. Reviews run the drain through **Aug 12** under a **30-min box measured in TIME** (full ≈ 6 min · one-draft ≈ 4, **6 if recursive** · verbal ≈ 0.5).

## 🟡 The slipped session is still owed
**Jul 29 had no session.** Days 38–53 is **16 sessions**; Aug 4 → Aug 19 is **16 available days.** **Zero buffer.** His call, logged Jul 30: he'll recover it. **The recovery is one triple-new day, and it still needs a date.**

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | **17** | 🟡 runway exists, slack does not |
| **Sprint throughput** (new/day) | Day 37 = **3** (#70, #746, #198) | 🟢 above the floor |
| **Schedule fit** (Days 38–53) | **16 sessions into 16 available days** | 🟡 **buffer owed** — needs a date |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Aug 4 = **7** (25 min) · Aug 5 = 8 (27 min) | 🟡 Block 1 reached 2 of 8 on Day 37 |
| Review backlog carried | **all dated** through **Aug 12** · re-spread Day 37 | 🟡 **drain extending, not shrinking** |
| **Open blockers** | **3 — B-10 (no progress), B-5, B-8** | 🔴 **B-10 drill now** |
| Review pass rate (Day 37) | **1 / 2 reached** | 🔴 **6 of 8 items never reached — the box ran out** |
| **🎯 Unaided timed mediums** | **1 of 3 taken** · Mock #2 **Sat Aug 8** | 🟢 first data point beat expectation |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | **3/5** | **B-10 open and static.** Priced a doubly-recursive function as linear (M-042) on top of the Mock #1 TLE |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| **Sliding Window** | **3/5** | **#567's `O(n)` version written Day 37 — 2,600× faster than the mock's.** When a window slides, only TWO characters change: update, don't rebuild |
| Binary Search | 3/5 | #74 clean Day 35 — the two-template distinction held |
| Stack | 3/5 | #155 → 21d |
| Linked List | 4/5 | #143 clean, LRU rebuilt cold |
| Trees & BFS/DFS | 3/5 | #110 box clean |
| Binary Search Tree | 4/5 | stable |
| Tries | 3/5 | #211 clean Day 30 |
| Heap | 3/5 | #973/#215 clean |
| Backtracking | 3/5 | #46 and #90 clean Day 36 |
| Intervals | 3/5 | Four problems clean. 4/5 needs a novel one cold (#253) |
| **Graphs (BFS/DFS)** | **3/5** ↓ | Six problems, all passing Day 36 — but **#200's one-draft failed Day 37** on `==` for `=` |
| **1-D DP** | **2/5** *(new)* | **Day 37 — #70, #746, #198. Every recurrence derived unaided, but a ~4-hour scaffolded first contact. The 1d/3d reps decide the number** |
| **Greedy** *(previewed)* | **1/5** | Named block Aug 9–11 |

## Blockers

- **⛔ B-10 · M-006 — price the loop body. NO PROGRESS Day 37.** Three prompts for both halves of a complexity; volunteered zero times across four problems. Plus **M-042**: priced the naive `#70` recursion as `O(n)` when it's `O(2ⁿ)`. **Drill: *"one pass costs ___, there are ___ passes"* — before every complexity statement.**
- **🟡 B-5 · M-036 — container vs contents.** 1 clean session; `#133` not due Day 37.
- **⛔ B-8 · M-029 — naming precision.** Not exercised Day 37.
- **✅ B-9 · M-001 — the recursive return channel. CLEARED Day 36.** Standing habit; re-escalate on recurrence.
- **M-041 (patch before diagnosis) · M-042 · M-040 · M-039 · M-034 · M-037 · M-038 · B-2 · B-4 · M-027 · M-005** — 👁 watch.

*(Cleared → standing habits: B-1 names, B-3 return, B-4 guards, B-6 target-first, B-7 `self.`/ownership, **B-9 recursive return**, M-025 pointer surgery.)*

## Next Session Focus  → **Day 38 (Tue Aug 4)** · 1-D DP continues ⇒ **Block 2 first**

1. **Block 2 — new:** **#5 Longest Palindromic Substring and #91 Decode Ways** — `#5` is the one where the expected answer is expand-around-centre rather than a `dp` table, and `#91` is the first recurrence with a **condition** attached: a 1-digit branch and a 2-digit branch, each valid only sometimes.
2. **Block 1 — 7 items, ~25 min:** full **#70 · #746 · #198** (1d) · **#200** (reset) → 🗣 **#739 · #121 · #153**.
3. **⛔ B-10 — say BOTH halves unprompted.** *"One pass costs ___, there are ___ passes."* Three prompts on Day 37, volunteered zero times — and it's exactly how the Mock #1 TLE happened.
4. **⛔ On `#200`:** `=` not `==`, and `0 <= nr < len(grid)`. Both were correct on `#994` an hour before they were wrong here.
5. **⛔ Diagnose before patching (M-041).** The arithmetic *is* the fix.
6. **Run everything before sending.**
7. **The slipped session still needs a date**, and **Mock #2 is Sat Aug 8.**

---
*Weekly snapshots can be appended below as the sprint progresses.*
