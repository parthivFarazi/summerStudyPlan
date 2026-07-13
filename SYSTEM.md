# SYSTEM.md — How this LeetCode tracker works

> **Read this first in any new chat.** It tells you (Claude or Parthiv) how the system is laid out, how to start a session, and how to record one. Adapted from a two-layer knowledge system, right-sized for a single-domain LeetCode sprint.

## The one-paragraph idea

Two layers. The **event layer** (`logs/LOG.md`) is an append-only diary of what happened each session — never edited. The **knowledge layer** (`patterns/`) is what's *true now* — one living file per pattern, edited in place as understanding improves. Between them sit three control loops: a spaced-repetition **QUEUE** (what to re-solve), a **MISTAKES** log (what keeps going wrong), and a **DASHBOARD** (am I on pace?). Every update touches only what changed — you never reread history to know the current state.

## Layout

| Path | Role |
|---|---|
| `CLAUDE.md` | **Auto-loaded entry point for any new chat.** Read order + the hard rules. |
| `COACHING.md` | **The standing contract** — every instruction Parthiv has given about how to coach him. Never expires; never needs repeating. New instruction → append it there. |
| `SYSTEM.md` | This file. Architecture + protocols. |
| `DASHBOARD.md` | 2-minute status: pace-health, mastery, due count, next-session focus. Regenerated each update. |
| `GOALS.md` | The goal, the Aug 20 pivot, pace floors, readiness gates, review schedule. |
| `plan/Day-by-Day-Roadmap.md` | The curriculum: what to learn each day (Summer Sprint → Fall Maintenance). |
| `plan/FAANG-Prep-Plan.md` · `plan/Learning-Science-Playbook.md` | The strategy + the evidence base. |
| `patterns/` | **Knowledge layer.** One file per pattern (template, triggers, complexity, *your* gotchas) + `INDEX.md`. |
| `review/QUEUE.md` | **Spaced-rep engine.** Single source of truth for what's due. Ladder + reset-on-fail. |
| `review/MISTAKES.md` | **Error engine.** Root-caused, recurrence-counted. |
| `review/BLOCKERS.md` | Mistakes that recurred ≥3× → drill now. |
| `logs/LOG.md` | **Event layer.** Append-only short index, one entry per day. |
| `notebooks/` | Full per-day notebook copies (verbatim: code + coaching), archived from your working folder. |

## Conventions (kept deliberately light)

- **Sessions** are numbered continuously: `Day N`. **The current day is always in `DASHBOARD.md` — never hardcoded here or anywhere else.**
- **Mistakes** get IDs `M-001, M-002, …` so recurrences can be counted.
- **Patterns** are referenced by filename (`patterns/sliding-window.md`), no IDs.
- **Mastery** is 1–5 per pattern (1 = just met it; 5 = can solve a novel one cold while narrating). Lives in the pattern file + DASHBOARD.
- **No fabricated data.** Metrics reflect logged work only. A review that isn't logged didn't happen.

## Session-start protocol  ← this is what makes any new chat pick up where you left off

When Parthiv opens a new chat with this folder selected, do this in order:

0. **Read `COACHING.md`** — the standing contract (how to coach him). **He should never have to repeat an instruction.** If he gives a new one, append it there the same session.
1. **Read `DASHBOARD.md`** (pace-health first — are we on the sprint? any ⚠️ standing schedule notes?).
2. **Pull due items from `review/QUEUE.md`** (`Next due ≤ today`), ordered **resets → 1d → 3d → oldest**. Work a **review budget of ~6–8 items, time-boxed ~30–40 min** (overflow rolls forward — don't try to clear everything):
   - **Full re-solve from a blank screen** for *fragile* items (resets, 1d, anything learned in the last ~week).
   - **30-second verbal recall** for *mastered* items (**21d rung, streak ≥ 3**): state the *pattern + approach + time/space* out loud; only convert to a full solve if he blanks.
   - Claude pulls, orders, and labels each item (full vs verbal); Parthiv just works the list.
3. **Glance at `review/BLOCKERS.md`** — any "drill-now" mistakes to watch this session.
4. **Pick new material** from `plan/Day-by-Day-Roadmap.md` at the current Day (or the largest mastery gap if behind). Pre-teach any new Python concept in isolation first (Parthiv is a beginner — one new thing at a time).

## Session-end protocol (the "ingest")

After studying, record it — this is ~5 minutes and keeps the system alive:

1. **Notebook + log.** Save the day's full notebook (verbatim: code + coaching) to `notebooks/DayN-Practice-Notebook.md`, and append a short dated entry to `logs/LOG.md` (Day N, problems, what happened — keep struggles and dead ends in; tag `[STRUGGLE] [INSIGHT] [NEEDS_RECALL]`).
2. **QUEUE:** add the new problem at rung 1d; for each re-solve, advance on pass / **reset to 1d on fail**.
3. **MISTAKES:** log each slip with a root cause. Same root cause as before ⇒ increment its recurrence; at **≥3 ⇒ escalate to `BLOCKERS.md`**.
4. **Pattern file:** if a new pattern was learned or a new insight/gotcha surfaced, update `patterns/<name>.md` in place (bump mastery if earned).
5. **DASHBOARD + README:** refresh `DASHBOARD.md` (status, pace-health, mastery, due count, next focus), then run `python3 scripts/sync_readme.py` to regenerate the README's live block + badges from the dashboard. The repo-local pre-commit hook also runs this sync automatically.
6. **Hand Parthiv the git command** (see below) — Claude does *not* run git itself.

## Spaced-repetition ladder

`1d → 3d → 7d → 21d → 60d`, then graduated. **Pass = advance one rung. Fail (needed a hint, blanked, or bug you couldn't self-fix) = reset to 1d** and log the cause in MISTAKES. (Research-backed: reset on lapse, don't *soften* it — softening intervals hides the problem items.) Re-solves are *from scratch*, never re-reading the solution.

**Load management (added Day 18 — the queue hit its ~10/day steady-state ceiling):**
- **Fuzz / load-balance due dates:** when setting a new due date, jitter it **±1–2 days toward the lightest upcoming day** so items learned together stop clustering. Keep any single day **≤ ~6–8 due**.
- **Verbal tier:** once an item passes at the **21d** rung, it becomes a **30-second verbal recall** (pattern + approach + complexity), not a full re-solve — full-solve only if he blanks (then reset). This is the big time-saver.

Full rules live in `review/QUEUE.md`.

## Git (your "GitHub-like" layer)

This folder is a git repo (remote `origin` → github.com/parthivFarazi/summerStudyPlan, branch `master`).

**Claude does NOT run git in the sandbox.** The mounted filesystem can't unlink git's `.git/*.lock` files, so ANY in-sandbox git — even a read-only `git status` — leaves stale locks (e.g. `.git/index.lock`, `.git/HEAD.lock`, `.git/objects/maintenance.lock`) that jam the next real commit. Claude only Writes/Edits the tracker files. At session end Claude hands Parthiv ONE command to run on his own machine:

```bash
cd ~/Documents/Claude/Projects/LeetCode\ Practice
git add -A && git commit -m "Day N: <topic>" && git push
```

Never force-push. Git is the real undo button; the log is the human-readable history. *(Workflow confirmed with Parthiv 2026-07-02, after sandbox commits left stale locks twice.)*

## Invariants (what keeps it honest)

- `logs/LOG.md` is append-only. Mistakes are never deleted — status changes only.
- Review state lives in `QUEUE.md` only. Never keep a second history table.
- One pattern, one file. Counters are derived, never stored twice.
- Mastery scores are honest: 5 means you proved it cold. A fail is data, not failure.
