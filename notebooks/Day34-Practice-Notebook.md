# Day 34 — 2026-07-30 (Thu)
## Graphs cont. — #994 Rotting Oranges, #207 Course Schedule · Block 1 **3/6**

> **The day in one line:** four failures across four different problems, and **every one was the same disease — the exact identity of the value in front of you.** Not one was a comprehension gap.

---

# Warm-up — `O(V + E)` cold, no notes ✅

**5 nodes, 6 undirected edges → 12 entries.** Reason correct: each undirected edge is stored twice.

**Why `+` and not `×`, in your words:** *"along with the walks, you are doing a job at each vertex — it's not that you are doing E amount of work for each V vertices."* Two piles of work, added.

**That's the thing that had to be animated yesterday, back cold in under a minute.** The banking worked.

*(Two naming catches — B-8: **"entry walks"** fuses two different things. An **entry** sits in memory; a **walk** is traversing one. 12 entries exist before you run anything. And **vertex** is singular, **vertices** plural.)*

---

# Block 2 — new material (ran first)

## #994 Rotting Oranges — ✅ **1:12:18 total · 22:24 unaided**

### The wall you had to hit first

Your opening plan was DFS: find a rotten orange, recurse, take the longest depth. **You spotted the multi-source problem yourself** — *"if there are two, it will take less time, so I don't know how to go about that"* — which is the good instinct; most people submit the single-source version and let the judge tell them.

**But the plan was broken with a single source too**, and finding that was the point:

```
[[2,1,1],
 [1,1,1]]      true answer 3      your DFS reports 5
```

> **DFS depth is the length of the path it happened to take. It is not the shortest distance.** And the permanent mark makes it permanent — `(0,1)` got stamped at depth 3 when its real distance is 1, and once it's `"#"` nothing can correct it downward.
>
> **Time is a shortest distance.** So any algorithm whose answer depends on which branch it wandered down first cannot compute time.

**Why `#200` was fine with DFS:** it asks *"are these cells connected?"* — a yes/no that doesn't care about the route. `#994` asks *"how far?"* **That one word changes the traversal.**

### 🔴 What actually went wrong in that trace — and it wasn't the algorithm

Asked to trace *your* DFS, you answered with **the correct process** instead: *"at min 1, (0,1) and (1,0) rot…"* That's how the oranges rot. It is not what your code does.

Then, asked what the BFS counter ends at, you said **"it does give 3."** It gives **4**.

> **M-034 in its purest form: you are not checking what your code does — you are checking what the answer is, and assuming your code agrees.** Two different acts. The gap between them is every failed submission this month.

### The algorithm

```python
from collections import deque

def orangesRotting(grid):
    q, fresh, minute = deque(), 0, 0
    for r in range(len(grid)):                 # ONE pass, TWO jobs
        for c in range(len(grid[0])):
            if grid[r][c] == 1:   fresh += 1
            elif grid[r][c] == 2: q.append([r, c])

    while q and fresh > 0:                     # the guard IS the off-by-one fix
        for _ in range(len(q)):                # snapshot = exactly one level
            row, col = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = row+dr, col+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append([nr, nc])
        minute += 1

    return minute if fresh == 0 else -1
```

**Seed the queue with every source, and the hard part evaporates.** All sources sit at level 0 together, so level 1 is "one minute from *any* rotten orange." **You never compare sources. Multi-source BFS is single-source BFS with a fuller starting queue.**

**The off-by-one.** With a bare `while q`, the last level pops cells that rot nothing and `minute += 1` fires anyway:

```
minute = 3 | popped [(1,1),(0,2)] | queue now [(1,2)]
minute = 4 | popped [(1,2)]       | queue now []        <- the phantom minute
```

Your `minute - 1` fix was better than it looked — I tested **all 81 2×2 grids and 20,000 random grids**, and it's correct on every one **except a grid of all `0`s** (no rotten, no fresh → should be `0`, gives `-1`). You chose the `fresh > 0` guard instead, which has no such hole.

### 💡 `range(len(q))` is evaluated ONCE
You believed it re-evaluates and would grow. It doesn't — Python calls `len(q)`, builds a `range` from that number, and iterates *that*. `level_length = len(q)` first is harmless but unnecessary. **`while i < len(q)` *does* re-check every pass.** Know which constructs re-evaluate.

### Complexity
`O(m·n)` time · **`O(m·n)` space.** Measured peak deque on a 10×10: corner source **10**, centre source **19**, all-rotten **100**.
> **BFS space is the widest level — and in multi-source BFS the seeding IS a level.** (M-005, new face.)

