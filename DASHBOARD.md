# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-22 (Day 28 logged)
- **Phase:** Summer Sprint · Block B — *Depth phase. **Backtracking started (#78, #39)** — new pattern #12. Heap depth done Day 27; B-6 cleared, B-7 re-escalated. Day 29 = more Backtracking. (Jul 26 = rest.)*
- **Sessions logged:** 28 · **Patterns learned:** 12 · **Mistakes tracked:** 28 · **Open blockers:** 1 (B-7 drill-now) + watches (M-027, B-4, M-005, M-026, M-028)
- **Review queue:** Day 29 (Jul 23) = **8 due**, all fragile. The 5 Day-27 items (now spaced) + 3 Day-28 resets (#143, #199, #146).

## 🟡 The honest read

**Two sessions in one day (Days 27 + 28), and the signal is the sharpest it's been: he reconstructs correct algorithms and designs cold, and loses to a single site on the final pass.** Day 28's three resets were each *one* thing in otherwise-flawless work — a `curr`/`curr3` typo (#143), a dropped root-guard (#199), a missing `self.` (#146). None was a comprehension gap.

**B-6 cleared (Day 27) — but B-7 came right back.** The `self.`/ownership slip fired #211 on Day 27 and #146 on Day 28 — **two days running** — so it's re-escalated to drill-now. It's the same disease every cleared blocker was: the knowledge is there, the first draft leaves one thing out. **M-027 ("one site missed on the final pass") is the umbrella** — negate/rename/paired-op/guard/name/`self.`, all the same failure.

**The single highest-leverage habit, stated for his whole prep:** before submitting, a deliberate **final read-through of every site** — guard present? every name real and owned (`self.remove`, `node.isEnd`)? every branch returns? a transform on all its boundaries? That one scan converts his reset days into clean ones. The algorithms are not the gap; they haven't been for weeks.

**The real bright spot — recursion, his weakest area, is moving.** He **derived Subsets by hand-tracing** and the code fell out; and the call-stack animator got him from "lost from the start" to explaining how a `return` cascades and halts. That's a genuine step in the thing he's found hardest all sprint. Heap is also solid now (#973/#215, size-k both directions).

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Every branch returns? · All args passed? · Whose thing is every attribute/method (self.remove, node.isEnd)? · Multi-site change complete & every name real? · Which side can contain the answer (target-first)?**

## ⚠️ Standing schedule note
Core complete; depth phase (Heap ✓ → **Backtracking (in progress)** → Intervals → Graphs → DP). **Jul 26 is a rest day** (Sunday). Heavy review backlog (double session + the skipped Jul 20 stacked the fragile/3d layers) — rides the ~8/day cap through ~Jul 28, then eases.

## Pace Health
*(🟡 = off the sprint target · 🔴 = at risk. Refreshed each session.)*

| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 29 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Days 27–28 = **4** (#973/#215/#78/#39) | 🟢 ahead (2 sessions/day) |
| Sessions last 7 days (target ≥ 6) | 6 (incl. 2 today; Jul 20 skipped, Jul 19 rest) | 🟢 caught up |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | 8 (Jul 23) + 8 (Jul 24) | 🟡 rides the cap; fragile-heavy |
| **Open blockers** | **1** (B-7 drill-now) + 4 watches | 🟡 B-7 fired 2 days running |
| Review pass rate (Day 28) | **3 / 6** | 🟡 all 3 = one-site final-pass slips |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | O(log k), O(n·2^n), O(T/M) all derived |
| Arrays & Hashing | 3/5 | #271 container-bug cleared |
| Two Pointers | 3/5 | stable |
| Sliding Window | 3/5 | solid |
| Binary Search | 3/5 | stable |
| Stack | 3/5 | stable |
| Linked List | 4/5 | #143 flawless algo (typo reset); LRU rebuilt cold |
| Trees & BFS/DFS | 3/5 | #199 reset — dropped guard + BFS-space slip |
| Binary Search Tree | 4/5 | #98 bounds clean; **B-6 cleared on #235** |
| Tries | 2/5 | #211 cold-correct algo, ownership slip |
| **Heap** | **3/5** | #973 / #215, size-k both directions, tuple keys |
| **Backtracking** | **2/5** | **new — #78 derived by hand-trace, #39 w/ animator** |

## 🔴 Open blocker & watches

- **B-7 (M-020, `self.`/ownership) — 🔴 DRILL-NOW (re-escalated Day 28).** Fired #211 (Day 27) + #146 (Day 28). Micro-drill start of next 2–3 sessions: *whose thing is every attribute/method?* Clears on 2 clean sessions.
- **M-027 (one site missed on final pass)** — 👁 the through-line of Days 27–28 (negate/rename/paired-op/guard/name). Drill = the deliberate final read-through.
- **B-4 (guards)** — 👁 watch, fired Day 28 (#199 root guard).
- **M-005 (BFS space = O(n), not O(1))** — 👁 watch, fired Day 28 (#199).
- **M-026 (terminal line), M-028 (box channel)** — 👁 watches.

*(Cleared → standing habits: B-1 names, B-2 range/len, B-3 return, B-4 guards, B-5 container/contents, **B-6 target-first (Day 27)**, M-025 pointer surgery. B-7 was cleared Day 26 — reopened.)*

## Next Session Focus  → **Day 29 (Jul 23)**
1. **Block 1 — review (8 due, all fragile):** resets/deferred first — **#211 → #1046 → #110 → #973 → #215** (the Day-27 batch, now properly spaced), then **#143 → #199 → #146** (Day-28 resets). **B-7 micro-drill up front.**
2. **Block 2 — new:** **Backtracking cont.** — Subsets II (#90, dedup with sorted + skip-duplicates) and/or Combination Sum II (#40), or Permutations (#46). Keep going slow on the recursion; reuse the animator.
3. **Habits (out loud before submit):** **final read-through — every name real & owned? guard present? multi-site change complete? (M-027 / B-7)** · complexity time AND space.

---
*Weekly snapshots can be appended below as the sprint progresses.*
