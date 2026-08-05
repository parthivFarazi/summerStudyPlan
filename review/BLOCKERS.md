# Blockers — drill now

> A mistake that recurs **≥ 3 times** is no longer a slip — it's a habit to break. It escalates here from `MISTAKES.md` and gets an explicit drill until it's clean twice in a row, then drops back to dormant.

## Active blockers

### ⛔ B-10 · M-006 — price the loop body  *(ESCALATED Day 36, from 🎯 Mock #1)*
**Third occurrence, and the first one with a measured cost.**

```python
while right <= len(s2):
    key1 = "".join(sorted(s1))            # loop-INVARIANT, recomputed every pass
    key2 = "".join(sorted(s2[left:right]))
    ...
```

Stated `O(n log n)`. Actually **`O((n − m)·m log m)`** — worst case `O(n² log n)`. Measured at the constraint ceiling (`len ≤ 10⁴`):

| version | time |
|---|---|
| as submitted | **5.67 s** ⛔ TLE |
| `key1` hoisted out of the loop | **2.80 s** ⛔ still TLE |
| `O(n)` rolling frequency count | **0.001 s** ✅ |

**History:** Group Anagrams called `O(n)` with a hidden `sorted()` (Day 3, Day 8). Same disease, identical cause, three difficulty tiers apart.

**🔧 THE DRILL — two habits, both said out loud:**
1. **Before stating any complexity:** *"one pass of this loop costs ___."* Multiply by the number of passes. **An `O(m log m)` operation inside an `O(n)` loop is `O(n·m log m)`.**
2. **Before writing a line inside a loop, ask: does this depend on the loop variable?** If not, it belongs outside. Hoisting `key1` alone halved the runtime for free.

**Cleared when:** two consecutive sessions in which every stated complexity correctly accounts for in-loop costs, and no loop-invariant computation appears inside a loop.

> **📉 Day 37 — no progress.** Three prompts were needed to get both halves of a complexity, and he volunteered them **zero** times across four problems. He also priced the naive `#70` recursion as `O(n)` when it is `O(2ⁿ)` (**M-042**) — *"it computes n, then n−1, then n−2"* describes a chain, but each call makes **two** calls. **Same disease from the other side: he priced one call rather than the number of calls.**
> **The drill is one sentence and it is not optional:** *"one pass costs ___, there are ___ passes."*

> **📈 Day 38 — FIRST REAL MOVEMENT, and one large miss.**
> **🟢 Volunteered both halves twice, unasked** — `2n−1` centres on `#5` (*"which has a big O of `O(n)`"*), and the memoized `#91` bound with **both space sources named**, dictionary *and* call stack. Day 37 that number was **zero**.
> **🟢 Self-corrected the trap.** Asked whether `s[i-2:i]` makes one pass `O(n)`, he said **yes** (over-correcting from `#5`), then reversed himself into the complete drill sentence: *"it is always O(2) so essentially it is O(1) so a single pass costs O(1), and there are n passes."*
> **🔴 But M-042 fired again, one day later, identically:** he wrote the un-memoized `#91` recursion and priced it `O(n)` using *"there are `n` passes"*. **Measured: 3,524,577 calls at n=30, ×11.1 per +5 chars, and 1.15×10²¹ calls ≈ 7.3 million years at the n=100 ceiling.**
> **🔴 And he guessed `len()` costs `O(n)`.** It is `O(1)` — a `str` stores its own length. **The cost is the SLICE.**
>
> ## 🔑 The generalisation, and it is the most valuable thing Day 38 produced
> **He prices his INTENT, not his CODE.** Day 37: the intent was "walk down the chain", the code branched. Day 38: the intent was "loop over n", the code recursed. **Both times the bound he stated was correct — about a program he had not written.**
>
> **⛔ THE DRILL IS NOW TWO QUESTIONS, IN THIS ORDER:**
> 1. **"Is what I wrote a LOOP or a RECURSION?"** — look at the code, not the plan.
> 2. **Loop ⇒ *"one pass costs ___, there are ___ passes."* Recursion ⇒ *"one call costs ___, there are ___ CALLS."*** Never "passes" for a recursion.
>
> **📈 Day 38 TAIL (Aug 5) — EIGHT complexities volunteered unasked across seven review items, zero prompts.** Day 37: zero. Day 38 Block 2: two. **This blocker is genuinely moving.** Every one was in the drill shape — *"O(1) work per iteration and there are n iterations"* — and the space half was correct every time, including `#200`'s `O(m·n)` recursion depth and `#91`'s *"O(n) space because of the recursion and dictionary"* (both sources named).
>
> **🔴 THE REMAINING EDGE, and it is the interview-grade one: AMORTIZED analysis.** On `#739` Daily Temperatures he said *"each iteration requires O(1) work."* **It does not — the inner `while` can pop many times in one pass, so a single iteration can cost `O(n)`.** The bound comes from counting **total** pushes and pops across the whole run: each index enters once and leaves at most once.
> **⛔ New drill line: when a loop body contains its own loop, "one pass costs ___" is almost always FALSE. Say instead "each element enters and leaves once, so total work is ___."**
>
> **🔴 Minor, same family:** `#121`'s `minVal = max(nums)` is a full extra `O(n)` scan before the loop starts — doesn't move the bound, walks the array twice to avoid choosing a starting value. `prices[0]` or `float('inf')` is free. **Same disease as Mock #1's un-hoisted `key1`.**

