# Blockers — drill now

> A mistake that recurs **≥ 3 times** is no longer a slip — it's a habit to break. It escalates here from `MISTAKES.md` and gets an explicit drill until it's clean twice in a row, then drops back to dormant.

## Active blockers

### B-2 · M-003 — `range(len(x))` scramble  🟡 *(escalated Day 16 — light)*
Index-loop range/len ordering keeps getting scrambled: `range(x)` (Day 1), `range(x)` (Day 4), `len(range(s))` (Day 16). He *knows* the idiom (fixes it instantly on a nudge) — a low-frequency slip under load, so this is a **light** drill, not a heavy one.

**Drill — 5-second pre-empt:** at session start, write `for i in range(len(x)):` once from memory; on any index loop, read it back — is it `range(len(x))`, not `len(range(x))`?
**Clears when:** two consecutive sessions with zero range/len scrambles ⇒ back to `MISTAKES.md` as dormant. *(Day 17: clean ✅ — `range(len(nums))` / `range(len(s))` correct — 1 of 2.)*

*(Also on the watchlist at recurrence 2: forgetting `return`, `()` vs `[]`, hidden in-loop Big-O cost, binary-search direction (M-012), converging-return (M-015).)*

## Resolved / dormant

### B-1 · M-004 — wrong-variable / naming imprecision  ✅ *(CLEARED Day 16)*
Escalated Day 11 (kept #125 red for 5 sessions). **Cleared after two consecutive clean-on-names sessions (Day 15 + Day 16)**, capped by a fully clean #125 (Day 14) and clean 3Sum/#424 (Day 16). History: `nums.add`/`seen.add` (Day 1), `s`/`clean` (Day 9), `.isalum` (Day 10), `strs`/`s` + `nums`/`numbers` (Day 11), `appened`/`append` (Day 12), `self.stack`/`self.minStack` (Day 14). **Keep the variable audit as a standing habit** — if a wrong-name slip recurs, re-escalate.

## How a blocker clears
1. A targeted micro-drill at the start of the next 2–3 sessions (e.g., write 3 list-method calls correctly from memory).
2. Two clean reps in a row with no occurrence ⇒ move back to `MISTAKES.md` as `dormant`.
