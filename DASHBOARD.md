# Dashboard — LeetCode Tracker

> **Goal:** answer technical questions at any eligible company · grad Dec 2026 · **sprint deadline Aug 20**.
> "Current Status" is regenerated each update. Readable in under 2 minutes.

## Current Status
- **Last updated:** 2026-07-02 (Day 12 logged)
- **Phase:** Summer Sprint · Block A — *Interleave day done (#238, #3, #153). Day 13 = **Search in Rotated Array (#33)** + **Valid Parentheses (#20, Stack)**.*
- **Sessions logged:** 12 · **Patterns learned:** 5 · **Mistakes tracked:** 15 · **Open blockers:** 1 (B-1: variable audit)
- **Review queue:** 3 due 2026-07-03 (#153, #704, #74); #125 & #875 Jul 4

## Pace Health
*(🟡 = off the sprint target · 🔴 = at risk. Refreshed each session.)*

| Indicator | Value | Status |
|---|---|---|
| Days to Aug 20 pivot | 49 | 🟢 runway exists |
| **Sprint throughput** (new/day) | Day 12 = interleave (0 new by design); resumes Day 13 | 🟢 on plan |
| Sessions last 7 days (target ≥ 6) | 7 | 🟢 |
| Days since last session | 1 | 🟢 |
| Queue due (next 2 days) | 5 | 🟡 stay on top of it |
| **Open blockers** | 1 (B-1 M-004, drill active) | 🟡 drilling |

## Pattern Mastery  *(1–5; 5 = solve a novel one cold while narrating)*

| Pattern | Mastery | Note |
|---|---|---|
| Big-O & complexity | 3/5 | states time+space unprompted most of the time |
| Arrays & Hashing | 3/5 | #238 prefix/suffix reproduced cold (mechanism right; missed the *name*) |
| Two Pointers | 3/5 | Two Sum II + Container clean on review |
| Sliding Window | 3/5 | #3 cold w/ unprompted amortized O(n); named it crisply |
| Binary Search | 3/5 | invariant + both loop reflexes solid; slipped on the converge-**return** (tracked `answer` vs `nums[left]`, M-015) |

## 🔴 Open Blocker — B-1 (M-004, variable-name imprecision)
Kept #125 red for 5 sessions; escalated Day 11. **Drill: "variable audit before every submit"** — scan each variable/method name against what's actually declared. Clears after **2 consecutive slip-free (self-caught, no nudge)** sessions. *(Day 11: audit cleared #125 ✅. Day 12: audit caught `appened`→`append` on #238 — but only after a nudge, so the clear-counter does **not** advance; still drilling.)*

## Next Session Focus  → **Day 13**
1. **Block 1 — review:** Container With Most Water (#11), Koko (#875), + due (#153 reset, #704, #74). Name the pattern first; state complexity unprompted.
2. **Block 2 — new:** Search in Rotated Array (#33, binary search); Valid Parentheses (#20, stack — list as stack `.append`/`.pop`, pair dict).
3. **Blocker drill:** variable audit on every submit (B-1). **New watch — M-015:** converging binary search → `return nums[left]`; don't track a candidate (a default leaks on `[2,1]` / `[5]`).

---
*Weekly snapshots can be appended below as the sprint progresses.*