> **And the slice rule, settled:** a slice costs `O(k)` in its **WIDTH**. `s[left+1:right]` on `#5` is width up to `n`; `s[i-2:i]` on `#91` is width 2 forever. **Same syntax, different cost — read the indices, not the operator.** `len()` is never the expensive part.


### ⛔ B-5 · M-036 — container vs contents, REOPENED  *(Day 35 — three identical failures)*
**`#133 Clone Graph` has now failed three sessions running, and every failure is the same question: *which `neighbors` list?***

| | the line | what went wrong |
|---|---|---|
| Day 33 | `Node(node.val, node.neighbors)` | passed the **original's** list into the clone |
| Day 34 | `Node(node.val, node.neighbors)` | identical |
| Day 35 | `for neighbor in adict[node].neighbors` | walked the **clone's** empty list |

**⚠️ On Day 35 his notes were open and he still mis-picked.** That rules out recall. Two objects share the attribute name `neighbors`, and `node.neighbors` versus `adict[node].neighbors` are nearly identical on the page.

**🔧 THE DRILL — mechanical, not attentional:**

```python
clone = Node(node.val, [])
adict[node] = clone
for neighbor in node.neighbors:                 # the ORIGINAL's list
    clone.neighbors.append(dfs(neighbor))       # the CLONE's list
```

1. **Give the second object its own name.** `node` and `clone` are two different words; the confusion becomes impossible rather than merely avoidable.
2. **Whenever two variables carry the same attribute name, say each access out loud as *"the ___'s list"*** before writing it.
3. **When two things are easy to confuse, change the names — don't try harder.** Same move as `answer[-1]` replacing `pop()` + `append()` on `#56`.

**Cleared when:** `#133` passes twice consecutively, and no further container-vs-contents slip appears.

