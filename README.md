# 📈 Summer Study Plan — LeetCode Interview Prep, in the Open

A beginner working from near-zero toward **FAANG-ready by interview season**, one tracked day at a time. This repo *is* my real prep — the plan, the daily notebooks, the mistakes, and the spaced-repetition system that ties it together. Not polished-for-show: the actual journey, decay and dumb bugs included.

<!-- README-LIVE:START -->
![Day](https://img.shields.io/badge/Day-19-2563eb)
![Phase](https://img.shields.io/badge/Phase-Summer_Sprint-7c3aed)
![Focus](https://img.shields.io/badge/Focus-Linked_Lists_started_Day_20_Reorder_List_Remove_Nth_Node-0891b2)
![Pace](https://img.shields.io/badge/Pace-ahead-16a34a)
![Goal](https://img.shields.io/badge/Goal-FAANG_ready_by_Sept-ea580c)
![Language](https://img.shields.io/badge/Language-Python-3776ab)

## 📍 Where I'm at right now

- **Day 19** · **Summer Sprint → Block B**
- **Current focus:** Linked Lists started. Day 20 = Reorder List + Remove Nth Node.
- **Up next (Day 20):** Linked List Mediums
- **Tracker totals:** 19 sessions · 7 patterns learned · 20 mistakes tracked
- **Open blockers:** 1 (B-3: forgetting `return` — light)
- **Review queue:** Day 20 (Jul 11) ≈ 7 due (#875 reset + 6, incl. 2 verbal) — new protocol keeps it smoothed
- **Last dashboard update:** 2026-07-10
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
