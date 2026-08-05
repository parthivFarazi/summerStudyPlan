# Spaced-Repetition QUEUE — single source of truth for review state

> **Ladder:** `1d → 3d → 7d → 21d → 60d` → graduated. **Pass** = advance one rung. **Fail** (needed a hint, blanked, or a bug you couldn't self-fix) = **reset to 1d** + log the cause in `MISTAKES.md`. Re-solves are **from a blank screen**, never re-reading the solution.

## How to use each session
1. Pull rows with **Next due ≤ today**; order **resets → 1d → 3d → verbal**. Budget **~6–8 items** under a **hard 30-minute box**.
2. **The rung sets the tier** *(2026-07-25 — full rationale in `SYSTEM.md`)*:

| Rung | Tier | Cost | What you do |
|---|---|---|---|
| **1d · reset** | **Full solve** | ~6 min | Blank screen. Write it, run it, debug it. |
| **3d** | **✍️ One-draft** | ~4 min · **6 if recursive** | Write it **once**. **Cap = 4 min, or 6 when the solution needs a nested recursive helper** *(Day 34 — the cap exists to stop slow deliberation, not to time your keyboard)*. **Don't run it. Don't debug it.** The cap is on WRITING; the self-audit that follows is untimed and is part of the tier. **Pass = correct when handed over, having never been executed.** |
| **7d · 21d · 60d** | **🗣 Verbal** | ~30 sec | Say pattern + approach + time/space out loud. Blank ⇒ full solve ⇒ reset. |

3. **The 30-min box is hard.** Anything unreached gets a **concrete date written into the table** before the session ends — never an undated roll.
4. Update the row: new rung + new **fuzzed** due date (jitter toward the lightest day; keep any day ≤ ~8) + append result to `Results` (`P`/`F`). One write, here only.
5. **⛔ A full solve you hand over WITHOUT EXECUTING is a FAIL.** *(installed Day 33, 2026-07-28.)* Full-solve means **write it, run it, debug it** — no partial credit for "the algorithm was right." #133 was algorithmically correct at submission two and still took three submissions, on a mistyped attribute. Running it costs 20 seconds; not running it costs the interview.
6. **Weight-balance and batch when scheduling:** heavy Block 2 (Graphs, DP) ⇒ light reviews **and Block 2 runs first**; group same-pattern reviews together, except on interleave days.


> ## ✅ THE PACE DECISION — made 2026-08-05, his call, Day 39 opener
> **2 new/day through Day 46, then re-decide.** Presented with the arithmetic:
>
> | | remaining | lands |
> |---|---|---|
> | **core** | **14** — `#322 #152 #139 #300 #62 #1143 #72 #53 #55 #134 #763 #136 #191 #338` | **Day 46 ≈ Aug 12** |
> | depth | 13 — `#213 #647 #416 #309 #518 #494 #695 #417 #261 #131 #17 #110 #90` | Days 47–53 |
>
> **`GOALS.md` targets "all 66 core + a head start on depth" by Aug 20 — depth is fall material.** At 2/day the load-bearing curriculum finishes **with 7 sessions to spare**, and the only thing at risk is material that was never meant to land this summer.
>
> **Dropping to 1/day now would have cost CORE:** 14 core + 2 zero-new mock days = **16 sessions into 15 available**, pushing core past Aug 19. The intuitive "slow down" option was the one that hurt.
>
> **Coach's caveat, stated before he chose:** Day 38's 2h43m was mostly `#91`, and ~1 hour of `#91` was the coach running the Socratic method on a base case — **the exact failure `COACHING.md` rule 20 now forbids.** Day 38's Block 1 took **22 minutes for 7 items** once it ran on its own. **He should not be making schedule decisions off a data point the coach caused.**
>
> **⛔ Re-decide at Day 47 (≈ Aug 13), on a week of post-rule-20 session lengths. Put it to him again then; do not let it lapse.**

## Overflow rule
A wall of 12-due is a **scheduling** problem, not a work problem. If **due count > 8** after prioritizing: full-solve the fragile ones, verbal the stable ones, and **re-date the leftover** so no day exceeds ~8. Interleave days also drain the queue. Decay is the enemy, not volume.

> **⛔ A roll-forward must land on a real date.** *(added 2026-07-25 — `COACHING.md` rule 10.)* Rolling an item "to Jul 28" and then rolling it again is deferral, not scheduling. **Every roll writes a concrete `Next due` into the row below**, and the day it lands on must still be ≤ 8.

> **Steady-state note:** at 2-new/day this ladder settles at **~7 reviews/session** — ~3.5 full, ~1.4 one-draft, ~2.2 verbal, **~28 min**. That number is set by the ladder, not chosen; see `SYSTEM.md` → *What the review load actually is*. **Stretching the rung intervals does not reduce it** — it only delays it.

---

## 🔴 Backlog drain · Jul 26 → Aug 5 *(built 2026-07-25 · re-tiered + weight-balanced same day)*

**The honest count.** After Day 30, **43 items were due or overdue on/before Jul 28** — 18 already past due (dated Jul 24–25, unworked because Day 30's interleave sampled only 6). The Day-30 note rolled them all onto "Jul 28," which would have made Jul 28 a **29-item day** against a cap of 8. That is not a schedule; that is a pile.

**Six levers applied.** The first four spread the load; the last two make each item cheaper and each day gentler:

1. **Three review tiers, set by rung** *(`SYSTEM.md`)* — **1d/reset = full solve · 3d = ✍️ one-draft (4-min cap, no debugging) · 7d+ = 🗣 verbal.** Only ~2 items per session now involve write-run-debug.
2. **Drain stretched to Aug 5** — 10 sessions, not 7.
3. **Backtracking cluster split** — Day 31 takes only the three that actually failed; #79/#39 → Jul 27.
4. **Overdue sweep moved off Day 31.**
5. **Weight-balanced against Block 2** — the Graph days (Jul 28–30) and DP days (Aug 1–5) get **light** reviews (arrays, two-pointers, stack, binary search, heap); the light Intervals day and the interleave day absorb the **heavy** ones (backtracking, linked-list surgery, LRU).
6. **Batched by pattern** so context stays loaded — trees together, heap together, linked-list together. *(Jul 31 is deliberately unbatched: it's the interleave day and mixing is the point.)*

**Result: no day exceeds 8 items or ~29 minutes, and the average is 6.4 items in ~24 min.**

| Session | Date | Block 2 weight | Full solve | ✍️ One-draft (4 min) | 🗣 Verbal | Time |
|---|---|---|---|---|---|---|
| ~~Day 31~~ | ~~Sun Jul 26~~ | ✅ **DONE** — #57/#56 | ~~#90·#46·#78~~ ✅ 3/3 | — | — | — |
| ~~Day 32~~ | ~~Mon Jul 27~~ | ✅ **DONE** — #435/#252 | ~~#79·#39·#57·#56~~ 1/4 | *(#146 moved)* | ~~#704·#33~~ ✅ | 37 min ⚠️ |
| ~~Day 33~~ | ~~Tue Jul 28~~ | ✅ **DONE** — #200/#133 | ~~#79·#39·#57·#435·#252~~ ✅ **5/5** | — | — | **26:55** ✅ |
| ~~Day 34~~ | ~~Thu Jul 30~~ | ✅ **DONE** — #994/#207 | ~~#200~~ ✅ · ~~#133~~ ❌ | ~~#90~~ ✅ · ~~#46~~ ❌ · *(#78 → Jul 31)* | ~~#155~~ ✅ · ~~#74~~ ❌ | **3/6** |
| ~~Day 35~~ | ~~Fri Jul 31~~ | ✅ **DONE** — #210/#323 | ~~#74~~ ✅ · ~~#207~~ ✅ · ~~#133~~ ❌ · ~~#46~~ ❌ · ~~#994~~ ❌ | — | — | **2/5 · 26:12** |
| ~~Day 36~~ | ~~Sat Aug 1~~ | ✅ 🎯 **MOCK #1 — 19:38, correct, 15 min under cap** | ~~#133·#46·#994·#210·#323~~ ✅ **5/5** | — | — | **52:53** |
| — | **Sun Aug 2** | 🟢 **REST** | — | — | — | — |
| ~~Day 37~~ | ~~Mon Aug 3~~ | ✅ **DONE** — 1-D DP acquired: #70/#746/#198 | ~~#567~~ ✅ **TLE fixed 5.67s → 0.0022s** | ~~#200~~ ❌ · *(#79/#39/#57 → Aug 5–6)* | *(→ Aug 4)* | **2 of 8 reached** |
| ~~Day 38~~ | ~~Tue Aug 4~~ | ✅ **DONE** — #5 ✅ 61:25 · #91 ✅ 1:42:00 (~2h43m) | ⛔ **0 of 7 reached — Block 2 consumed the whole session** | — | — | **BLOCK 1 NOT RUN** |
| ~~Day 38 *tail*~~ | ~~Wed Aug 5~~ | ✅ **DONE — 7 of 7 in ~22 min.** Day 38 CLOSED | ~~#200 ✅ 7:59 · #70 ✅ 2:03 · #746 ✅ 3:39 · #198 ✅ 3:53~~ | — | ~~#739 ✅ · #121 ✅ · #153 ✅~~ | **7/7 · 22 min** ✅ |
| **Day 39** | **Wed Aug 5 · later** | **DP · HEAVY** ⇒ B2 first | **#5 · #91** (1d) | *(#79 · #39 → Aug 7)* | #347 · #238 · #150 · **#21 · #104 · #206** | **15 min** |
| Day 40 | Thu Aug 6 | **DP · HEAVY** ⇒ B2 first | #322 · #152 | **#567 · #57 · #56 · #994 · #74** | #3 · #167 · #90 · #98 | ⚠️ **34 min** |
| Day 41 | Fri Aug 7 | **DP · HEAVY** ⇒ B2 first | #139 · #300 | #875 · #424 · **#133 · #215 · #79 · #39 · #207** | #235 · #271 · #226 · #128 | ⚠️ **48 min — OVER THE BOX** |
| Day 42 | Sat Aug 8 | 🎯 **MOCK #2** — unaided 35-min medium *(replaces Block 2)* | #62 · #1143 | #1046 · #199 · **#210** | #11 · #125 | 27 min |
| Day 43 | Sun Aug 9 | *(Sunday worked)* Greedy | — | #242 · #252 · #15 · #20 · **#78 · #46** | — | 28 min |
| Day 44 | Mon Aug 10 | Greedy / Bit Manip | *(2 new at 1d)* | **#435 · #141 · #230 · #146** | — | 28 min |
| Day 45 | Tue Aug 11 | Bit Manip | *(2 new at 1d)* | **#208 · #703 · #543 · #973** | — | 28 min |
| Day 46 | Wed Aug 12 | Bit / DP depth | *(2 new at 1d)* | **#323 · #143 · #19 · #110 · #211** | — | 30 min |

> ## 🔴 A SESSION SLIPPED — the buffer is gone *(logged 2026-07-30)*
> **Day 33 ran Thu Jul 28. Jul 29 had no session. Day 34 ran Fri Jul 30.** Every date below has been shifted one day.
>
> **The arithmetic, re-run:** Days 35–53 is **19 sessions**. Jul 31 → Aug 19 is 20 calendar days minus the Aug 2 rest = **19 available.** **19 into 19 — the one-day Aug 19 buffer is spent. There is now zero slack against Aug 20.**
>
> **Two ways back to a buffer, and it is his call:**
> 1. **One triple-new day** (3 new problems in one session) — the standing recovery rule.
> 2. **Work Sunday Aug 2** — the last rest day in the sprint.
>
> **Until one of those happens, a single further slip puts Day 53 past the deadline.**

> **His call, 2026-07-30:** *"I will be able to catch up with the new schedule — I'm just a day behind right now, I'll catch up and still have the Aug 19 buffer."* **Accepted.** The recovery is one extra session's worth of new material somewhere in the next two weeks — a triple-new day or a worked Aug 2. **Track it as OWED until a specific day carries it, then mark that day here.** Not a crisis; just a debt that needs a date on it, same as any roll-forward *(rule 10)*.

**🔴 Day-37 — the review load is now the binding constraint. Read this before the next re-fuzz.**
Day 37's Block 2 carried **three** new problems, which arrive as **three full solves** the next day (18 min) on top of a reset. Block 1 reached **2 of 8 items** inside the 27-minute box. That is not a scheduling error — **it is arithmetic: at 3 new/day the ladder generates more review minutes than a 30-minute box can absorb.**

**🟢🟢 Day-38 tail (Wed Aug 5 morning) — 7 of 7, ~22 minutes, inside the box. Day 38 is CLOSED.**
**Four full solves, all passing, all verified against INDEPENDENT oracles** (union-find for `#200`, path enumerator for `#746`, subset enumerator for `#198`): 5,706 grids · 500 values of n · 27,840 cost arrays · 14,840 rob arrays, **zero failures across all of it.**
**Both Day-37 `#200` bugs gone** (`=` not `==`; `0 <= nr < len(grid)`), and **`#198` guarded `[5]` unprompted** — the exact case that threw `IndexError` yesterday after being named out loud beforehand.
**He self-caught two bugs on `#746` by running the code**; the range off-by-one was wrong on **1,415 of 2,000** random arrays. **Rule 14, in one number.**
**⛔ B-10: eight complexities volunteered unasked, zero prompts, across seven items.** Day 37 was zero. **Two precision gaps remain:** `#739`'s bound is **amortized** (a loop containing a `while` is not `O(1)` per pass — count total pushes/pops), and `#121`'s `minVal = max(nums)` is a wasted extra `O(n)` scan.
**This does NOT resolve the capacity problem below** — Block 1 was only reachable because it ran as its own sitting with no Block 2 in front of it. **The decision still stands.**

**🔴🔴 Day-38 — Block 2 day: Block 1 was NOT REACHED AT ALL. Second consecutive under-delivery, and the queue no longer fits.**

Day 38's Block 2 ran **~2 h 43 m** for two new problems (`#5` 61:25, `#91` 1:42:00). **Block 1 reached 0 of 7.** Day 37 reached 2 of 8. **Two sessions running, and the trend is the wrong direction.**

**Re-dated honestly, not rolled:** all 7 Day-38 items → **Wed Aug 5, on waking**, as a separate 25-min sitting that closes Day 38; Day 39 then runs later the same day at **15 min** (its one-drafts `#79`/`#39` displaced to Aug 7). The two genuinely-overdue rows from Aug 3 — `#207`, `#74` — finally have real dates (Aug 7, Aug 6). Four rows whose `Next due` disagreed with this table (`#875`, `#424`, `#347`, `#238`) are now consistent with it.

> **⛔ BUT THE ARITHMETIC NO LONGER CLOSES. Aug 7 is now 48 minutes against a 30-minute box.** Every day Aug 5 – Aug 12 was already at 25–30 min with no absorbency; there is nowhere left to push. **Re-dating has run out of room — this is the third re-spread in eight days and each one has been larger than the last.**
>
> **Only three levers exist** (`SYSTEM.md`): fewer new problems/day · fewer rungs · cheaper reviews. **The tiers are already pulled and the 60d rung is already outside the sprint window. The only remaining lever is the new-problem rate**, which `COACHING.md` rule 11 fixes at 2/day and rule 17 confirms as his explicit decision.
>
> **This is his call and it must be made on Day 39, not deferred again.** Present the arithmetic: **15 sessions, 15 available days, zero buffer, a slipped session still owed a date, and a review backlog that no longer fits inside its own box.**

**Handled for now** by spreading the six unreached items onto real dates (#739/#121/#153 → **Aug 4**, #79/#39 → **Aug 5**, #57 → **Aug 6**) and **extending the drain to Aug 12**. Every day Aug 4 – Aug 12 sits at **25–30 min**.

**But the trend is one-directional and worth naming:** passes advance and stack, failures stay put, and new problems keep arriving. **If Block 1 under-delivers again this week, the choice is a longer box or fewer new problems — and that is HIS call, not mine.** Raise it after Day 39.

**Day-36 re-fuzz — the drain now ends Aug 11, and the reason is a good problem to have.** Day 36 went **5/5**, so five items advanced to 3d **at once**, landing in a week already at 27–30 min every day — plus `#567` from the mock. Rather than cram, the five were spread one per day across **Aug 4 → Aug 8** (`#994` → Aug 4, `#133` → Aug 5, `#46` → Aug 6, `#210` → Aug 7, `#323` → Aug 8), and the displaced one-drafts land on **two new tail days, Aug 10 and Aug 11**. Every day Aug 3 – Aug 11 now sits at **22–28 minutes**. **Nothing dropped, nothing rolled without a date.** *(Worth noting: a 5/5 day costs more future load than a 2/5 day — passes advance and stack, failures stay put. That is the ladder working, not a problem.)*

**Day-35 re-fuzz — Aug 1 carries the mock AND five full solves, and that is deliberate.** Day 35 produced **three resets** (#133, #46, #994) on top of **two new 1d items** (#210, #323) — exactly five full solves, exactly the 30-minute box. **Aug 1 is an interleave day with no new-material teaching**, so the session is Mock (35 min) + Block 1 (30 min) ≈ **65 minutes — shorter than the last three days** despite looking heavier on paper. Everything else moved off Aug 1 onto real dates: #78 → Aug 3, #150 → Aug 5, #98 → Aug 6. Downstream shuffle to hold every day at 27–30 min: #435 → Aug 4, #230 → Aug 5, #146 → Aug 6, #703 → Aug 7, #128 → Aug 7, #973 → Aug 9. **Nothing dropped, nothing rolled without a date.**

**Day-34 re-fuzz — the drain now ends Aug 9, not Aug 7, and here is the honest arithmetic.** Day 34 added **three resets** (#133, #46, #74) on top of **two new 1d items** (#994, #207), and the new 6-minute recursive one-draft cap raises total load ~15%. Five full solves is exactly 30 minutes, so **Day 35 is those five and nothing else** — every one-draft and verbal that sat on Jul 30 moved out. **Jul 31 is deliberately light (19 min)** because Mock #1 takes 35 minutes and replaces Block 2 that day. **Nothing was dropped and nothing rolled without a date**: #56/#102/#100 → Aug 3–5 batching, #79/#39/#57/#435 → Aug 1, #703 → Aug 5, #973 → Aug 6, #242/#252/#15/#20 → **Aug 8 (the new tail)**. Every day Jul 31 – Aug 9 sits at **16–30 minutes**. *(Superseded Day-33 note below.)*

**Day-33 re-fuzz — the five passes land on Jul 31 / Aug 1, and Jul 31's old load moved out.** All five Day-33 items advanced to **3d**, so they were placed on their true 3d date (Jul 31), with **#252** fuzzed one day to Aug 1 to keep Jul 31 at 28 min. **The fragile items kept the date; the stable ones absorbed the shuffle** — #543 → Aug 6, #146 → Aug 4, #242 → Aug 7, #153 → Aug 1, #206 → Aug 3, #128 → Aug 5, batched onto days already holding their pattern (LL with LL, trees with trees).

**Arithmetic, done rather than assumed** *(rule 10)*: every day Jul 29 – Aug 7 now sits at **6–8 items and 25–29 minutes**. None exceeds the cap. Drain still ends **Aug 7**.

*(Cost of a full solve ≈ 6 min · one-draft ≈ 4 min · verbal ≈ 30 sec. That's how each day's total is computed — the box is on TIME, not item count.)*

*(Full-solve items are almost always the previous day's new problems arriving at 1d — those can never be cheapened.)*

**Hard 30-minute box on Block 1.** Order: resets → 1d → 3d → verbal. Whatever isn't reached gets a **concrete date written into the table below** before the session closes. Never an undated roll.

---

## Due / Active

**Tier is set by rung:** blank = **full solve** (1d/reset) · **✍️ = one-draft**, 4-min cap, no running or debugging (3d) · **🗣 = 30-second verbal** (7d+).

| Problem | Pattern | Rung | Tier | Next due | Streak | Results |
|---|---|---|---|---|---|---|
| Subsets II (#90) | backtracking | **7d** | 🗣 | **2026-08-06** | 2 | (new)·F·P·**P** |
| Permutations (#46) | backtracking | **3d** | ✍️ *(6 min)* | **2026-08-09** | 1 | (new)·F·P·F·F·**P** |
| Subsets (#78) | backtracking | **3d** | ✍️ *(6 min)* | **2026-08-09** | 1 | (new)·F·**P** |
| Word Search (#79) | backtracking (grid DFS) | **3d** | ✍️ *(6 min)* | **2026-08-05** | 1 | (new)·F·**P** |
| Combination Sum (#39) | backtracking | **3d** | ✍️ *(6 min)* | **2026-08-05** | 1 | (new)·F·**P** |
| Insert Interval (#57) | intervals | **3d** | ✍️ | **2026-08-06** | 1 | (new)·F·**P** |
| Merge Intervals (#56) | intervals | **3d** | ✍️ | **2026-08-06** | 1 | (new)·**P** |
| Non-overlapping Intervals (#435) | intervals / greedy | **3d** | ✍️ | **2026-08-10** | 1 | (new)·**P** |
| Meeting Rooms (#252) | intervals / greedy | **3d** | ✍️ | **2026-08-09** | 1 | (new)·**P** |
| Number of Islands (#200) | graphs (implicit/grid DFS) | **3d** | ✍️ *(6 min)* | **2026-08-08** | 1 | (new)·P·F·**P** — 7:59, both Day-37 bugs fixed, 5,706 grids clean |
| Climbing Stairs (#70) | **1-D DP** | **3d** | ✍️ | **2026-08-10** | 1 | (new)·**P** — 2:03, O(1)-space version, n=1..500 clean |
| Min Cost Climbing Stairs (#746) | **1-D DP** | **3d** | ✍️ | **2026-08-10** | 1 | (new)·**P** — 3:39, self-caught 2 bugs by running (one was wrong on 71% of random inputs) |
| House Robber (#198) | **1-D DP** | **3d** | ✍️ | **2026-08-11** | 1 | (new)·**P** — 3:53, **guarded `[5]` unprompted** (yesterday's IndexError) |
| **Longest Palindromic Substring (#5)** | **expand-around-centre** *(two-pointer, NOT dp)* | **1d** | full | **2026-08-05** | 0 | (new) |
| Decode Ways (#91) | **1-D DP** *(conditional recurrence)* | **3d** | ✍️ | **2026-08-09** | 1 | (new)·**P** — 1d rep met on Aug 5 by writing **tabulation AND the O(1)-space rolling version cold**, both verified on 1.1M strings. Debt cleared |
| Clone Graph (#133) | graphs (explicit) | **3d** | ✍️ *(6 min)* | **2026-08-07** | 1 | (new)·F·F·F·**P** |
| Rotting Oranges (#994) | graphs (multi-source BFS) | **3d** | ✍️ | **2026-08-06** | 1 | (new)·F·**P** |
| Course Schedule II (#210) | graphs (topological sort) | **3d** | ✍️ *(6 min)* | **2026-08-08** | 1 | (new)·**P** |
| Connected Components (#323) | graphs (undirected) | **3d** | ✍️ *(6 min)* | **2026-08-12** | 1 | (new)·**P** |
| Permutation in String (#567) | sliding window (fixed size) | **3d** | ✍️ | **2026-08-06** | 1 | (new)·**P** — 🎯 Mock #1's TLE fixed: 5.67 s → 0.0022 s |
| Course Schedule (#207) | graphs (cycle detect, directed) | **3d** | ✍️ *(6 min)* | **2026-08-07** | 1 | (new)·**P** |
| LRU Cache (#146) | design / linked-list | 3d | ✍️ | **2026-08-10** | 1 | (new)·F·P·F·**P** |
| Binary Search (#704) | binary-search | **21d** | 🗣 | **2026-08-17** | 3 | P·P·**P** |
| Search in Rotated Array (#33) | binary-search | **21d** | 🗣 | **2026-08-17** | 3 | P·P·**P** |
| Valid Anagram (#242) | arrays-hashing | 3d | ✍️ | **2026-08-09** | 1 | P·P·P·F·F·P |
| 3Sum (#15) | two-pointers | 3d | ✍️ | **2026-08-09** | 1 | F·P·F·P |
| Valid Parentheses (#20) | stack | 3d | ✍️ | **2026-08-09** | 1 | P·F·P |
| Min Stack (#155) | stack | **21d** | 🗣 | **2026-08-19** | 3 | P·P·**P** |
| Search a 2D Matrix (#74) | binary-search | **3d** | ✍️ | **2026-08-06** | 1 | P·P·F·**P** |
| Evaluate RPN (#150) | stack | 7d | 🗣 | **2026-08-05** | 2 | P·P |
| Level Order Traversal (#102) | trees | 3d | ✍️ | **2026-08-05** | 1 | (new)·F·F·P |
| Same Tree (#100) | trees | 3d | ✍️ | **2026-08-06** | 1 | P |
| Diameter of Binary Tree (#543) | trees | 3d | ✍️ | **2026-08-11** | 1 | P |
| Lowest Common Ancestor BST (#235) | binary-search-tree | 7d | 🗣 | **2026-08-05** | 2 | (new)·F·P·**P** |
| Encode/Decode Strings (#271) | arrays-hashing | 7d | 🗣 | **2026-08-05** | 2 | P·F·F·P·**P** |
| Invert Binary Tree (#226) | trees | 7d | 🗣 | **2026-08-05** | 2 | P·F·P·**P** |
| Kth Largest in Stream (#703) | heap | 3d | ✍️ | **2026-08-11** | 1 | (new)·P |
| K Closest Points (#973) | heap | 3d | ✍️ | **2026-08-11** | 1 | (new)·**P** |
| Kth Largest in Array (#215) | heap | 3d | ✍️ | **2026-08-07** | 1 | (new)·**P** |
| Validate BST (#98) | binary-search-tree | 7d | 🗣 | **2026-08-06** | 2 | (new)·P·**P** |
| Find Min in Rotated Sorted Array (#153) | binary-search | **21d** | 🗣 | **2026-08-26** | 3 | F·P·F·P·P·**P** — convergence template clean (M-015 held) |
| Longest Consecutive Sequence (#128) | arrays-hashing | 7d | 🗣 | **2026-08-07** | 2 | P·P |
| Reorder List (#143) | linked-list | 3d | ✍️ | **2026-08-12** | 1 | (new)·F·P·F·**P** |
| Remove Nth Node From End (#19) | linked-list | 3d | ✍️ | **2026-08-12** | 1 | (new)·P |
| Linked List Cycle (#141) | linked-list | 3d | ✍️ | **2026-08-10** | 1 | P |
| Kth Smallest in BST (#230) | binary-search-tree | 3d | ✍️ | **2026-08-10** | 1 | (new)·P |
| Daily Temperatures (#739) | stack | **21d** | 🗣 | **2026-08-26** | 3 | P·F·P·P·**P** — ⚠️ said "O(1) per iteration"; it is AMORTIZED (each index pushed/popped once) |
| Best Time to Buy/Sell (#121) | sliding-window | **60d** | 🗣 | **2026-10-04** | 4 | P·P·P·**P** — ⚠️ `minVal = max(nums)` is a wasted extra O(n) scan |
| Balanced Binary Tree (#110) | trees | 3d | ✍️ | **2026-08-12** | 1 | (new)·F·**P** |
| Add & Search Words (#211) | tries | 3d | ✍️ | **2026-08-12** | 1 | (new)·F·F·**P** |
| Implement Trie (#208) | tries | 3d | ✍️ | **2026-08-11** | 1 | (new)·F·P |
| Reverse Linked List (#206) | linked-list | 7d | 🗣 | **2026-08-05** | 2 | P·P |
| Merge Two Sorted Lists (#21) | linked-list | 7d | 🗣 | **2026-08-05** | 2 | P·P |
| Maximum Depth of Binary Tree (#104) | trees | 7d | 🗣 | **2026-08-05** | 2 | P·P |
| Koko Eating Bananas (#875) | binary-search | 3d | ✍️ | **2026-08-07** | 1 | P·F·P·F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | ✍️ | **2026-08-07** | 1 | P |
| Top K Frequent (#347) | arrays-hashing | 21d | 🗣 | **2026-08-05** | 3 | P·P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d | 🗣 | **2026-08-05** | 3 | P·P·P |
| Last Stone Weight (#1046) | heap | 3d | ✍️ | **2026-08-05** | 1 | (new)·F·F·**P** |
| Right Side View (#199) | trees | 3d | ✍️ | **2026-08-05** | 1 | (new)·P·F·F·**P** |
| Longest Substring No Repeat (#3) | sliding-window | 21d | 🗣 | **2026-08-05** | 3 | P·P·P |
| Two Sum II (#167) | two-pointers | 21d | 🗣 | **2026-08-05** | 3 | P·P·P |
| Container With Most Water (#11) | two-pointers | 21d | 🗣 | **2026-08-06** | 3 | P·P·P |
| Valid Palindrome (#125) | two-pointers | 21d | 🗣 | **2026-08-06** | 3 | F·F·F·F·P·P·P |
| Group Anagrams (#49) | arrays-hashing | 60d | 🗣 | 2026-09-09 | 4 | P·P·P·P |
| Two Sum (#1) | arrays-hashing | 60d | 🗣 | 2026-09-12 | 4 | P·P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 60d | 🗣 | 2026-09-12 | 4 | P·P·P·P |

*(A bolded `Next due` was re-dated by the 2026-07-25 drain. New problems join at 1d — always full solve — as they're learned.)*

---

## Session history

**Day 27 (Jul 21):** #102/#208/#703→3d, #235→7d (**B-6 CLEARED**); #211/#1046/#110 reset; #973/#215 new.
**Day 28 (Jul 22):** #271/#226/#98→7d; #143/#199/#146 reset; #78/#39 new.
**Day 29 (Jul 23):** **5/8** — #110/#973/#215/#143/#146 **PASS→3d**; #211/#1046/#199 **reset** (fresh facets: #211 constructor/keys/return, #1046 return-negation *again*, #199 enqueue direction); new **#90/#46 backtracking→1d**. **Named checks HELD.** **B-7 held → 1 clean session.**
**Day 30 (Jul 25 — interleave day) — DONE.** 3/6 interleave: **#211/#1046/#199 PASS→3d** (every older named cause held — #1046 un-negate FINALLY, #211's 3 Day-29 facets, #199 enqueue direction); **#78/#90/#46 reset→1d** (all backtracking — the youngest pattern). **Plus #79 Word Search** ✅ (grid DFS, built cold, 2 M-027 nudges) — carried over from Day 29. ✅ **Throughput fine:** interleave days are built to carry 0–1 new, so 1 new + a full interleave block is *above* baseline. *(An earlier note in this file called it a sub-floor miss — that was wrong and is retracted.)*

**Day 37 (Mon Aug 3) — DONE. 1-D DP ACQUIRED (#70, #746, #198). Block 1: 2 of 8 reached.**
**~4-hour Block 2, correctly so — the four hours bought the PATTERN, not the problem.** [INSIGHT] **He derived the #70 recurrence himself** (split the n=4 sequences by last move), **named memoization before I did**, and **killed his own even/odd idea for #198** on `[2,1,1,2]`.
**Two load-bearing misconceptions cleared: (1) the recurrence is a FORMULA, not recursion** — you need it either way, and tabulation is the same formula in a loop; **(2) `a, b = b, a + b` is not a Fibonacci trick** — the collapse works with any recurrence reaching back a fixed number of steps. Built `viz/dp-memo-vs-tabulation.html` twice (the first lacked call ORDER).
🔴 **`[5]` crashed #198 after I named that exact test case**, and **#200's one-draft had `==` for `=`** (448/512 grids crash). **#567 ✅ — the mock's TLE is dead: 5.67 s → 0.0022 s.**
⚠️ **Box enforced with 6 items unreached, all dated.** 🔴 **At 3 new/day the review load is now the binding constraint** — see the note above the drain table.

**Day 36 (Sat Aug 1) — DONE. 🟢 Block 1 5/5 in 52:53 + 🎯 MOCK #1.**
**🎯 Mock #1 (#567 Permutation in String): 19:38 — fifteen minutes UNDER the 35-min cap, correct code, pattern named in the first sentence.** Self-scored 4.5/2.5/1.5/3 against my 4/2.5/2/3 — **calibrated: least confident exactly where he was wrong.** 🔴 But it would **TLE** (`O(n² log n)`, measured 5.67 s at the constraint ceiling) and **he identified the optimal approach and rejected it as "more complicated"** (M-040). `#567` enters at 1d to be rewritten properly.
**Block 1: #133 ✅ 6:49 · #46 ✅ 6:48 · #994 ✅ 17:40 · #210 ✅ 11:40 · #323 ✅ 9:56 — all → 3d.** Three resets, two first retrievals, all passed.
🔑 **Yesterday these same five went 2/5, with three correct algorithms that never executed. Today 5/5. The understanding didn't change — he ran the code before sending it.** #133's first draft contained the IDENTICAL Day-35 bug; he ran it, caught it, fixed it, told me.
🟢 **The scheduling call was his** — he spotted that pushing 2 items onto a 3-new DP Monday would stack, took a real break, and finished in a defined 12 minutes. **✅ B-9 CLEARED. ⛔ B-10 opened (price the loop body, M-006 ×3).**

**Day 35 (Fri Jul 31) — DONE. Block 1 2/5 in 26:12, 2 new (#210, #323).**
**#74 ✅ 4:26 → 3d** (the loop condition that reset it yesterday, held first-draft). **#207 ✅ 5:38 → 3d** (**`if not dfs(child): return False` first-draft — B-9's exact failure from yesterday, caught cold**).
**#133 ❌ reset ×3** (walked the CLONE's empty list — third session on the same *which-`neighbors`-list* ambiguity; **he self-reported a notes peek, second time unprompted**). **#46 ❌ reset ×2** (`backtrack()` defined and never called). **#994 ❌ reset** (`range(grid)` → TypeError — **B-2 reopened after 17 clean sessions**).
🔴 **All three failures were correct algorithms that never executed** — each dies on the FIRST example. **The gap between his solve rate and his pass rate is one execution.** And **the one problem where he applied the B-9 drill is the one that stopped failing.**
**Block 2 — NEW: #210 (17:21) + #323 (31:14) — 48 min against 116 yesterday.** Derived post-order-then-reverse himself; transferred #323 from #200 himself; **correctly did NOT bring `path` over.** **M-036 ×3 ⇒ B-5 REOPENED.**

**Day 34 (Thu Jul 30) — DONE. Block 1 3/6, 2 new (#994, #207).**
**#200 ✅ 7:17 → 3d · #90 ✅ 6:15 first draft → 7d · #155 ✅ → 21d.** **#133 ❌ · #46 ❌ · #74 ❌.** All four failures were one disease — **the exact identity of the value in front of him** (two discarded recursive returns, a list compared to an int, the wrong template's exit condition). **B-9 opened; B-8 rescoped.**

**Day 33 (Tue Jul 28) — DONE. 🟢 Block 1 5/5 in 26:55, 2 new (#200, #133).**
**#79 ✅ 6:22 · #39 ✅ 7:24 · #57 ✅ 6:06 · #435 ✅ 4:50 · #252 ✅ 2:13 — all → 3d.** Five FULL solves inside the 30-min box with three minutes spare — the first time the box has held on an all-full-solve day. Each solve verified by executing his exact code against 6–10 cases.
**Every Day-32 named cause held first-draft:** #79's mark/un-mark idiom cold (peeked yesterday), #39's prune the right way round (M-033), #57's post-loop terminal append present (M-026), #435 comparing against the interval it KEPT. **Yesterday: 3 of 4 full solves failed. Today: 5 of 5 passed, and each was a fix to the exact thing that broke.**
**Block 2 — NEW PATTERN: Graphs.** #200 Number of Islands ✅ 44:14 (derived it as "#79's DFS with a permanent mark" unprompted; reasoned out himself why `4^L` doesn't apply — *you can only work with a node once*). #133 Clone Graph ✅ 45:28 (two bugs: the clone built from the ORIGINAL's neighbour list → **M-036**; and `node.neighbor` missing the `s` → the third submission on an already-correct solution). `O(V + E)` had to be animated — `viz/graph-edges-and-traversal.html` — and he then produced *"if there are E edges, it will always be 2E entries"* himself.
**⛔ Two honest problems: 90 minutes for two new problems** (readiness is measured in minutes on unseen material), and **M-029 escalated to B-8** — six sessions of slightly-wrong names, and on Day 33 it broke working code rather than just the narration.

**Day 32 (Mon Jul 27) — DONE. 3/6 reviews, 2 new (#435, #252).**
**#56 ✅ 7:20** (down from 26:24 — both Day-31 corrections applied unprompted: `answer[-1] = [...]` single-site, and `[a, ...]` because the sort guarantees the left edge never moves). **#704 ✅ · #33 ✅ → both 21d.**
**#79 ❌ 10:06** — peeked at notes for the mark/un-mark idiom, **and volunteered it**; both Day-30 nudges (all 4 directions, `dfs(r,c,0)`) held. **#39 ❌ 9:33** — prune written backwards (`target > total` instead of `total > target`), killing the recursion at the root. **#57 ❌ 9:57** — **the post-loop terminal append was missing (M-026)** on the exact problem whose comment said *"make sure to have the isInserted boolean."*
⚠️ **Block 1 box blown** (36:56 solve time) → #146 dated to Jul 31, not rolled.
**Block 2 — NEW: #435 (greedy interval scheduling) + #252.** Derived the greedy criterion (*remove the one that ends later*), reached "I only need to count, not remove" himself off the `pop` hazard, and **flipped to a forward sweep unprompted** after the reference bug. **[FEEDBACK] The reference bug was partly MY error** — I validated his backward sweep on two cases with a plausible-but-insufficient argument. Two passing tests is not a proof, for the coach either.
**The finding:** all four full solves were **first retrievals**. Three failed. **The one that passed (#56) was the one he struggled with hardest yesterday** — desirable difficulty, visible in his own data.

**Day 31 (Sun Jul 26 — Sunday worked) — DONE. 3/3 reviews, 2 new.**
**Block 1: #90 ✅ 4:30 · #46 ✅ 4:28 · #78 ✅ 2:57 — all three first-draft correct from a blank screen, all → 3d.** Three problems that failed Day 30, back in 12 minutes total. **The backtracking fragility watch is answered:** the pattern was young, not broken.
**Block 2 pre-teach ran long** — had to rebuild `sort(key=)`/`lambda` from "a function is a value" upward, plus iterable unpacking. Both landed; all checks correct.
**Block 3: NEW PATTERN — Intervals. #57 Insert Interval ✅ (one self-found bug), #56 Merge Intervals ✅ 26:24.** Derived `overlap = (b >= c) and (d >= a)` by counting the *failure* cases instead of the success cases. Learned the `answer[-1]`-is-the-growing-interval representation. **Space error worth banking: stated `O(1)` for #56 — a sort costs `O(n)` auxiliary, not just `O(n log n)` time.**
**New watches (both behavioural, both first observed today):** **M-029** vocabulary looseness (called a `while` loop an "if" three times — code right, language wrong) · **M-030** confirm-seeking instead of self-testing (4×). Same root: outsourcing verification.

**Day 38 order (Tue Aug 4) — 1-D DP continues ⇒ Block 2 first.**
Block 2: **#5 Longest Palindromic Substring** (expand-around-centre is the expected answer, not a `dp` table) and **#91 Decode Ways** (the first recurrence with a *condition* attached — a 1-digit and a 2-digit branch, each valid only sometimes).
Block 1, **~25 min, 7 items**: full **#70 · #746 · #198** (1d) · **#200** (reset) → 🗣 **#739 · #121 · #153**.
**⛔ B-10 — say BOTH halves unprompted.** *"One pass costs ___, there are ___ passes."* Three prompts needed on Day 37, volunteered zero times.
**⛔ On #200:** `=` not `==`, and `0 <= nr < len(grid)`. Both were correct on #994 an hour before they were wrong on #200.
**⛔ Diagnose before patching (M-041).** On Day 37 he proposed fixes for two #567 bugs before doing the three-line arithmetic that reveals them.
**⛔ Run everything before sending.**

> **⛔ B-10 — NO progress Day 37.** Three prompts to get both halves of a complexity; volunteered zero times. Not a formality: it is exactly how the Mock #1 TLE happened.
> **👁 M-041 NEW Day 37 — proposing a fix before completing the diagnosis.** Twice on #567. **The arithmetic IS the fix.**
> **🔴 M-035 fired TWICE Day 37 — both MINE.** Hand-written expected values in the #746 and #567 test lists, both wrong, both caught only because I also ran against reference implementations. **A hand-written expected value is a guess wearing a test's clothing.**
> **✅ B-9 (the recursive return channel) CLEARED Day 36** — two clean sessions; the return was caught correctly on all five solves.
> **⛔ B-10 OPENED Day 36 — price the loop body.** M-006 ×3 (Group Anagrams D3, Longest Substring D8, Mock #1). The mock solution TLEs at 5.67 s; hoisting one loop-invariant line halves it.
> **🟡 B-5 — 1 clean session Day 36** (#133 passed). Needs one more; he still wrote `graph[node].neighbors` rather than using the name `clone`.
> **⛔ B-5 (container vs contents) REOPENED Day 35 as a drill-now blocker.** M-036 ×3 — #133 has failed three sessions running on *which `neighbors` list*, and on Day 35 he had his notes open and still mis-picked. **The fix is mechanical: name the clone.**
> **👁 B-2 (`range(len(x))`) reopened Day 35** — `range(grid)` on #994, first slip since Day 18.
> **✅ B-9 HELD Day 35** on #207 (1 clean session — clears after 1 more).
> **⛔ B-9 (the recursive return channel) OPENED Day 34 — the priority blocker.** `dfs(child)` on #207 and `dfs(neighbor)` on #133, both discarded, **two hours apart**. Drill: *"the callee hands me back ___, and I catch it at ___"* before writing any recursive function.
> **⛔ B-8 (naming precision) — RESCOPED Day 34.** Three of Day 33's catches were the coach's fault (no signature supplied; he writes in IDLE from scratch). Scope is now names **visible in front of him** that still came out wrong, plus construct-naming in narration. Valid Day-34 instances: 1.
> **🔴 Day 34's four failures were ONE disease:** `dfs(child)` discarded · `dfs(neighbor)` discarded · `combo == len(nums)` (list vs int) · `while left < right` (wrong template's exit condition). **The exact identity of the value in front of you. Not one was a comprehension gap.**
> **✅ M-034 (scan said but not run) HELD Day 33** — 5/5, every named cause correct first-draft. The checklist works when it is walked against the code.
> **⚠️ Backtracking fragility — ANSWERED Day 33.** #79 and #39, the two that failed their first-ever review on Day 32, both came back clean (6:22 / 7:24). *Solid on rehearsed, fragile on first retrieval* still holds as the reading — the fix is the second retrieval, and it landed.
> **✅ B-7 (self./ownership) CLEARED Day 30** (2nd clean session); all of B-1…B-7 clear.
> **👁 M-027 — the through-line, but the one *repeat* is CLOSED.** #1046's un-negate finally landed Day 30 after two identical misses. Keep the final read-through.
> **⚠️ Backtracking fragility — REOPENED Day 32.** #79 and #39 both failed on their first-ever review (notes peek; reversed prune). Day 31's 3/3 was on problems with 3–4 prior passes. **The honest split: backtracking is solid on rehearsed problems, fragile on first retrieval.**
> **👁 M-026 (dropped terminal line) — FIRED Day 32** on #57, and it is item two on his own scan. **The scan didn't fail; it didn't run.**
> **✅ Backtracking fragility — ANSWERED Day 31 (superseded above).** All three (#78/#90/#46) came back first-draft correct in 12 min total, → 3d. The pattern was young, not broken. Keep watching #79/#39 on Jul 27.
> **👁 M-029 (vocabulary looseness) · M-030 (confirm-seeking instead of self-testing)** — new Day 31, both behavioural. Not blockers (first session observed), but high intra-session frequency. See `MISTAKES.md`.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
