# Blockers — drill now

> A mistake that recurs **≥ 3 times** is no longer a slip — it's a habit to break. It escalates here from `MISTAKES.md` and gets an explicit drill until it's clean twice in a row, then drops back to dormant.

## Active blockers

> **⚠️ Day 22–23 — the honest read.** Three blockers open, and **they are one disease: first-draft precision on problems he has ALREADY solved correctly in his head.** Treat as a single drill: **questions said OUT LOUD before any submit.**
>
> 1. **Box or contents?** (B-5) — **Day 23: CLEAN ✅ 1 of 2**
> 2. **Is it guarded?** (B-4) — **Day 23: CLEAN ✅ 1 of 2**
> 3. **Which side can still contain the answer?** (B-6) — **Day 23: FAILED AGAIN ❌ — now has a mechanical fix: write comparisons TARGET-first**
> 4. **Am I looping where I should loop?** (M-018 — recurrence 2, one rep from escalating)
> 5. **What decides the next step IN THIS problem?** (M-009 — recurrence 2, one rep from escalating; don't paste a template's body)
>
> **Day 23 progress:** B-4 and B-5 each got their **first clean rep** — one more clean session and both drop. **B-6 is the stubborn one.**

### B-5 · M-021 — container vs. contents  🔴 *(escalated Day 22 — recurrence 4)*
Reaching for the **handle** instead of the **thing it points at**.
- `while j != "#"` — compared the **index** to a **char**; needs `s[j]` (#271, Day 21 — **and the IDENTICAL bug again on #271, Day 22**)
- swapped `.val` instead of the `.left`/`.right` **subtree pointers** (#226, Day 21)
- used `left`/`right`, which hold **heights**, to count **nodes** in the res-drill (Day 22)
- *(caught pre-code, Day 22:* `p.left.val` *on #100 — the `None.val` crash again)*

**The same bug reset the same problem (#271) twice in a row.** That is what makes it a blocker and not a slip.
**Drill — say it out loud on every comparison and every variable use:** ***"Is this the box, or what's in the box?"*** `j` vs `s[j]` · `i` vs `nums[i]` · `node` vs `node.val` · `.left` (a NODE) vs `.val` (a NUMBER).
**And the Day-22 corollary:** ***being in scope does not mean being relevant.*** `left`/`right` sat right there looking useful; they were the wrong quantity. **Before you use a variable, say what it is actually holding.**
**Clears when:** two consecutive sessions with zero container/contents slips. *(**Day 23: CLEAN ✅ — #271 re-solved with `s[j]`. 1 of 2.**)*

### B-6 · M-012 — inverted search direction  🔴 *(escalated Day 22 — recurrence 4, the stubborn one)*
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
**Clears when:** two consecutive sessions with zero direction inversions. *(**Day 23: FAILED ❌. 0 of 2.**)*

### B-4 · M-011 — dropping edge-case guards  🟡 *(escalated Day 20 — recurrence 6)*
Keeps omitting a required guard: anagram length check (Day 7, **again on #242 Day 20, and AGAIN on #242 Day 22** — `"aab"`/`"ab"` returns `True`), empty-stack before pop (#20 Day 18), empty-stack guard in the #739 `while` (Day 20), **`node.left.val` with no None-check on #226 (Day 21) — crashes on every leaf**.
**Day 22 is the galling one: *"lengths equal?" is literally on his own checklist below.*** He knew the algorithm cold, wrote it in 3:11, and shipped without running the scan. The scan exists; **it isn't being run.**
**Drill — pre-submit edge scan, SAID OUT LOUD (not mentally):** *"empty? single element? none-found? **lengths equal?** **is this thing None?**"*
**Clears when:** two consecutive sessions with zero dropped guards. *(**Day 23: CLEAN ✅ — #242 guard present, #141 guarded the single-node `None==None`. 1 of 2.**)*

*(B-1 (names, Day 16), B-2 (range/len, Day 18), B-3 (return, Day 21) — all cleared; keep as standing habits. Watchlist at recurrence 2 — **each one rep from escalating**: **`if` where a `while` belongs (M-018 — Day 17 #15, Day 22 #235)**, **importing a template's BODY (M-009 — Day 8, Day 23 #143)**, `()` vs `[]` (M-002), hidden in-loop Big-O (M-006), space-scales=O(n) (M-005), for/while (M-016), missing `self.` (M-020).)*

## Resolved / dormant

### B-3 · M-001 — forgetting `return`  ✅ *(CLEARED Day 21)*
Escalated Day 19 (3rd occurrence: Day 4, Day 6, `return prev` on #206). **Cleared after two consecutive clean sessions (Day 20 + Day 21)** — Day 21 was 8-for-8 (six reviews + #104 + #226), every function handed its answer back. **Keep the pre-submit "does it return?" check** as a standing habit; re-escalate on any recurrence.

### B-1 · M-004 — wrong-variable / naming imprecision  ✅ *(CLEARED Day 16)*
Escalated Day 11 (kept #125 red for 5 sessions). **Cleared after two consecutive clean-on-names sessions (Day 15 + Day 16)**, capped by a fully clean #125 (Day 14) and clean 3Sum/#424 (Day 16). History: `nums.add`/`seen.add` (Day 1), `s`/`clean` (Day 9), `.isalum` (Day 10), `strs`/`s` + `nums`/`numbers` (Day 11), `appened`/`append` (Day 12), `self.stack`/`self.minStack` (Day 14). **Keep the variable audit as a standing habit** — if a wrong-name slip recurs, re-escalate.

### B-2 · M-003 — `range(len(x))` scramble  ✅ *(CLEARED Day 18)*
Escalated Day 16 (3rd occurrence: `range(x)` Day 1 & Day 4, `len(range(s))` Day 16). Cleared after two clean range/len sessions (Day 17 + Day 18). **Keep the 5-sec `range(len(x))` pre-empt** as a standing habit; re-escalate if it recurs.

## How a blocker clears
1. A targeted micro-drill at the start of the next 2–3 sessions (e.g., write 3 list-method calls correctly from memory).
2. Two clean reps in a row with no occurrence ⇒ move back to `MISTAKES.md` as `dormant`.
