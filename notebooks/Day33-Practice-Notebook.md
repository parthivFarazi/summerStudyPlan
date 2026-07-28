# Day 33 — 2026-07-28 (Tue)
## NEW PATTERN: Graphs — #200 Number of Islands, #133 Clone Graph · Block 1 **5/5**

> **Session shape:** Graphs is heavy, so **Block 2 ran FIRST** while fresh, then Block 1 under the 30-minute box.
> **Headline: Block 1 was 5 for 5 in 26:55, all full solves — and every single one was a problem that failed the day before.**

---

# Block 2 — NEW MATERIAL (ran first)

## The frame: a graph is things + connections

Every graph algorithm is the same three lines — **visit a node → mark it seen → go to its neighbours.** The only thing that ever changes is **where the neighbours come from**:

| | **Implicit** (grid) | **Explicit** (objects) |
|---|---|---|
| A node is | a cell `(row, col)` | a `Node` object |
| Neighbours are | **computed** — `(r±1, c)`, `(r, c±1)` | **stored** — `node.neighbors` |
| Bounds check | **required** | not a thing |
| Today | **#200** | **#133** |

**You already knew grid DFS from #79 Word Search.** Graphs did not add a new traversal today. They added a second place neighbours can come from.

---

## #200 Number of Islands — ✅ **44:14**

**Your idea, unprompted:** *"Use the word search DFS technique, but instead of temporarily marking the used node, permanently mark them."*

That is the entire problem, and you had it before writing a line.

```python
def islandCount(grid):
    count = 0

    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == "0" or grid[row][col] == "#":
            return

        grid[row][col] = "#"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        return

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1

    return count
```

### The permanent mark is the whole idea

**#79 un-marks** (`board[r][c] = temp`) because a cell that isn't in *this* word may be in a word starting elsewhere. **#200 never un-marks** — once a cell is known to be part of an island, no later search should ever see it again.

### 💡 Your complexity reasoning — this was the best moment of Block 2

> *"The reason `4^L` is not considered is because you can only work with a node once, so there is no need to consider it 4 times."*

**Exactly right, and it generalises:**

> **Backtracking explores PATHS → exponential. Graph traversal visits NODES → linear.**
> **The un-mark is the entire difference between the two.**

### The thing that confused you: where does `count += 1` go?

Not inside `dfs`. **`dfs` sinks an entire island**, however many cells that is. The counter belongs in the **outer double loop, beside the call** — one call that actually *started* = one island. The `if grid[r][c] == "1"` guard is what makes "actually started" true, because an already-sunk `"#"` cell never triggers a call.

**Complexity: `O(m·n)` time · `O(m·n)` space** (call stack, worst case a grid that is one long snake of land). Both correct.

---

## #133 Clone Graph — ✅ **45:28** (after two fixes)

```python
class Solution:
    def cloneGraph(self, node):
        adict = {}                                # original -> its clone

        def dfs(node):
            if node is None:
                return None
            if node in adict:
                return adict[node]

            adict[node] = Node(node.val, [])      # 1. shell first, registered FIRST
            for neighbor in node.neighbors:       # 2. then fill it with CLONES
                adict[node].neighbors.append(dfs(neighbor))

            return adict[node]

        return dfs(node)
```

### Three ideas this problem is actually testing

**1. `adict` is not a visited set — it's the mapping.** It answers two questions with one structure: *have I seen this node?* and *what is its clone?* A `set` can't do the second, which is why it isn't enough.

**2. Register the shell BEFORE recursing.** This is what makes cycles terminate. If you filled the neighbour list first and only *then* stored the clone, `A → B → A` would recurse forever. Empty shell in the dict first ⇒ the cycle comes back, finds the entry, returns it.

**3. 🔴 The real bug: `Node(node.val, node.neighbors)`.**

That hands the clone **the original's neighbour list** — the original nodes themselves, not their clones. It *looks* right when printed and is not a deep copy at all: mutate the clone and the original changes with it.

