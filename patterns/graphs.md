# Graphs (BFS/DFS, topo, union-find)

**Status:** **learned Day 33** (#200 Number of Islands, #133 Clone Graph) · **Mastery: 2/5** · Block B
*(2/5 = both problems built correctly, but 44 and 45 minutes each, and the `O(V + E)` accounting had to be animated before it landed. Bump it on the 1d/3d reps and on #994/#207.)*

## In one line
A graph is **things + connections**. Every graph algorithm is the same three lines: **visit a node → mark it seen → recurse/enqueue its neighbours.** The only thing that changes is where the neighbours come from.

---

## The one distinction that organises everything: implicit vs explicit

You met both on the same day, and they are the same algorithm.

| | **Implicit** (the grid) | **Explicit** (the object graph) |
|---|---|---|
| Example | #200 Number of Islands, #79 Word Search | #133 Clone Graph, #207 Course Schedule |
| A node is | a cell `(row, col)` | a `Node` object (or an int id) |
| Neighbours are | **computed** — `(r±1, c)`, `(r, c±1)` | **stored** — `node.neighbors`, or `adj[u]` |
| "Visited" lives in | the grid itself (mark `"#"`) or a `visited` set | a `dict` / `set` keyed by node |
| Bounds check | **required** — `r < 0 or r >= len(grid)` | **not a thing** — you can only reach what's in the list |

> **The insight from Day 33:** you already knew grid DFS from #79. Graphs did not add a new traversal — they added a **second place neighbours can come from.** That's it.

---

## Skeleton 1 — implicit / grid DFS (#200)

```python
def numIslands(grid):
    count = 0

    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == "0" or grid[row][col] == "#":
            return

        grid[row][col] = "#"          # mark PERMANENTLY - no un-mark
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                dfs(r, c)             # sink the whole island
                count += 1            # ...and that was ONE island
    return count
```

### The one thing that separates this from #79: **the mark is permanent**

#79 Word Search un-marks on the way out (`board[r][c] = temp`) because a cell that isn't part of *this* word might be part of a word starting somewhere else. **#200 never un-marks** — once a cell is known to belong to an island, no later search should ever see it again.

**That single difference is what makes the complexity `O(m·n)` instead of `O(m·n·4^L)`,** and you derived it yourself:

> *"The reason 4^L is not considered is because you can only work with a node once, so there is no need to consider it 4 times."*

That's exactly right, and it's the general rule: **backtracking explores paths (exponential); graph traversal visits nodes (linear).** The un-mark is the whole difference between the two.

### Where the `count += 1` goes — the thing that confused you
Not inside `dfs`. `dfs` sinks **an entire island**, however many cells it is. The counter belongs in the **outer double loop**, next to the call: *one call that actually started = one island.* The `if grid[r][c] == "1"` guard is what makes "actually started" true — an already-sunk `"#"` cell never triggers a call.

**Complexity:** `O(m·n)` time (every cell entered a bounded number of times) · `O(m·n)` space (call-stack worst case — a grid that is one giant snake of land).

---

## Skeleton 2 — explicit graph, and the clone (#133)

```python
class Solution:
    def cloneGraph(self, node):
        adict = {}                                # original node -> its clone

        def dfs(node):
            if node is None:
                return None
            if node in adict:                     # already cloned -> return the SAME clone
                return adict[node]

            adict[node] = Node(node.val, [])      # 1. make the shell, register it FIRST
            for neighbor in node.neighbors:       # 2. then fill it
                adict[node].neighbors.append(dfs(neighbor))
            return adict[node]

        return dfs(node)
```

### Three things this problem is really testing

**1. `adict` is not a "visited set" — it is the mapping.** It answers two questions with one structure: *have I seen this node?* and *what is its clone?* That double duty is why a `set` isn't enough.

**2. Register the shell BEFORE recursing.** This is what makes cycles terminate. If you built the neighbour list first and only then put the clone in the dict, `A → B → A` would recurse forever. Putting the empty shell in the dict first means the cycle comes back, finds the entry, and returns it.

**3. ⚠️ The bug that actually happened: `Node(node.val, node.neighbors)`.** That hands the clone **the original's neighbour list** — the originals themselves, not their clones. The result looks fine on a print and is not a deep copy at all: mutate the clone and the original changes with it. **The fix is the shape above:** empty list, then `append(dfs(neighbor))` — the clone's neighbours must be *built from clones*, never copied from the original's fields.

> **The generalisation, and it's one you already own:** this is **container vs contents** (M-021) at object scale. `node.neighbors` is a *handle to the originals*. You wanted the *things they map to*.

---

## `O(V + E)` — the accounting, since this is the part that didn't land at first

**V = vertices (nodes). E = edges (connections).** The traversal is `O(V + E)` and **not** `O(V·E)`, because those are two *separate* piles of work that you add, not multiply:

- **The `V` part** — you do the fixed work at each node exactly once: check the dict, build the shell, return. `V` nodes ⇒ `V` units.
- **The `E` part** — you walk each connection. The `for neighbor in node.neighbors` loops don't each cost `V`; **across the whole traversal they cost the total number of entries in all the adjacency lists**, and that total is fixed by the number of edges.

### The 2E fact — you said it yourself

> *"So if there are E edges, it will always be 2E entries."*

**Yes, for an undirected graph.** One edge `A — B` is stored twice: once in `A.neighbors` and once in `B.neighbors`. So the adjacency lists hold `2E` entries total, you touch each once, and `2E` drops to `O(E)`.

| Graph type | Entries per edge | Total entries | Traversal |
|---|---|---|---|
| **Undirected** | **2** (`A` lists `B`, `B` lists `A`) | `2E` | `O(V + E)` |
| **Directed** | **1** (only `A` lists `B`) | `E` | `O(V + E)` |

**Why "V +" is there at all:** an isolated node with no edges still costs work. If you only counted edges, a graph of 1000 disconnected nodes would look free. `V` pays for existing; `E` pays for connecting.

*(Animation of this, built Day 33: `viz/graph-edges-and-traversal.html` — Part 1 is one edge becoming two entries, Part 2 counts V and E separately through a clone traversal.)*

**Space for #133:** `O(V)` — the dict holds one entry per node, and the call stack is at most `V` deep. The clone graph itself is output, not auxiliary.

---

## Complexity summary

| Problem | Time | Space | Why |
|---|---|---|---|
| #200 Number of Islands | `O(m·n)` | `O(m·n)` | every cell entered a bounded number of times; stack = worst-case snake |
| #133 Clone Graph | `O(V + E)` | `O(V)` | fixed work per node + one touch per adjacency entry (`2E` undirected) |
| #79 Word Search *(contrast)* | `O(m·n·4^L)` | `O(L)` | **un-marks** ⇒ explores paths, not nodes |

---

## Your gotchas

- **`node.neighbor` vs `node.neighbors`.** Cost three submissions on #133; the algorithm was already correct at submission two. **The attribute is named in the class definition three lines above — read it, don't recall it.** *(M-029, sixth session of names being slightly wrong. Escalated to blocker B-8 on Day 33.)*
- **Don't hand the original's list to the clone.** `Node(node.val, [])`, then append clones.
- **Register the clone in the dict before you recurse**, or cycles never terminate.
- **`count += 1` belongs beside the call, not inside the recursion.**
- **Permanent mark for traversal, un-mark for backtracking.** If you catch yourself writing `temp` in a graph problem, ask whether you actually need to revisit that node — usually you don't.

## Still to come
**#994 Rotting Oranges** (multi-source BFS — the first one where BFS is *required*, not just an option: you need level = time) · **#207 Course Schedule** (cycle detection in a directed graph) · **#210 Course Schedule II** (topological order) · **#323 Connected Components** (union-find) · **#417 Pacific Atlantic**.

---

# Day 34 — the two graph problems that are not "traverse and mark"

**Status update:** #994 Rotting Oranges + #207 Course Schedule added. **Mastery still 2/5** — both were built correctly but with heavy guidance and 72 / 44 minutes. The reps decide the number, not the acquisition.

## Shape 3 — multi-source BFS (#994)

**The trigger word is TIME.** `#200` asks *"are these connected?"* — a yes/no that doesn't care about the route. `#994` asks *"how many minutes?"* — and **a minute is a shortest distance.**

> **⚠️ DFS cannot answer a distance question.** DFS depth is the length of the path it *happened* to take, not the shortest one — and a permanent mark freezes that wrong number in place. Measured on `[[2,1,1],[1,1,1]]` with a single source: **DFS reports 5, the true answer is 3.** Not a tie-breaking subtlety; just wrong. *(Day 34.)*

```python
from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q, fresh, minute = deque(), 0, 0

    for r in range(rows):                       # ONE pass, TWO jobs
        for c in range(cols):
            if grid[r][c] == 1:   fresh += 1
            elif grid[r][c] == 2: q.append((r, c))

    while q and fresh > 0:                      # the guard IS the off-by-one fix
        for _ in range(len(q)):                 # snapshot = one level
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minute += 1

    return minute if fresh == 0 else -1
```

**Seed the queue with EVERY source.** That is the whole trick, and it dissolves the problem that looks hardest: *"two rotten oranges, which one reaches this cell first?"* You never compare them. **All sources sit at level 0 together, so level 1 means "one minute from ANY source."** The nearest one wins automatically. **Multi-source BFS is single-source BFS with a fuller starting queue.**

**⚠️ The off-by-one, and it is the most common wrong submission.** With a bare `while q`, the final level pops cells that rot nothing new — and `minute += 1` still fires. Verified: `[[2,1,1],[1,1,1]]` returns **4**, true answer **3**.

Two correct fixes:

| fix | works? | catch |
|---|---|---|
| `while q and fresh > 0` | ✅ always | none — and the empty grid returns `0` for free |
| `return minute - 1` | ✅ **except one shape** | a grid with **no rotten AND no fresh** (all `0`s) returns `-1`, should be `0`. *(Checked: all 81 2×2 grids + 20,000 random — exactly one failing class.)* |

**`range(len(q))` is evaluated ONCE**, when the `for` starts — appending to `q` inside the loop cannot extend it. `while i < len(q)` *does* re-evaluate. Know which constructs re-check their condition. *(Day 34 misconception.)*

**Complexity:** `O(m·n)` time · **`O(m·n)` space** — the seeding pass alone can put every cell in the deque. *(Measured peak deque on a 10×10: corner source **10**, centre source **19**, all-rotten **100**. So `O(m+n)` is right for a single source and wrong as the bound.)* **BFS space = the widest level, and in multi-source BFS the seeding IS a level.**

---

## Shape 4 — cycle detection in a DIRECTED graph (#207)

**Input isn't a graph yet.** It's a flat list of pairs — build the adjacency dict first, then traverse. Two parts, always.

```python
def canFinish(numCourses, prerequisites):
    adj = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        adj[prereq].append(course)          # arrow prereq -> course

    path, visited = set(), set()

    def dfs(node):
        if node in path:    return False    # still INSIDE it -> cycle
        if node in visited: return True     # proven clean -> skip
        path.add(node)                      # choose
        for child in adj[node]:
            if not dfs(child):              # CATCH the answer
                return False
        path.remove(node)                   # un-choose
        visited.add(node)                   # NOW it is certified
        return True

    for node in range(numCourses):          # the cycle may not be reachable from 0
        if not dfs(node):
            return False
    return True
```

### 🔑 The idea worth the whole week: TWO marks, two jobs

> **A cycle is not "I've seen this node before." A cycle is "I've seen this node before AND I'M STILL INSIDE IT."**

| set | marked | un-marked? | job | drop it and… |
|---|---|---|---|---|
| **`path`** | on the way **in** | **yes**, on the way out | detects the cycle | **wrong answer** |
| **`visited`** | when the node **finishes** | **never** | never redo a proven subtree | **right answer, exponential time** |

**`path` is choose/un-choose — it is literally backtracking** (`#79`'s `board[r][c] = "#"` … `= temp`). **`visited` is the permanent mark — it is literally `#200`.** `#207` carries one of each.

> **Graph traversal and backtracking are not two patterns. They are the permanent mark and the temporary mark.** `#79` un-marks ⇒ explores *paths* ⇒ exponential. `#200` marks permanently ⇒ visits *nodes* ⇒ linear. `#207` needs both properties at once.

**Measured cost of dropping `visited`** — a chain of diamonds, answer identical, calls exploding:

| diamonds | nodes | edges | calls **with** `visited` | **without** |
|---|---|---|---|---|
| 5 | 16 | 20 | 36 | 462 |
| 10 | 31 | 40 | 71 | 16,299 |
| 18 | **55** | **72** | **127** | **4,194,163** |

Each diamond gives two routes to its merge node, so each one **doubles** the work below it: `2^k`.

**Why loop over every node?** The graph can be disconnected — `(4, [[2,0],[1,2],[3,1],[2,3]])` hides its cycle away from node `0`.

**Pick a return convention and say it out loud before writing the body** — `True` = clean, or `True` = cycle found. The bug is base cases in one convention and the caller in the other. Both `node in path` and `node in visited` feel like "stop", so both tempt `return False`; only the first one is. *(M-033 family.)*

**Complexity:** `O(V + E)` time and space.

### Why intervals / sliding window / binary search cannot touch this *(asked Day 34)*
`[1, 0]` is **not** an interval. An interval is a *range on a line*; a prerequisite is an *ordered pair of two labels*. Decisive check: both the acyclic and the cyclic example contain "overlapping" pairs, so overlap can't tell them apart.

> **The general tool: test a proposed method against a symmetry the answer must respect.** Course labels are arbitrary names — swap `0` and `5` everywhere and the answer *must* not change. Any method that reads the numbers as positions is dead before you write it. **That kills every ordering-based pattern on any graph problem.**

## Vocabulary — get these right *(B-8)*
**vertex** (one) / **vertices** (many) · an **entry** is stored in memory, a **walk** is traversing one · a **tree** has no node with two parents — a diamond is a **graph**; a graph with no cycles is a **DAG**.

## Still to come
#210 Course Schedule II (Kahn's — indegree + queue, gives the actual order) · #323 Connected Components (union-find) · #417 Pacific Atlantic · #695 Max Area of Island.

---

# Day 35 — the order, and the second way to ask about connectivity

**Mastery: 2/5 → 3/5.** Six problems. **#210 in 17:21 and #323 in 31:14, against 44 and 72 the day before** — same pattern family, second day. That's consolidation on a clock.

## Shape 5 — topological order (#210) = **#207 plus two lines**

```python
def findOrder(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    path, visited, revAnswer = set(), set(), []

    def dfs(node):
        if node in path:    return False
        if node in visited: return True
        path.add(node)
        for child in graph[node]:
            if not dfs(child):
                return False
        path.remove(node)
        visited.add(node)
        revAnswer.append(node)          # <-- LINE 1: append when it FINISHES
        return True

    for node in range(numCourses):
        if not dfs(node):
            return []
    return revAnswer[::-1]              # <-- LINE 2: reverse
```

**Append at the moment the node FINISHES — after every child has returned. That's a post-order DFS.**

### Why the finish order is backwards — say it precisely

> **Every node that finishes before `X` is reachable FROM `X`** — i.e. it depends on `X`, directly or transitively. So `X` must come **before** all of them. Finish-order therefore lists dependents first and prerequisites last; **reversing puts prerequisites first.**

*(The stack version of the same fact: the **last** node to finish is the one at the **bottom** of the recursion — the course you started from, a prerequisite. After the reverse it lands **first**.)*

### ⚠️ `return []` belongs inside the loop; `return answer` does not

```python
for node in range(numCourses):
    if not dfs(node):
        return []          # early EXIT - one cycle anywhere is enough
answer = revAnswer[::-1]   # a CONCLUSION - only true after the loop ends
return answer
```

**Putting `return answer` inside the loop makes it run exactly once.** *(Day 35 bug — 2,103 of 5,000 random inputs failed.)* It survives every single-component example, because `dfs(0)` alone does the whole job there; **it only breaks when the graph has a piece node `0` can't reach.** `numCourses = 2, prerequisites = []` catches it instantly — two isolated nodes.

> **The rule: `return` inside a loop means "done after ONE iteration."** Ask what the loop's job is. Here it's *"every node has been started from"*, which is only true **after** it ends. **An early exit lives inside; a conclusion lives after.**

**Complexity:** unchanged — `O(V + E)` time and space. One append per node and one reverse are both `O(V)`.

*(The other standard topological sort is **Kahn's**: compute in-degrees, queue everything with in-degree 0, pop and decrement. BFS-shaped, no recursion, and it detects the cycle by counting how many nodes came out. Worth knowing it exists; the post-order DFS above is the one you own.)*

---

## Shape 6 — connected components (#323) = **#200 on an explicit graph**

```python
def countComponents(n, edges):
    graph = {i: [] for i in range(n)}
    for node1, node2 in edges:
        graph[node1].append(node2)      # UNDIRECTED -> both
        graph[node2].append(node1)      # directions. This IS your 2E.

    seen = set()
    counter = 0

    def dfs(i):                          # returns NOTHING, deliberately
        if i in seen: return
        seen.add(i)
        for neighbor in graph[i]:
            dfs(neighbor)

    for i in range(n):
        if i not in seen:
            dfs(i)
            counter += 1
    return counter
```

**It's `#200` with `seen` instead of `"#"`.** The counter sits beside the call in the outer loop, exactly as in Number of Islands: **one DFS that actually started = one component.**

**You never compare two nodes to ask if they're connected.** DFS from an unvisited node reaches exactly that node's component; anything still unvisited afterwards is by definition in a different one. **The traversal partitions the graph for you.**

**Undirected ⇒ two appends per edge**, into two *different* lists. No guard, no duplication — that is what "undirected" means, and it's literally where the `2E` from Day 33's warm-up comes from.

**No `path` set.** `#207` needed one; this doesn't — undirected connectivity has no cycle question to answer. **Transferring a pattern without transferring the parts you don't need is the hard half of pattern recognition.**

### `dfs` returning nothing is CORRECT here — the B-9 converse
B-9 says *know what the callee hands back*. Here the answer is **nothing, deliberately**: `dfs` only mutates `seen`, and the counting happens outside it. **Mixed intent is the bug, not the absence of a return.**

**Complexity:** `O(V + E)` time · **`O(V + E)` space.**

> ### 🔑 Space: count what YOU allocate
> `#133` was `O(V)` because the `neighbors` lists **arrived inside the input** — you only allocated one dict entry per node. `#323` is `O(V + E)` because **you build the adjacency structure yourself**: `V` keys plus `2E` entries.
>
> **And a dict's space is not its key count.** `{0: [a million ints]}` has one key and is not `O(1)`. **A container's space is its own overhead plus the total size of everything it holds.** Same rule as Timsort's `O(n)` scratch on `#56`. *(Asked and answered Day 35.)*

## Complexity summary

| Problem | Time | Space |
|---|---|---|
| #200 Number of Islands | `O(m·n)` | `O(m·n)` |
| #133 Clone Graph | `O(V + E)` | `O(V)` — lists arrived with the input |
| #994 Rotting Oranges | `O(m·n)` | `O(m·n)` — seeding is a level |
| #207 Course Schedule | `O(V + E)` | `O(V + E)` |
| #210 Course Schedule II | `O(V + E)` | `O(V + E)` |
| #323 Connected Components | `O(V + E)` | `O(V + E)` — you build the adjacency |
