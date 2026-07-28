# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-28 (Day 33 logged) · **Graphs learned · Block 1 5/5 · one new blocker**
- **Phase:** Summer Sprint · Block B — *Depth phase — **Graphs learned (2/5)**, Intervals held at 3/5, Backtracking answered on second retrieval. **Block 1 went 5/5 in 26:55, all full solves** — every Day-32 named cause held first-draft, so M-034 (the scan) is answered for one session. **The two live problems are the clock on new material (44 and 45 min) and B-8, naming precision.** Aug 9 + Aug 16 are working days, closing the deficit against Aug 20.*
- **Sessions logged:** 33 · **Patterns learned:** 14 · **Mistakes tracked:** 36 · **Open blockers:** 1 (**B-8 naming precision — ESCALATED Day 33**) + watches (M-036, M-027, M-026, M-033, M-034, M-030, M-032, B-4, M-005, M-028)
- **Review queue:** **Day 34 (Wed Jul 29) — 7 items, ~25 min:** full **#200 · #133** (yesterday's new) · ✍️ **#90 · #46 · #78** · 🗣 **#155 · #74**. Backlog re-fuzzed after Day 33 and still lands on real dates through **Aug 7**; every day Jul 29 – Aug 7 sits at 6–8 items and 25–29 min.

## 🔴 The schedule, honestly *(rebuilt 2026-07-25 · re-checked Day 33)*

**The fix, agreed 2026-07-25:** work Sundays. **Day 31 moved onto Sun Jul 26** (recovered 1), and **Aug 9 + Aug 16 became working days** (recovered 2). Aug 2 stays rest.

**Arithmetic re-run on Day 33** *(rule 10 — do it every time the schedule moves)*: **Day 34 → Day 53 is 20 sessions**; Jul 29 → Aug 19 is **22 days minus Sunday Aug 2 = 21 available**. **20 into 21 — the buffer is still exactly one day (Aug 19).** One slip eats it. **If a session slips, the recovery is a triple-new day — not a shrug.**

