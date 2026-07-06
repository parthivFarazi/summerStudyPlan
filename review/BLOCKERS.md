# Blockers — drill now

> A mistake that recurs **≥ 3 times** is no longer a slip — it's a habit to break. It escalates here from `MISTAKES.md` and gets an explicit drill until it's clean twice in a row, then drops back to dormant.

## Active blockers

### B-1 · M-004 — wrong-variable / naming imprecision  🔴 *(escalated Day 11)*
The algorithm is never the problem — a wrong variable name is. History: `nums.add`/`seen.add` (Day 1), `s`/`clean` (Day 9), `.isalum` typo (Day 10), `strs`/`s` + `nums`/`numbers` (Day 11), `appened`/`append` (Day 12), `self.stack`/`self.minStack` (#155, Day 14). It kept #125 red for **5 sessions**.

**Drill — "variable audit before every submit":** before sending any solution, scan each variable/method name against the names actually declared (parameters + your own vars): *"is it `s` or `strs`? `numbers` or `nums`? is `append` spelled right?"* Do it on every submit for the next 2–3 sessions.
**Clears when:** two consecutive sessions with **zero** wrong-name slips, self-caught (no nudge) ⇒ back to `MISTAKES.md` as dormant.
*(Day 11: audit cleared #125 ✅. Day 12: audit caught `appened`→`append` on #238 (nudged) — counter didn't advance. Day 14: #125 re-solved **fully clean** ✅ (correct `clean` / `.isalnum()`), BUT a `self.stack`/`self.minStack` mixup on the new #155 keeps the blocker active — clearing needs a session clean on BOTH reviews and new problems. Day 15: clean on names ✅ (correct `self.minStack` on #155) — 1st of 2 clean-on-names sessions; one more clean session clears it.)*

*(Also on the watchlist at recurrence 2, one repeat from escalating: forgetting `return`, `()` vs `[]`, `range(len(x))`, hidden in-loop Big-O cost.)*

## How a blocker clears
1. A targeted micro-drill at the start of the next 2–3 sessions (e.g., write 3 list-method calls correctly from memory).
2. Two clean reps in a row with no occurrence ⇒ move back to `MISTAKES.md` as `dormant`.
