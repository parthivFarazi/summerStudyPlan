# Blockers — drill now

> A mistake that recurs **≥ 3 times** is no longer a slip — it's a habit to break. It escalates here from `MISTAKES.md` and gets an explicit drill until it's clean twice in a row, then drops back to dormant.

## Active blockers

> **⚠️ Days 22–24 — the honest read.** All the blockers are **one disease: first-draft precision on problems he has ALREADY solved correctly in his head.** The drill = **questions said OUT LOUD before any submit.** And it WORKS: **Day 24 cleared B-4 AND B-5.** Two facets clear; the disease persists in new facets (B-7 emerged same day).
>
> **The reflexes, before every submit:**
> 1. **The `self.` test** (B-7): `self.x=` or a method of this class → `self.`; parameter/local → bare — **Day 25 CLEAN ✅ 1 of 2**
> 2. **Count the pointers · mutate the FIELD not a local** (M-025 — **NEW Day 25**; #146 `addFront` 2-of-4, #226 swapped locals)
> 3. **Does it return?** (B-3 — watch, Day 25 clean)
> 4. **Which side can still contain the answer?** — target-first (B-6 — 1 of 2, awaiting #235)
> 5. **Box or contents? / mutating the object's field or a local?** (B-5 — **watch reopened Day 25**: #226)
> 6. **Both structures in sync?** (M-024 — Day 25 clean) · looping where I should? (M-018) · what decides the next step HERE? (M-009)

### B-7 · M-020 — the `self.` rule  🔴 *(escalated Day 24 — recurrence 3)*
`self.` confusion inside a class, **both directions**:
- dropped it on an attribute (`minStack` vs `self.minStack`, #155, Day 19)
- dropped it on recursive **calls** (`invert(...)` vs `self.invert(...)`, #226, Day 21)
- **#146 (Day 24): `self.node` on a PARAMETER (spurious `self.`) AND `remove(node)`/`insert_front(node)` calls missing `self.`** — both errors in one class

**He KNOWS this rule** — he asked for it on Day 21 and it's written up in [`patterns/python-classes.md`](../patterns/python-classes.md). The problem is identical to B-4: **the rule exists, it just isn't run on the first draft.**
**Drill — run THE TEST on every `X.y` and every bare call inside a class:** *"Is it attached with `self.x =` in `__init__`, or is it a method of this class? → `self.`. Is it a parameter or a local? → bare."* `self.node` is nonsense because `node` is a parameter — it lives on no object.
**Clears when:** two consecutive sessions with zero `self.` slips. *(**Day 25: CLEAN ✅ — #146 rebuild + #104 both perfect on `self.`. 1 of 2.**)*

### 👁 M-025 · pointer surgery — count the pointers, mutate the field  *(NEW Day 25, watch — 1 rep from a blocker)*
Two related first-draft slips, same day: **#146 `addFront` wrote only 2 of the 4 required pointers** (dropped both backward links); **#226 swapped LOCAL `left`/`right` instead of `node.left`/`node.right`** (mutating a local doesn't touch the tree). Both are "the assignment doesn't do what I think."
**Drill:** *(1)* **count the pointers** — inserting a node between two others = **4** writes (2 fwd, 2 back); remove = **2**; if the helper has fewer lines, it's incomplete. *(2)* **mutate the object's FIELD** (`node.left = ...`), never a local copy. *(Kin to B-5 container-vs-contents.)*

### B-6 · M-012 — inverted search direction  🟡 *(escalated Day 22 — recurrence 4)*
Moving toward the half that **cannot possibly contain the target**.
- #704 — inverted the discard direction (Day 9)
- #33 — inverted **all four** pointer updates (Day 13)
- #235 BST — both-smaller, walked RIGHT (Day 22)
- **#235 AGAIN, same inversion, next day (Day 23)** — his own *comment* said "both left → go left"; the *code* did the opposite.

**🔧 THE MECHANICAL FIX (installed Day 23) — write the comparison TARGET-first.**
The inversion happens because he writes `node.val > p.val` (node-first) and then has to **mentally flip it** — *"node bigger than p ⇒ p smaller ⇒ p left"* — and **the flip is where he inverts.** Remove the flip:
```python
if p.val > node.val and q.val > node.val:    # "p, q BIGGER"  → go RIGHT  (word matches branch)
    node = node.right
elif p.val < node.val and q.val < node.val:  # "p, q SMALLER" → go LEFT
    node = node.left
else:
    return node
```
> **Rule: put the TARGET on the left of the comparison. `target > node → right`. `target < node → left`.**
> (Array BS: `target > nums[mid]` → answer is right → `left = mid + 1`.)

**Drill — say it, then spell it target-first:** ***"Which side can still contain the answer?"***
**Clears when:** two consecutive sessions with zero direction inversions. *(Day 23: FAILED ❌ · **Day 24: CLEAN ✅ — #235 target-first. 1 of 2.**)*

### B-3 · M-001 — forgetting `return`  🟡 *(watch REOPENED Day 24)*
Cleared Day 21, but recurred on Day 24: **`get` fell off the end of #146 with no `return node.val`** → returned `None` on a cache hit. One slip, in the hardest problem of the sprint, among four precision bugs — but the standing rule is **re-escalate on any recurrence.**
**Drill — the pre-submit "does it return?" check is MANDATORY again** on every function that's supposed to hand back a value. **Full re-escalation to drill-now if it recurs once more.**

*(B-1 names (Day 16), B-2 range/len (Day 18) — cleared, standing habits. **B-4 dropped guards and B-5 container-vs-contents CLEARED Day 24 — see below.** Watchlist at recurrence 2 — each one rep from escalating: **`if` where a `while` belongs (M-018 — Day 17, Day 22)**, **importing a template's BODY (M-009 — Day 8, Day 23)**, **dual-structure sync (M-024 — Day 24)**, `()` vs `[]` (M-002), hidden in-loop Big-O (M-006), space-scales=O(n) (M-005), for/while (M-016).)*

## Resolved / dormant

### B-5 · M-021 — container vs. contents  🟡 *(CLEARED Day 24 — watch REOPENED Day 25)*
Escalated Day 22 (recurrence 4 — the same index-vs-char bug reset #271 twice). Cleared after two clean sessions (Day 23–24). **Reopened Day 25:** #226 swapped LOCAL `left`/`right` instead of the node's `.left`/`.right` fields — same family (handle vs. thing, local vs. object-field). **Now tracked jointly with M-025 (pointer surgery) above.** Keep the *"am I changing the object's field, or just a local?"* check; full re-escalation if it recurs again.

### B-4 · M-011 — dropping edge-case guards  ✅ *(CLEARED Day 24)*
Escalated Day 20 (recurrence 6). History: anagram length check (Days 7, 20, 22), empty-stack guards (#20 Day 18, #739 Day 20), `node.left.val` no None-check (#226 Day 21). **Cleared after two clean sessions (Day 23: #242 guard + #141 `None==None` guard; Day 24: #739 empty-stack guard in both branches).** **Keep the pre-submit edge scan** — *"empty? single? none-found? lengths equal? is this None?"* — as a standing habit; re-escalate on recurrence.

### B-3 · M-001 — forgetting `return`  ✅ *(CLEARED Day 21 — but see watch, reopened Day 24 above)*
Escalated Day 19 (3rd occurrence: Day 4, Day 6, `return prev` on #206). **Cleared after two consecutive clean sessions (Day 20 + Day 21)** — Day 21 was 8-for-8 (six reviews + #104 + #226), every function handed its answer back. **Keep the pre-submit "does it return?" check** as a standing habit; re-escalate on any recurrence.

### B-1 · M-004 — wrong-variable / naming imprecision  ✅ *(CLEARED Day 16)*
Escalated Day 11 (kept #125 red for 5 sessions). **Cleared after two consecutive clean-on-names sessions (Day 15 + Day 16)**, capped by a fully clean #125 (Day 14) and clean 3Sum/#424 (Day 16). History: `nums.add`/`seen.add` (Day 1), `s`/`clean` (Day 9), `.isalum` (Day 10), `strs`/`s` + `nums`/`numbers` (Day 11), `appened`/`append` (Day 12), `self.stack`/`self.minStack` (Day 14). **Keep the variable audit as a standing habit** — if a wrong-name slip recurs, re-escalate.

### B-2 · M-003 — `range(len(x))` scramble  ✅ *(CLEARED Day 18)*
Escalated Day 16 (3rd occurrence: `range(x)` Day 1 & Day 4, `len(range(s))` Day 16). Cleared after two clean range/len sessions (Day 17 + Day 18). **Keep the 5-sec `range(len(x))` pre-empt** as a standing habit; re-escalate if it recurs.

## How a blocker clears
1. A targeted micro-drill at the start of the next 2–3 sessions (e.g., write 3 list-method calls correctly from memory).
2. Two clean reps in a row with no occurrence ⇒ move back to `MISTAKES.md` as `dormant`.
