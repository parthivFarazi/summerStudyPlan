# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-31 (Day 35 logged) · **Three correct algorithms that never ran · B-5 reopened · Mock #1 tomorrow**
- **Phase:** Summer Sprint · Block B — *Graphs 3/5 (six problems), DP starts Aug 3. **Block 2 halved its time — 48 minutes for two new problems against 116 the day before.** Block 1 went 2/5, and **all three failures were correct algorithms that never executed**: the wrong object's list, a function never invoked, and `range()` of a list. **The gap between his solve rate and his pass rate is one execution.** Aug 9 and Aug 16 are working days.*
- **Sessions logged:** 35 · **Patterns learned:** 14 · **Mistakes tracked:** 39 · **Open blockers:** 3 (**B-5 container/contents — reopened**, **B-9 recursive return channel — held once**, B-8 naming — quiet) + watches (B-2 reopened, M-039, M-034, M-037, M-038, M-027, M-005)
- **Review queue:** **Day 36 (Sat Aug 1) — 🎯 MOCK #1 first, then 5 full solves, 30 min:** #133 · #46 · #994 (resets) · #210 · #323 (1d). **Nothing else** — five full solves *is* the box. Drain re-spread on real dates through **Aug 9**; every day Aug 1 – Aug 9 sits at 20–30 min.

## 🎯 Tomorrow is Mock #1 *(Sat Aug 1)*

**The first unaided data point in 35 sessions.** Unseen medium from an already-learned pattern · **35-minute hard cap** · **the coach says nothing until the timer stops** · narrate throughout · then self-score communication / problem-solving / technical correctness / testing.

> **Expected result: over 35 minutes. That is information, not failure.** One data point is noise; **three is a trend** (Aug 1 · Aug 8 · ~Aug 14). The risk was never a bad number in August — it was reaching September without ever having taken the reading.

**It replaces Block 2 and runs first, while he's fresh.** Total session ≈ 65 min — shorter than the last three days.

## 🔴 The honest read — Day 35

**Block 1 was 2/5, and the three failures line up exactly as they did yesterday:**

```
#133   for neighbor in adict[node].neighbors    walked the wrong object's list
#46    (backtrack never invoked)                the function was never called
#994   for r in range(grid)                     range() of a list -> TypeError
```

> **Not one is an algorithm.** `#994` with `len()` added and nothing else: every 6-cell grid and 20,000 random grids pass. `#46` with one `backtrack()` line: every permutation correct. `#133`'s structure was right, `None` guard included. **All three crash or return empty on the FIRST example.**

**🟢 And the counter-evidence sits in the same block.** `#207` passed first-draft **on exactly the line that reset it the day before** — because he said the B-9 sentence before writing. `#74` passed on exactly the condition that reset it. **When the check gets run, it works. The problem isn't knowing what to check.**

**⛔ B-5 reopened — `#133` has failed three sessions on one ambiguity.** Day 33 and 34: `Node(node.val, node.neighbors)`. Day 35: `for neighbor in adict[node].neighbors`. **Every failure is the same question — *which `neighbors` list?* — and on Day 35 his notes were open and he still mis-picked**, which rules out recall.

> **The fix is mechanical, not attentional: name the clone.** `clone = Node(node.val, [])` … `for neighbor in node.neighbors: clone.neighbors.append(dfs(neighbor))`. **When two things are easy to confuse, change the names rather than trying harder.**

**🟢 Block 2 is where the real progress is.** **17:21 and 31:14 — 48 minutes against 116 the day before.** He derived post-order-then-reverse himself (*"when we add to visited, we add it to a list and then return the reverse"*), transferred `#323` from `#200` himself, and made two judgment calls unprompted: **he did not carry `path` into an undirected problem**, and **he wrote a `dfs` that returns nothing** — correct, because the counting happens outside it.

