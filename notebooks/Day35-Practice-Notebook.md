# Day 35 — 2026-07-31 (Fri)
## Graphs cont. — #210 Course Schedule II, #323 Connected Components · Block 1 **2/5**

> **The day in one line:** Block 2 halved its time against yesterday, and **all three Block 1 failures were correct algorithms that never executed.**

---

# Warm-up ✅ — the two sets, cold

Both definitions right first try. But asked *what breaks*, you gave the definitions again — so the follow-up mattered:

| delete… | result |
|---|---|
| **`visited`** | **right answer**, 4,194,163 calls instead of 127 |
| **`path`** | **wrong answer**, fast |

> **`visited` is a speed guarantee. `path` is a correctness guarantee. One is an optimisation, one is the algorithm.** Know which of your data structures is which — interviewers ask that directly.

---

# Block 2 — new material (ran first)

## #210 Course Schedule II — ✅ **17:21**

**You derived it yourself:** *"when we add to visited, we add it to a list and then return the reverse of the list."* Your first instinct — *"right before unchoosing"* — was the same moment in the function. **`#207` plus two lines.**

### Why the finish order is backwards
Your stack intuition was right; the precise version is:

> **Every node that finishes before `X` is reachable FROM `X`** — it depends on `X`. So `X` must come **before** all of them. Finish-order lists dependents first, prerequisites last; reversing fixes it.

*(One label was backwards: the **last** node to finish is at the **bottom** of the stack — the course you started from, a prerequisite — and it lands **first** after the reverse.)*

### 🔴 The bug: `return answer` inside the loop

```python
for node in range(numCourses):
    if not dfs(node):
        return []
    else:
        answer = revAnswer[::-1]
        return answer            # <- loop runs exactly ONCE
```

**2,103 of 5,000 random inputs failed.** Every failure was a graph with more than one component:

```
component A      component B      C      D
   0                 2            4      5
   |                 |          (alone) (alone)
   v                 v
   1                 3

your loop: dfs(0) -> visits 0,1 -> returns [0,1]. Nodes 2,3,4,5 never reached.
```

**It survived every example I gave** because they all had one component, where `dfs(0)` does the whole job. `numCourses = 2, prerequisites = []` catches it in one second.

> **`return` inside a loop means "done after ONE iteration."** Ask what the loop's job is — here, *"every node has been started from"*, only true **after** it ends.
>
> **`return []` genuinely belongs inside** — one cycle anywhere is enough. **An early EXIT lives inside the loop; a CONCLUSION lives after it.** Two different things.

Fixed version: 11 named cases + **30,000 random** — zero failures.

---

## #323 Connected Components — ✅ **31:14**

**You transferred it from `#200` yourself** once asked *"how did you know the next `1` was a different island?"* — the `seen` set replaces the `"#"` flood, and the counter sits beside the call in the outer loop.

**Two judgment calls you made correctly without being told:**

1. **You didn't bring `path` over.** `#207` needed it; undirected connectivity has no cycle question. **Transferring a pattern without transferring the parts you don't need is the hard half of pattern recognition.**
2. **Your `dfs` returns nothing — and that's right.** With B-9 live, be explicit: the drill is *know what the callee hands back*, not *always catch a return*. Here the answer is **nothing, deliberately**. **Mixed intent is the bug.**

**Undirected ⇒ two appends per edge**, into two *different* lists. No guard needed — that's what undirected means, and it's exactly the `2E` from Day 33's warm-up.

### 🔑 The space discussion — worth more than the problem

You said `O(V)`. It's `O(V + E)`, and the reason is a rule you now own:

> **Count the space YOU allocate, not the space the input arrived in.**
> `#133` was `O(V)` because the `neighbors` lists **came inside the input nodes**. `#323` is `O(V + E)` because **you build the adjacency yourself** — `V` keys plus `2E` entries.

And the sub-question you asked — *"isn't a dictionary's space just its number of keys?"*:

```python
d = {0: [1, 2, 3, ..., 1_000_000]}     # one key. NOT O(1).
```

> **A container's space is its own overhead PLUS the total size of everything it holds.** Same rule as Timsort's `O(n)` scratch on `#56`, and as the BFS queue on `#994`. M-005 in a third costume.

Verified: 8 named cases · **every possible simple graph on ≤4 nodes, exhaustively** · 20,000 random incl. self-loops and duplicate edges · a 900-node chain. Zero mismatches.