> **🔴 Day 38 — FIRED HARD, on a problem with no graph in it. Clean streak reset to 0.**
> `#91` took **1:42:00**, and roughly an hour of that was a single base case. He would not accept `ways(0) = 1`:
>
> > *"if it's empty shouldn't it be 0 because there are 0 letters to it"*
>
> **He was counting the CONTENTS when asked to count the CONTAINERS.**
>
> | question | answer |
> |---|---|
> | how many **letters** in the decoding of `""`? | **0** — he was right |
> | how many **decodings** does `""` have? | **1** |
>
> ```
> decodings of ""   =  { [] }    ONE element, which happens to be empty
> decodings of "0"  =  {   }     ZERO elements — this is what a real 0 looks like
> ```
>
> **`{ [] }` is not `{ }`.** A box containing an empty bag is not an empty box.
>
> **Four prose explanations failed** (the arithmetic proof, `0`=impossible/`1`=already-done, routes-from-your-house-to-your-house, one-way-to-climb-zero-stairs). He wrote `ways("") = 0` **three times**, twice immediately after being handed `1`, and on `"10"` produced the right total from **two cancelling errors** — crediting `[1, 0]`, which is not a decoding, and discarding `[10]`, which is the answer.
>
> **What finally worked: `viz/decode-ways-dp.html`**, stepping the dp table cell by cell and printing **the actual SET of decodings at each cell**, so `ways(0) = { [] }` sits beside `ways(1) = { }`. *(Rule 9: when prose fails on a counting/recursion concept, visualise — third time this has been the thing that landed it.)*
>
> **⛔ The drill extends beyond `#133`.** Whenever a count is in play, say which of these is being counted **out loud, before answering**: *"am I counting the things, or what's inside the things?"* This blocker is not about graphs. It is about **holding a container distinct from its contents, anywhere.**


### ✅ B-9 · M-001 — the recursive return channel — **CLEARED Day 36**
> **Two clean sessions.** Day 35: `#207` passed first-draft on exactly the line that reset it the day before. Day 36: the return was caught correctly on **all five** solves — `#210`'s `if not dfs(child): return False`, `#133`'s `clone.neighbors.append(dfs(neighbor))`, and `#323`'s deliberately-returns-nothing `dfs`. **The drill worked.** *"The callee hands me back ___, and I catch it at ___"* stays a standing habit; re-escalate on recurrence.

### ~~⛔ B-9 · M-001 — the recursive return channel~~  *(escalated Day 34, CLEARED Day 36 — kept for the record)*
**Twice in one session, two hours apart, on two different problems:**

```python
for child in adj[node]:
    dfs(child)                      # #207 - the False evaporates
for neighbor in node.neighbors:
    dfs(neighbor)                   # #133 - the clone is never appended
```

`#207` then **passed every `True` case and failed every `False` case** — the cycle *was* detected and the answer landed nowhere. `#133` returned a "clone" wired to the four original nodes.

**Why it's a blocker and not a slip:** he would **never** drop a return value in ordinary code. It only happens **across a recursive boundary**, because there it feels like the callee *does something to shared state* rather than *hands back an answer you must catch*. Same root as `#110`'s box-pattern wobble (Day 27 — what does the return channel carry vs what does the box collect) and `#1046`'s un-negate-on-the-way-out.

**🔧 THE DRILL — before writing ANY recursive function, one sentence out loud:**
> ***"The callee hands me back ___, and I catch it at ___."***

If the answer is *"nothing"*, that had better be deliberate — a `dfs` that only mutates shared state and returns nothing is legitimate (`#200`), but then the function must have **no** `return` value anyone depends on. **Mixed intent is the bug.**

**Cleared when:** two consecutive sessions with zero dropped or uncaught recursive returns.


### ⛔ B-8 · M-029 — naming precision  *(ESCALATED Day 33 · **RESCOPED Day 34**)*
> **⚠️ Rescoped 2026-07-29.** Three of Day 33's catches were **the coach's fault** — he writes in a bare IDLE and never sees LeetCode's stub, and I hadn't been supplying the signature on review prompts. **I now give the exact signature every time.** The blocker's scope is now: **names that were visible in front of him and still came out wrong** (`node.neighbor` with `self.neighbors` three lines above) and **constructs misnamed in narration** (`while` → "guard", "entry walks", "tree" for a graph). Invented method names, absent a supplied signature, do not count. **Valid Day-34 instances: 1.**
**Six consecutive sessions of names being slightly wrong, and on Day 33 it stopped being cosmetic.**

- **Day 31** — called #90's dedup `while` loop "a guard", then "a guard with a while loop", then "the if statement guard". Code correct every time.
- **Day 32** — **four method names renamed**: `exist` → `wordSearch`, `merge` → `mergeInterval`, `insert` → `insertInterval`, `eraseOverlapIntervals`. Plus *"the mid value… that is the index"* (B-5 flavour).
- **Day 33** — **`for neighbor in node.neighbor:`** on #133, with `self.neighbors` written **three lines above** in the class definition. **The algorithm was correct at submission two; this typo cost the third submission.**

