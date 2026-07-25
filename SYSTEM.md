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
   - **The rung sets the tier** (full table under *Spaced-repetition ladder*): **1d/reset → full solve** (~6 min) · **3d → ✍️ one-draft**, 4-min cap, no running or debugging (~4 min) · **7d+ → 🗣 verbal recall** (~30 sec).
   - **Hard 30-min box.** Whatever isn't reached gets a concrete date written into `QUEUE.md` before the session ends.
   - **Balance the weight against Block 2**: heavy new material (Graphs, DP) ⇒ light reviews, and **run Block 2 first** on those days. **Batch same-pattern reviews** together (except on interleave days).
   - Claude pulls, orders, weight-balances, and labels each item; Parthiv just works the list.
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
- **Three review tiers — the rung sets the tier.** *(Established 2026-07-25, after he raised that 6–8 full re-solves would be exhausting on hard-topic days. An item is at 3d precisely because it just passed at 1d, so "3d rung" and "clean last result" are the same condition — no extra bookkeeping.)*

| Rung | Tier | Cost | What he does |
|---|---|---|---|
| **1d · reset** | **Full solve** | ~6 min | Blank screen, write it, run it, debug it. Never cheapened — this is where fragility lives. |
| **3d** | **✍️ One-draft** | ~4 min | Write the full solution **once**, hard 4-min cap. **No running it, no debugging.** Then audit your own draft against the scan. **Pass = the first draft was correct.** |
| **7d · 21d · 60d** | **🗣 Verbal** | ~30 sec | Say pattern + approach + time/space out loud. Blank ⇒ convert to a full solve ⇒ reset. |

  **Why one-draft rather than a structure sketch:** his failure mode is **first-draft precision**, not comprehension — dropped returns, missing guards, `.val` where a node pointer belongs. A skeleton/pseudocode tier would be cheaper still but would skip exactly the line-level execution his reviews exist to catch. One-draft is *faster than* a solve-and-debug **and** trains the weakness head-on: no debugger to rescue you, so the first draft has to be right.

  **Full solve vs. one-draft — the difference is the safety net and the pass bar** *(he asked, 2026-07-25; answer it from here, don't re-derive)*:

| | Full solve | ✍️ One-draft |
|---|---|---|
| Run the code? | Yes | **No** |
| Fix what you find? | Yes | **No — stop typing at the cap** |
| Time | ~6 min | **4 min, hard cap** |
| **Pass =** | reached a working solution unaided | **the draft was right, OR his own audit caught what was wrong** |
| **Fail =** | needed a hint, blanked, or a bug he couldn't self-fix | **still wrong after his audit — Claude had to point it out** |

  **The cheaper tier is graded harder, on purpose.** Forget a `return`: on a full solve he runs it, sees `None`, fixes it, **passes**. On a one-draft the same code passes *only if his own read-through catches it*. An item at 3d already proved comprehension when it passed at 1d — what's still unproven is whether he can produce it **correctly on the first try**, which is exactly where his reviews fail. Running the code hides that; the interpreter does his checking for him. **Less work and less fatigue, but a narrower standard, not a softer one.**

  **The audit is the graded skill.** He says the scan out loud over his own draft before any verdict. Catching his own slip there is a **pass** — that's the habit working.

- **Hard 30-minute box on Block 1.** *(2026-07-25.)* Block 1 stops at 30 minutes regardless of what's left, ordered **resets → 1d → 3d → verbal**. Anything unreached gets a **concrete date written into `QUEUE.md`** before the session closes. The ceiling is structural, not a willpower test.

- **Balance review difficulty against the day's new material.** Heavy new-material days (Graphs, DP) get **light reviews** — arrays, two-pointers, stack, binary search. Light or interleave days absorb the **heavy** ones — backtracking, graphs, DP, design. Assign by due-date *and* by weight, never by due-date alone.

- **On heavy days, Block 2 runs first.** New material is construction and degrades fast when tired; review is recall and holds up better. So on Graph/DP days: **new material while fresh, reviews after.** Normal days keep reviews first.

- **Batch same-pattern reviews within a day** so context stays loaded — four trees problems in a row is markedly cheaper than four unrelated ones. **Exception: interleave days, where mixing is the entire point.**

Full rules live in `review/QUEUE.md`.

### What the review load actually is *(computed 2026-07-25 — don't re-derive it)*

Parthiv asked how many reviews Block 1 carries on an average day going forward. The ladder determines this; it isn't a dial.

| Period | Items/session | Full | ✍️ One-draft | 🗣 Verbal | Time |
|---|---|---|---|---|---|
| **Days 31–40** (backlog draining) | **6.4** | ~2 | ~2.3 | ~2.2 | **~24 min** |
| **Days 41–53** (steady state) | **~7** | ~3.5 | ~1.4 | ~2.2 | **~28 min** |

**Why ~7:** at 2 new/day, each rung (1d / 3d / 7d / 21d / 60d) receives ~2 items per day, plus failures re-entering at 1d. That's ~5.5 scheduled + ~1.5 resets.

**Stretching the rung intervals does NOT reduce this.** In steady state the arrival rate at each rung equals the rate of items passing into it, independent of interval length. Longer intervals delay load; they don't shrink it. Don't propose it as a fix — it was considered and rejected 2026-07-25.

**Only three things reduce Block 1:** fewer new problems/day (no calendar slack before Aug 20), fewer rungs (the 60d rung already falls outside the sprint window — nothing to cut), or **cheapening each review** (the tier table above). The third is the only live lever, and it's now pulled.

**The load is insensitive to his pass rate.** At 60% / 70% / 80% the totals are 6.4 / 7.1 / 7.9 per day, but **full solves stay ~3.5 in all three cases.** Passing more doesn't reduce the writing; it promotes items into cheaper tiers. Passing less feeds resets back into 1d.

**The warning line:** if his pass rate drops below **~55%**, resets accumulate at 1d and the full-solve count climbs — the 30-min box starts truncating real work. **That's the signal to slow new material, not to trim reviews.** Flag it on the DASHBOARD if it appears.

**Honest sizing of the fix:** the tier change buys ~6–8 minutes of clock, which is modest. **The larger effect is intensity, not duration** — only ~2 items per session now involve write-run-debug, down from ~5. The difficulty-balancing and the new-material-first ordering do more for how a hard day *feels* than the clock saving does.

*(Fall, post-Aug 20: new drops to ~2–3/week, so the load falls to ~3–4/day and is mostly verbal, since by then most items sit at the 21d and 60d rungs.)*

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
