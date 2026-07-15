# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-15 (Day 23 logged)
- **Phase:** Summer Sprint · Block B — *Trees + **BFS learned** (#102, #199). Box pattern transferred to #110. Day 24 = **LRU Cache (#146)** + interleave.*
- **Sessions logged:** 23 · **Patterns learned:** 9 · **Mistakes tracked:** 23 · **Open blockers:** 3 (B-4, B-5, B-6)
- **Review queue:** Day 24 (Jul 16) = **6 due** (interleave + LRU day). Resets first: **#235, #143**.

## 🟡 The one thing that matters right now

Two-part story, and both parts are true:

**The fix is working where he practices it.** Day 22 he lost to imported templates/complexities. **Day 23 in Block 2 he re-derived all three complexities from scratch** — DFS O(h), BFS O(n), iterative-BST O(1) — instead of recalling. That discrimination is exactly what was missing. And **B-4 and B-5 each got their first clean rep** — one more clean session and both drop.

**But the same failure mode is still live in review:**

- **B-6 (search direction) failed a 4th time — #235, same problem, two days running.** Now has a mechanical fix: **write comparisons TARGET-first** (`p.val > node.val → right`) so there's nothing to mentally flip.
- **#143 reset** — imported #21's value-comparison merge into a problem that forbids touching values (**M-009**).

**The through-line: recognizing a pattern gives the SKELETON, not the BODY. Re-derive what decides each step, every time.**

## The reflexes (say them OUT LOUD before submitting)
1. **Box or contents?** *(B-5 — clean Day 23 ✅)*
2. **Is it guarded?** *(B-4 — clean Day 23 ✅)*
3. **Which side can still contain the answer?** — **write it target-first** *(B-6 — failed Day 23 ❌)*
4. **Am I looping where I should loop?** *(M-018)*
5. **What decides the next step IN THIS problem?** — don't paste a template body *(M-009)*

## ⚠️ Standing schedule note
**LRU Cache (#146) is Day 24 (Jul 16)** — the last unplaced core problem. Jul 16 held to **6** reviews to protect it. **Do not let it drift.**
**#98 Validate BST** deferred Day 23 → **Day 25** (clusters with #230, both BST).

## Pace Health
*(🟡 = off the sprint target · 🔴 = at risk. Refreshed each session.)*

| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 36 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 23 = **3** (#102, #199, #110) + BFS taught | 🟢 ahead of plan |
| Sessions last 7 days (target ≥ 6) | 6 | 🟢 |
| Days since last session | 0 | 🟢 |
| Queue due (next 2 days) | 6 + 6 | 🟢 balanced, under cap |
| **Open blockers** | **3** (B-4 ✅1/2 · B-5 ✅1/2 · B-6 ❌0/2) | 🟡 two clearing, one stubborn |
| Review pass rate (Day 23) | **5 / 7** | 🟡 both fails = imported template / direction |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | **4/5** | **re-derived DFS O(h) / BFS O(n) / BST O(1) all correct in one block** — the anti-recall fix working |
| Arrays & Hashing | 3/5 | **#271 reset ×2 CLEARED** ✅ · #242 reset cleared ✅ |
| Two Pointers | 3/5 | #15 clean |
| Sliding Window | 3/5 | solid |
| Binary Search | 3/5 | stable — but direction inversion (B-6) still recurring on BST |
| Stack | 3/5 | stable |
| Linked List | 3/5 | #141 clean; **#143 reset** (imported #21's value merge) |
| **Trees** | **3/5** | **BFS learned** (#102, #199) · box pattern transferred (#110) · #543/#100/#226/#104 all clean |
| **Binary Search Tree** | **2/5** | #235 reset — direction, not concept (B-6) |

## 🟡 Open Blockers

- **B-6 (M-012, search direction)** — 🔴 **recurrence 4, 0 of 2.** The stubborn one. #235 inverted **again**, same problem next day. **Fix installed: comparisons target-first** — `target > node → right`. *If it inverts a 3rd time, stop and drill direction cold.*
- **B-5 (M-021, container vs. contents)** — 🟢 **CLEAN Day 23 ✅ (1 of 2)** — #271 re-solved with `s[j]`. One more clean session → drops.
- **B-4 (M-011, edge guards)** — 🟢 **CLEAN Day 23 ✅ (1 of 2)** — #242 guard present, #141 guarded the `None==None` trap. One more → drops.
- **Watchlist (one rep from escalating):** **M-018** (`if` where a `while` belongs) · **M-009** (importing a template's body — fired on #143 Day 23).

*(B-1 names, B-2 range/len, B-3 `return` — all cleared; standing habits.)*

## Next Session Focus  → **Day 24**
1. **Block 1 — interleave + review (6 due, mix unlabeled where you can):** resets **#235 → #143** first (fragile, full re-solve — **#235 target-first!**), then #19, #739, #206, #21.
2. **Block 2 — new:** **LRU Cache (#146)** — `dict` + doubly-linked list (dummy head/tail), O(1) get/put. **Pre-teach in isolation first:** the doubly-linked node, and "the hashmap maps key → node." One new piece at a time.
3. **Habits (out loud before submit):** **target-first comparisons (B-6)** · box or contents · is it guarded · **re-derive the body, don't paste (M-009)** · complexity out loud, time AND space.

---
*Weekly snapshots can be appended below as the sprint progresses.*
