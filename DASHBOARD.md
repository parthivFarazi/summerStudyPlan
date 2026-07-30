# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-30 (Day 34 logged) · **Four failures, one disease · B-9 opened · mocks scheduled**
- **Phase:** Summer Sprint · Block B — *Graphs 2/5, DP starts Aug 1. Block 1 went **3/6** and **all four failures were the same disease: the exact identity of the value in front of him** — two discarded recursive returns, a list compared to an int, and the wrong template's exit condition. **Not one was a comprehension gap.** #994 multi-source BFS and #207 cycle detection both built correctly but at 72 and 44 minutes. Aug 9 + Aug 16 are working days.*
- **Sessions logged:** 34 · **Patterns learned:** 14 · **Mistakes tracked:** 38 · **Open blockers:** 2 (**B-9 recursive return channel — priority**, B-8 naming precision — rescoped) + watches (M-036 ×2, M-034, M-037, M-038, M-027, M-026, M-033, M-030, M-032, B-4, M-005)
- **Review queue:** **Day 35 (Fri Jul 31) — 5 items, 30 min, all full solves:** #133 · #46 · #74 (resets) · #994 · #207 (1d). **Deliberately nothing else** — five full solves *is* the box. Drain re-spread on real dates and now runs to **Aug 9**; every day Jul 31 – Aug 9 sits at 16–30 min.

## 🔴 A SESSION SLIPPED — the buffer is spent *(2026-07-30)*

**Day 33 ran Thu Jul 28. There was no session on Jul 29. Day 34 ran Fri Jul 30.** Every review date has been shifted one day.

**The arithmetic, re-run** *(rule 10 — do it every time the schedule moves)*: Days 35–53 is **19 sessions**. Jul 31 → Aug 19 is 20 calendar days minus the Aug 2 rest = **19 available.** **19 into 19. The one-day Aug 19 buffer is gone.**

**Two ways back to a buffer — his call:**

1. **One triple-new day** — 3 new problems in a single session. This is the standing recovery rule agreed on Jul 25.
2. **Work Sunday Aug 2** — the last rest day left in the sprint.

> **Until one of those happens, a single further slip puts Day 53 past Aug 20.** This is not a reason to panic; it is a reason to pick one of the two this week rather than next.

> **His call, 2026-07-30:** *"I will be able to catch up with the new schedule — I'm just a day behind right now, I'll catch up and still have the Aug 19 buffer."* **Accepted.** The recovery is one extra session's worth of new material somewhere in the next two weeks — a triple-new day or a worked Aug 2. **Track it as OWED until a specific day carries it, then mark that day here.** Not a crisis; just a debt that needs a date on it, same as any roll-forward *(rule 10)*.

## 🎯 The gate that was never measured — now scheduled *(new, Day 34)*

**`GOALS.md` requires: 4 of 5 unseen Mediums in ≤ 35 min, unaided. After 34 sessions there are ZERO unaided data points.** Every new problem has had a pre-teach. Times *with* help: 44:14 · 45:28 · 72:18 · 43:52. Review times (seen, unaided) are strong — 2:13 · 4:50 · 6:22 · 7:17 — but those measure retention, not this.

**Fixed at zero throughput cost — his proposal, better than mine: unaided timed mediums on the interleave days, which carry 0–1 new by design.**

| | date |
|---|---|
| **🎯 Mock #1** | **Sat Aug 1** |
| **🎯 Mock #2** | **Sat Aug 8** |
| **🎯 Mock #3** | **~Fri Aug 14** |

**Protocol:** unseen problem from an already-learned pattern · **35-min hard cap** · **the coach says nothing until the timer stops** · narrate throughout · self-score communication / problem-solving / technical correctness / testing.

> **The first one probably goes over 35 minutes. That is information, not failure.** One data point is noise; three is a trend. The risk was never a bad number in July — it was reaching September without ever having taken the reading.

## 🔴 The honest read — Day 34

**Block 1 was 3/6, and the four failures line up too neatly to be coincidence:**

```
#207   dfs(child)              answer computed, discarded
#133   dfs(neighbor)           answer computed, discarded
#46    combo == len(nums)      a list compared to an int
#74    while left < right      the wrong template's exit condition
```

> **Four problems, four failures, ONE disease: the exact identity of the value in front of him.** He explained the two-mark idea for `#207` unaided and named `path` as backtracking himself. **Not one failure was comprehension.** This is the narrowest diagnosis this project has produced.

