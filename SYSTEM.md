# SYSTEM.md — How this LeetCode tracker works

> **Read this first in any new chat.** It tells you (Claude or Parthiv) how the system is laid out, how to start a session, and how to record one. Adapted from a two-layer knowledge system, right-sized for a single-domain LeetCode sprint.

## The one-paragraph idea

Two layers. The **event layer** (`logs/LOG.md`) is an append-only diary of what happened each session — never edited. The **knowledge layer** (`patterns/`) is what's *true now* — one living file per pattern, edited in place as understanding improves. Between them sit three control loops: a spaced-repetition **QUEUE** (what to re-solve), a **MISTAKES** log (what keeps going wrong), and a **DASHBOARD** (am I on pace?). Every update touches only what changed — you never reread history to know the current state.

## Layout

| Path | Role |
|---|---|
| `SYSTEM.md` | This file. Architecture + protocols. Read first. |
| `DASHBOARD.md` | 2-minute status: pace-health, mastery, due count, next-session focus. Regenerated each update. |
| `GOALS.md` | The goal, the Aug 20 pivot, pace floors, readiness gates, review schedule. |
| `plan/Day-by-Day-Roadmap.md` | The curriculum: what to learn each day (Summer Sprint → Fall Maintenance). |
| `plan/FAANG-Prep-Plan.md` · `plan/Learning-Science-Playbook.md` | The strategy + the evidence base. |
| `patterns/` | **Knowledge layer.** One file per pattern (template, triggers, complexity, *your* gotchas) + `INDEX.md`. |
| `review/QUEUE.md` | **Spaced-rep engine.** Single source of truth for what's due. Ladder + reset-on-fail. |
| `review/MISTAKES.md` | **Error engine.** Root-caused, recurrence-counted. |
| `review/BLOCKERS.md` | Mistakes that recurred ≥3× → drill now. |
| `logs/LOG.md` | **Event layer.** Append-only daily session notebook. |

## Conventions (kept deliberately light)

- **Sessions** are numbered continuously: `Day N`. (You're on Day 8 done; next is Day 9.)
- **Mistakes** get IDs `M-001, M-002, …` so recurrences can be counted.
- **Patterns** are referenced by filename (`patterns/sliding-window.md`), no IDs.
- **Mastery** is 1–5 per pattern (1 = just met it; 5 = can solve a novel one cold while narrating). Lives in the pattern file + DASHBOARD.
- **No fabricated data.** Metrics reflect logged work only. A review that isn't logged didn't happen.

## Session-start protocol  ← this is what makes any new chat pick up where you left off

When Parthiv opens a new chat with this folder selected, do this in order:

1. **Read `DASHBOARD.md`** (pace-health first — are we on the sprint?).
2. **Pull due items from `review/QUEUE.md`** (`Next due ≤ today`, by age). Have Parthiv **re-solve them from a blank screen *before* opening any pattern file** — that's the retrieval rep. Cap ~3 in the sprint.
3. **Glance at `review/BLOCKERS.md`** — any "drill-now" mistakes to watch this session.
4. **Pick new material** from `plan/Day-by-Day-Roadmap.md` at the current Day (or the largest mastery gap if behind). Pre-teach any new Python concept in isolation first (Parthiv is a beginner — one new thing at a time).

## Session-end protocol (the "ingest")

After studying, record it — this is ~5 minutes and keeps the system alive:

1. **Append** a dated entry to `logs/LOG.md` (Day N, duration, problems, what happened — keep struggles and dead ends in; tag inline with `[STRUGGLE] [INSIGHT] [NEEDS_RECALL]`).
2. **QUEUE:** add the new problem at rung 1d; for each re-solve, advance on pass / **reset to 1d on fail**.
3. **MISTAKES:** log each slip with a root cause. Same root cause as before ⇒ increment its recurrence; at **≥3 ⇒ escalate to `BLOCKERS.md`**.
4. **Pattern file:** if a new pattern was learned or a new insight/gotcha surfaced, update `patterns/<name>.md` in place (bump mastery if earned).
5. **DASHBOARD:** refresh status, pace-health, mastery, due count, next-session focus.
6. **Commit** (see below).

## Spaced-repetition ladder

`1d → 3d → 7d → 21d → 60d`, then graduated. **Pass = advance one rung. Fail (needed a hint, blanked, or bug you couldn't self-fix) = reset to 1d** and log the cause in MISTAKES. Re-solves are *from scratch*, never re-reading the solution. Full rules live in `review/QUEUE.md`.

## Git (your "GitHub-like" layer)

This folder is a git repo. After each session:

```bash
cd "path/to/LeetCode Practice"
git add -A && git commit -m "Day N: <topic>"
```

To back it up to GitHub, create an empty repo there and `git remote add origin <url> && git push -u origin main` (one-time). Never force-push. Git is the real undo button; the log is the human-readable history.

## Invariants (what keeps it honest)

- `logs/LOG.md` is append-only. Mistakes are never deleted — status changes only.
- Review state lives in `QUEUE.md` only. Never keep a second history table.
- One pattern, one file. Counters are derived, never stored twice.
- Mastery scores are honest: 5 means you proved it cold. A fail is data, not failure.
