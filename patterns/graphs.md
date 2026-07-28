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
