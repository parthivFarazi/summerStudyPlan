# 📈 Summer Study Plan — LeetCode Interview Prep, in the Open

A beginner working from near-zero toward **FAANG-ready by interview season**, one tracked day at a time. This repo *is* my real prep — the plan, the daily notebooks, the mistakes, and the spaced-repetition system that ties it together. Not polished-for-show: the actual journey, decay and dumb bugs included.

<!-- README-LIVE:START -->
![Day](https://img.shields.io/badge/Day-33-2563eb)
![Phase](https://img.shields.io/badge/Phase-Summer_Sprint-7c3aed)
![Focus](https://img.shields.io/badge/Focus-Depth_phase_Graphs_learned_Intervals_held_at_3_5_Backtracking_answered_on_second_retrieval_Block_1_went_5_5_in_26_55_all_full_solves_every_Day_32_named_cause_held_first_draft_so_M_034_is_answered_for_one_session_The_two_live_problems_are_the_clock_on_new_material_and_B_8_naming_precision_Aug_9_Aug_16_are_working_days_closing_the_deficit_against_Aug_20-0891b2)
![Pace](https://img.shields.io/badge/Pace-on_plan-16a34a)
![Goal](https://img.shields.io/badge/Goal-FAANG_ready_by_Sept-ea580c)
![Language](https://img.shields.io/badge/Language-Python-3776ab)

## 📍 Where I'm at right now

- **Day 33** · **Summer Sprint → Block B**
- **Current focus:** Depth phase — Graphs learned, Intervals held at 3/5, Backtracking answered on second retrieval. Block 1 went 5/5 in 26:55, all full solves — every Day-32 named cause held first-draft, so M-034 is answered for one session. The two live problems are the clock on new material and B-8, naming precision. Aug 9 + Aug 16 are working days, closing the deficit against Aug 20.
- **Up next (Day 34 (Wed Jul 29)):** Graphs cont.
- **Tracker totals:** 33 sessions · 14 patterns learned · 36 mistakes tracked
- **Open blockers:** 1 (B-8 naming precision — ESCALATED Day 33) + watches (M-036, M-027, M-026, M-033, M-034, M-030, M-032, B-4, M-005, M-028)
- **Review queue:** Day 34 (Wed Jul 29) — 7 items, ~25 min: full #200 · #133 (yesterday's new) · ✍️ #90 · #46 · #78 · 🗣 #155 · #74. Backlog re-fuzzed after Day 33 and still lands on real dates through Aug 7; every day Jul 29 – Aug 7 sits at 6–8 items and 25–29 min.
- **Last dashboard update:** 2026-07-28
- 👉 Full live status — pace health, what's due, mastery per pattern — in **[DASHBOARD.md](DASHBOARD.md)**

*This block is generated from `DASHBOARD.md`. Run `python3 scripts/sync_readme.py` after dashboard edits; the pre-commit hook also runs it automatically.*
<!-- README-LIVE:END -->

## Why this repo exists

1. **Accountability.** It's public on purpose. The people following along — my family, my friends — can see exactly where I am and whether I'm holding pace. Hard to quietly skip a day when it's all here.
2. **A reference for other learners.** If you want to study LeetCode, this is a worked example of *how* to prepare day by day — not just a problem list, but the method, the schedule, and what a real beginner's progress (and mistakes) actually look like.

## The method in 60 seconds

Built on cognitive-science evidence (the receipts are in [the playbook](plan/Learning-Science-Playbook.md)):

- **Patterns, not volume.** ~17 reusable patterns (Blind 75 / NeetCode 150) mastered 2–3× each beats grinding 300 problems once.
- **Two blocks a day.** *Block 1:* re-solve a due problem cold from a blank screen. *Block 2:* one new problem, narrated out loud, then re-implemented from scratch.
- **Spaced repetition, reset-on-fail.** Every problem returns on a `1→3→7→21→60`-day ladder; miss it and it resets to tomorrow. State lives in [review/QUEUE.md](review/QUEUE.md).
- **Mistakes are data.** Every slip is logged with a root cause; repeat offenders escalate to a drill list — [review/MISTAKES.md](review/MISTAKES.md).
- **Interleaving + mocks.** Mixed, unlabeled sets train the real interview skill — spotting which pattern a cold problem needs.

## 👀 Following along? (family / friends)

Read these, in order:

1. **[DASHBOARD.md](DASHBOARD.md)** — where I am today, and am I on pace.
2. **[notebooks/](notebooks/)** — the full write-up of every single day: what I solved, where I got stuck, what I fixed.
3. **[GOALS.md](GOALS.md)** — the target and the deadline I'm accountable to.

## 🧭 Want to use this to study yourself?

You can run this exact system:

1. **Follow the curriculum** — [plan/Day-by-Day-Roadmap.md](plan/Day-by-Day-Roadmap.md) lays out every day (the Days 1–8 foundation, then the sprint from Day 9). Start at Day 1.
2. **Use the pattern library** — [patterns/](patterns/) has one cheat-sheet per pattern: the template, when to reach for it, complexity, and common gotchas.
3. **Copy the system** — keep your own [QUEUE](review/QUEUE.md) (spaced reviews), [MISTAKES](review/MISTAKES.md) log, and a daily notebook. [SYSTEM.md](SYSTEM.md) explains exactly how it runs.
4. **Trust the boring method** — solve before you look, narrate everything, re-solve cold a few days later. It feels slow; that slowness is the learning.

## Repo map

| Path | What it is |
|---|---|
| **[DASHBOARD.md](DASHBOARD.md)** | 2-minute status: stage, pace-health, mastery, what's due. |
| **[GOALS.md](GOALS.md)** | The goal, the Aug-20 pivot, pace floors, readiness gates. |
| **[plan/](plan/)** | The curriculum + strategy: day-by-day roadmap, prep plan, learning-science playbook. |
| **[patterns/](patterns/)** | One living file per pattern — template, triggers, complexity, my gotchas. |
| **[review/](review/)** | `QUEUE.md` (spaced reps) · `MISTAKES.md` (root-caused) · `BLOCKERS.md` (drill-now). |
| **[notebooks/](notebooks/)** | Full write-up of each day's session. |
| **[logs/](logs/)** | `LOG.md` — one-line-per-day index. |
| **[SYSTEM.md](SYSTEM.md)** | How the whole tracker works. |

## The daily loop

> Block 1 (review due recalls cold) → Block 2 (new problem, narrate, re-implement from scratch) → write the notebook → commit.

## A note on honesty

This is a live, in-progress, **beginner's** journey. You'll see failed re-solves, off-by-ones, and patterns that took a few attempts to stick — that's the point. Real learning looks like this, and the spaced-repetition system exists precisely to catch the decay and fix it. **Progress over polish.**

---

<details>
<summary><b>For me — running a session</b></summary>

**Start a session** (paste into a new chat with this folder open):

```
Read SYSTEM.md, then DASHBOARD.md, GOALS.md, and the due rows in review/QUEUE.md
and review/BLOCKERS.md. Run the session-start protocol: give me my due recalls
(re-solve from scratch), flag my watchlist mistakes, then start today's new problem
from plan/Day-by-Day-Roadmap.md.
```

**Log a session when done:**

```
Ingest this session. Day {N}, ~{minutes}, {source}.
{raw notes — keep my struggles and dead ends in; tag [STRUGGLE] [INSIGHT] [NEEDS_RECALL]}
```

**Back up to GitHub:** `git add -A && git commit -m "Day N: <topic>" && git push`

</details>
