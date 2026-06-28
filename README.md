# LeetCode Practice — study tracker

A self-contained system so **any new chat can pick up exactly where I left off.** Inspired by a friend's two-layer knowledge tracker, right-sized for a focused LeetCode interview sprint.

## Start any session (copy-paste into a new chat with this folder selected)

```
Read SYSTEM.md, then DASHBOARD.md, GOALS.md, and the due rows in review/QUEUE.md
and review/BLOCKERS.md. Run the session-start protocol: give me my due recalls
(re-solve from scratch), flag my watchlist mistakes, then start today's new problem
from plan/Day-by-Day-Roadmap.md.
```

## Log a session when done

```
Ingest this session. Day {N}, ~{minutes}, {source}.
{raw notes — keep my struggles and dead ends in; tag [STRUGGLE] [INSIGHT] [NEEDS_RECALL]}
```
…and I'll update the log, queue (reset-on-fail), mistakes (recurrence), the pattern file, and the dashboard.

## What's here

| File / folder | What it is |
|---|---|
| **SYSTEM.md** | How it all works + the session protocols. **Read first.** |
| **DASHBOARD.md** | 2-minute status: pace-health, mastery, what's due, next focus. |
| **GOALS.md** | The goal, the Aug 20 pivot, pace floors, readiness gates. |
| **plan/Day-by-Day-Roadmap.md** | The curriculum: what to learn each day. |
| **plan/FAANG-Prep-Plan.md** / **plan/Learning-Science-Playbook.md** | Strategy + the evidence base. |
| **patterns/** | One living file per pattern (template, triggers, complexity, my gotchas) + INDEX. |
| **review/** | `QUEUE.md` (spaced reps), `MISTAKES.md` (root-caused), `BLOCKERS.md` (drill-now). |
| **logs/** | `LOG.md` — append-only session diary. |

## The daily loop
Block 1 (review due recalls cold) → Block 2 (new problem, narrate aloud, re-implement from scratch) → log + commit.

## Keep it backed up (git)
```bash
git add -A && git commit -m "Day N: <topic>"
```
To push to GitHub: make an empty repo there, then `git remote add origin <url> && git push -u origin main` once.
