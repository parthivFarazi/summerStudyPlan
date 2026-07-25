# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-25 (Day 30 logged) · **Day 31 set up in advance · calendar rebuilt**
- **Phase:** Summer Sprint · Block B — *Depth phase — Backtracking done, Intervals next; calendar rebuilt, Sundays now worked. **Backtracking** has 4 shapes incl. grid DFS (#79 Word Search — bridge to graphs). B-7 CLEARED — no drill-now blocker. **Calendar rebuilt 2026-07-25: Day 31 moves onto Sun Jul 26 and Aug 9 + Aug 16 become working days**, closing a 2-session deficit against Aug 20.*
- **Sessions logged:** 30 · **Patterns learned:** 12 · **Mistakes tracked:** 28 · **Open blockers:** 0 (B-7 cleared Day 30) + watches (M-027, backtracking-fragility, B-4, M-005, M-026, M-028)
- **Review queue:** **Day 31 (Sun Jul 26, ~90 min)** — just the three backtracking items that actually failed: #90, #78, #46, full re-solve. **The 43-item backlog is landed on real dates across Jul 26 – Aug 5** and **re-tiered by rung** (1d/reset = full · 3d = ✍️ one-draft · 7d+ = 🗣 verbal). **No day exceeds 8 items or ~29 min; average 6.4 in ~24 min.** Run-sheet: `plan/Day-31-Runsheet.md`.

## 🔴 The schedule, honestly *(rebuilt 2026-07-25)*

**The roadmap did not fit.** Day 31 on Jul 27 → Day 53 on Aug 19 needed **23 sessions into 21 working days** (minus Sundays Aug 2/9/16). **A 2-session deficit.** *(Day 30's single new problem is **not** part of the problem — it was an interleave day, which is built to carry 0–1 new. An earlier version of this file called it a miss; that was wrong.)*

**The fix, agreed 2026-07-25:** work Sundays. **Day 31 moves onto Sun Jul 26** (recovers 1), and **Aug 9 + Aug 16 become working days** (recovers 2). Aug 2 stays rest. Result: **24 sessions for 23 days of content, with Aug 19 as a one-day buffer.**

**The buffer is one day wide.** One slip eats it. Two puts Day 53 past the deadline. **If a session slips, the recovery is a triple-new day — not a shrug.**

**The queue was also carrying a hidden pile:** 43 items due-or-overdue on/before Jul 28, 18 already past due and rolled forward with no landing date. All 43 now sit on real dates across **Jul 26 – Aug 5**. *(New standing rule: a roll-forward must land on a concrete date — `COACHING.md` rule 10.)*

**And the first re-spread was still too heavy — he called it, twice, correctly.** Six levers now applied: **three review tiers set by rung** (1d/reset = full solve · **3d = ✍️ one-draft, 4-min cap, no debugging** · 7d+ = 🗣 verbal), **drain stretched to Aug 5**, **backtracking cluster split** (#79/#39 → Jul 27), **overdue sweep moved off Day 31**, **reviews weight-balanced against Block 2** (Graph/DP days get light reviews and run Block 2 first), and **same-pattern reviews batched**. **Day 31 is 3 re-solves + 2 new in ~90 min; no later day exceeds 8 items or ~29 min.** Nothing was dropped.

**The honest size of that fix:** the tier change buys ~6–8 minutes of clock — modest. **What actually changed is intensity:** ~2 items per session now involve write-run-debug, down from ~5. The one-draft tier was chosen over a cheaper structure-sketch on purpose — his failures are execution slips, and a sketch tier would stop catching them.

## 🟢 The honest read

**Day 30 is the cleanest structural signal of the sprint: the reset-causes have fully MIGRATED to the newest material.** In the interleave, the three that passed each reset on a *named* cause on a prior day — and every one of those causes held first-draft: **#1046's un-negate finally landed** (`return -maxHeap[0]` — closing the sprint's one twice-identical repeat, missed Day 27 AND Day 29), **#211's** three Day-29 facets all fixed (constructor parens, `.children` keys, the dropped return) with ownership clean, and **#199's** enqueue direction fixed. The three that reset — **#78, #90, #46 — are all backtracking**, the pattern that's less than a week old. **He no longer misses the same thing twice; the fragility only ever sits on the freshest pattern.** That's exactly the shape you want the ladder to produce.

**The one twice-identical repeat is closed.** #1046's un-negate-on-the-way-out — the single stubborn miss that reset it identically on two separate days — was correct on the first draft. Bank the rule that fixed it: **negate going in → un-negate at the return.**

**B-7 CLEARED (2nd clean session) → no drill-now blocker; all of B-1…B-7 are clear.** The start-of-session ownership micro-drill answered cleanly, and #211's ownership was correct first-draft on the exact problem that fired B-7. The `self.` rule is now a standing habit, not a live blocker.

**Block 2 added the 4th backtracking shape — grid DFS (#79 Word Search), built cold.** Structure right first try (base cases, mark/un-mark pair, both complexities); two wire-it-up nudges (a dropped **left** direction and `dfs(0,0,0)` vs `dfs(r,c,0)`), both M-027 flavor. Good spec-first instinct — he stopped to make sure he understood the question before coding. **Grid DFS is the bridge into graphs** (an implicit graph, neighbors = adjacent cells).

**The one honest caution:** backtracking is genuinely fragile — three straight reviews reset. It's young, not broken. Day 31 takes **the three that actually failed** (#90/#46/#78) from a blank screen; **#79/#39 follow Jul 27** (never failed — at 1d because they're new). Watch it climb before layering more new backtracking on top.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Every branch returns? · All args passed? · Whose thing is every attribute/method? · Multi-site change complete & every name real? · Un-negate on the way out? · Which side can contain the answer (target-first)?**

## ⚠️ Standing schedule note
Core complete; depth phase (Heap ✓ → **Backtracking (4 shapes ✓, incl. grid DFS)** → **Intervals (Day 31)** → Graphs → DP). **🔴 Jul 26 is no longer a rest day — it is Day 31.** Rest is **Aug 2**; **Aug 9 and Aug 16 are worked**; **Aug 19 is the buffer**. Full mapping in `plan/Day-by-Day-Roadmap.md` → *Recovered calendar*. Reviews run the **backlog drain** (QUEUE) through Aug 5 under a **hard 30-min box**, weight-balanced so the **Graph days (Jul 28–30) and DP days (Aug 1–5) get light reviews and run Block 2 first.**

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 26 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 30 = **1** (#79) + a full interleave block | 🟢 on plan — interleave days carry 0–1 new by design |
| **Schedule fit** (Days 31–53) | 23 sessions into **24** available days | 🟡 fits — **1-day buffer only** |
| Sessions last 7 days (target ≥ 6) | 7 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Jul 26 = **3** · Jul 27 = 6 | 🟢 re-spread, well under cap |
| Review backlog carried | 43 items, **all dated** Jul 26 – Aug 5 · re-tiered by rung | 🟢 drain running, avg 6.4 items / ~24 min |
| **Open blockers** | **0** (B-7 cleared Day 30) | 🟢 all B-1…B-7 clear |
| Review pass rate (Day 30) | **3 / 6** (50%) | 🟡 **below the 55% line** — all 3 resets = newest pattern (backtracking); every older named cause held |
| **Expected Block 1 load** | **~7/session** (≈3.5 full + 1.4 ✍️ + 2.2 🗣) | 🟢 **hard 30-min box** · matches the agreed 6–8 |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | O(n·2ⁿ), O(n·n!), O(T/M) all derived |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| Sliding Window | 3/5 | solid |
| Binary Search | 3/5 | stable |
| Stack | 3/5 | stable |
| Linked List | 4/5 | #143 clean, LRU rebuilt cold |
| Trees & BFS/DFS | 3/5 | #110 box clean; **#199 fixed (enqueue direction) Day 30** |
| Binary Search Tree | 4/5 | stable; B-6 cleared |
| Tries | 3/5 | **#211 clean Day 30 — all Day-29 facets fixed, ownership held** |
| Heap | 3/5 | #973/#215 clean; **#1046 fixed Day 30 (un-negate finally landed)** |
| **Backtracking** | **3/5** | **4 shapes: take/skip, dedup, for-loop+used-set, grid DFS (#79). Young — #78/#90/#46 reset Day 30** |

## 🟢 No open blocker · watches only

- **B-7 (M-020, `self.`/ownership) — ✅ CLEARED Day 30** (2 clean sessions). All of B-1…B-7 clear. Ownership check is now a standing habit; re-escalate on recurrence.
- **M-027 (one site missed on final pass)** — 👁 the through-line, **but the one *repeat* (#1046 un-negate) is CLOSED Day 30.** Residual: the two #79 nudges (dropped left direction; `dfs(0,0,0)` vs `dfs(r,c,0)`). Drill = the final read-through.
- **Backtracking fragility** — 👁 NEW watch. #78/#90/#46 all reset Day 30 — youngest pattern (<1 week). Not a blocker; those three re-solve **Sun Jul 26**, #79/#39 **Mon Jul 27**.
- **B-4 (guards), M-005 (BFS space), M-026 (terminal line), M-028 (box)** — 👁 all held recently; watch.

*(Cleared → standing habits: B-1 names, B-2 range/len, B-3 return, B-4 guards, B-5 container/contents, **B-6 target-first**, **B-7 `self.`/ownership**, M-025 pointer surgery.)*

## Next Session Focus  → **Day 31 (Sun Jul 26)**
> **Fully set up in advance — see `plan/Day-31-Runsheet.md` for the timed blocks, examples, and pre-teach script. Sized to ~90 min.**

1. **Block 1 — the three backtracking items that failed (35 min, ~12 min each):** **#90 → #46 → #78** from a blank screen, stopwatch on each. **#79 and #39 are deliberately NOT today** — neither has ever failed; they sit at 1d because they're new, and they land Jul 27.
2. **Block 2 — new:** **Intervals — #57 Insert Interval, #56 Merge Intervals** (40 min). Locked, not conditional. Pre-teach `lambda` as a sort key and `for a, b in pairs:` in isolation first — 5 min each, before #57.
3. **If the clock runs out, Block 1 is what gets trimmed — never Block 2.** New material has no slack in the calendar; reviews have a ten-day drain behind them. Any trim gets written onto **Day 32 in `QUEUE.md`** before the session closes — never silently.
4. **Habits (out loud before submit):** the one scan — **every direction in a neighbor sweep · un-negate on the way out (M-027) · loop vars actually feed the call · every name real** · complexity time AND space **stated before the code**. (B-7 cleared — ownership check now automatic.)

---
*Weekly snapshots can be appended below as the sprint progresses.*
