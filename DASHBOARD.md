# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-08-01 (Day 36 logged) · **🎯 Mock #1: 19:38 unaided · Block 1 5/5 · B-9 cleared**
- **Phase:** Summer Sprint · Block B — *The best session of the sprint. **Mock #1 came in at 19:38 against a 35-minute cap**, correct, with the pattern named in the first sentence. **Block 1 went 5/5** on the same five problems that went 2/5 yesterday — **the understanding didn't change overnight; he ran the code before sending it.** Graphs 3/5 with all six problems now passing. **1-D DP starts Monday.** Aug 9 and Aug 16 are working days.*
- **Sessions logged:** 36 · **Patterns learned:** 14 · **Mistakes tracked:** 40 · **Open blockers:** 3 (**B-10 price the loop body — new**, B-5 container/contents — 1 clean, B-8 naming) · **✅ B-9 cleared**
- **Review queue:** **Day 37 (Mon Aug 3) — 8 items, ~27 min:** full **#567** (write the `O(n)` version) · ✍️ **#200 · #79 · #39 · #57** · 🗣 **#739 · #121 · #153**. Drain re-spread through **Aug 11**; every day Aug 3 – Aug 11 sits at 22–28 min.

## 🎯 Mock #1 — the first unaided data point in 36 sessions

| | date | problem | time | outcome |
|---|---|---|---|---|
| **Mock #1** | Sat Aug 1 | **#567 Permutation in String** | **19:38** ✅ *(cap 35)* | **correct, but would TLE** |

**I told him to expect over 35 minutes. He came in fifteen under, with correct code, unaided, on an unseen problem** — against 44–72 minutes for every previous new problem *with* coaching. **And he named the pattern in his first sentence**, so the `GOALS.md` recognition gate is met.

| | self | coach | |
|---|---|---|---|
| Communication | 4.5 | **4** | stated his index convention explicitly — interview-grade |
| Problem-solving | 2.5 | **2.5** | exactly right |
| Technical correctness | 1.5 | **2** | he was right to be unsure |
| Testing | 3 | **3** | tested, found a real bug, reported it |

> **The calibration is the quiet result: he was least confident exactly where he was wrong and most confident exactly where he was right.** Four days after asserting *"it does give 3"* about an untraced output, that is a real change.

**The two gaps it exposed — both invisible in coached reviews:**

1. **⛔ B-10 opened.** The solution TLEs: `O(n² log n)` where he said `O(n log n)`, with a **loop-invariant `sorted()` inside the loop**. Measured at the constraint ceiling: **5.67 s** as written · **2.80 s** with one line hoisted · **0.001 s** for the `O(n)` version. **M-006's third appearance** (Group Anagrams Day 3, Longest Substring Day 8).
2. **M-040 — he named the optimal approach and rejected it.** *"I would have had to complicate it more by using a dictionary."* That dictionary is the answer. **"I know a better approach but it's fiddlier" is not a reason to skip it — it's what the interviewer asks for next.**

## 🟢 The finding of the sprint: the delta was twenty seconds

| | Day 35 | Day 36 |
|---|---|---|
| #133 | ❌ wrong object's list | ✅ **same bug in the first draft — caught by running** |
| #46 | ❌ `backtrack()` never called | ✅ |
| #994 | ❌ `range(grid)` → TypeError | ✅ |
| #210 | — | ✅ |
| #323 | — | ✅ 31:14 → **9:56, no prompt** |

**The same five problems, one day apart: 2/5 → 5/5.** `#133` is the proof — its first draft contained the *identical* Day-35 bug plus a `.children`-for-`.neighbors` slip. **He ran it, both surfaced, he fixed them and reported them.** Two sessions ago that arrives broken and costs a reset.

> **This retires the "correct algorithms that never executed" finding from Days 34–35** — one clean session, keep watching.

**And the scheduling judgment was his.** At the 30-minute mark with two items left he asked to break and finish rather than defer, **because he did Monday's arithmetic himself** (3 new DP problems + 2 full solves = 10 items, 39.5 min, 30% over). Real break, defined twelve minutes, 5/5. **That's what the hard box exists to teach — not obedience to a timer, but noticing when deferral costs more than finishing.**

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Did the function actually get CALLED? · What does the callee hand back, and where do I catch it? · Whose list/attribute is this — the original's or the copy's? · 🔴 What does ONE PASS of this loop cost, and is anything in it loop-invariant? · `range(len(x))` not `range(x)`? · Is there a better approach I'm skipping because it's fiddlier?**

## ⚠️ Standing schedule note
Depth phase (Heap ✓ → Backtracking 3/5 → Intervals ✓ 3/5 → **Graphs 3/5, six problems, all passing** → **1-D DP starts Mon Aug 3**). Rest was **Aug 2**; **Aug 9 and Aug 16 are worked**. **2 new/day stays and long sessions are accepted** (`COACHING.md` rule 17); Block 2 runs first on first-contact days. Reviews run the drain through **Aug 11** under a **30-min box measured in TIME** (full ≈ 6 min · one-draft ≈ 4, **6 if recursive** · verbal ≈ 0.5).