**⛔ B-9 opened — the recursive return channel.** M-001 fired **twice in one session, two hours apart**. He would never drop a return value in ordinary code; it only happens across a recursive boundary, where it feels like the callee *does something to shared state* rather than *hands back an answer you must catch*. Drill: ***"the callee hands me back ___, and I catch it at ___"*** before writing any recursive function.

**🔴 #133 failed with yesterday's two bugs, identical — and the mechanism matters more than the failure.** `#133` is the one problem he **never wrote correctly himself**: on Day 33 I gave him the fix and he applied it. Everything he *fought* for on Day 34 — the DFS-can't-measure-time counter-example, the off-by-one, the two marks — survived intact. **A correction you are handed decays far faster than one you derive.** Now `COACHING.md` rule 15: give the counter-example, never the correction.

**🟢 The teaching landed where he fought for it.** He spotted `#994`'s multi-source problem before writing a line, derived the seeding himself from *"what's in the deque before the first `popleft`?"*, and produced the `#207` cycle criterion after one killed guess: ***"the first `dfs(0)` has not returned yet, whereas `dfs(3)` had."*** Then named `path`'s add/remove shape as **backtracking** unprompted.

> **The idea of the week, and it's now in three pattern files:** graph traversal and backtracking are **not two patterns** — they are the **permanent mark** and the **temporary mark**. Un-mark ⇒ explore *paths* ⇒ exponential (#79). Never un-mark ⇒ visit *nodes* ⇒ linear (#200). **#207 needs one of each.** Measured: 55 nodes, 72 edges → **127 calls with `visited`, 4,194,163 without.**

**🟢 The warm-up worked.** `O(V + E)` cold, no notes, in under a minute — the thing that needed an animation the day before. Banking it instead of grinding it at the end of a long session was right.

**🔴 M-034 fired twice.** Asked to trace his own DFS he simulated the *correct process*; asked what his counter ends at he asserted *"it does give 3"* (it gives 4). He objected that he had no code to run — **half fair, and that half was mine.** The point that stands is narrower: **he stated a result he had not derived.** *"I haven't checked"* costs nothing.

**🟢 And two things worth as much as any solve:** he said *"I pretty much just copied this and can't visualise it"* when he could have stayed quiet — which is what got `viz/dfs-cycle-detection-stepper.html` built — and he **measured** his one-draft overrun (*"at 4:00 I was at `combo.append(nums[i])`"*) instead of complaining, which changed the rule.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Every branch returns? · 🔴 What does the callee hand back, and where do I catch it? · All args passed? · Whose thing is every attribute/method? · Multi-site change complete & every name real? · Which side can contain the answer (target-first)?**