> **Two rules banked today, both general:** **an early EXIT lives inside the loop; a CONCLUSION lives after it** (`#210`'s bug — 2,103 of 5,000 random inputs failed, every one a multi-component graph). And **count the space YOU allocate, not the space the input arrived in** — a dict's space is not its key count; `{0: [a million ints]}` has one key and is not `O(1)`.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Every branch returns? · 🔴 What does the callee hand back, and where do I catch it? · 🔴 Whose list/attribute is this — the original's or the copy's? · Did the function actually get CALLED? · `range(len(x))` not `range(x)`? · All args passed? · Which side can contain the answer?**

## ⚠️ Standing schedule note
Depth phase (Heap ✓ → Backtracking 3/5 → Intervals ✓ 3/5 → **Graphs 3/5, six problems** → **DP starts Aug 3**). Rest is **Aug 2**; **Aug 9 and Aug 16 are worked**. **2 new/day stays and long sessions are accepted** (`COACHING.md` rule 17); Block 2 runs first on first-contact days and Block 1 is never dropped. Reviews run the drain through **Aug 9** under a **hard 30-min box measured in TIME** (full ≈ 6 min · one-draft ≈ 4, **6 if recursive** · verbal ≈ 0.5).

## 🟡 The slipped session is still owed
**Jul 29 had no session.** Days 36–53 is **18 sessions**; Aug 1 → Aug 19 minus the Aug 2 rest is **18 available days.** **Zero buffer.** His call, logged Jul 30: he'll recover it. **The recovery is one triple-new day or a worked Aug 2, and it needs a date.**

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | **20** | 🟡 runway exists, slack does not |
| **Sprint throughput** (new/day) | Day 35 = **2** (#210, #323) | 🟢 on plan — hits the floor |
| **Schedule fit** (Days 36–53) | **18 sessions into 18 available days** | 🟡 **buffer owed** — needs a date |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Aug 1 = **5** (30 min + mock) · Aug 3 = 8 (27 min) | 🟢 boxed on TIME |
| Review backlog carried | **all dated** through Aug 9 · re-spread Day 35 | 🟢 drain on track |
| **Open blockers** | **3 — B-5 (reopened), B-9 (held once), B-8 (quiet)** | 🔴 B-5 drill now |
| Review pass rate (Day 35) | **2 / 5** (40%) | 🔴 **all three failures were correct algorithms that never executed** |
| **Time on new problems** | **17:21 · 31:14** (48 min total) | 🟢 **halved** — 116 min the day before |
| **🎯 Unaided timed mediums** | **0 taken** · **Mock #1 tomorrow** | 🔴 the only gate genuinely off-track |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | `O(V+E)` cold Day 34. **Day 35: "count the space YOU allocate" — a dict's space is not its key count** |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| Sliding Window | 3/5 | solid |
| **Binary Search** | **3/5** | **#74 clean Day 35 (4:26)** — the two-template distinction held first-draft after resetting on it |
| Stack | 3/5 | #155 → 21d |
| Linked List | 4/5 | #143 clean, LRU rebuilt cold |
| Trees & BFS/DFS | 3/5 | #110 box clean |
| Binary Search Tree | 4/5 | stable |
| Tries | 3/5 | #211 clean Day 30 |
| Heap | 3/5 | #973/#215 clean |
| **Backtracking** | **3/5** | #90 first-draft correct Day 34. **#46 reset ×2 — never the algorithm, twice the wiring** (base case, then the missing call) |
| **Intervals** | **3/5** | Four problems clean. 4/5 needs a novel one cold (#253) |
| **Graphs (BFS/DFS)** | **3/5** ↑ | **Six problems.** #210 (topological sort) and #323 both derived largely unaided, **48 min for the pair**. #133 still failing on a naming ambiguity, not on the algorithm |
| **Greedy** *(previewed)* | **1/5** | Named block Aug 6–10 |

## 🔴 Three open blockers

- **⛔ B-5 · M-036 — container vs contents. REOPENED Day 35.** `#133` three sessions running on *which `neighbors` list*, notes open on the third. **Fix is mechanical: name the clone.** Cleared when #133 passes twice consecutively.
- **⛔ B-9 · M-001 — the recursive return channel.** ✅ **HELD Day 35** on `#207` — 1 clean session, clears after 1 more. Drill: *"the callee hands me back ___, and I catch it at ___."*
- **⛔ B-8 · M-029 — naming precision.** Quiet Day 35. Rescoped Day 34 to names visible in front of him.
- **👁 B-2 (`range(len(x))`) reopened** — `range(grid)` on `#994`, first slip since Day 18. Watch, not a re-escalation.
- **M-039 (a function defined and never invoked) · M-034 · M-037 · M-038 · M-027 · M-005** — 👁 watch.

*(Cleared → standing habits: B-1 names, B-3 return, B-4 guards, B-6 target-first, B-7 `self.`/ownership, M-025 pointer surgery.)*

## Next Session Focus  → **Day 36 (Sat Aug 1)** · 🎯 **MOCK #1 runs FIRST**

1. **Block 2 — new:** **🎯 MOCK #1 replaces new material today.** Unseen problem from a pattern already learned, **35-minute hard cap**, the coach silent until the timer stops, narrate throughout, then self-score the four dimensions. **Say in advance that going over 35 minutes is the expected result.**
2. **Block 1 — 5 full solves, 30 min, nothing else:** **#133 · #46 · #994** (resets) → **#210 · #323** (1d).
3. **⛔ B-5 drill on `#133` — name the clone.** `clone = Node(node.val, [])`, then `for neighbor in node.neighbors: clone.neighbors.append(dfs(neighbor))`.
4. **⛔ B-9 sentence before every recursive function**, and it's what saved `#207` today.
5. **⛔ Run every solve before sending.** Three of yesterday's five failures die to a single execution — that is the entire gap between the score and the understanding.
6. **The slipped session still needs a date.** One triple-new day, or work Aug 2.

---
*Weekly snapshots can be appended below as the sprint progresses.*
