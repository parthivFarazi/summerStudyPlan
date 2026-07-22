# Blockers — drill now

> A mistake that recurs **≥ 3 times** is no longer a slip — it's a habit to break. It escalates here from `MISTAKES.md` and gets an explicit drill until it's clean twice in a row, then drops back to dormant.

## Active blockers

> **⚠️ Days 22–24 — the honest read.** All the blockers are **one disease: first-draft precision on problems he has ALREADY solved correctly in his head.** The drill = **questions said OUT LOUD before any submit.** And it WORKS: **Day 24 cleared B-4 AND B-5.** Two facets clear; the disease persists in new facets (B-7 emerged same day).
>
> **✅ Day 27: B-6 CLEARED — no drill-now blocker for a moment. ⚠️ Day 28: B-7 RE-ESCALATED (fired #211 Day 27 AND #146 Day 28).** The disease is unchanged; Days 27–28 it lived at the EDIT level — **M-027: one site missed on the final pass** (a transform/rename/paired-op/name/guard/`self.` that lands on all-but-one site). Every reset both days = reconstruct-correct-then-lose-one-site.
>
> **⚠️ THE ONE SCAN (Days 22–28).** Every recurring impl slip is **one disease: first-draft completeness.** **Before every submit, walk the operation top to bottom AND do a final read-through of every site:**
> 1. **Guard present?** — empty? None? lengths? (B-4 — reopened Day 26, fired Day 28 #199 dropped root guard)
> 2. **Terminal line / mark written?** — `isEnd = True`, the final set (M-026)
> 3. **Does every branch return?** (B-3 — watch)
> 4. **All args passed?** — `heappush(h, x)` not `heappush(x)`
> 5. **Whose thing is every attribute / method?** — `self.remove` not `remove`, `node.isEnd` not `isEnd` (**B-7 — DRILL-NOW, Day 28**)
> 6. **Which side can still contain the answer?** — target-first (B-6 — CLEARED Day 27 ✅)
> 7. **Multi-site change complete? Every name real?** — negate hits push/pop/return; a rename hits every occurrence; no `curr` where `curr3` belongs (**M-027 — the through-line**)

### 👁 B-4 · M-011 — dropping edge-case guards  *(CLEARED Day 24 — watch REOPENED Day 26)*
Cleared Day 24, but recurred Day 26: **#102 dropped BOTH None-guards it had on Day 23** — the root-`None` check and the `if node.left / if node.right` before enqueuing → a `None` gets enqueued → `node.val` crashes.
**Drill — pre-submit edge scan, OUT LOUD:** *"empty? single? none-found? lengths equal? is this None? (for BFS: are the children None before I enqueue them?)"* Full re-escalation to drill-now if it recurs again.

### 👁 M-026 · dropped the terminal line of an operation  *(NEW Day 26, watch — 1 rep from a blocker)*
Forgot **`node.isEnd = True`** at the end of a Trie `insert`/`addWord` — **twice the same session** (#208 review, #211) → every `search` returns False. An operation isn't finished when the loop ends; the **completing line** (the mark, the return, the final set) is part of it.
**Drill:** after the loop, ask *"did I mark/return the result?"* Kin to B-4 (guard) and B-3 (return) — all "first draft leaves a required line out."

### B-7 · M-020 — the `self.` / attribute-ownership rule  🔴 *(RE-ESCALATED Day 28 → DRILL-NOW)*
Cleared Day 26, then fired **two days running**: **#211 (Day 27)** `dfs(0, root)`→`self.root` and `return isEnd`→`node.isEnd`; **#146 (Day 28)** `remove(lru)`→`self.remove` — an attribute or method used without naming its owner.
**Drill (start of next 2–3 sessions): before submit, point at every attribute/method and ask "whose thing is this?"** — attached via `self.x=` or a method of this class → `self.`; a field of an object → `object.field`; parameter/local → bare. **Clears when:** two consecutive sessions with zero ownership slips.

### 👁 M-027 · one site missed on the final pass  *(the through-line of Days 27–28 — drill the final read-through)*
The reconstruction is correct; a change/name/paired-op lands on all-but-one site. Day 27: negation #1046, rename #215, evict #973. Day 28: `curr`/`curr3` #143, root guard #199, `self.` #146. **Drill: a deliberate final read-through** — enumerate every site a change touches (in/out/return · every occurrence of a renamed var · both halves of a paired op · every guard · every attribute's owner) and confirm each. This one habit turned Day-28's 3 resets into 3 avoidable ones.

### B-6 · M-012 — inverted search direction  ✅ *(CLEARED Day 27 — was the last drill-now blocker)*
> **Cleared Day 27:** #235 target-first, zero inversion, 2:27 — rep 2 after Day 24. The mechanical fix held cold and even transferred to #973's negated max-heap compare. Keep "which side can contain the answer? — target-first" as a standing habit; re-escalate on recurrence. History below.
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
**Cleared:** two consecutive sessions with zero direction inversions. *(Day 23: FAILED ❌ · Day 24: CLEAN ✅ · **Day 27: CLEAN ✅ → CLEARED.**)*

### B-3 · M-001 — forgetting `return`  🟡 *(watch REOPENED Day 24)*
Cleared Day 21, but recurred on Day 24: **`get` fell off the end of #146 with no `return node.val`** → returned `None` on a cache hit. One slip, in the hardest problem of the sprint, among four precision bugs — but the standing rule is **re-escalate on any recurrence.**
**Drill — the pre-submit "does it return?" check is MANDATORY again** on every function that's supposed to hand back a value. **Full re-escalation to drill-now if it recurs once more.**

*(B-1 names (Day 16), B-2 range/len (Day 18) — cleared, standing habits. **B-4 dropped guards and B-5 container-vs-contents CLEARED Day 24 — see below.** Watchlist at recurrence 2 — each one rep from escalating: **`if` where a `while` belongs (M-018 — Day 17, Day 22)**, **importing a template's BODY (M-009 — Day 8, Day 23)**, **dual-structure sync (M-024 — Day 24)**, `()` vs `[]` (M-002), hidden in-loop Big-O (M-006), space-scales=O(n) (M-005), for/while (M-016).)*

## Resolved / dormant

### B-7 · M-020 — the `self.` rule  ✅ *(CLEARED Day 26)*
Escalated Day 24 (recurrence 3: `minStack` #155 Day 19, `invert(...)` calls #226 Day 21, `self.node` + bare `remove()` calls #146 Day 24). **Cleared after two clean sessions (Day 25: #146 rebuild + #104; Day 26: #146 rebuild again — both perfect on `self.`).** The test (in [`python-classes.md`](../patterns/python-classes.md)): attached via `self.x=` or a method of this class → `self.`; parameter/local → bare. **Keep the test as a standing habit; re-escalate on recurrence.**

### 👁 M-025 · pointer surgery  *(watch cleared Day 26 — dormant)*
#146 `addFront` 2-of-4 pointers, #226 swapped locals (Day 25). **Day 26 clean — #146 all 4 pointers, #226 mutated the fields.** Keep: **count the pointers (insert-between = 4, remove = 2); mutate the field, not a local.**

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
