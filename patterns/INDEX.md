# Pattern Library — Index

One file per pattern: template, when-to-use triggers, complexity, and *your* gotchas. Mastery 1–5 (5 = solve a novel one cold while narrating).

## Learned

| Pattern | Mastery | File |
|---|---|---|
| Big-O & complexity | **4/5** | [big-o](big-o.md) — *Day 22: O(h) unprompted; bounded-map O(1); `sorted()` vs `.sort()`* |
| Arrays & Hashing | 3/5 | [arrays-hashing](arrays-hashing.md) |
| Two Pointers | 3/5 | [two-pointers](two-pointers.md) |
| **Sliding Window** | **3/5** | [sliding-window](sliding-window.md) — *#3, #424 (grow/shrink) · **#567 fixed-size + frequency compare (Mock #1)** — when a window slides, only TWO characters change: update, do not rebuild. A bounded 26-slot map is O(1)*
| Binary Search | 3/5 | [binary-search](binary-search.md) |
| Stack | 3/5 | [stack](stack.md) |
| Linked List | 3/5 | [linked-list](linked-list.md) |
| Trees & BFS/DFS | 3/5 | [trees](trees.md) — *recursion Day 21; box pattern Day 22; **BFS** Day 23 (#102, #199)* |
| **Binary Search Tree** | **3/5** | [binary-search-tree](binary-search-tree.md) — *invariant → pick ONE side (#235); **bounds passed down** (#98); **in-order = sorted** (#230)* |
| **Tries (Prefix Trees)** | **2/5** | [tries](tries.md) — *nested dicts of nodes; char = the KEY; `is_end` flag. #208; **wildcard `.` → DFS** #211 (Day 26)* |
| **Heap / Priority Queue** | **3/5** | [heap](heap.md) — *`heapq` min-heap; negate for max; **size-k heap** (min→k-largest, max→k-closest); **tuple keys**. #703, #1046, #973, #215* |
| **Backtracking** | **3/5** | [backtracking](backtracking.md) — *choose → recurse → **un-choose**. 4 shapes: take/skip (#78,#39), dedup (#90), for-loop+used-set (#46 derived cold), **grid DFS in-place (#79, Day 30 — bridge to graphs)*** |
| **Intervals** | **3/5** | [intervals](intervals.md) — *`overlap = (b >= c) and (d >= a)`; insert (#57) vs merge (#56) = what the input PROMISED; **greedy interval scheduling** (#435, #252) — sort so best-is-first, one variable for the last commitment*
| **Graphs (BFS/DFS)** | **3/5** | [graphs](graphs.md) — *implicit (grid) vs explicit (objects). #200 permanent mark ⇒ O(m·n) · #133 dict = visited AND mapping · #994 multi-source BFS (DFS depth ≠ distance) · #207 TWO marks: path finds the cycle, visited keeps it linear · **#210 post-order + reverse = topological sort** · **#323 = #200 on an explicit graph**. O(V+E), 2E entries undirected*

## Language concepts *(not patterns — the machinery the patterns run on)*

| Concept | File |
|---|---|
| **Classes & `self.`** | [python-classes](python-classes.md) — *when `self.` goes in front, and why. Day 21. Load-bearing for recursion (a value that survives across calls), and for every design problem.* |
| Recursion | [trees](trees.md#prerequisite-recursion-learned-day-21) — base case + call stack + the O(h) space cost |
| **`sorted()` vs `.sort()`** | [big-o](big-o.md#sorted-vs-sort) — *Day 22. **Mutating methods return `None`; builder functions return the object.** `x = nums.sort()` sets `x = None`. `sorted()` → O(n) space; `.sort()` → O(1) from your code.* |

## Upcoming

| Pattern | Starts | File |
|---|---|---|
| Backtracking | Day ~28 | [backtracking](backtracking.md) |
| Graphs — topo sort & union-find | **Day 34–36** | [graphs](graphs.md) — *#994, #207, #210, #323* |
| Dynamic Programming — 1D | Day ~52 | [dynamic-programming-1d](dynamic-programming-1d.md) |
| Dynamic Programming — 2D | Day ~57 | [dynamic-programming-2d](dynamic-programming-2d.md) |
| Greedy | Day ~58 | [greedy](greedy.md) |
| Bit Manipulation | Day ~61 | [bit-manipulation](bit-manipulation.md) |
