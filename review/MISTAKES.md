# Mistake Database

> Append-only registry of mistakes with root-cause analysis. Same root cause again ⇒ increment recurrence. **Recurrence ≥ 3 ⇒ escalate to `BLOCKERS.md`** (drill now). Mistakes are never deleted — they are data. Status: active / dormant (≥30d clean).

**Format:** `M-NNN | date | type | what happened | root cause | recurrence | sessions | status`
**Type:** `impl` (implementation/syntax) · `strategy` (wrong/unrecognized pattern, complexity, spec-reading).

## Mistakes

| ID | Date | Type | What happened | Root cause | Recur | Sessions | Status |
|---|---|---|---|---|---|---|---|
| M-001 | 2026-06-22 | impl | **Computed a value and didn't return / catch it.** Day 4/6; `return prev` #206 (19); `get` #146 (24); #211 both branches (26). **Day 34: TWICE IN ONE SESSION — `dfs(child)` on #207 and `dfs(neighbor)` on #133, both discarding the recursive return.** #207 then passed every True case and failed every False case; #133 never appended a single clone | Conflating *computing* a value with *returning* it — **and, in recursion, with *catching* what the callee hands back.** He would never drop a return value in ordinary code; it only happens across a recursive boundary | **7** | Day 4, 6, 19, 24, 26, **34 (×2)** | **⛔ ESCALATED → B-9 (Day 34) — drill now** |
| M-002 | 2026-06-24 | impl | `.append[x]` with brackets instead of `.append(x)` | Method **calls** use `()`; `[]` is indexing | 2 | Day 5, Day 8 | active |
| M-003 | 2026-06-19 | impl | `range(x)` / `len(range(x))` instead of `range(len(x))` when looping indexes | Scrambling the `range(len(x))` index-loop idiom | 3 | Day 1, Day 4, Day 16 | dormant (B-2 cleared Day 18) |
| M-004 | 2026-06-19 | impl | Wrong variable/container — `nums.add`/`seen.add`, `s`/`clean`, `strs`/`s` (#125), `nums`/`numbers` (#167), `appened`/`append` (#238), `self.stack`/`self.minStack` (#155) | Variable-name imprecision — losing track of which name holds what | 5 | Day 1, Day 9, Day 11, Day 12, Day 14 | dormant (B-1 cleared Day 16) |
| M-005 | 2026-06-24 | strategy | Called O(1)/O(h) for something O(n) — #125, #150, #15; #230 (Day 25). **Day 28: #199 called BFS space O(1) — the deque holds a whole level → O(n) (had it right on #102 the day before)** | A structure that scales with input = **O(n) space**. **BFS space = widest level = O(n)**; a bounded map (≤26) or the output does NOT count | 4 | Day 5, Day 17, Day 25, **Day 28** | active (self-corrects on nudge; watchlist) |
| M-006 | 2026-06-20 | strategy | Called Group Anagrams O(n) — missed the hidden `sorted()` | Not counting the cost of operations *inside* the loop | 2 | Day 3, Day 8 | active |
| M-007 | 2026-06-26 | strategy | Over-engineered sliding window (4 vars + time guards, buggy) | Not reducing to the **minimum necessary state** | 1 | Day 7 | active |
| M-008 | 2026-06-26 | strategy | Jumped to code; used `i`/`j`; skipped naming the approach | Coding before verbalizing the pattern | 1 | Day 6 | active |
| M-009 | 2026-06-28 | strategy | Imported `k log k` from Group Anagrams into Longest Substring (Day 8); **imported #21 Merge's VALUE comparison (`if curr1.val <= curr2.val`) into #143 Reorder, which forbids touching values (Day 23)** | Carrying a template's BODY across problems without re-deriving. Pattern recognition gives the skeleton, not the body — ask "what decides the next step IN THIS problem?" The spec tell: "may not modify values" ⇒ a value comparison is a red flag | 2 | Day 8, **Day 23** | active (watchlist) |
| M-010 | 2026-06-28 | strategy | Missed "alphanumeric only" in the spec = real work to do | Under-reading the problem statement / examples | 1 | Day 8 | active |
| M-011 | 2026-06-26 | impl | Dropped a required guard — anagram length (Days 7/20/22); empty-stack #20/#739; `node.left.val` (#226). Cleared Day 24. Day 26 #102 dropped both None-guards. **Day 28: #199 dropped the root-None guard (had it on #102 the day before) → None.val crash on empty tree** | Incomplete validation — keep the edge-case guard | 8 | Day 7, Day 18, Day 20, Day 21, Day 22, Day 26, **Day 28** | **B-4 watch (reopened Day 26, fired Day 28)** |
| M-012 | 2026-06-29 | strategy | Inverted search direction; #704 (Day 9); #33 (Day 13); #235 (Day 22); #235 again (Day 23). Day 24 CLEAN; **Day 27 CLEAN ✅ (rep 2, target-first; also transferred to #973 negated compare)** | Not re-deriving which side can still contain the target. **FIX: write the comparison TARGET-first** — `target > node → right`, `target < node → left` — nothing to mentally flip | 4 | Day 9, Day 13, Day 22, Day 23 | **B-6 CLEARED Day 27 ✅** |
| M-013 | 2026-06-30 | strategy | Returned on exact match (`hours == h`) in a find-minimum binary search → returned a non-minimal value | In boundary search an exact hit is still just a *candidate* — record it and keep shrinking | 1 | Day 10 | active |
| M-014 | 2026-07-01 | impl | Converging binary search with `while left <= right` + `right = mid` → infinite loop | `<=` never terminates when two pointers converge to one spot; use strict `<` | 1 | Day 11 | active |
| M-015 | 2026-07-02 | strategy | Converging binary search: tracked a separate `answer` instead of returning the convergence point → returned 0 on `[2,1]`/`[5]` (#153) and on Koko `h=5` when answer = max(piles) (#875) | In a converge-to-boundary search the loop-exit index IS the answer (`return left`); a tracked candidate/default leaks on edge cases | 2 | Day 12, Day 15 | active |
| M-016 | 2026-07-03 | impl | for/while mix-up: `for left <= right` (#704, Day 13); `while n in range(l)` (#271, Day 18) | Pick the loop keyword: `for x in iterable` to iterate; `while cond` for a condition | 2 | Day 13, Day 18 | active |
| M-017 | 2026-07-06 | strategy | Converging find-min used `right = mid - 1` (discarded the candidate min) instead of `right = mid` → failed `[3,1,2]` | On the keep-candidate side of a converging search, `mid` might BE the answer — move `right = mid`, never `mid - 1` | 1 | Day 15 | active |
| M-018 | 2026-07-08 | strategy | Wrote a bare `if/elif` where the whole thing is a LOOP — 3Sum omitted the `while left < right` wrapper so the two-pointer never swept (Day 17); **#235 LCA reassigned `node = node.left` then fell off the bottom of the function → returned `None` (Day 22)** | A scan / a descent / a skip is a **LOOP**, not a single check. Moving a pointer once is not traversing | 2 | Day 17, **Day 22** | active (watchlist) |
| M-019 | 2026-07-10 | impl | Koko search used `left = 0` (min speed is 1) → `mid=0` → `math.ceil(p/0)` division by zero on `[1]` | Respect the valid LOWER bound of an answer-search range (eating speed ≥ 1) | 1 | Day 19 | active |
| M-020 | 2026-07-10 | impl | `self.` / attribute-ownership. #155/#226/#146 (Days 19–24), cleared Day 25–26. RECURRED Day 27 (#211) + Day 28 (#146). **Day 29 HELD (1 clean); Day 30 HELD (#211 ownership + micro-drill both clean) → 2nd clean** | The ONE test (`python-classes.md`): attached via `self.x=` OR a method of this class → `self.`; a field → `object.field`; parameter/local → bare. **Every attribute needs its owner named** | 5 | Day 19, Day 21, Day 24, Day 27, Day 28 | **B-7 CLEARED Day 30 ✅ (2 clean) → standing habit** |
| M-021 | 2026-07-13 | impl | **Container vs. contents** — index vs. `"#"` instead of `s[j]` (#271, Day 21); `.val` vs the `.left`/`.right` pointers (#226, Day 21); #271 AGAIN (Day 22); `left`/`right` heights to count nodes (Day 22). Cleared Day 24. **Day 25: RECURRED — #226 swapped LOCAL `left`/`right` instead of `node.left`/`node.right` (mutating a local ≠ mutating the object's field)** | Reaching for the handle instead of the thing it points at. **And: assigning to a local does NOT change the object's attribute** | 5 | Day 21 (×2), Day 22 (×2), **Day 25** | **B-5 watch REOPENED (Day 25) — see M-025** |
| M-022 | 2026-07-13 | impl | 3Sum dedup used `if nums[left] == nums[left+1]` instead of `while` → skipped only ONE duplicate, not a run of them | Skipping a **run** of equal values is a LOOP, not a single check | 1 | Day 21 | dormant (clean Day 22 ✅) |
| M-023 | 2026-07-14 | strategy | **Stated the algorithm in the wrong ORDER out loud** — verbal recall of #1/#217 as "add it to the set, then check" (which returns `True` on `[1,2,3,4]` and `[0,0]` on Two Sum). The mental model was right; the sentence was not | The map/set holds **only what you've already passed** — **check first, then insert**. And: in an interview the interviewer only has what you SAY — narrate the loop body in the order it executes | 1 | Day 22 | active |
| M-024 | 2026-07-16 | impl | **Dual-structure sync** — #146 LRU keeps the cache in TWO structures (dict + linked list); updated one, forgot the other, twice: overwrite branch didn't repoint `adict[key]` at the new node; eviction unlinked the LRU node but didn't `del adict[lru.key]` (dict grows unbounded). Plus an off-by-one: capacity check ran before the insert | When one abstraction is backed by two structures, EVERY mutation must touch BOTH. The design-problem cousin of container-vs-contents (M-021) | 1 | Day 24 | dormant (#146 dict-sync clean Day 25 ✅) |
| M-025 | 2026-07-17 | impl | **Pointer-surgery slips — incomplete or wrong-target field mutation.** #146 `addFront` did only 2 of 4 pointer writes; #226 swapped LOCAL `left`/`right` not the node's fields. **Day 26 CLEAN ✅ — #146 all 4 pointers, #226 mutated the fields** | **(1) count the pointers** — insert-between = 4 writes, remove = 2. **(2) mutate the object's FIELD, not a local.** Kin to M-021 | 1 | Day 25 (×2) | dormant (clean Day 26 ✅) |
| M-026 | 2026-07-18 | impl | **Dropped the terminal line of an operation** — forgot `node.isEnd = True` after building a word in a Trie `insert`/`addWord` (#208 review AND #211, same session) → every `search` returns False | An operation isn't done when the loop ends — the **final state-marking / completing line** (isEnd, the return, the mark) is part of it. Walk the op to its end. Kin to M-011 (dropped guard) and M-001 (dropped return) — all "first-draft leaves a required line out" | 1 | Day 26 (×2) | active |
| M-027 | 2026-07-21 | impl | **One site missed on the final pass** — reconstruction correct, a change/name/paired-op lands on all-but-one site. **Day 27:** #1046 negation, #215 rename, #973 evict. **Day 28:** #143 `curr`, #199 guard, #146 `self.`. **Day 29:** #1046 return-negation (SAME as Day 27, the repeat), #199 enqueue, #211 ×3. **Day 30:** the one *repeat* CLOSED — **#1046 `return -maxHeap[0]` correct first-draft** after two identical misses; #79 Word Search 2 nudges (dropped **left** direction from the 4-neighbor line; `dfs(0,0,0)` vs `dfs(r,c,0)` in the start-cell loop). | Enumerate every site a change must land and confirm each. **The through-line of the sprint** — but the twice-identical repeat (#1046 un-negate) is now closed. Generalizes M-024; kin to M-004, M-020 | 3 (×11) | Day 27, 28, 29, **30** | **active — through-line (repeat closed Day 30); drill = the final read-through** |
| M-028 | 2026-07-21 | strategy | **Box-pattern channel recall** — #110 stated "the return is always a boolean"; the return must carry the **height** (what the parent needs) while the **box** holds the boolean. Recovered on a nudge; code then flawless | In the box pattern the **return channel carries what the PARENT needs; the box collects what YOU need** (#543). Recursion-heavy — his slowest area (rule 9) | 1 | Day 27 | active (recall wobble, not comprehension) |
| M-029 | 2026-07-26 | comms | **Names slightly wrong — a construct, a method or an attribute.** Day 31: called #90's dedup `while` loop "a guard", "a guard with a while loop", "the if statement guard"; garbled the #56 narration. Day 32: **four method names renamed** (`exist`→`wordSearch`, `merge`→`mergeInterval`, `insert`→`insertInterval`, `eraseOverlapIntervals`) + *"the mid value… that is the index"*. **Day 33: `node.neighbor` instead of `node.neighbors` on #133 — with `self.neighbors` written three lines above — cost a third submission on a solution that was already correct** | **Pin the real name; read it, don't recall it.** Started as a language slip with correct code; **Day 33 it broke working code.** `GOALS.md`: interviewers probe "what does this line do?" — wrong names read as not knowing your own solution | **3 (×9)** | Day 31, 32, **33** | **⛔ ESCALATED → B-8 (Day 33) — drill now** |
| M-030 | 2026-07-26 | process | **Confirm-seeking instead of self-testing.** "Am I right about this?" ×4 — most sharply on the four-clause overlap condition, which one 15-second hand-test on `[1,3]`vs`[3,5]` would have settled | **Run one concrete case before asking.** In an interview the only verification available is his own. Same root as M-029: outsourcing verification — of his claims and of his own words | 1 (×4) | Day 31 | **active — new watch** |
| M-031 | 2026-07-26 | impl | **#57 — a flag was SET but never GATED the branch.** `isMerged = True` recorded that `newInterval` had been placed, but the "after" branch didn't check it, so on `[[1,2],[12,16],[20,25]]` it re-appended `newInterval` once per remaining interval. **Self-found from the test case** | A flag only helps if it's *read* where it matters. Two sites for one fact — **M-027 family**. Alternative: return early instead of flagging | 1 | Day 31 | resolved same session (self-found) |
| M-032 | 2026-07-26 | strategy | **#56 — stated `O(1)` space next to an `O(n log n)` sort.** Noticed the sort's time cost, missed its space cost | **A sort costs space too** — Python's Timsort is `O(n)` auxiliary worst case. Never pair `O(n log n)` time with `O(1)` space. Kin to M-005 (a structure that scales with input = O(n) space) | 1 | Day 31 | **active — new watch** |
| M-033 | 2026-07-27 | impl | **A prune/guard written backwards.** #39: `target > total` instead of `total > target` — says "stop when I haven't got there yet" instead of "stop when I've overshot." True at the root call, so the whole recursion died instantly and `res` returned empty | **Say what the prune KILLS, in English, before writing it**: *"kills the branch when the running total has gone past target"* → `total > target`. Then read the code and confirm it says the same. Same family as B-6 (right operands, wrong order) | 1 | Day 32 | **active — new watch** |
| M-034 | 2026-07-27 | process | **The scan was said but not run.** #57's missing terminal append is item TWO on his own scan ("Terminal line/mark written?"), and his own comment named the flag he then failed to use | **Running the scan means walking it against the code in front of you, line by line — not reciting it from memory.** Three Day-32 failures were all items already on the list. Kin to M-030 (outsourcing verification) | 1 | Day 32 | **active — the current bottleneck** |
| M-035 | 2026-07-27 | coaching | **[MINE] Validated his backward-sweep approach for #435 after two passing examples plus a plausible argument.** It fails on `[[1,3],[2,4],[3,5]]`. He built on my wrong confirmation | **The coach is not exempt from the verification rule.** Two passing tests and a nice-sounding reason is not a proof. Find the counter-example before endorsing an approach | 1 | Day 32 | resolved same session (owned + corrected) |
| M-036 | 2026-07-28 | impl | **#133 — the wrong object's `neighbors` list, three sessions running.** D33/D34: `Node(node.val, node.neighbors)` handed the clone the ORIGINALS (measured: 5 reachable nodes instead of 4). **D35: `for neighbor in adict[node].neighbors` walked the CLONE's empty list — the loop body never ran, returning one isolated node. ⚠️ He had his notes OPEN and still mis-picked** | **Two objects share the attribute name `neighbors` and he cannot reliably tell them apart.** Not recall — the notes were in front of him. **Fix is mechanical, not attentional: name the clone.** `clone = Node(node.val, [])` … `for neighbor in node.neighbors: clone.neighbors.append(dfs(neighbor))`. Kin to M-021/B-5 | **3** | Day 33, 34, **35** | **⛔ ESCALATED → B-5 REOPENED (Day 35)** |
| M-037 | 2026-07-29 | impl | **Compared a container to a number.** #46: `if combo == len(nums)` — a list against an int, always `False`, so the base case never fired and `res` returned `[]` on every input. Should be `len(combo) == len(nums)` | **B-5, container vs contents.** Reaching for the box instead of the box's size. Kin to M-021 and to *"the mid value… that is the index"* | 1 | Day 34 | **active — B-5 fired** |
| M-038 | 2026-07-29 | impl | **Mixed the two binary-search templates.** #74: `while left < right` (converging exit) with `right = mid - 1` (exact-match shrink) → the final single cell is never examined. **4 of 6 cases wrong**, incl. `[[1]]` target `1`. Also stated `O(log n)` where it is `O(log(m·n))` | **Does the `right` assignment discard `mid`?** `mid - 1` ⇒ `while left <= right`. `right = mid` ⇒ `while left < right`, return `left`. Full table now in `binary-search.md`. Kin to M-014/M-015 | 1 | Day 34 | **active — new** |
| M-039 | 2026-07-31 | impl | **A function defined and never invoked.** #46: `backtrack` fully written, then `return res` — the recursion never started, so `[]` on every input. Add one `backtrack()` line and every permutation is correct | **A nested helper needs a launch line.** Kin to M-026 (dropped terminal line) — the operation isn't done when the definition ends. **Catches instantly on the first example** | 1 | Day 35 | **active — new** |
| M-003 | *(reopened)* | impl | **`range(x)` where `range(len(x))` belongs.** Day 35: `for r in range(grid)` on #994 → `TypeError: 'list' object cannot be interpreted as an integer`. **He wrote `len(grid)` correctly four lines later in the same function** | The index-loop idiom. **Cleared as B-2 on Day 18 and clean for 17 sessions** — treat as a watch, not a re-escalation, unless it recurs | 4 | Day 1, 4, 16, **35** | **👁 B-2 reopened as a watch** |

## Recurrence Watchlist (count ≥ 2 — one rep from escalating)

| ID | Type | Root cause | Count |
|---|---|---|---|
| **M-001 → B-9** | impl | **Computed a value and didn't catch it** — twice in one session across a recursive boundary | **7** ⛔ **→ escalated to B-9** |
| **M-027** | impl | **One site missed on the final pass** (transform/rename/paired-op/name/guard) — the through-line of Days 27–28 | **2 (×6)** |
| **M-005** | strategy | **A structure that scales with input = O(n) space** (BFS space = level width; dominates an O(h) stack) | **4** *(self-corrects; watchlist)* |
| **M-018** | strategy | **A scan / descent / skip is a LOOP, not a single check** (`if` where `while` belongs) | **2** |
| **M-009** | strategy | **Importing a template's BODY across problems without re-deriving** ("what decides the next step HERE?") | **2** |
| **M-026** | impl | **Dropped the terminal line of an operation** (isEnd marker / final mark) — #208, #211 | **1 (×2)** |
| **M-029** | comms | **Names slightly wrong** — constructs (Day 31), method names ×4 (Day 32), **`node.neighbor` broke working code (Day 33)** | **3 (×9)** ⛔ **→ escalated to B-8** |
| **M-030** | process | **Asking for confirmation instead of running one test case** | **1 (×4)** *(Day 31; **improving Day 32** — tested his own sweep when asked, self-reported a notes peek)* |
| **M-034** | process | **Checking what the ANSWER is instead of what the CODE does** — Day 34: simulated the correct rotting process instead of tracing his own DFS, then asserted an untraced output (*"it does give 3"*; it gives 4) | **2** *(HELD Day 33; **fired twice Day 34**)* |
| **M-033** | impl | **Prune/guard written backwards** (right operands, wrong order) | **1** *(Day 32; **HELD Day 33** — #39's prune correct first-draft)* |
| **M-036 → B-5** | impl | **The wrong object's `neighbors` list** — #133, three sessions running, notes open on the third | **3** ⛔ **→ B-5 REOPENED** |
| **M-039** | impl | **A function defined and never invoked** (#46) | **1** *(new Day 35)* |
| **M-003** | impl | **`range(x)` for `range(len(x))`** — #994 | **4** *(👁 B-2 reopened; clean Days 18–34)* |
| **M-037** | impl | **Container compared to a number** (`combo == len(nums)`) — B-5 | **1** *(new Day 34)* |
| **M-038** | impl | **The two binary-search templates mixed** (exit condition of one, shrink of the other) | **1** *(new Day 34)* |
| **M-032** | strategy | **A sort costs SPACE too** (`O(n)` Timsort aux) — stated `O(1)` beside `O(n log n)` | **1** *(new Day 31)* |
| M-002 | impl | `()` call vs `[]` index | 2 |
| M-006 | strategy | Counting hidden in-loop cost in Big-O | 2 |
| M-015 | strategy | Converging search — return convergence point, not a tracked answer | 2 |
| M-016 | impl | for/while mix-up | 2 |

*(M-025 pointer-surgery → dormant, clean Day 26. M-005 self-corrects — watchlist not drill-now.)*

*Cleared blockers → standing habits: M-004 → B-1 (Day 16); M-003 → B-2 (Day 18); M-001 → B-3 (Day 21, watch); M-011 → B-4 (Day 24, reopened Day 26, fired Day 28); M-021 → B-5 (Day 24); **M-012 → B-6 (CLEARED Day 27)**; **M-020 → B-7 (re-escalated Day 28, CLEARED Day 30 after 2 clean)**.*

**No drill-now blocker — B-7 CLEARED Day 30; all of B-1…B-7 clear. Day 31 added no blocker: M-029/M-030 are high-frequency but were FIRST OBSERVED Day 31, and recurrence is counted across sessions, not within one.** Escalate if either appears again Day 32+. See `BLOCKERS.md`. **On watch (all one disease — one site missed on the final pass): M-027 (the through-line — but the one *repeat*, #1046 un-negate, is now CLOSED Day 30; the two #79 nudges were this flavor), ~~backtracking fragility~~ **CLEARED Day 31 — #78/#90/#46 all first-draft correct, 12 min total**, B-4 (guards, held), M-005 (BFS space, held), M-026, M-028 (box, held).**

> **The shape of the problem (Days 22–26).** Every recurring impl mistake — guards (M-011), returns (M-001), isEnd (M-026), pointer surgery (M-025), container-vs-contents (M-021), `self.` (M-020) — is **one disease: first-draft completeness.** As each facet gets a named out-loud check it clears (B-1/B-2/B-3/B-4/B-5/B-7 all cleared) — then a new facet surfaces. **The single scan: before submitting, walk the operation top to bottom — guard present? terminal line/mark written? every branch returns? all args passed? mutating the field not a local?**

> **The shape of the problem (Days 22–24).** M-011, M-021, M-018, M-012, M-020, M-001, M-024 are **all one failure mode wearing different clothes: first-draft precision.** Every one fired on a problem whose *algorithm he had already derived correctly*. The gap is not comprehension. **B-4 and B-5 cleared on Day 24 — the drill works when run.** The reflexes, said OUT LOUD before submitting: **the `self.` test · does it return? · box or contents? · both structures in sync? · target-first comparison · am I looping where I should loop?**

---

## Day 31 addendum — the shape of the problem has moved

Through Day 30 every recurring mistake was **first-draft precision** in *code* (guards, returns, terminal marks, one-site-missed). Day 31's two new entries are not code at all:

- **M-029** — he names constructs loosely (`while` → "if") while writing them correctly.
- **M-030** — he asks whether he's right instead of testing whether he's right.

**These are one disease: outsourcing verification.** M-027 is its code-shaped form (didn't walk every site); M-030 is its process-shaped form (didn't run the case); M-029 is its language-shaped form (didn't pin the word). The drill is the same in all three: **before handing it over, verify it yourself — every site, one test case, and the actual name of the thing.**

Counter-evidence worth keeping, because Day 31 also showed the drill working: he **test-diagnosed his own overlap condition's two holes**, **found the #57 flag bug from a test case**, and **dropped `self.` on #46 unprompted in the same session as the correction.** When he does run the check himself, it works.

---

## Day 32 addendum — the bottleneck moved again

Day 31 named the disease as **outsourcing verification**. Day 32 narrows it to one act: **M-034, the scan is said but not run.**

All three Day-32 failures were things already written on his own eight-item scan — a missing terminal line (item 2), a reversed comparison (the "which side" item), a half-recalled mechanism. **The checklist is complete. The execution of the checklist is the gap.** Reciting it at the start of a session is not the same as walking it against the code in front of him before he hands it over.

**Structural finding worth keeping** *(and worth repeating to him on a bad day)*: all four Day-32 full solves were **first retrievals**. Three failed — and the one that passed, #56, is the one that cost 26 minutes and three explanations the day before. **The material that felt worst is the material that stuck.** Smooth acquisition retains worse than effortful acquisition; his own log now demonstrates it.

**And M-035 is mine**, kept in this file on purpose: I endorsed an approach after two passing examples. Same disease, different person.


---

## Day 33 addendum — the scan ran, and one thing got worse

**M-034 is answered, at least for one session.** Day 32's diagnosis was that the checklist was complete and the *execution* of it was the gap. Day 33: **five full solves, five passes, 26:55** — and every one was a problem that had failed the day before on a named cause. **M-026** (terminal line), **M-033** (reversed prune), the #79 idiom and the **#435 reference bug all held first-draft.** When he walks the scan against the code, the code is right. That is now demonstrated, not asserted.

**But M-029 got worse in the way that matters: it stopped being a language slip and started breaking code.** Days 31–32 were *names said wrong while the code was right* — annoying, interview-visible, not fatal. **Day 33's `node.neighbor` was in the code**, on a solution that was already algorithmically correct at submission two, and it cost a third submission. Six consecutive sessions, three by the recurrence count. **Escalated to B-8.**

**The remaining honest number is not pass/fail — it's the clock.** 44:14 and 45:28 on the two new problems. Both correct, both brand-new material, and the pattern was derived unaided in each case. But readiness is measured in minutes on unseen problems and a FAANG medium is ~20–25. **From Day 34 the new-problem stopwatch is a tracked metric, not a note.**

> **And the standing consequence, installed today:** a full solve handed over **without having been executed** is a **fail on the spot** — no partial credit for "the algorithm was right." Three submissions on #133 is precisely what that rule exists to prevent.


---

## Day 34 addendum — four failures, one disease, and the narrowest diagnosis yet

```
#207   dfs(child)              answer computed, discarded
#133   dfs(neighbor)           answer computed, discarded
#46    combo == len(nums)      a list compared to an int
#74    while left < right      the wrong template's exit condition
```

**Four different problems. Four failures. One disease: the exact identity of the value in front of him.** He understood all four algorithms — he explained the two-mark idea for `#207` unaided and named `path` as backtracking himself. **Not one failure was comprehension.**

**Two of the four are the same recursion mistake within two hours**, which is why M-001 escalates to **B-9** after six weeks on the watchlist. The tell is that he would *never* drop a return value in ordinary code. It only happens across a recursive boundary, because in recursion it feels like the callee "does something" to shared state rather than *hands you back an answer you must catch*.

> **The drill: before writing any recursive function, out loud — *"the callee hands me back ___, and I catch it at ___."*** One sentence. It prevents `#207`, `#133`, `#110`'s Day-27 box wobble and `#1046`'s un-negate.

### The mechanism behind #133, and it generalises

**`#133` is the one problem he never wrote correctly himself.** On Day 33 I told him the fix and he applied it. On Day 34 it was gone — both bugs, identical.

Meanwhile everything he *fought* for on Day 34 stuck: the DFS-can't-measure-time counter-example, the off-by-one, the two marks, the multi-source seeding.

> **A correction you are HANDED decays far faster than one you DERIVE.** Same finding as Day 32's `#56`-versus-`#57` split, from the opposite direction. **Coaching consequence: when he gets something wrong, make him produce the fix — never hand it over — even when handing it over is faster.**

### M-034 fired twice, and he pushed back fairly

Asked to trace his own DFS, he simulated the *correct process*. Asked what his BFS counter ends at, he asserted *"it does give 3"* — it gives 4.

He objected that he had no code to run, which is **half right, and that half is mine** — I framed it as "you didn't run it" when he had nothing to run. The real point is narrower and stands: **he stated a result he had not derived.** *"I haven't checked"* costs nothing. And he had hand-traced the DFS correctly ten minutes earlier, so the capability was present.

### 🟢 The counter-evidence, which is substantial

He derived the multi-source seeding, the cycle criterion, and the `path`-is-backtracking connection **unaided**. He asked *"why do we even need `visited`?"* — the sharpest question of the week. He said *"I pretty much just copied this and can't visualise it"* when he could have stayed quiet, which is what got the stepper animation built. **And he measured his own one-draft overrun** (*"at 4:00 I was at `combo.append(nums[i])`"*) instead of complaining, which is exactly the calibrated reporting M-030 is about — and it changed the rule.


---

## Day 35 addendum — three correct algorithms that never executed

```
#133   for neighbor in adict[node].neighbors    walked the wrong object's list
#46    (backtrack never invoked)                the function was never called
#994   for r in range(grid)                     range() of a list -> TypeError
```

**Not one of these is an algorithm.** With `len()` added and nothing else changed, `#994` passed every 6-cell grid and 20,000 random ones. With one `backtrack()` line, `#46` produced every permutation correctly. `#133`'s structure was right including the `None` guard he'd missed the day before.

> **All three crash or return empty on the FIRST example.** `range(grid)` is a `TypeError` — the program does not start. **The gap between his solve rate and his pass rate is one execution**, and that has now been the finding two sessions in a row.

**The counter-evidence is in the same block.** `#207` passed first-draft on **exactly the line that reset it the day before**, because he ran the B-9 sentence before writing. `#74` passed on exactly the condition that reset it. **When the check gets run, it works.** The problem is not knowing what to check.

### M-036 → B-5, and why the fix is mechanical

Three sessions, three wrong answers to one question: *which `neighbors` list?* On Day 35 **his notes were open and he still mis-picked**, which rules out recall as the cause. Two objects share an attribute name and the expressions `node.neighbors` and `adict[node].neighbors` are nearly identical on the page.

> **Prescription: `clone = Node(node.val, [])`, then `for neighbor in node.neighbors: clone.neighbors.append(dfs(neighbor))`.** `node` and `clone` are two different words; the confusion becomes impossible rather than merely avoidable. **When two things are easy to confuse, stop relying on care and change the names.** Same move as `answer[-1]` replacing `pop()` + `append()` on `#56`.

### 🟢 What actually improved

**Block 2 went 17:21 and 31:14 — 48 minutes for two new problems, against 116 the day before.** He derived post-order-then-reverse himself, transferred `#323` from `#200` himself, and made two judgment calls unprompted: **he did not bring `path` over** to an undirected problem, and **he wrote a `dfs` that returns nothing** — correctly, because the counting happens outside it. With B-9 live that second one matters: **the drill is *know what the callee hands back*, not *always catch a return*.**

**And he self-reported a notes peek for the second time**, on a problem where nobody would have known. That is the M-030 muscle working.
