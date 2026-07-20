# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-18 (Day 26 logged)
- **Phase:** Summer Sprint · Block B — *Depth phase. **First Heaps done (#703, #1046)** + Trie wildcard (#211). Day 27 = more Heap (#973, #215). (Jul 19 = rest.)*
- **Sessions logged:** 26 · **Patterns learned:** 11 · **Mistakes tracked:** 26 · **Open blockers:** 1 (B-6) + watches (B-4, B-3, M-026)
- **Review queue:** Day 27 (Jul 20) = **6 due**. Resets #102, #208 first; #235 is the B-6 canary.

## 🟡 The honest read

**The pattern of the whole sprint is now crystal clear: he understands the algorithms; he loses to first-draft completeness — and each facet of that clears the moment it gets a named out-loud check.**

Look at the blocker history: **B-1 (names), B-2 (range/len), B-3 (return), B-4 (guards), B-5 (container/contents), B-7 (`self.`) have ALL cleared at least once.** Each was "the knowledge is there, the first draft leaves something out." Each cleared in ~2 sessions once we named a specific pre-submit check. **B-6 (search direction) is the last drill-now blocker** — one clean rep to go (#235 on Jul 20).

**But as fast as facets clear, new ones surface** — Day 26 it was **dropping a required line**: None-guards (#102, B-4 recurred), the `isEnd` end-marker (#208, #211, → M-026), and `return`s (#211). Plus `heapq` argument friction. Same disease, new clothes.

**So the standing work is one habit, and it's worth stating as the through-line of his prep:** before submitting, **walk the operation top to bottom** — guard present? terminal line/mark written? every branch returns? all args passed? mutating the field not a local? That single scan is what separates his current 4-of-6 review days from clean ones. The algorithms are not the gap.

**The bright spots are real:** M-025 (pointer surgery) and B-7 (`self.`) both **cleared** Day 26. He rebuilt LRU cold in 16 min (was 35). He wrote the optimized #230 unprompted. And the **wildcard-DFS (#211) is the deepest recursion he's handled** — the call-stack animations were the unlock, and he asked (now standing rule #9) to always go slow on recursion.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written (isEnd, final set)? · Does every branch return? · All args passed (`heappush(h, x)`)? · Mutating the field not a local? · Which side can contain the answer (target-first)?**

## ⚠️ Standing schedule note
Core complete; depth phase (Heap → Backtracking → Intervals → Graphs → DP). **Jul 19 is a rest day** (end of Sprint Week 3). No unplaced core problems.

## Pace Health
*(🟡 = off the sprint target · 🔴 = at risk. Refreshed each session.)*

| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 33 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 26 = **3** (#211, #703, #1046) | 🟢 ahead of plan |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | 6 (Jul 20) + 7 (Jul 21) | 🟡 fragile cluster; resets up front |
| **Open blockers** | **1** (B-6) + 3 watches | 🟡 B-6 one rep from clearing |
| Review pass rate (Day 26) | **4 / 6** | 🟡 both fails = dropped-line precision |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | re-derives per problem |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| Sliding Window | 3/5 | solid |
| Binary Search | 3/5 | stable |
| Stack | 3/5 | stable |
| Linked List | 4/5 | LRU rebuilt cold in 16 min, verified |
| Trees & BFS/DFS | 3/5 | **#102 reset — dropped None-guards** (execution) |
| Binary Search Tree | 3/5 | #98, #230 both clean |
| **Tries** | **2/5** | **#211 wildcard-DFS** — hard recursion, done w/ guidance |
| **Heap** | **2/5** | **new — #703 (min-heap-of-k), #1046 (max via negation)** |

## 🟡 Open blocker & watches

- **B-6 (M-012, search direction)** — 🟡 **the last drill-now blocker, 1 of 2.** #235's target-first re-solve on **Jul 20** is the pending 2nd clean test. If it inverts again, stop and drill direction cold.
- **B-4 (M-011, edge guards)** — 👁 **watch reopened Day 26** (#102 dropped both None-guards). Full re-escalation if it recurs.
- **M-026 (dropped the terminal line, isEnd)** — 👁 **NEW watch** (#208, #211). One rep from a blocker.
- **B-3 (M-001, returns)** — 👁 watch (#211 missing returns).

*(Cleared → standing habits: B-1 names, B-2 range/len, B-3 return [watch], B-4 guards [watch], B-5 container/contents, **B-7 `self.` (Day 26)**, **M-025 pointer surgery (Day 26)**.)*

## Next Session Focus  → **Day 27 (Jul 20)** *(Jul 19 rest)*
1. **Block 1 — review (6 due):** resets **#102 → #208** first (**#102: root-None + child-None guards; #208: `node.isEnd = True`**), then new **#211 → #703 → #1046** (1d), then **#235** (B-6 canary — **target-first**).
2. **Block 2 — new:** **Heap** — K Closest Points to Origin (#973, heap with tuple keys), Kth Largest in Array (#215, heap or quickselect).
3. **Habits (out loud before submit):** **walk the op to the end — guard? terminal line? does it return? all args?** · target-first (B-6) · complexity time AND space.

---
*Weekly snapshots can be appended below as the sprint progresses.*
