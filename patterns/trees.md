# Trees & BFS/DFS

**Status:** learning (started Day 21, 2026-07-13) · **Mastery: 2/5** · Block B

## In one line
Recurse on left/right (DFS) or level-by-level (BFS with a deque).

## Reach for it when
- Anything on a binary tree / BST
- 'Depth / height / diameter / path'
- Level-order or 'right side view' → BFS
- Validate / search a BST → use the ordering

## Prerequisite: recursion (learned Day 21)

Every recursive function has exactly two parts. **Without a base case it never stops.**

```python
def f(problem):
    if <smallest possible case>:      # BASE CASE
        return <the answer for it>
    return <what THIS level contributes>  <combined with>  f(smaller problem)
```

**The call stack:** calls pile up on the way *down*; nobody returns until the deepest one hits the base case, then answers unwind on the way *up*. Those stacked frames are **real memory** → that's where the `O(h)` space comes from.

**The key reframe (the thing that made trees click):** the constant in front of the recursive calls is **what this ONE node contributes** — *not* how many children it has.
- summing values → `node.val + ...`
- counting nodes → `1 + ...`
- measuring depth → `1 + ...` (this node is one level)

## The tree node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # a NUMBER
        self.left = left      # a NODE (or None)
        self.right = right    # a NODE (or None)
```

**`.left`/`.right` hold NODES. `.val` holds a VALUE.** Reassigning `.left` moves an entire subtree; reassigning `.val` moves one number. Confusing the two is mistake **M-021**.

## Template — the base case is almost always "empty tree"

```python
def solve(self, root):
    if root is None:                    # BASE CASE — an empty tree is not an error,
        return <identity>               #   it has a real answer (0, True, None...)
    left  = self.solve(root.left)       # trust the recursion: it returns the right
    right = self.solve(root.right)      #   answer for the subtree. Don't trace it.
    return <combine root.val, left, right>
```

### The two flavors

| Flavor | You do | Return | Example |
|---|---|---|---|
| **Compute & combine** | ask the children for answers, merge them | the answer | #104 Max Depth |
| **Do work & mutate** | change this node, then recurse to fix the rest | usually the root | #226 Invert |

### #104 — Maximum Depth (compute & combine)
```python
def maxDepth(self, root):
    if root is None:
        return 0                                    # empty tree = 0 levels
    return 1 + max(self.maxDepth(root.left),        # me (1) + my deeper child
                   self.maxDepth(root.right))
```

### #226 — Invert Binary Tree (do work & mutate)
```python
def invertTree(self, root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left   # swap the POINTERS, not .val
    self.invertTree(root.left)                      # self. — it's a method!
    self.invertTree(root.right)
    return root
```

### BFS skeleton (Day 23 — level order)
```python
from collections import deque
q = deque([root])
while q:
    for _ in range(len(q)):     # freeze the level size FIRST
        node = q.popleft()
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
```

## Complexity
- **Time: O(n)** for a full traversal — every node visited exactly once.
- **Space: O(h)** — the call stack holds one frame per level, where `h` = height.
  - balanced tree → `h ≈ log n` → **O(log n)**
  - skewed tree (a linked list) → `h = n` → **O(n)** worst case
- **"Recursion is free" is wrong.** If it recurses, it costs stack space. Always say O(h) and name the worst case.
- BFS space is **O(w)** (widest level) → worst **O(n)**.

## Your gotchas
- **`.val` vs `.left`/`.right`** (M-021) — #226 attempt 1 swapped the *values*, which (a) only mirrors one level and (b) crashes on any leaf via `node.left.val` when `node.left` is `None`. **Swap the pointers.**
- **Missing `self.`** on recursive calls inside a class method (M-020) — `self.invert(...)`, not `invert(...)`. **The test: did I attach it with `self.x = ...` in `__init__`, or is it a method of this class? Yes → `self.`; parameter or local → bare.** `self.node.left` is nonsense — `node` is a *parameter*, it lives on no object. Full write-up: **[python-classes.md](python-classes.md)**.
- **Need a value that survives across recursive calls?** (a running max, a counter, a result list) — a local **can't**; each call gets its own copy. Attach it to the object: `self.diameter = 0`. **local = one per call · `self.` = one per object.** This is exactly how #543 works.
- **The `None` guard IS the base case** (B-4). Every tree function starts with `if root is None`. Skipping it doesn't just break an edge case — it breaks the recursion.
- **"return 0" isn't a failure signal.** An empty tree genuinely *has* depth 0. The base case returns the true answer for the smallest input, not an error code.
- **Don't trace the recursion in your head.** Assume the recursive call returns the correct answer for its subtree, and just write how to combine. Trace only to debug.
