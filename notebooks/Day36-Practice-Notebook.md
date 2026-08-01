# Day 36 — 2026-08-01 (Sat)
## 🎯 MOCK #1 (#567) + Block 1 **5/5**

> **The best session of the sprint, and the reason is one sentence: yesterday these same five problems went 2/5 with three correct algorithms that never executed. Today they went 5/5. Nothing about the understanding changed. The twenty seconds changed.**

---

# 🎯 Mock #1 — #567 Permutation in String

**The first unaided data point in 36 sessions.** Unseen problem, 35-minute cap, coach silent.

## Result: **19:38 — fifteen minutes under the cap, correct code**

I told you to expect over 35 minutes. Every previous new problem took 44–72 minutes *with* me talking.

**And you named the pattern in the first sentence** — *"this is very clearly a sliding window problem."* `GOALS.md` sets that gate at 2–3 minutes.

Verified: 9 named cases + **20,000 random string pairs** against brute force, zero mismatches.

## Scores

| | you | me | |
|---|---|---|---|
| **Communication** | 4.5 | **4** | genuinely good |
| **Problem-solving** | 2.5 | **2.5** | exactly right |
| **Technical correctness** | 1.5 | **2** | you were right to be unsure |
| **Testing** | 3 | **3** | agreed |

> **Your calibration is the quiet result here. You were least confident exactly where you were wrong and most confident exactly where you were right.** Four days ago you told me *"it does give 3"* about an output you hadn't computed. That's a real change.

## Communication — 4/5
Stated the return type, the length guard, and — the one that matters — **your index convention**: *"right refers to the index after the last word I want to compare."* Half-open intervals are where off-by-ones live; saying it out loud is what a good candidate does.

**Missing:** you never asked about constraints, and never said *"is there something better?"* aloud. Both are free points in a real room.

## Problem-solving — 2.5/5, and this is the finding

> *"If I were to take a more optimal route, I would have had to complicate it more by using a dictionary like the valid anagram question."*

**You identified the optimal solution and rejected it for being more complicated.**

In an interview that is not a reason to skip it — **it's the answer.** The interviewer's next words are *"can you do better?"*, and you write it anyway, now under time pressure.

**Say this instead:** *"Sorting each window is `O(m log m)`; a frequency map makes the comparison `O(26)`. Let me do that."* That sentence turns a partial into a pass.

## Technical correctness — 2/5: **it would TLE**

You said `O(n log n)`. It's **`O((n − m)·m log m)`** — worst case `O(n² log n)`. At the constraint ceiling:

| version | time |
|---|---|
| **yours** | **5.67 s** ⛔ |
| yours with `key1` hoisted out of the loop | 2.80 s ⛔ |
| `O(n)` rolling frequency count | **0.001 s** ✅ |

**Note the middle row.** `key1 = "".join(sorted(s1))` doesn't depend on the loop variable and is recomputed every single pass. **Hoisting that one line halves the runtime.**

> **M-006, third occurrence** — *not counting the cost of operations inside the loop.* Group Anagrams (Day 3), Longest Substring (Day 8), here. **Escalated to blocker B-10.**
>
> **The rule: when you write a loop, price the body.**

## Testing — 3/5
You tested, found a real bug (`while right > len(s2)` — the condition inverted), fixed it fast, and **reported it unprompted.**

**Missing:** only the provided examples. No edge cases of your own, and **you stated a complexity and never tested against the constraint ceiling** — which is exactly what would have shown you the problem.

## The `O(n)` fix — you derived it after one question

**"The window slides one position. How many characters actually change?"** → **Two.** One enters right, one leaves left. **So you never rebuild — you update.** Comparison over 26 slots is `O(1)`.

`#567` is now in the queue at 1d; you'll write the optimal version rather than lose Block 1 time to it today.

---

# Block 1 — **5 / 5, 52:53**

| # | Item | Time | Result | → |
|---|---|---|---|---|
| 133 | Clone Graph | **6:49** | ✅ | 3d |
| 46 | Permutations | **6:48** | ✅ | 3d |
| 994 | Rotting Oranges | **17:40** | ✅ | 3d |
| 210 | Course Schedule II | **11:40** | ✅ | 3d |
| 323 | Connected Components | **9:56** | ✅ | 3d |

**Three resets and two first retrievals. All five passed.** Every one verified hard — `#133` against 2,000 random connected graphs with object-identity checks; `#46` against 3,000 random inputs; `#994` and `#323` exhaustively over every small grid/graph plus 30,000 random; `#210` against 30,000 random with a validity checker.

## 🔑 The finding of the sprint so far

| | Day 35 | Day 36 |
|---|---|---|
| #133 | ❌ wrong object's list | ✅ **same bug in the first draft — caught by running** |
| #46 | ❌ `backtrack()` never called | ✅ |
| #994 | ❌ `range(grid)` → TypeError | ✅ |
| #210 | — | ✅ `return` outside the loop |
| #323 | — | ✅ 31:14 → **9:56, no prompt** |

> **Same five problems, one day apart, 2/5 → 5/5. Your understanding did not change overnight. You ran the code before sending it.** That is the entire delta, and it is now measured rather than asserted.

**`#133` is the proof.** Its first draft had `for neighbor in clone.neighbors` — the *identical* Day-35 bug — plus `.children` for `.neighbors`. You ran it, both surfaced, you fixed them and told me. Two sessions ago that arrives here broken and costs a reset.

*(One note: you named the clone and then wrote `graph[node].neighbors.append(...)` anyway. **Use the name.** The point of `clone` is that it can't be confused with `node`.)*

---

# The scheduling call — yours, and it was right

At the 30-minute mark with two items left, you asked to take a break and finish rather than push them to Monday. **You spotted that Monday carries three new DP problems and that adding two full solves would stack.** The arithmetic:

- Monday as planned: 8 items, 27.5 min, plus **first contact with DP**
- Plus `#210` and `#323`: **10 items, 39.5 min** — 30% over, on the least absorbent day of the week

**You took a real break and came back to a defined twelve minutes.** That isn't blowing the box; it's managing it — and it's the judgment the box exists to teach.

---

# Bank these

- **When a window slides, ask what actually CHANGED.** Usually two things. Update, don't rebuild.
- **Price the body of every loop.** `sorted()` inside a loop is never free.
- **Anything not depending on the loop variable belongs outside the loop.**
- **A bounded map (26 letters) is `O(1)` space and `O(1)` to compare.**
- **"I know a better approach but it's fiddlier" is not a reason to skip it — it's the answer.**
- **An early EXIT lives inside the loop; a CONCLUSION lives after it.** *(#210, held.)*

---

# Day 37 (Mon Aug 3) — DP begins

- **Block 2 — new: 1-D DP.** **#70 Climbing Stairs · #746 Min Cost Climbing Stairs · #198 House Robber.** First contact with an entirely new pattern, and **three** new problems — the heaviest teaching day of the sprint. Block 2 runs first.
- **Block 1 — 8 items, ~28 min:** full **#567** (write the `O(n)` version) → ✍️ **#200 · #79 · #39 · #57** → 🗣 **#739 · #121 · #153**.
- **⛔ B-10, new: price the loop body.** Before stating any complexity, say what one pass of the loop costs.
- **⛔ B-5: on `#133`, use the name `clone`.** One more clean pass and it closes.
- **✅ B-9 cleared** — two clean sessions. The recursive return channel held on all five solves.
- **Run everything before sending.** It is now the measured difference between 2/5 and 5/5.
