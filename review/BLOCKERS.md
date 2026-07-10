# Blockers — drill now

> A mistake that recurs **≥ 3 times** is no longer a slip — it's a habit to break. It escalates here from `MISTAKES.md` and gets an explicit drill until it's clean twice in a row, then drops back to dormant.

## Active blockers

### B-3 · M-001 — forgetting `return`  🟡 *(escalated Day 19 — light)*
He always *computes* the answer correctly, then doesn't hand it back: forgot the `return` value (Day 4, Day 6), and `return prev` on #206 (Day 19).
**Drill — pre-submit "does it return?":** the very last check before submitting is *"does this function `return` the answer, not just compute it?"* Fold it into the standing audit.
**Clears when:** two consecutive sessions with zero forgotten `return`s.

*(B-1 (variable names, cleared Day 16) and B-2 (range/len, cleared Day 18) — keep as standing habits. Watchlist at recurrence 2: `()` vs `[]` (M-002), hidden in-loop Big-O (M-006), space-scales=O(n) (M-005), dropped guard (M-011), binary-search direction (M-012), converging-return (M-015), for/while (M-016).)*

## Resolved / dormant

### B-1 · M-004 — wrong-variable / naming imprecision  ✅ *(CLEARED Day 16)*
Escalated Day 11 (kept #125 red for 5 sessions). **Cleared after two consecutive clean-on-names sessions (Day 15 + Day 16)**, capped by a fully clean #125 (Day 14) and clean 3Sum/#424 (Day 16). History: `nums.add`/`seen.add` (Day 1), `s`/`clean` (Day 9), `.isalum` (Day 10), `strs`/`s` + `nums`/`numbers` (Day 11), `appened`/`append` (Day 12), `self.stack`/`self.minStack` (Day 14). **Keep the variable audit as a standing habit** — if a wrong-name slip recurs, re-escalate.

### B-2 · M-003 — `range(len(x))` scramble  ✅ *(CLEARED Day 18)*
Escalated Day 16 (3rd occurrence: `range(x)` Day 1 & Day 4, `len(range(s))` Day 16). Cleared after two clean range/len sessions (Day 17 + Day 18). **Keep the 5-sec `range(len(x))` pre-empt** as a standing habit; re-escalate if it recurs.

## How a blocker clears
1. A targeted micro-drill at the start of the next 2–3 sessions (e.g., write 3 list-method calls correctly from memory).
2. Two clean reps in a row with no occurrence ⇒ move back to `MISTAKES.md` as `dormant`.
