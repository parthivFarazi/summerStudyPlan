# Spaced-Repetition QUEUE — single source of truth for review state

> **Ladder:** `1d → 3d → 7d → 21d → 60d` → graduated. **Pass** = advance one rung. **Fail** (needed a hint, blanked, or a bug you couldn't self-fix) = **reset to 1d** + log the cause in `MISTAKES.md`. Re-solves are **from a blank screen**, never re-reading the solution.

## How to use each session
1. Pull rows with **Next due ≤ today**; order **resets → 1d → 3d → verbal**. Budget **~6–8 items** under a **hard 30-minute box**.
2. **The rung sets the tier** *(2026-07-25 — full rationale in `SYSTEM.md`)*:

| Rung | Tier | Cost | What you do |
|---|---|---|---|
| **1d · reset** | **Full solve** | ~6 min | Blank screen. Write it, run it, debug it. |
| **3d** | **✍️ One-draft** | ~4 min | Write it **once**, 4-min cap. **Don't run it. Don't debug it.** Then audit your own draft against the scan. **Pass = the first draft was correct.** |
| **7d · 21d · 60d** | **🗣 Verbal** | ~30 sec | Say pattern + approach + time/space out loud. Blank ⇒ full solve ⇒ reset. |

3. **The 30-min box is hard.** Anything unreached gets a **concrete date written into the table** before the session ends — never an undated roll.
4. Update the row: new rung + new **fuzzed** due date (jitter toward the lightest day; keep any day ≤ ~8) + append result to `Results` (`P`/`F`). One write, here only.
5. **Weight-balance and batch when scheduling:** heavy Block 2 (Graphs, DP) ⇒ light reviews **and Block 2 runs first**; group same-pattern reviews together, except on interleave days.

## Overflow rule
A wall of 12-due is a **scheduling** problem, not a work problem. If **due count > 8** after prioritizing: full-solve the fragile ones, verbal the stable ones, and **re-date the leftover** so no day exceeds ~8. Interleave days also drain the queue. Decay is the enemy, not volume.

> **⛔ A roll-forward must land on a real date.** *(added 2026-07-25 — `COACHING.md` rule 10.)* Rolling an item "to Jul 28" and then rolling it again is deferral, not scheduling. **Every roll writes a concrete `Next due` into the row below**, and the day it lands on must still be ≤ 8.

> **Steady-state note:** at 2-new/day this ladder settles at **~7 reviews/session** — ~3.5 full, ~1.4 one-draft, ~2.2 verbal, **~28 min**. That number is set by the ladder, not chosen; see `SYSTEM.md` → *What the review load actually is*. **Stretching the rung intervals does not reduce it** — it only delays it.

---

## 🔴 Backlog drain · Jul 26 → Aug 5 *(built 2026-07-25 · re-tiered + weight-balanced same day)*

**The honest count.** After Day 30, **43 items were due or overdue on/before Jul 28** — 18 already past due (dated Jul 24–25, unworked because Day 30's interleave sampled only 6). The Day-30 note rolled them all onto "Jul 28," which would have made Jul 28 a **29-item day** against a cap of 8. That is not a schedule; that is a pile.

**Six levers applied.** The first four spread the load; the last two make each item cheaper and each day gentler:

1. **Three review tiers, set by rung** *(`SYSTEM.md`)* — **1d/reset = full solve · 3d = ✍️ one-draft (4-min cap, no debugging) · 7d+ = 🗣 verbal.** Only ~2 items per session now involve write-run-debug.
2. **Drain stretched to Aug 5** — 10 sessions, not 7.
3. **Backtracking cluster split** — Day 31 takes only the three that actually failed; #79/#39 → Jul 27.
4. **Overdue sweep moved off Day 31.**
5. **Weight-balanced against Block 2** — the Graph days (Jul 28–30) and DP days (Aug 1–5) get **light** reviews (arrays, two-pointers, stack, binary search, heap); the light Intervals day and the interleave day absorb the **heavy** ones (backtracking, linked-list surgery, LRU).
6. **Batched by pattern** so context stays loaded — trees together, heap together, linked-list together. *(Jul 31 is deliberately unbatched: it's the interleave day and mixing is the point.)*

**Result: no day exceeds 8 items or ~29 minutes, and the average is 6.4 items in ~24 min.**

| Session | Date | Block 2 weight | Full solve | ✍️ One-draft (4 min) | 🗣 Verbal | Time |
|---|---|---|---|---|---|---|
| **Day 31** | **Sun Jul 26** | Intervals · medium | **#90 · #46 · #78** *(backtracking, batched)* | — | — | **~35 min** |
| Day 32 | Mon Jul 27 | Intervals · **light** | #79 · #39 · #57 · #56 | #146 *(heavy — light day absorbs it)* | #704 · #33 | ~29 min |
| Day 33 | Tue Jul 28 | **Graphs · HEAVY** ⇒ B2 first | #435 · #252 | #242 · #15 · #20 *(all light)* | #155 · #74 · #150 | ~25 min |
| Day 34 | Wed Jul 29 | **Graphs · HEAVY** ⇒ B2 first | #200 · #133 | #102 · #100 · #543 *(trees batch)* | #235 · #271 · #226 | ~25 min |
| Day 35 | Thu Jul 30 | **Graphs · HEAVY** ⇒ B2 first | #994 · #207 | #703 · #973 · #215 *(heap batch)* | #98 · #153 · #128 | ~25 min |
| Day 36 | Fri Jul 31 | *interleave — no new* | #210 · #323 | #143 · #19 · #141 · #230 *(unbatched on purpose)* | #739 · #121 | ~29 min |
| Day 37 | Sat Aug 1 | **DP · HEAVY** (3 new) ⇒ B2 first | — | #110 · #211 · #208 | #206 · #21 · #104 | ~14 min |
| — | **Sun Aug 2** | 🟢 **REST** | — | — | — | — |
| Day 38 | Mon Aug 3 | **DP · HEAVY** ⇒ B2 first | #70 · #746 · #198 | #875 · #424 | #347 · #238 | ~27 min |
| Day 39 | Tue Aug 4 | **DP · HEAVY** ⇒ B2 first | #5 · #91 | #1046 · #199 | #3 · #167 | ~21 min |
| Day 40 | Wed Aug 5 | **DP · HEAVY** ⇒ B2 first | #322 · #152 | — | #11 · #125 | ~13 min |

*(Full-solve items are almost always the previous day's new problems arriving at 1d — those can never be cheapened.)*

**Hard 30-minute box on Block 1.** Order: resets → 1d → 3d → verbal. Whatever isn't reached gets a **concrete date written into the table below** before the session closes. Never an undated roll.

---

## Due / Active

**Tier is set by rung:** blank = **full solve** (1d/reset) · **✍️ = one-draft**, 4-min cap, no running or debugging (3d) · **🗣 = 30-second verbal** (7d+).

| Problem | Pattern | Rung | Tier | Next due | Streak | Results |
|---|---|---|---|---|---|---|
| **Subsets II (#90)** | backtracking | **1d (reset)** | full | **2026-07-26** | 0 | (new)·**F** |
| **Permutations (#46)** | backtracking | **1d (reset)** | full | **2026-07-26** | 0 | (new)·**F** |
| **Subsets (#78)** | backtracking | **1d (reset)** | full | **2026-07-26** | 0 | (new)·**F** |
| **Word Search (#79)** | backtracking (grid DFS) | **1d** | full | **2026-07-27** | 0 | (new) |
| **Combination Sum (#39)** | backtracking | **1d** | full | **2026-07-27** | 0 | (new) |
| LRU Cache (#146) | design / linked-list | 3d | ✍️ | **2026-07-27** | 1 | (new)·F·P·F·**P** |
| Binary Search (#704) | binary-search | 7d | 🗣 | **2026-07-27** | 2 | P·P |
| Search in Rotated Array (#33) | binary-search | 7d | 🗣 | **2026-07-27** | 2 | P·P |
| Valid Anagram (#242) | arrays-hashing | 3d | ✍️ | **2026-07-28** | 1 | P·P·P·F·F·P |
| 3Sum (#15) | two-pointers | 3d | ✍️ | **2026-07-28** | 1 | F·P·F·P |
| Valid Parentheses (#20) | stack | 3d | ✍️ | **2026-07-28** | 1 | P·F·P |
| Min Stack (#155) | stack | 7d | 🗣 | **2026-07-28** | 2 | P·P |
| Search a 2D Matrix (#74) | binary-search | 7d | 🗣 | **2026-07-28** | 2 | P·P |
| Evaluate RPN (#150) | stack | 7d | 🗣 | **2026-07-28** | 2 | P·P |
| Level Order Traversal (#102) | trees | 3d | ✍️ | **2026-07-29** | 1 | (new)·F·F·P |
| Same Tree (#100) | trees | 3d | ✍️ | **2026-07-29** | 1 | P |
| Diameter of Binary Tree (#543) | trees | 3d | ✍️ | **2026-07-29** | 1 | P |
| Lowest Common Ancestor BST (#235) | binary-search-tree | 7d | 🗣 | **2026-07-29** | 2 | (new)·F·P·**P** |
| Encode/Decode Strings (#271) | arrays-hashing | 7d | 🗣 | **2026-07-29** | 2 | P·F·F·P·**P** |
| Invert Binary Tree (#226) | trees | 7d | 🗣 | **2026-07-29** | 2 | P·F·P·**P** |
| Kth Largest in Stream (#703) | heap | 3d | ✍️ | **2026-07-30** | 1 | (new)·P |
| K Closest Points (#973) | heap | 3d | ✍️ | **2026-07-30** | 1 | (new)·**P** |
| Kth Largest in Array (#215) | heap | 3d | ✍️ | **2026-07-30** | 1 | (new)·**P** |
| Validate BST (#98) | binary-search-tree | 7d | 🗣 | **2026-07-30** | 2 | (new)·P·**P** |
| Find Min in Rotated Sorted Array (#153) | binary-search | 7d | 🗣 | **2026-07-30** | 2 | F·P·F·P·P |
| Longest Consecutive Sequence (#128) | arrays-hashing | 7d | 🗣 | **2026-07-30** | 2 | P·P |
| Reorder List (#143) | linked-list | 3d | ✍️ | **2026-07-31** | 1 | (new)·F·P·F·**P** |
| Remove Nth Node From End (#19) | linked-list | 3d | ✍️ | **2026-07-31** | 1 | (new)·P |
| Linked List Cycle (#141) | linked-list | 3d | ✍️ | **2026-07-31** | 1 | P |
| Kth Smallest in BST (#230) | binary-search-tree | 3d | ✍️ | **2026-07-31** | 1 | (new)·P |
| Daily Temperatures (#739) | stack | 7d | 🗣 | **2026-07-31** | 2 | P·F·P·P |
| Best Time to Buy/Sell (#121) | sliding-window | 21d | 🗣 | 2026-07-31 | 3 | P·P·P |
| Balanced Binary Tree (#110) | trees | 3d | ✍️ | **2026-08-01** | 1 | (new)·F·**P** |
| Add & Search Words (#211) | tries | 3d | ✍️ | **2026-08-01** | 1 | (new)·F·F·**P** |
| Implement Trie (#208) | tries | 3d | ✍️ | **2026-08-01** | 1 | (new)·F·P |
| Reverse Linked List (#206) | linked-list | 7d | 🗣 | **2026-08-01** | 2 | P·P |
| Merge Two Sorted Lists (#21) | linked-list | 7d | 🗣 | **2026-08-01** | 2 | P·P |
| Maximum Depth of Binary Tree (#104) | trees | 7d | 🗣 | **2026-08-01** | 2 | P·P |
| Koko Eating Bananas (#875) | binary-search | 3d | ✍️ | **2026-08-03** | 1 | P·F·P·F·P |
| Longest Repeating Char Replace (#424) | sliding-window | 3d | ✍️ | **2026-08-03** | 1 | P |
| Top K Frequent (#347) | arrays-hashing | 21d | 🗣 | **2026-08-03** | 3 | P·P·P |
| Product of Array Except Self (#238) | arrays-hashing | 21d | 🗣 | **2026-08-03** | 3 | P·P·P |
| Last Stone Weight (#1046) | heap | 3d | ✍️ | **2026-08-04** | 1 | (new)·F·F·**P** |
| Right Side View (#199) | trees | 3d | ✍️ | **2026-08-04** | 1 | (new)·P·F·F·**P** |
| Longest Substring No Repeat (#3) | sliding-window | 21d | 🗣 | **2026-08-04** | 3 | P·P·P |
| Two Sum II (#167) | two-pointers | 21d | 🗣 | **2026-08-04** | 3 | P·P·P |
| Container With Most Water (#11) | two-pointers | 21d | 🗣 | **2026-08-05** | 3 | P·P·P |
| Valid Palindrome (#125) | two-pointers | 21d | 🗣 | **2026-08-05** | 3 | F·F·F·F·P·P·P |
| Group Anagrams (#49) | arrays-hashing | 60d | 🗣 | 2026-09-09 | 4 | P·P·P·P |
| Two Sum (#1) | arrays-hashing | 60d | 🗣 | 2026-09-12 | 4 | P·P·P·P |
| Contains Duplicate (#217) | arrays-hashing | 60d | 🗣 | 2026-09-12 | 4 | P·P·P·P |

*(A bolded `Next due` was re-dated by the 2026-07-25 drain. New problems join at 1d — always full solve — as they're learned.)*

---

## Session history

**Day 27 (Jul 21):** #102/#208/#703→3d, #235→7d (**B-6 CLEARED**); #211/#1046/#110 reset; #973/#215 new.
**Day 28 (Jul 22):** #271/#226/#98→7d; #143/#199/#146 reset; #78/#39 new.
**Day 29 (Jul 23):** **5/8** — #110/#973/#215/#143/#146 **PASS→3d**; #211/#1046/#199 **reset** (fresh facets: #211 constructor/keys/return, #1046 return-negation *again*, #199 enqueue direction); new **#90/#46 backtracking→1d**. **Named checks HELD.** **B-7 held → 1 clean session.**
**Day 30 (Jul 25 — interleave day) — DONE.** 3/6 interleave: **#211/#1046/#199 PASS→3d** (every older named cause held — #1046 un-negate FINALLY, #211's 3 Day-29 facets, #199 enqueue direction); **#78/#90/#46 reset→1d** (all backtracking — the youngest pattern). **Plus #79 Word Search** ✅ (grid DFS, built cold, 2 M-027 nudges) — carried over from Day 29. ✅ **Throughput fine:** interleave days are built to carry 0–1 new, so 1 new + a full interleave block is *above* baseline. *(An earlier note in this file called it a sub-floor miss — that was wrong and is retracted.)*

**Day 31 order (Sun Jul 26 — Sunday worked · ~90 min):**
**#90 → #46 → #78**, full re-solve from a blank screen (~35 min — all three are resets, so no cheaper tier applies) → pre-teach `lambda` sort key + tuple unpacking (10 min) → new: **Intervals #57 → #56** (40 min). Reviews run first: Intervals is a new pattern but not a heavy one, and Block 1 is only 3 items. Run-sheet: `plan/Day-31-Runsheet.md`.

> **✅ B-7 (self./ownership) CLEARED Day 30** (2nd clean session) — no drill-now blocker; all of B-1…B-7 clear.
> **👁 M-027 — the through-line, but the one *repeat* is CLOSED.** #1046's un-negate finally landed Day 30 after two identical misses. Keep the final read-through.
> **👁 Backtracking fragility (Day 30):** #78/#90/#46 all reset — the pattern is <1 week old. Not a blocker; the three failures drain Sun Jul 26, #79/#39 follow Mon Jul 27.

## Graduated (≥60d, never deleted)
| Problem | Pattern | Graduated | Results |
|---|---|---|---|