> **This is container-vs-contents (M-021) at object scale.** `node.neighbors` is a **handle to the originals**. You wanted **the things they map to**. Fix: empty list, then `append(dfs(neighbor))`.

### 🔴 The other bug — and this one is the one to be annoyed about

`for neighbor in node.neighbor:` — **missing the `s`.** The attribute is named `self.neighbors` in the class definition **three lines above it**.

**The algorithm was correct at submission two. This typo cost the third submission.** That's the sixth session in a row of names being slightly wrong: `exist` → `wordSearch`, `merge` → `mergeInterval`, `insert` → `insertInterval`, `eraseOverlapIntervals`, *"the mid value… that is the index"*, and now `neighbor` → `neighbors`.

**It has been escalated to a blocker (B-8) today.** In a real interview this is the difference between a clean solve and a candidate who looks like he doesn't read his own code.

---

## `O(V + E)` — the part that had to be animated

You asked for it three times, correctly, until it landed: *"you gotta visualise it, I have no clue what you're talking about with the edges."* Built: **`viz/graph-edges-and-traversal.html`** *(also saved in this folder)*.

**V = vertices (nodes). E = edges (connections). It's `O(V + E)`, not `O(V · E)`, because those are two separate piles of work you ADD, not multiply:**

- **The `V` part** — fixed work at each node, exactly once: check the dict, build the shell, return.
- **The `E` part** — the `for neighbor in ...` loops don't each cost `V`. **Across the whole traversal they cost the total number of entries in all the adjacency lists**, and that total is fixed by the edges.

### 💡 And then you said it yourself:

> *"So if there are E edges, it will always be 2E entries."*

**Yes — for an undirected graph.** The edge `A — B` is stored twice: once in `A.neighbors`, once in `B.neighbors`.

| Graph type | Entries per edge | Total entries | Traversal |
|---|---|---|---|
| **Undirected** | **2** | `2E` | `O(V + E)` |
| **Directed** | **1** | `E` | `O(V + E)` |

**Why "`V +`" is there at all:** an isolated node with no edges still costs work. Count only edges and a graph of 1000 disconnected nodes looks free. **`V` pays for existing; `E` pays for connecting.**

**Space `O(V)`** — the dict is one entry per node, stack depth at most `V`. The clone graph itself is output, not auxiliary.

---

# Block 1 — reviews · 30-minute box · **5/5 in 26:55**

All five were **full solves** — the expensive tier, blank screen, run it, debug it. Every one of them was verified by executing your exact code against 6–10 cases including edge cases.

| # | Problem | Time | Result | Rung |
|---|---|---|---|---|
| 79 | Word Search | **6:22** | ✅ | reset → **3d** |
| 39 | Combination Sum | **7:24** | ✅ | reset → **3d** |
| 57 | Insert Interval | **6:06** | ✅ | reset → **3d** |
| 435 | Non-overlapping Intervals | **4:50** | ✅ | 1d → **3d** |
| 252 | Meeting Rooms | **2:13** | ✅ | 1d → **3d** |

### What makes this the strongest review block of the sprint

**Yesterday you failed three of four full solves. Today you passed five of five — and each one was a fix to the exact thing that broke.**

- **#79** — the mark/un-mark idiom you had to peek at yesterday, written cold today: `temp` saved, `"#"` written, all four directions, restore on the way out.
- **#39** — the prune was **backwards** yesterday (`target > total`, true at the root, killed the recursion instantly). Today: `if i == len(candidates) or total > target: return`. Correct.
- **#57** — the post-loop terminal append was **missing** yesterday, on the exact problem whose own comment named the flag. Today it's there:
  ```python
  if not isInserted:
      answer.append(newInterval)
  return answer
  ```
- **#435** — the reference bug (comparing to the physically adjacent interval instead of the last one KEPT) was yesterday's. Today the sweep compares against `temp`, the thing that survived.

**These aren't lucky passes. Every named cause from Day 32 held first-draft.**

### #252 — and the thing you got away with

