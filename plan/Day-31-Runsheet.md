# Day 31 Run-Sheet · Sunday, Jul 26 2026 · **~90 minutes**

> **Built 2026-07-25, the day before.** Plan of record for Day 31, sized to a **90-minute** session so it actually gets finished.
>
> **Day 31 is a converted rest day.** Sunday was rest; it's now a working session, because the roadmap was 2 sessions short of fitting before Aug 20. Working it recovers one. *(`COACHING.md` rule 10; calendar in `plan/Day-by-Day-Roadmap.md`.)*
>
> **Working folder for today's code:** `~/Documents/job-search/LeetCode Practice/Week 6/Day 31/` *(W = ceil(31/6) = 6)*

---

## The shape of the day — 93 min

| # | Block | Time | What |
|---|---|---|---|
| 0 | Warm-up | 3 min | Say the scan out loud |
| 1 | **Backtracking — the 3 that failed** | **35 min** | **#90 → #46 → #78**, full re-solve, blank screen |
| 2 | Pre-teach | 10 min | `lambda` sort key · tuple unpacking — in isolation, one at a time |
| 3 | **New — Intervals** | **40 min** | **#57 Insert Interval → #56 Merge Intervals** |
| 4 | Ingest | 5 min | Report times + slips; the file writing is Claude's job |

**Review tiers now apply** *(new 2026-07-25, `SYSTEM.md`)* — **the rung sets the tier**: 1d/reset = full solve · 3d = ✍️ one-draft (4-min cap, no running, no debugging) · 7d+ = 🗣 verbal. **All three of today's items are resets, so all three are full solves** — there is no cheaper tier for a reset, and that's deliberate.

**Order today: reviews first.** Block 2 goes first only on heavy-topic days (Graphs, DP). Intervals is a new pattern but not a heavy one, and Block 1 is only 3 items.

**What moved off today, and where it went** *(nothing dropped — `review/QUEUE.md` has the dates)*:

- **#79 Word Search, #39 Combination Sum → Mon Jul 27.** Neither has ever failed; they're at 1d because they're *new*. A 1d→2d shift is a ladder decision, not a skip.
- **#102, #208, #703 → Jul 28–29**, inside the weekday drain.
- **The rest of the backlog → re-tiered and weight-balanced** across Jul 27 – Aug 5: 21 items at 3d become ✍️ one-drafts, 22 at 7d+ become 🗣 verbal, and the Graph/DP days get the *light* patterns. No day after today exceeds 8 items or ~29 min.

**If the clock runs out, Block 1 is what gets trimmed — never Block 3.** New material has no slack left in the calendar; reviews have a ten-day drain behind them. A trim gets written onto Day 32 before the session closes.

---

## Block 0 — Warm-up (3 min)

Say it out loud, all of it:

> Guard present? · Terminal line/mark written? · Every branch returns? · All args passed? · Whose thing is every attribute/method? · Multi-site change complete & every name real? · Un-negate on the way out? · Which side can contain the answer (target-first)?

---

## Block 1 — Backtracking: the three that failed (35 min) · ~12 min each

These three **failed on Day 30** and reset to 1d. The pattern is under a week old — the goal is to make the shape *set*.

**Rules:** blank screen · no re-reading the old solution · **stopwatch on each** · complexity (time **and** space) stated **before** any code.

| Order | Problem | Example |
|---|---|---|
| 1 | **Subsets II (#90)** | `nums = [1,2,2]` → `[[],[1],[1,2],[1,2,2],[2],[2,2]]` |
| 2 | **Permutations (#46)** | `nums = [1,2,3]` → `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]` |
| 3 | **Subsets (#78)** | `nums = [1,2,3]` → `[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]` |

**Watch for, but do not pre-empt** *(let him hit it and find it himself — `COACHING.md` rule 1)*: the un-choose step, the `path.copy()`, and whether the loop variable actually reaches the recursive call. That's where Day 30 broke.

**After each:** pass or fail, honestly. Needed a hint, blanked, or couldn't self-fix ⇒ **fail ⇒ reset to 1d ⇒ cause into `MISTAKES.md`.** No softening.

---

## Block 2 — Pre-teach (10 min) · **before #57, not during it**

Two new pieces of Python. Teach them **separately, with a toy example each** — not inside the problem. *(`COACHING.md` rule 2.)*

**1. `lambda` as a sort key (~5 min).** What `lambda x: x[0]` *is* as an object; what `key=` does to `sort()`. Sort a small list of pairs by first element, then by second, and watch the order change. Don't mention intervals yet.

**2. Unpacking in a `for` loop (~5 min).** `for a, b in pairs:` vs `for p in pairs:` then `p[0]`/`p[1]`. Same list, both ways, side by side.

If either is fuzzy, **stop and drill it** — cheaper here than mid-problem.

---

## Block 3 — New material: Intervals (40 min) · **2 new**

Brand-new pattern. **He states time and space before writing code**, then again after, and gets corrected on the second.

### #57 — Insert Interval (Medium)
Given a list of non-overlapping intervals sorted by start, insert a new interval and merge where necessary; return the resulting list.

> `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]` → `[[1,5],[6,9]]`

### #56 — Merge Intervals (Medium)
Given a list of intervals, merge all overlapping ones and return the non-overlapping intervals covering the input.

> `intervals = [[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]`

**Ask before he codes, in this order:** what does "overlap" mean as a comparison between two intervals? · does input order matter, and does that differ between the two? · what's the difference in the *input guarantee* between #57 and #56, and what does that cost?

Let him derive it. Questions and minimal hints only.

---

## Block 4 — Ingest (5 min of his time)

He reports: stopwatch times, pass/fail per item, every slip. Claude writes: notebook → **both** folders (`notebooks/Day31-Practice-Notebook.md` + `Week 6/Day 31/`), `logs/LOG.md`, `review/QUEUE.md` (**#57/#56 join at 1d, due Jul 27**), `review/MISTAKES.md`, `patterns/intervals.md`, `DASHBOARD.md`, then `python3 scripts/sync_readme.py` — then hands over the git command. **Claude never runs git.**

---

## Scoreboard

| Target | Met? |
|---|---|
| #90, #46, #78 re-solved from a blank screen | ☐ |
| **2 new problems** (#57, #56) | ☐ |
| Complexity stated **before** code, every problem | ☐ |
| Scan said out loud before every submit | ☐ |
| Ingest completed + committed | ☐ |

---

<details>
<summary><b>Coach reference — complexity check (don't read ahead)</b></summary>

- #90 `O(n · 2ⁿ)` · #46 `O(n · n!)` · #78 `O(n · 2ⁿ)` — space in each is the recursion depth plus the output
- #57 `O(n)` time, `O(n)` output space — input already sorted, so no sort needed
- #56 `O(n log n)` time (the sort dominates), `O(n)` space
- The #56-vs-#57 contrast is the teaching point: the sort is the entire difference, and he should get there by noticing #56 drops the sorted-input guarantee.

</details>
