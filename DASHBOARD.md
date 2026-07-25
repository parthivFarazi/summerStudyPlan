# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-25 (Day 30 logged)
- **Phase:** Summer Sprint · Block B — *Depth phase. **Backtracking** now 4 shapes incl. grid DFS (#79 Word Search — bridge to graphs). B-7 CLEARED — no drill-now blocker. Day 31 = drain the backtracking 1d cluster + new material.*
- **Sessions logged:** 30 · **Patterns learned:** 12 · **Mistakes tracked:** 28 · **Open blockers:** 0 (B-7 cleared Day 30) + watches (M-027, backtracking-fragility, B-4, M-005, M-026, M-028)
- **Review queue:** Day 31 (Jul 27) — backtracking 1d cluster #90, #46, #78, #79, #39 first (all fresh/reset), then new material. Jul 26 = REST. **Jul 28 heavy** — overflow rule live (see QUEUE).

## 🟢 The honest read

**Day 30 is the cleanest structural signal of the sprint: the reset-causes have fully MIGRATED to the newest material.** In the interleave, the three that passed each reset on a *named* cause on a prior day — and every one of those causes held first-draft: **#1046's un-negate finally landed** (`return -maxHeap[0]` — closing the sprint's one twice-identical repeat, missed Day 27 AND Day 29), **#211's** three Day-29 facets all fixed (constructor parens, `.children` keys, the dropped return) with ownership clean, and **#199's** enqueue direction fixed. The three that reset — **#78, #90, #46 — are all backtracking**, the pattern that's less than a week old. **He no longer misses the same thing twice; the fragility only ever sits on the freshest pattern.** That's exactly the shape you want the ladder to produce.

**The one twice-identical repeat is closed.** #1046's un-negate-on-the-way-out — the single stubborn miss that reset it identically on two separate days — was correct on the first draft. Bank the rule that fixed it: **negate going in → un-negate at the return.**

**B-7 CLEARED (2nd clean session) → no drill-now blocker; all of B-1…B-7 are clear.** The start-of-session ownership micro-drill answered cleanly, and #211's ownership was correct first-draft on the exact problem that fired B-7. The `self.` rule is now a standing habit, not a live blocker.

**Block 2 added the 4th backtracking shape — grid DFS (#79 Word Search), built cold.** Structure right first try (base cases, mark/un-mark pair, both complexities); two wire-it-up nudges (a dropped **left** direction and `dfs(0,0,0)` vs `dfs(r,c,0)`), both M-027 flavor. Good spec-first instinct — he stopped to make sure he understood the question before coding. **Grid DFS is the bridge into graphs** (an implicit graph, neighbors = adjacent cells).

**The one honest caution:** backtracking is genuinely fragile — three straight reviews reset. It's young, not broken, and Day 31 front-loads the whole 1d cluster (#90/#46/#78/#79/#39) to drain it. Watch it climb before layering more new backtracking on top.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Every branch returns? · All args passed? · Whose thing is every attribute/method? · Multi-site change complete & every name real? · Un-negate on the way out? · Which side can contain the answer (target-first)?**

## ⚠️ Standing schedule note
Core complete; depth phase (Heap ✓ → **Backtracking (4 shapes ✓, incl. grid DFS)** → Intervals → Graphs → DP). **Jul 26 = rest** (Sunday). Day 31 (Jul 27) front-loads the **backtracking 1d cluster** (#90/#46/#78/#79/#39 — the young/fragile pattern) then new material; **Jul 28 heavy** (the Day-30 passes drop back in) — overflow rule live: fragile first, verbal the 21d, roll stable 3d/7d forward.

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 26 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 30 = **1** (#79 Word Search) | 🟢 on plan |
| Sessions last 7 days (target ≥ 6) | 7 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Jul 27 (backtracking cluster) + Jul 28 heavy | 🟡 overflow rule live |
| **Open blockers** | **0** (B-7 cleared Day 30) | 🟢 all B-1…B-7 clear |
| Review pass rate (Day 30) | **3 / 6** | 🟢 every older named cause held; all 3 resets = newest pattern (backtracking) |

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
- **Backtracking fragility** — 👁 NEW watch. #78/#90/#46 all reset Day 30 — youngest pattern (<1 week). Not a blocker; drain the 1d cluster Jul 27.
- **B-4 (guards), M-005 (BFS space), M-026 (terminal line), M-028 (box)** — 👁 all held recently; watch.

*(Cleared → standing habits: B-1 names, B-2 range/len, B-3 return, B-4 guards, B-5 container/contents, **B-6 target-first**, **B-7 `self.`/ownership**, M-025 pointer surgery.)*

## Next Session Focus  → **Day 31 (Jul 27)**
1. **Block 1 — drain the backtracking 1d cluster (fragile first):** **#90 → #46 → #78 → #79 → #39** — the whole young/reset cluster from a blank screen. This is the priority; get the shape to set. Roll any 3d overflow to Jul 28.
2. **Block 2 — new:** **Intervals** (Insert/Merge Intervals — #57/#56) *or* Backtracking cont. (#40 Comb Sum II / #131 Palindrome Partitioning) if the cluster still feels shaky. Pick based on how Block 1 lands.
3. **Habits (out loud before submit):** the one scan — **every direction in a neighbor sweep · un-negate on the way out (M-027) · loop vars actually feed the call · every name real** · complexity time AND space. (B-7 cleared — ownership check now automatic.)

---
*Weekly snapshots can be appended below as the sprint progresses.*
