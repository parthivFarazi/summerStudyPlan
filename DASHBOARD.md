# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-23 (Day 29 logged)
- **Phase:** Summer Sprint · Block B — *Depth phase. **Backtracking deepening** (#90 dedup, #46 permutations — derived cold). B-7 has 1 clean session. Day 30 = interleave + #79 Word Search.*
- **Sessions logged:** 29 · **Patterns learned:** 12 · **Mistakes tracked:** 28 · **Open blockers:** 1 (B-7 drill-now, 1 clean) + watches (M-027, B-4, M-005, M-026, M-028)
- **Review queue:** Day 30 (Jul 24) — resets #211, #1046, #199 first, then new #90, #46, #78. **Backlog exceeds cap Jul 24–25** — apply overflow rule live (see QUEUE).

## 🟢 The honest read

**The clearest signal yet that the drills are working: on Day 29 every *previously-named* reset-cause was correct on the first draft.** `self.` held (#211, #146), the `curr3` name held (#143), the root guard + O(n) space held (#199), the box channel held (#110). Five reviews passed. The three that reset did so on **fresh** facets — #211's constructor-`()`/keys-vs-values/dropped-return, #1046's return-negation, #199's enqueue-direction. **The costume closet is emptying: he's not missing the same thing twice** (with one stubborn exception below).

**The one repeat: `#1046` dropped `return -maxHeap[0]` — the exact same un-negate-on-the-way-out miss as Day 27.** That's the one to burn in: **negate going in → un-negate at the return.** Everything else is genuinely new facets, which is progress.

**B-7 held in his actual writing today** — the morning micro-drill surfaced that his *understanding* is sound (the nested-function-vs-method distinction), and it's an execution slip, not a knowledge gap. One clean session banked; one more clears it.

**The headline win is recursion — his weakest area — visibly moving.** He built **Subsets II** cold (dedup skip-all-copies) and **derived Permutations from scratch** — reframing the take/skip-index structure into a for-loop-over-all-with-a-used-set entirely through reasoning, after being asked to. Two call-stack/decision-tree animators now live in his artifacts for review. Backtracking, the thing that was "rough" two days ago, is becoming a place he can *think*.

**Coaching note to self (feedback):** on #46 the coach led with the code skeleton; Parthiv pushed back ("are you forgetting what you have to do?"). Restarting concept-first and Socratic is what unlocked the derivation. **Teach the model first, never lead with the skeleton** (COACHING #1/#9).

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Every branch returns? · All args passed? · Whose thing is every attribute/method? · Multi-site change complete & every name real? · Un-negate on the way out? · Which side can contain the answer (target-first)?**

## ⚠️ Standing schedule note
Core complete; depth phase (Heap ✓ → **Backtracking (deepening)** → Intervals → Graphs → DP). **Jul 26 = rest** (Sunday). **Review backlog exceeds ~8/day for Jul 24–25** (three big sessions stacked the fragile/3d layers) — apply the overflow rule live: fragile first, verbal the 21d, roll stable 3d/7d forward. Eases after Jul 26. **#79 Word Search carried to Day 30.**

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 28 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 29 = **2** (#90, #46) | 🟢 on plan |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Jul 24 + Jul 25 both over cap | 🔴 backlog — overflow rule live |
| **Open blockers** | **1** (B-7, 1 clean session) | 🟡 one more clean clears it |
| Review pass rate (Day 29) | **5 / 8** | 🟢 all prior-named causes held; resets = fresh facets |

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
| Trees & BFS/DFS | 3/5 | #110 box clean; #199 reset (enqueue direction) |
| Binary Search Tree | 4/5 | stable; B-6 cleared |
| Tries | 2/5 | #211 reset — 3 fresh facets, ownership held |
| Heap | 3/5 | #973/#215 clean; #1046 reset (return-negation) |
| **Backtracking** | **3/5** | **#90 dedup cold, #46 permutations derived from scratch** |

## 🟡 Open blocker & watches

- **B-7 (M-020, `self.`/ownership) — 🟡 drill-now, 1 clean session (Day 29).** Held on #211 & #146. One more clean session clears it. Keep the ownership check in the final read-through.
- **M-027 (one site missed on final pass)** — 👁 the through-line. **#1046 return-negation missed Day 27 AND Day 29 (identical)** — the one repeat; bank "un-negate on the way out."
- **B-4 (guards), M-005 (BFS space)** — 👁 both *held* Day 29 (#199 had them right); watch.
- **M-026 (terminal line), M-028 (box channel)** — 👁 watches; box held Day 29.

*(Cleared → standing habits: B-1 names, B-2 range/len, B-3 return, B-4 guards, B-5 container/contents, **B-6 target-first**, M-025 pointer surgery.)*

## Next Session Focus  → **Day 30 (Jul 24)**
1. **Block 1 — interleave/review (overflow — fragile first):** resets **#211 → #1046 → #199**, then new **#90 → #46 → #78** (1d). Verbal-tier the 21d items; roll the 3d cluster forward. **B-7 micro-drill up front** (one more clean clears it).
2. **Block 2 — new:** **#79 Word Search** (grid DFS + visited-backtracking — the bridge to graphs; carried from Day 29). Go slow (rule 9); pre-teach the grid-DFS + un-mark on the decision tree.
3. **Habits (out loud before submit):** the one scan — **un-negate on the way out (M-027) · whose thing is every attribute (B-7) · every name real** · complexity time AND space.

---
*Weekly snapshots can be appended below as the sprint progresses.*