**Why it's a blocker and not a nitpick.** `GOALS.md` records that interviewers probe *"what does this line do — remove it, what breaks?"* A candidate who calls a `while` loop an "if guard", invents a method name the problem already gave him, and mistypes an attribute he defined himself reads as **not knowing his own solution** — regardless of whether the algorithm is right. And as of Day 33 it also breaks the code.

**🔧 THE DRILL — three parts, every session until two consecutive clean ones:**
1. **The problem gives you the method name. Use it.** Before writing the signature, read the name off the problem statement. Never invent, never paraphrase.
2. **Read attribute names off the definition, don't recall them.** If a class is in the file, look at it. `neighbors` is not a thing to remember when it's on screen.
3. **Name the construct you just wrote, out loud, correctly.** "This is a **while** loop that skips duplicate copies" — not "a guard". If the word doesn't come, that's the tell: go and read it.

**Cleared when:** two consecutive sessions with zero renamed methods, zero mistyped attributes, and zero misnamed constructs in narration.


> **⚠️ Days 22–24 — the honest read.** All the blockers are **one disease: first-draft precision on problems he has ALREADY solved correctly in his head.** The drill = **questions said OUT LOUD before any submit.** And it WORKS: **Day 24 cleared B-4 AND B-5.** Two facets clear; the disease persists in new facets (B-7 emerged same day).
>
> **⛔ Day 37: B-10 — NO progress (three prompts, zero volunteered; M-042 added). B-5 and B-8 not exercised (#133 not due). ✅ B-9 remains cleared.** *(Day 30: B-7 cleared on its 2nd clean session.)* The disease's remaining residue is **M-027: one site missed on the final pass** (a transform/rename/paired-op/name/guard/`self.` that lands on all-but-one site) — now on *watch*, not drill-now, and its one twice-identical *repeat* (#1046 un-negate) closed Day 30. Day 30's resets all landed on the **newest pattern (backtracking)**, not on any named old facet — the fragility has migrated to fresh material, which is exactly the goal.
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

### B-7 · M-020 — the `self.` / attribute-ownership rule  ✅ *(CLEARED Day 30 — 2 clean sessions)*
Cleared Day 26, fired Day 27 (#211) + Day 28 (#146) → re-escalated. **Day 29: HELD** (#211 ownership all correct first-draft; #146's one miss a confirmed paste-drop). **Day 30: HELD again** — the start-of-session micro-drill answered cleanly (*"call `self.expand` but `dfs` is good as it is"* — nested-def-bare vs method-`self.` distinction solid), and #211's ownership was correct first-draft on the exact problem that fired it. **2 clean in a row → CLEARED → standing habit.** The real gap was always execution, not knowledge; the final read-through closed it.
**Standing habit: before submit, point at every attribute/method and ask "whose thing is this?"** — `self.x=`/method of this class → `self.`; a field → `object.field`; param/local/nested-`def` → bare. Re-escalate on recurrence.

### 👁 M-027 · one site missed on the final pass  *(the through-line — the twice-identical repeat CLOSED Day 30)*
The reconstruction is correct; a change/name/paired-op lands on all-but-one site. Day 27: negation #1046, rename #215, evict #973. Day 28: `curr`/`curr3` #143, root guard #199, `self.` #146. Day 29: #1046 return-negation (repeat), #199 enqueue, #211 ×3. **Day 30: the repeat CLOSED** — #1046's `return -maxHeap[0]` correct first-draft; residual nudges on the new #79 (dropped **left** from the 4-neighbor line; `dfs(0,0,0)` vs `dfs(r,c,0)`). **Drill: a deliberate final read-through** — enumerate every site a change touches (in/out/return · every occurrence of a renamed var · both halves of a paired op · every guard · every attribute's owner · **every direction in a neighbor sweep**) and confirm each.

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