### Code note
Your four `if` blocks are twelve lines where a `for dr, dc in (...)` gives four. **Four copies = four sites any change must land on — M-027**, and precisely how you dropped the **left** direction on `#79`. Also: mark `2`, not `"#"` — `2` already means rotten in this problem's own encoding.

---

## #207 Course Schedule — ✅ **43:52** (after one bug)

### What makes it `False`: **a cycle.**

**Corrections to the opening plan:** no sort — the dictionary doesn't care about order. No "find the start" — there may be several starting points or none, so **you try every node**. And it isn't level-order: BFS gives *distance*, and a cycle isn't a distance question.

### The question that IS the problem

Running a plain `visited` set on the diamond `0→1, 0→2, 1→3, 2→3`, node `3` gets hit twice. **Is that a cycle?** No.

You guessed *"3 is a leaf, 0 has children"* — killed by adding `3→4`: still not a cycle, and now `3` has a child.

Then you got it, and this is the sentence:

> **In the cycle case, the first `dfs(0)` has NOT returned yet. In the diamond, the first `dfs(3)` HAD returned.**
>
> **A cycle is not "I've seen this node before." A cycle is "I've seen this node before AND I'M STILL INSIDE IT."**

### 🔑 Two marks, two jobs — the idea of the week

| set | marked | un-marked? | job | drop it and… |
|---|---|---|---|---|
| **`path`** | on the way **in** | **yes** | detects the cycle | **wrong answer** |
| **`visited`** | when the node **finishes** | **never** | never redo a proven subtree | **right answer, exponential time** |

**You named `path`'s shape yourself: backtracking.** Add on the way in, remove on the way out — `#79`'s `board[r][c] = "#"` … `= temp`.

> **Graph traversal and backtracking are not two patterns. They are the permanent mark and the temporary mark.** Un-mark ⇒ explore **paths** ⇒ exponential. Never un-mark ⇒ visit **nodes** ⇒ linear. `#207` needs both at once.

**Measured cost of dropping `visited`** (answer stays correct, work explodes — each diamond doubles it):

| diamonds | nodes | edges | with `visited` | without |
|---|---|---|---|---|
| 10 | 31 | 40 | 71 | 16,299 |
| 18 | **55** | **72** | **127** | **4,194,163** |

### 🔴 The bug — and it's the oldest entry in your database

```python
for child in adj[node]:
    dfs(child)              # the answer is computed and thrown away
```

Every `True` case passed, **every `False` case failed** — the function could never return `False`. The cycle *was* detected; the `False` landed nowhere and evaporated.

**M-001: conflating computing a value with returning it.** And it was item three of the four I listed before you started writing.

Fixed version: **all 6 named cases · all 4,096 possible directed graphs on 4 nodes · self-loops · duplicate edges · 20,000 random graphs — zero mismatches.**

### Why intervals can't be used here *(good question)*
`[1, 0]` is **not** an interval — an interval is a range on a line, a prerequisite is an ordered pair of two labels. Decisive: both the acyclic and the cyclic examples contain "overlapping" pairs.

> **The general tool: test a proposed method against a symmetry the answer must respect.** Course labels are arbitrary — swap `0` and `5` everywhere and the answer *must* not change. **Any method that reads the numbers as positions is dead before you write it.** That kills intervals, sliding window and binary search on every graph problem at once.

### 🟢 And the honest thing you said
*"I pretty much just copied from whatever you have given me."* **Saying that was worth more than the working code.** It got the `viz/dfs-cycle-detection-stepper.html` animation built, and after stepping through it you produced the model unaided: *"DFS verifies each node, and when it's fine it goes into visited."*

*(One correction: **"every way through it is fine"** is path-language, and paths are exponential. Say **"nothing reachable from this node leads back into the path I'm currently on."** Node-language.)*

---

# Block 1 — 3 / 6

| # | Item | Tier | Result | → |
|---|---|---|---|---|
| 200 | Number of Islands | full | ✅ **7:17** | 3d |
| 133 | Clone Graph | full | ❌ **yesterday's two bugs, identical** | **reset 1d** |
| 90 | Subsets II | ✍️ | ✅ **6:15**, first draft correct | 7d |
| 46 | Permutations | ✍️ | ❌ `combo == len(nums)` | **reset 1d** |
| 78 | Subsets | ✍️ | — box expired | **dated Jul 31** |
| 155 | Min Stack | 🗣 | ✅ | 21d |
| 74 | Search a 2D Matrix | 🗣 | ❌ `while left < right` | **reset 1d** |

