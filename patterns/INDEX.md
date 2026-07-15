# Pattern Library — Index

One file per pattern: template, when-to-use triggers, complexity, and *your* gotchas. Mastery 1–5 (5 = solve a novel one cold while narrating).

## Learned

| Pattern | Mastery | File |
|---|---|---|
| Big-O & complexity | **4/5** | [big-o](big-o.md) — *Day 22: O(h) unprompted; bounded-map O(1); `sorted()` vs `.sort()`* |
| Arrays & Hashing | 3/5 | [arrays-hashing](arrays-hashing.md) |
| Two Pointers | 3/5 | [two-pointers](two-pointers.md) |
| Sliding Window | 3/5 | [sliding-window](sliding-window.md) |
| Binary Search | 3/5 | [binary-search](binary-search.md) |
| Stack | 3/5 | [stack](stack.md) |
| Linked List | 3/5 | [linked-list](linked-list.md) |
| Trees & BFS/DFS | 3/5 | [trees](trees.md) — *recursion Day 21 (#226, #104); **the box outside the recursion** Day 22 (#543, #100)* |
| **Binary Search Tree** | **2/5** | [binary-search-tree](binary-search-tree.md) — ***new, Day 22.** The invariant → **compare and pick ONE side**. #235* |

## Language concepts *(not patterns — the machinery the patterns run on)*

| Concept | File |
|---|---|
| **Classes & `self.`** | [python-classes](python-classes.md) — *when `self.` goes in front, and why. Day 21. Load-bearing for recursion (a value that survives across calls), and for every design problem.* |
| Recursion | [trees](trees.md#prerequisite-recursion-learned-day-21) — base case + call stack + the O(h) space cost |
| **`sorted()` vs `.sort()`** | [big-o](big-o.md#sorted-vs-sort) — *Day 22. **Mutating methods return `None`; builder functions return the object.** `x = nums.sort()` sets `x = None`. `sorted()` → O(n) space; `.sort()` → O(1) from your code.* |

## Upcoming

| Pattern | Starts | File |
|---|---|---|
| Tries (Prefix Trees) | Day ~25 | [tries](tries.md) |
| Heap / Priority Queue | Day ~26 | [heap](heap.md) |
| Backtracking | Day ~28 | [backtracking](backtracking.md) |
| Intervals | Day ~29 | [intervals](intervals.md) |
| Graphs (BFS/DFS, topo, union-find) | Day ~49 | [graphs](graphs.md) |
| Dynamic Programming — 1D | Day ~52 | [dynamic-programming-1d](dynamic-programming-1d.md) |
| Dynamic Programming — 2D | Day ~57 | [dynamic-programming-2d](dynamic-programming-2d.md) |
| Greedy | Day ~58 | [greedy](greedy.md) |
| Bit Manipulation | Day ~61 | [bit-manipulation](bit-manipulation.md) |