## ⚠️ Standing schedule note
Depth phase (Heap ✓ → Backtracking 3/5 → Intervals ✓ 3/5 → **Graphs 2/5** → **DP starts Aug 1**). Rest is **Aug 2** *(and it is now the only recoverable slack)*; **Aug 9 and Aug 16 are worked**; **Aug 19 is the buffer**. **2 new/day stays and long sessions are accepted — his call, Day 34** (`COACHING.md` rule 17); consequence: **Block 2 runs first on first-contact days and Block 1 is never dropped.** Reviews run the drain (QUEUE) through **Aug 8** under a **hard 30-min box measured in TIME** (full ≈ 6 min · one-draft ≈ 4, **6 if recursive** · verbal ≈ 0.5).

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | **21** | 🟡 runway exists, slack does not |
| **Sprint throughput** (new/day) | Day 34 = **2** (#994, #207) | 🟢 on plan — hits the floor |
| **Schedule fit** (Days 35–53) | **19 sessions into 19 available days** | 🟡 **buffer owed** — Jul 29 slipped; he's committed to recovering it. Needs a date |
| Sessions last 7 days (target ≥ 6) | 7 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Jul 31 = **5** (30 min) · Aug 1 = 5 (19 min + 🎯 mock) | 🟢 boxed on TIME |
| Review backlog carried | **all dated** through Aug 9 · re-spread Day 34 | 🟢 drain on track |
| **Open blockers** | **2 — B-9 (priority), B-8 (rescoped)** | 🔴 **B-9 drill now** |
| Review pass rate (Day 34) | **3 / 6** (50%) | 🟡 **all four failures were value-identity, none comprehension** |
| **Time on new problems** | **72:18** (22:24 unaided) · **43:52** | 🔴 the number to watch — target ~20–25 |
| **🎯 Unaided timed mediums** | **0 taken** · first on **Sat Aug 1** | 🔴 **the only gate genuinely off-track** |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | **`O(V+E)` cold on Day 34** — needed animating 24h earlier |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| Sliding Window | 3/5 | solid |
| **Binary Search** | **3/5** ↓ | **#74 reset Day 34 — mixed the two templates' parts.** `right = mid - 1` ⇒ `while left <= right`; `right = mid` ⇒ `while left < right`. Table now in `binary-search.md` |
| Stack | 3/5 | **#155 clean Day 34 → 21d** (the `<=` and the empty-guard) |
| Linked List | 4/5 | #143 clean, LRU rebuilt cold |
| Trees & BFS/DFS | 3/5 | #110 box clean; #199 fixed Day 30 |
| Binary Search Tree | 4/5 | stable; B-6 cleared |
| Tries | 3/5 | #211 clean Day 30 |
| Heap | 3/5 | #973/#215 clean; #1046 fixed Day 30 |
| **Backtracking** | **3/5** | **#90 first-draft correct Day 34 → 7d.** #46 reset on `combo == len(nums)` — one character, structure otherwise right. **New: it also appears INSIDE #207 as the `path` set** |
| **Intervals** | **3/5** | Four problems, all clean Day 33. 4/5 needs a novel one cold (#253) |
| **Graphs (BFS/DFS)** | **2/5** | **4 problems now.** #200 ✅ 7:17 · #133 ❌ twice · #994 and #207 built correctly but with heavy guidance. **The reps decide this number, not the acquisition** |
| **Greedy** *(previewed)* | **1/5** | Named block Aug 6–10 |

## 🔴 Two open blockers

- **⛔ B-9 · M-001 — the recursive return channel. OPENED Day 34 (priority).** `dfs(child)` on #207 and `dfs(neighbor)` on #133, both discarded, two hours apart. Drill: ***"the callee hands me back ___, and I catch it at ___."*** Cleared after two clean sessions.
- **⛔ B-8 · M-029 — naming precision. RESCOPED Day 34.** Three of Day 33's catches were **mine** — he writes in a bare IDLE and I wasn't supplying signatures on review prompts. **I now supply the exact signature every time** (rule 16). Scope is names **visible in front of him** and constructs misnamed in narration. Valid Day-34 instances: **1**.
- **M-036 (a copy built from the original's fields)** — 👁 **twice identical**, Day 33 → 34.
- **M-034 (checking the answer, not the code)** — 👁 fired twice Day 34 after holding Day 33.
- **M-037 (container compared to a number, B-5) · M-038 (binary-search templates mixed)** — 👁 both new Day 34.
- **M-027, M-026, M-033, M-030, M-032, B-4, M-005** — 👁 watch.

*(Cleared → standing habits: B-1 names, B-2 range/len, B-3 return, B-4 guards, B-5 container/contents, B-6 target-first, B-7 `self.`/ownership, M-025 pointer surgery.)*

## Next Session Focus  → **Day 35 (Fri Jul 31)** · Graphs, HEAVY ⇒ **Block 2 runs FIRST**

1. **Block 2 — new:** **#210 Course Schedule II and #323 Connected Components** — Kahn's algorithm (indegree + queue) produces the actual **order**, not just yes/no, which is the first time the answer is a sequence rather than a boolean; then union-find as the second way to ask about connectivity.
2. **Block 1 — 5 full solves, 30 min, nothing else:** **#133 · #46 · #74** (resets) → **#994 · #207** (1d). Five full solves *is* the box; everything else moved to real dates.
3. **⛔ B-9 drill, before every recursive function:** ***"the callee hands me back ___, and I catch it at ___."*** On #133: *"the callee hands me back the clone, and I catch it in `clone.neighbors`."* Plus the `None` guard.
4. **⛔ Rule 15 is live for me too:** when he gets something wrong, give the **counter-example**, never the correction. Day 33 proved the handed-over version doesn't survive the night.
5. **⛔ Rule 14 stands:** a full solve handed over without being executed is a FAIL.
6. **🎯 Sat Aug 1 is MOCK #1** — say so at the end of Day 35 so he arrives expecting it.

---
*Weekly snapshots can be appended below as the sprint progresses.*