**#200 ✅** — all 7 named cases, **all 512 possible 3×3 grids**, 20,000 random. Pattern line written before the body again.

**#90 ✅ first draft, never executed** — all 7 named plus **3,000 random inputs with duplicates**, no duplicate subsets, `[]` → `[[]]`. The dedup `while` sits after the pop, guarding the *skip* branch — the exact line you narrated wrongly on Day 31 while writing it correctly. Right in both today.

**#155 ✅** — including the two things people miss: the **`<=`** (equal minimums both pushed) and the empty-`minStack` guard.

### 🔴 #133 — the finding of the day

| | Day 33 | Day 34 |
|---|---|---|
| `Node(node.val, node.neighbors)` | ✗ | ✗ **same** |
| discarded a recursive return | ✗ (`#207`) | ✗ **same** |

Measured: the returned "clone" reaches **5 nodes instead of 4** — one clone wired to the four originals. `node = None` crashes (B-4).

> **`#133` is the one problem you never wrote correctly yourself.** Yesterday I told you the fix and you applied it; today it was gone. **A correction you're handed decays far faster than one you derive.** Everything you fought for today — the DFS counter-example, the off-by-one, the two marks — will still be there tomorrow. This wasn't.

### #46 — one character
`if combo == len(nums)` compares a **list** to an **int**. Always `False`, base case never fires, `res` returns `[]` on every input. **B-5, container vs contents.** Everything else — the `seen`-set structure, the paired `popped = combo.pop()` / `seen.remove(popped)` undo — was correct.

### #74 — the exit condition of the wrong template
`while left < right` with `right = mid - 1` never examines the final single cell. **4 of 6 cases wrong**, including `[[1]]` target `1`. And the complexity is **`O(log(m·n))`**, not `O(log n)`.

> **The rule: does my `right` assignment discard `mid`?** Discards it (`mid - 1`) ⇒ **`<=`** (exact match). Keeps it (`mid`) ⇒ **`<`** (converging). Full table now in `binary-search.md`.

---

# 🔴 The one diagnosis

```
#207   dfs(child)              answer discarded
#133   dfs(neighbor)           answer discarded
#46    combo == len(nums)      list compared to int
#74    while left < right      wrong exit condition
```

**Four problems, four failures, one disease: the exact identity of the value in front of you.** You understood every one of these algorithms. **That is a narrower diagnosis than this project has ever had — and two of the four are the *same* recursion mistake within two hours.**

**The drill, from tomorrow, before writing any recursive function — one sentence out loud:**
> ***"The callee hands me back ___, and I catch it at ___."***

That single sentence prevents `#207`'s bug, `#133`'s bug, `#110`'s Day-27 wobble and `#1046`'s un-negate.

---

# Decisions made today (all now standing)

1. **2 new problems/day stays; long sessions accepted.** Your call, over shortening first-contact days. Consequence: Block 2 always runs first on those days, and Block 1 is never dropped.
2. **🎯 Unaided timed mediums on the interleave days — Aug 1, Aug 8, Aug 14.** Zero throughput cost. Unseen problem from a learned pattern · **35-minute hard cap** · **I say nothing** · narrate as you go · self-score on communication / problem-solving / technical correctness / testing. **This closes the only readiness gate that is genuinely off-track** — we currently have *zero* unaided data points.
3. **One-draft cap: 4 minutes — 6 if the solution needs a nested recursive helper.** You measured it (at 4:00 you were at `combo.append(nums[i])`); the cap was meant to stop slow deliberation, not to time your keyboard.
4. **I supply the exact signature on every review prompt.** You write in IDLE from scratch, so the method name has to come from somewhere. **B-8 rescoped** to names that were visible in front of you and still came out wrong.

---

# Day 35 (Fri Jul 31) — Graphs cont., Block 2 first

- **Block 2 — new:** **#210 Course Schedule II** (Kahn's — indegree + queue; gives the actual order, not just yes/no) and **#323 Connected Components**.
- **Block 1 — 5 full solves, 30 min, nothing else:** **#133 · #46 · #74** (resets) → **#994 · #207** (1d). Five full solves *is* the box.
- **Before every recursive function:** *"the callee hands me back ___, and I catch it at ___."*
- **#133 specifically:** *"the callee hands me back the clone, and I catch it in `clone.neighbors`."* Plus the `None` guard.