```python
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[1])
    temp = []
    for interval in intervals:
        if len(temp) == 0:
            temp = interval
        else:
            c, d = interval
            a, b = temp
            if b > c:
                return False
            else:
                temp = interval
    return True
```

You wrote the pattern as a **comment before the body** — *"similar to nonOverlapping, sort by `x[1]`, have a temp, if overlap return False."* That's retrieval first, then writing, and it's why this took 2 minutes instead of 6. Keep doing that.

**But:** in **#435** the sort-by-END is load-bearing — sort by start and the answer is wrong. In **#252 it isn't.** Sorting by start works equally well *(verified against brute force on 300,000 random cases)*.

> **Why: #435 SKIPS intervals; #252 never does.** In #435 you drop a conflicting interval and keep going, so `temp` diverges from "the previous element in the array" — that gap is the bug that's bitten twice. **#252 returns on the first conflict**, so nothing is ever skipped, so `temp` *is* always the previous element and the trap can't fire.
>
> **Don't file this as "sort by end for interval problems." File it as: the sort key exists to make the greedy choice come first — and if you never skip, there's no greedy choice to protect.**

---

# The honest read on Day 33

## 🟢 What went right

**1. The box held — with the most expensive possible load.** Five full solves, 26:55, three minutes spare. First time the 30-minute box has held on an all-full-solve day.

**2. Every Day-32 named cause held first-draft.** M-033 (reversed prune), M-026 (terminal line), the #79 idiom, the #435 reference bug. **That is the ladder working exactly as designed** — fail, name the cause, come back and it holds.

**3. You refused to give a complexity before you had an approach — and you were right.**
> *"I can't really give you a time and space complexity until I actually have an idea about the way I want to go about the solution first."*

I'd reverted to the review order on new material. That's now written into `COACHING.md` rule 3: **reviews = complexity first · new material = approach → complexity → code.** The invariant that never moves: **complexity before any code.**

**4. You demanded a visualisation instead of nodding along**, three times, and then produced the `2E` fact yourself. Asking for a better explanation of something you don't understand is a strictly better move than pretending, and it's what the animation was for.

**5. The stopwatch finally ran on new problems.** Three sessions of missing it, closed.

## 🔴 What didn't

**1. Ninety minutes for two new problems.** 44:14 and 45:28. The material was new and both were built correctly — but **the readiness gate is measured in minutes on unseen problems**, and a FAANG medium is ~20–25. This is now the number to watch, not the pass/fail.

**2. `node.neighbor`.** Sixth session. **Escalated to blocker B-8.**

**3. From Day 34, a full solve you hand over without executing is a FAIL on the spot** — no partial credit for "the algorithm was right." Three submissions on #133 is what that rule exists to prevent.

---

# Bank these

- **Backtracking explores paths (exponential); graph traversal visits nodes (linear). The un-mark is the entire difference.**
- **A graph = things + connections. The only variable is where the neighbours come from.**
- **`O(V + E)`: V pays for existing, E pays for connecting. Undirected stores 2E entries.**
- **A deep copy's fields must be built from copies, never assigned from the original's fields.**
- **Register the clone before you recurse, or cycles never end.**
- **The sort key exists to make the greedy choice come first — if you never skip, there's no greedy choice to protect.**
- **Read the attribute name; don't recall it. It's three lines above.**

---

# Day 34 (Wed Jul 29) — Graphs cont., **Block 2 first again**

- **Warm-up (cold, no notes): `O(V + E)`** — what V is, what E is, why it's `+` not `·`, and **how many adjacency entries a 6-edge undirected graph has vs a 6-edge directed one.** Banked from today deliberately rather than drilled at the end of a long session.
- **Block 2 — new:** **#994 Rotting Oranges** (multi-source BFS — the first problem where BFS is *required*, because level = time) and **#207 Course Schedule** (cycle detection, directed).
- **Block 1 — 7 items, ~25 min:** full **#200 · #133** · ✍️ one-draft **#90 · #46 · #78** · 🗣 verbal **#155 · #74**.