**Block 2 total: 48 minutes for two new problems, against 116 yesterday.**

---

# Block 1 — **2 / 5, 26:12**

| # | Item | Time | Result | → |
|---|---|---|---|---|
| 133 | Clone Graph | 3:40 | ❌ walked the clone's empty list · notes peek | **1d (reset ×3)** |
| 46 | Permutations | 4:22 | ❌ `backtrack()` never called | **1d (reset ×2)** |
| 74 | Search a 2D Matrix | **4:26** | ✅ | 3d |
| 994 | Rotting Oranges | 7:51 | ❌ `range(grid)` → TypeError | **1d (reset)** |
| 207 | Course Schedule | **5:38** | ✅ | 3d |

## 🔴 The finding: three correct algorithms that never ran

```
#133   for neighbor in adict[node].neighbors    walked the wrong object's list
#46    (backtrack never invoked)                the function was never called
#994   for r in range(grid)                     range() of a list -> TypeError
```

**Not one is an algorithm.** I ran `#994` with `len()` added and nothing else changed: **every 6-cell grid and 20,000 random grids passed.** `#46` with one `backtrack()` line: every permutation correct. `#133`'s structure was right, `None` guard included — the one you'd missed yesterday.

> **All three crash or return empty on the FIRST example.** `range(grid)` is a `TypeError` — the program doesn't start. **The gap between your solve rate and your pass rate is one execution.**

## 🔴 #133 — three sessions, one ambiguity

| | the line | what went wrong |
|---|---|---|
| Day 33 | `Node(node.val, node.neighbors)` | passed the **original's** list into the clone |
| Day 34 | `Node(node.val, node.neighbors)` | identical |
| Day 35 | `for neighbor in adict[node].neighbors` | walked the **clone's** list instead |

**Every failure is the same question: *which `neighbors` list?*** And this time **you had your notes open and still got it wrong** — so it isn't recall. When two objects both have an attribute called `neighbors`, you don't have a firm grip on which is which.

> **Prescription — give the clone its own name:**
> ```python
> clone = Node(node.val, [])
> adict[node] = clone
> for neighbor in node.neighbors:                 # the ORIGINAL's list
>     clone.neighbors.append(dfs(neighbor))       # the CLONE's list
> ```
> `node` and `clone` are two different words. `node.neighbors` and `adict[node].neighbors` are two nearly-identical expressions and you have mis-picked between them three sessions running. **When two things are easy to confuse, stop relying on care and change the names.** Same move as `answer[-1]` replacing `pop()` + `append()` on `#56`.

## The two passes

**#74 ✅ 4:26** — `while left <= right` correct, paired with `right = mid - 1`. **The exact thing that reset it yesterday held first-draft.** 10 named + 30,000 random matrices.

**#207 ✅ 5:38** — **`if not dfs(child): return False` first-draft.** That's B-9's exact failure from yesterday, caught cold. All 4,096 directed graphs on 4 nodes + 20,000 random.

> **The one problem where you applied the drill is the one that stopped failing.** That's not a coincidence and it's the whole argument for the drill.

---

# Bank these

- **An early EXIT lives inside the loop; a CONCLUSION lives after it.**
- **Post-order DFS = topological sort.** Append when the node finishes, then reverse.
- **`visited` is a speed guarantee; `path` is a correctness guarantee.**
- **Count the space YOU allocate.** A dict's space is not its key count.
- **`dfs` returning nothing can be correct** — mixed intent is the bug, not the absence of a return.
- **When two things are easy to confuse, change the names.**
- **`range(len(x))`, not `range(x)`.** *(B-2, reopened after 17 clean sessions.)*

---

# Day 36 (Sat Aug 1) — 🎯 **MOCK #1**

**The mock replaces Block 2 and runs FIRST, while you're fresh.**

- **Unseen medium from a pattern you already know · 35-minute hard cap · I say nothing until the timer stops · narrate as you go.** Then self-score: communication · problem-solving · technical correctness · testing.
- **Expected result: over 35 minutes. That is information, not failure.** One data point is noise; three is a trend.
- **Block 1 after it — 5 full solves, 30 min:** **#133 · #46 · #994** (resets) → **#210 · #323** (1d).
- **On `#133`: write `clone` as a named variable.** Say the B-9 sentence first: *"the callee hands me back the clone, and I catch it in `clone.neighbors`."*
- **And run every one of them before sending.** Three of today's five failures die to a single execution.