**The queue's hidden pile is still cleared.** All items sit on concrete dates across **Jul 29 – Aug 7**, re-fuzzed after Day 33's five passes: the five advanced items took their true 3d date (Jul 31 / Aug 1) and the **stable** items absorbed the shuffle (#543 → Aug 6, #146 → Aug 4, #242 → Aug 7, #153 → Aug 1, #206 → Aug 3, #128 → Aug 5), batched onto days already holding their pattern. *(Standing rule: a roll-forward must land on a concrete date — `COACHING.md` rule 10.)*

## 🟢 The honest read — Day 33

**Block 1 went 5 for 5 in 26:55, on the most expensive possible load — five full solves — and finished inside the box with three minutes spare.** First time the 30-minute box has held on an all-full-solve day.

> **The finding: yesterday three of four full solves failed. Today five of five passed, and every one was a fix to the exact thing that broke.** #79's mark/un-mark idiom written cold (he peeked at notes for it yesterday) · #39's prune the right way round (M-033) · #57's post-loop terminal append present (M-026, on the problem whose own comment had named the flag) · #435 comparing against the interval it **kept**, not the one physically next to it.

**🟢 M-034 is answered — for one session.** Day 32's diagnosis was that the checklist was complete and the *execution* of it was the gap. Day 33 is the counter-evidence: **when he walks the scan against the code, the code is right.** That is now demonstrated rather than asserted. Keep it on watch — one session is not a habit.

**Graphs landed, and the framing did the work.** Taught as **implicit vs explicit** — the traversal is identical, the only variable is where neighbours come from (computed from `(r±1, c)` vs stored in `node.neighbors`). He already owned grid DFS from #79, so graphs added a *neighbour source*, not a new algorithm.

**#200 was the best reasoning of the session.** He derived the approach unprompted — *"the word-search DFS, but mark permanently instead of temporarily"* — and then explained the complexity himself: *"the reason `4^L` is not considered is because you can only work with a node once."* **Generalised for him: backtracking explores PATHS (exponential); graph traversal visits NODES (linear). The un-mark is the entire difference.**

**He insisted on a real explanation of `O(V + E)` instead of nodding along** — three times, correctly. Built `viz/graph-edges-and-traversal.html`, and he then produced the key fact himself: ***"if there are E edges, it will always be 2E entries."***

**He also pushed back on the wrong question order and was right.** *"I can't really give you a time and space complexity until I actually have an idea about the way I want to go about the solution first."* Now `COACHING.md` rule 3: **reviews = complexity first; new material = approach → complexity → code. Invariant: complexity before any code.**

## 🔴 The two problems, stated plainly

**1. Ninety minutes for two new problems** — 44:14 and 45:28. Both correct, both brand-new material, patterns derived unaided. But **readiness is measured in minutes on unseen problems, and a FAANG medium is ~20–25.** From Day 34 this is a tracked metric, not a note. *(The stopwatch itself finally ran, after three sessions of missing it — that part is fixed.)*

**2. ⛔ B-8 opened — naming precision.** `for neighbor in node.neighbor:` on #133, with `self.neighbors` written **three lines above** in the class definition. **The algorithm was correct at submission two; the typo cost the third submission.** Six consecutive sessions of slightly-wrong names — and Day 33 is the one where it stopped being narration and started breaking code. Escalated per the standing ≥3 rule.

> **⛔ Standing rule installed Day 33: a full solve handed over WITHOUT being executed is a FAIL on the spot.** No partial credit for "the algorithm was right." Running it costs 20 seconds; not running it costs the interview.

## The one scan (say it OUT LOUD before every submit)
**Guard present? · Terminal line/mark written? · Every branch returns? · All args passed? · Whose thing is every attribute/method? · Multi-site change complete & every name real? · Un-negate on the way out? · Which side can contain the answer (target-first)?**

## ⚠️ Standing schedule note
Core complete; depth phase (Heap ✓ → **Backtracking (3/5)** → **Intervals ✓ (3/5, incl. greedy)** → **Graphs (2/5 — learned Day 33)** → DP Aug 1). **Sun Jul 26 worked as Day 31.** Rest is **Aug 2**; **Aug 9 and Aug 16 are worked**; **Aug 19 is the buffer**. Full mapping in `plan/Day-by-Day-Roadmap.md` → *Recovered calendar*. Reviews run the **backlog drain** (QUEUE) through **Aug 7** under a **hard 30-min box measured in TIME, not item count** (full ≈ 6 min · one-draft ≈ 4 · verbal ≈ 0.5). Graph and DP days get light reviews and **run Block 2 first**.

## Pace Health
| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 23 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 33 = **2** (#200, #133) | 🟢 on plan — hits the floor |
| **Schedule fit** (Days 34–53) | 20 sessions into **21** available days | 🟡 fits — **1-day buffer only** (Aug 19) |
| Sessions last 7 days (target ≥ 6) | 7 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 sessions) | Jul 29 = 7 (25 min) · Jul 30 = 7 (25 min) | 🟢 boxed on TIME, not count |
| Review backlog carried | **all dated** through Aug 7 · re-fuzzed Day 33 | 🟢 drain on track |
| **Open blockers** | **1 — B-8 naming precision** | 🔴 **drill now** (escalated Day 33) |
| Review pass rate (Day 33) | **5 / 5** (100%) | 🟢 **all five were FULL solves, 26:55, inside the box** — every Day-32 named cause held first-draft |
| **Time on new problems** | **44:14 · 45:28** | 🔴 **the number to watch** — target ~20–25 min for a medium |
| **Expected Block 1 load** | **~7/session** (≈3.5 full + 1.4 ✍️ + 2.2 🗣) | 🟢 **hard 30-min box** · matches the agreed 6–8 |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 4/5 | O(n·2ⁿ), O(n·n!), O(T/M) derived; **`O(V+E)` Day 33 — needed animating, then he produced the `2E` fact himself** |
| Arrays & Hashing | 3/5 | stable |
| Two Pointers | 3/5 | stable |
| Sliding Window | 3/5 | solid |
| Binary Search | 3/5 | stable |
| Stack | 3/5 | stable |
| Linked List | 4/5 | #143 clean, LRU rebuilt cold |
| Trees & BFS/DFS | 3/5 | #110 box clean; #199 fixed (enqueue direction) Day 30 |
| Binary Search Tree | 4/5 | stable; B-6 cleared |
| Tries | 3/5 | #211 clean Day 30 — all Day-29 facets fixed, ownership held |
| Heap | 3/5 | #973/#215 clean; #1046 fixed Day 30 (un-negate landed) |
| **Backtracking** | **3/5** | **Second retrieval landed: #79 (6:22) and #39 (7:24) both clean Day 33 after failing their first-ever review. Reading stands — solid on rehearsed, fragile on first retrieval; the fix is the second rep** |
| **Intervals** | **3/5** | **All four clean Day 33 (#57 6:06 · #435 4:50 · #252 2:13). Held at 3/5 on purpose — those are the four he was TAUGHT; 4/5 needs a novel one cold (#253 is the test)** |
| **Graphs (BFS/DFS)** | **2/5** *(new)* | **Day 33 — #200, #133 both correct but 44 and 45 min. Implicit vs explicit; permanent mark ⇒ `O(m·n)` not `4^L`; dict = visited AND mapping; `O(V+E)` with 2E entries undirected** |
| **Greedy** *(previewed)* | **1/5** | Met early via #435/#252. Named block arrives Aug 6–10 (#53/#55/#134/#763) |

## 🔴 One open blocker

- **⛔ B-8 · M-029 — naming precision. ESCALATED Day 33 (drill now).** Six sessions: constructs misnamed (Day 31), **four method names renamed** (Day 32), **`node.neighbor` for `node.neighbors` on #133 (Day 33) — the one that broke working code.** Drill: read the method name off the problem statement · read attribute names off the class definition, don't recall them · name each construct correctly out loud. Cleared after two clean sessions.
- **M-036 (a copy built from the original's fields)** — 👁 NEW Day 33. `Node(node.val, node.neighbors)` handed the clone the originals. **Container-vs-contents (M-021) at object scale.**
- **M-034 (scan said but not run)** — 👁 **HELD Day 33** (5/5, every named cause first-draft). One session is not a habit — keep watching.
- **M-026 (terminal line) · M-033 (reversed prune)** — 👁 both **HELD Day 33** on the exact problems that fired them (#57, #39).
- **M-027 (one site missed on the final pass)** — 👁 the through-line; the one *repeat* closed Day 30.
- **M-030 (confirm-seeking) · M-032 (a sort costs space)** — 👁 both improving; **M-032 was stated unprompted on #252.**
- **B-4 (guards), M-005 (BFS space), M-028 (box)** — 👁 all held recently; watch.

*(Cleared → standing habits: B-1 names, B-2 range/len, B-3 return, B-4 guards, B-5 container/contents, **B-6 target-first**, **B-7 `self.`/ownership**, M-025 pointer surgery.)*

## Next Session Focus  → **Day 34 (Wed Jul 29)** · Graphs, HEAVY ⇒ **Block 2 runs FIRST**

1. **Block 2 — new:** **Graphs cont. — #994 Rotting Oranges, #207 Course Schedule** — and it runs **FIRST, while fresh.** #994 is the first problem where **BFS is required rather than optional** (level = elapsed time, which DFS cannot give you); #207 is cycle detection in a **directed** graph — the first time the 1-entry-per-edge asymmetry actually matters.
2. **Warm-up, cold and no notes: `O(V + E)`** — what V is, what E is, why it's `+` and not `·`, and **how many adjacency entries a 6-edge undirected graph holds vs a 6-edge directed one.** Banked from Day 33 deliberately rather than drilled at the end of a long session.
3. **Block 1 — 7 items, ~25 min:** full **#200 · #133** → ✍️ one-draft **#90 · #46 · #78** → 🗣 verbal **#155 · #74**.
4. **⛔ B-8 drill, at the top of the session and before every submit:** read the method name off the problem statement · read attribute names off the class definition · name the construct you just wrote, correctly, out loud.
5. **⛔ Live from today: a full solve handed over without being executed is a FAIL.** Write it, run it, debug it — no partial credit for "the algorithm was right."
6. **Watch the clock on the new problems.** 44 and 45 minutes yesterday. Target ~20–25 for a medium; say the number out loud when the timer stops.

---
*Weekly snapshots can be appended below as the sprint progresses.*