## 🟡 The slipped session is still owed
**Jul 29 had no session.** Days 37–53 is **17 sessions**; Aug 3 → Aug 19 is **17 available days.** **Zero buffer.** His call, logged Jul 30: he'll recover it. **The recovery is one triple-new day, and it still needs a date.**

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | **19** | 🟡 runway exists, slack does not |
| **Sprint throughput** (new/day) | Day 36 = mock day *(0–1 new by design)* | 🟢 on plan |
| **Schedule fit** (Days 37–53) | **17 sessions into 17 available days** | 🟡 **buffer owed** — needs a date |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Aug 3 = 8 (27 min) · Aug 4 = 8 (28 min) | 🟢 boxed on TIME |
| Review backlog carried | **all dated** through Aug 11 · re-spread Day 36 | 🟢 drain on track |
| **Open blockers** | **3 — B-10 (new), B-5 (1 clean), B-8** | 🟡 **B-9 cleared** |
| Review pass rate (Day 36) | **5 / 5** (100%) | 🟢 **three resets and two first retrievals, all passed** |
| **🎯 Unaided timed mediums** | **1 of 3 taken** — **19:38, correct, TLE** | 🟢 **first data point beats expectation** |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | **3/5** ↓ | `O(V+E)` cold Day 34, the space rule Day 35 — **but Mock #1 mis-priced a loop body into a TLE. B-10** |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| **Sliding Window** | **3/5** | **#567 added (Mock #1)** — fixed-size window; when it slides, only TWO characters change |
| Binary Search | 3/5 | #74 clean Day 35 — the two-template distinction held |
| Stack | 3/5 | #155 → 21d |
| Linked List | 4/5 | #143 clean, LRU rebuilt cold |
| Trees & BFS/DFS | 3/5 | #110 box clean |
| Binary Search Tree | 4/5 | stable |
| Tries | 3/5 | #211 clean Day 30 |
| Heap | 3/5 | #973/#215 clean |
| **Backtracking** | **3/5** | **#46 clean Day 36** after two wiring resets. #90 first-draft correct Day 34 |
| **Intervals** | **3/5** | Four problems clean. 4/5 needs a novel one cold (#253) |
| **Graphs (BFS/DFS)** | **3/5** | **Six problems, all six now passing.** #133 finally clean on the 4th attempt; #323 went 31:14 → 9:56 in one day |
| **Greedy** *(previewed)* | **1/5** | Named block Aug 9–11 |
| **1-D DP** | **0/5** | **Starts Mon Aug 3 — three problems, first contact** |

## Blockers

- **⛔ B-10 · M-006 — price the loop body. OPENED Day 36.** Third occurrence, first with a measured cost (a TLE). Drill: *"one pass of this loop costs ___"* before stating any complexity, and **nothing loop-invariant inside a loop.**
- **🟡 B-5 · M-036 — container vs contents. 1 clean session.** `#133` passed on the fourth attempt. Needs one more — and he still wrote `graph[node].neighbors` instead of using the name `clone`.
- **⛔ B-8 · M-029 — naming precision.** A `.children`-for-`.neighbors` slip on `#133`'s first draft, self-caught by running.
- **✅ B-9 · M-001 — the recursive return channel. CLEARED Day 36** after two clean sessions. The drill stays a standing habit.
- **M-040 (skipped the better approach) · M-039 · M-034 · M-037 · M-038 · B-2 · M-027 · M-005** — 👁 watch.

*(Cleared → standing habits: B-1 names, B-3 return, B-4 guards, B-6 target-first, B-7 `self.`/ownership, **B-9 recursive return**, M-025 pointer surgery.)*

## Next Session Focus  → **Day 37 (Mon Aug 3)** · **1-D DP, FIRST CONTACT** ⇒ Block 2 runs FIRST

1. **Block 2 — new:** **#70 Climbing Stairs, #746 Min Cost Climbing Stairs and #198 House Robber** — an entirely new pattern *and* three new problems, which makes it the heaviest teaching day of the sprint. Budget the pre-teach generously and expect it to run long; that is the accepted trade under rule 17.
2. **Block 1 — 8 items, ~27 min:** full **#567** — write the `O(n)` rolling-count version, the mock's TLE fix → ✍️ **#200 · #79 · #39 · #57** → 🗣 **#739 · #121 · #153**.
3. **⛔ B-10, every complexity statement:** *"one pass of this loop costs ___."* And check nothing loop-invariant sits inside a loop.
4. **⛔ M-040:** when a better approach occurs to you, **say it and write it.** "More complicated" is not a reason.
5. **⛔ B-5 on `#133`:** use the name `clone`. One more clean pass closes it.
6. **Run everything before sending.** Measured on the same five problems one day apart: 2/5 → 5/5.
7. **The slipped session still needs a date.**

---
*Weekly snapshots can be appended below as the sprint progresses.*
