# Trees & BFS/DFS

**Status:** learning (started Day 21, 2026-07-13) · **Mastery: 3/5** *(Day 22: #543, #100)* · Block B
**See also:** [binary-search-tree.md](binary-search-tree.md) — a BST is a tree with an ordering invariant, and it changes the strategy completely (**pick one side, don't explore both**).

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

---

## 🔑 The box outside the recursion *(learned Day 22 — #543)*

**The situation:** what your **parent** needs and what **you** want to know are *different numbers*.

At any node:
1. **What you owe your parent.** Your parent is computing *its* height, so it needs *your* height. **The return channel is already spoken for.**
2. **What you actually want.** e.g. `left_height + right_height` — the longest path *bending at this node*. Your parent can't use it.

**You can't return both.** So the second one goes in a **box outside the recursion** — every node peeks in on the way up and overwrites it if it beat the record. At the end, read the box.

> **`dfs` returns what the PARENT needs. `res` collects what YOU need.**

### Why the box is MANDATORY, not a convenience
```
        1
       /
      2
     / \
    3   4
   /     \
  6       7
```
True diameter = `6→3→2→4→7` = **4 edges** — it **bends at node 2** and never touches the root.
At the root: `left=3`, `right=0` → `3 + 0 = 3`. **Wrong.**
**Why:** all the root ever receives from `dfs(node2)` is **one number** — `3`, a height. That number **has no memory of the fat path running across node 2.** The fact **cannot fit through the return pipe.** So node 2 writes `4` to the box on its way up, and the root never needs to know.

### The syntax trap
```python
res = 0
def dfs(node):
    res = max(res, left + right)   # ❌ UnboundLocalError
```
**Assigning** to `res` inside `dfs` makes Python treat it as a **brand-new local** — so the `res` on the right doesn't exist yet. Fix with **`self.res`** (use this on LeetCode) or **`nonlocal res`**.
> **local = one per call · `self.` = one per object.** See [python-classes.md](python-classes.md).

### The 6-slot anatomy — only slots 5 and 6 ever change
```python
class Solution:
    def someProblem(self, root):
        self.res = 0                  # 1. the box — OUTSIDE the recursion

        def dfs(node):                # 2. the helper
            if node is None:
                return 0              # 3. base case
            left  = dfs(node.left)    # 4. collect what the children owe you
            right = dfs(node.right)
            self.res = ???            # 5. UPDATE THE BOX ← "what did I learn here
                                      #                     that nobody upstream will hear?"
            return ???                # 6. RETURN ← "what does my parent need?"

        dfs(root)                     # 7. kick off — DISCARD the return value.
                                      #    You call it for the SIDE EFFECT: it filled the box.
        return self.res               # 8. read the box — THAT is the answer
```

### #543 — Diameter of Binary Tree
```python
def diameterOfBinaryTree(self, root):
    self.res = 0

    def dfs(node):
        if node is None:
            return 0
        left  = dfs(node.left)
        right = dfs(node.right)
        self.res = max(self.res, left + right)   # the path BENDING here (edges)
        return 1 + max(left, right)              # my HEIGHT, for my parent

    dfs(root)
    return self.res
# O(n) time · O(h) space
```

| Node | `left` | `right` | `left+right` (bend) | returns | box |
|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 1 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 |
| 2 | 1 | 1 | **2** | 2 | **2** |
| 3 | 0 | 0 | 0 | 1 | 2 |
| 1 | 2 | 1 | **3** | 3 | **3** |

**⚠️ Capture the child results in variables.** The moment a child's result feeds **both** the box and the return, it must go in a variable:
```python
left  = dfs(node.left)     # ✅ called ONCE, used twice
# NOT: self.res = max(self.res, dfs(node.left) + dfs(node.right))
#      ...then dfs(node.left) AGAIN in the return → re-walks the whole subtree
```
**That's a correctness-of-complexity bug, not a style choice** — inlining blows O(n) up to exponential.

**Same pattern:** #110 Balanced (done Day 23) · #124 Max Path Sum · Longest Univalue Path.

**When do you NOT need a box?** When the return channel **isn't** spoken for — i.e. the thing you want to know *is* the thing you hand your parent. **#100 Same Tree needs no box.**

### #110 Balanced Binary Tree — the box pattern transferred *(Day 23)*
The return carries the **height** (for the parent); the **is-balanced boolean** can't share the channel → it goes in a box.
```python
def isBalanced(self, root):
    self.res = True
    def dfs(node):
        if node is None:
            return 0
        left  = dfs(node.left)
        right = dfs(node.right)
        self.res = abs(left - right) <= 1 and self.res   # 🔑 ONLY-EVER-FALSIFY
        return 1 + max(left, right)                       # height, for the parent
    dfs(root)
    return self.res
# O(n) time · O(h) space
```
> **The "only-ever-falsify" move:** `... <= 1 and self.res`. Once `self.res` is `False`, `X and False` stays `False` — a later balanced node **cannot** erase an earlier failure. It's the boolean analog of #543's `max` (which only ever grows). **Whenever the box accumulates a verdict across all nodes, the update must be monotonic — `max`/`min`/`and`/`or`, never a bare assignment that can overwrite.**
> *(This version doesn't short-circuit — the `-1` sentinel form bails early. Know it as the "can you optimize?" answer; this form is the more readable one.)*

---

## #100 — Same Tree (two trees, one walk)
```python
def isSameTree(self, p, q):
    if p is None and q is None:
        return True                 # ← the `and` check MUST come first
    if p is None or q is None:
        return False                # ← by here "not both None", so `or` = EXACTLY ONE
    if p.val != q.val:
        return False
    return (self.isSameTree(p.left,  q.left) and
            self.isSameTree(p.right, q.right))
# O(n) time (n = the SMALLER tree — it short-circuits) · O(h) space
```

**Neither base case works alone. Each catches what the other misses:**

| Scenario | `or…return False` alone | `and…return True` alone |
|---|---|---|
| both `None` | returns `False` ✗ (should be True) | ✅ |
| exactly one `None` | ✅ | falls through → touches `p.val` → **crash** ✗ |

**Order is load-bearing.** Flip them and two empty trees return `False`.

> **The reframe that makes it click:** `isSameTree(p, q)` asks ***"is the ENTIRE SUBTREE at `p` identical to the entire subtree at `q`?"*** — **not** "do these two nodes match." Passing the value gate proves the **nodes** match; it proves **nothing** about what's below. So `True` needs **all three**: values match **AND** left subtrees identical **AND** right subtrees identical.
> *(Counterexample if you think the value gate is enough: `1` with a left child `2`, vs `1` with a right child `2`. Roots match. Trees differ.)*

> **STOP PEEKING DOWN.** Never write `p.left.val` — that's `None.val` on any leaf (the Day-21 #226 crash). **Compare the node you're STANDING on, and let the recursion handle the children. The base case is where `None` gets handled — so nobody ever has to peek ahead.**

---

---

## 🔑 BFS — level-order traversal *(learned Day 23 — #102, #199)*

**DFS dives deep; BFS goes level by level, top-to-bottom, left-to-right.** Reach for BFS whenever the problem cares about **levels**: "level order", "right side view", "min depth", "zigzag", "widest level".

**Why a queue, not recursion:** recursion is the call stack = **LIFO**. Level-order needs **FIFO** — the node seen *first* (leftmost) is processed *first*.

**The deque = a line at a coffee shop:**
- `q.append(x)` — join the **back**
- `q.popleft()` — leave the **front** ← **O(1)**
> ⚠️ **Never use a plain list's `pop(0)` for this — it's O(n)** (shifts every element), silently making BFS **O(n²)**. Always `from collections import deque`.

**Popping = "it's your turn":** pull a node off the front, **use it** (append its value to the answer), then **put its children at the back** for later.

### The skeleton — with the `level_size` freeze
```python
from collections import deque

def levelOrder(self, root):
    if root is None:                     # guard
        return []
    q = deque([root])
    answer = []
    while q:
        level_size = len(q)              # 🔑 FREEZE — the queue right now IS one whole level
        level = []
        for _ in range(level_size):      # pop exactly that many
            node = q.popleft()
            level.append(node.val)       # ← use it
            if node.left:  q.append(node.left)     # kids to the back for the NEXT round
            if node.right: q.append(node.right)
        answer.append(level)             # one clean level
    return answer
```

**Why freeze `len(q)` into a variable?** Inside the loop you `append` the next level's kids, so **`len(q)` grows while you loop.** Reading it live (`for _ in range(len(q))`) never stops at the level boundary — it bleeds into the next level and the grouping collapses to a flat stream. Capture the count **before** appending, so the fence can't move.
*(In Python `range(len(q))` happens to evaluate once anyway — but write `level_size = len(q)` to state intent and stay safe in `while` conditions / other languages.)*

**The insight:** at the top of each round, **the queue holds exactly one complete level and nothing else.** After processing level 0, it's exactly level 1; after level 1, exactly level 2. That's what makes `len(q)` the level size.

### #199 Right Side View — one-line change
Rightmost node of each level = the **last** node popped that round: `answer.append(level[-1])`.

## 🔑 DFS vs BFS space — the guaranteed follow-up
| | Time | Space | Governed by |
|---|---|---|---|
| **DFS** (recursion) | O(n) | **O(h)** — call stack, one frame per level of DEPTH | tree's **HEIGHT** |
| **BFS** (queue) | O(n) | **O(n)** — queue holds the widest level (~n/2 at the bottom of a full tree) | tree's **WIDTH** |
> **DFS space = height. BFS space = width.** The level information BFS gives you costs O(n) space. *(Contrast: an iterative BST descent has neither a stack nor a wide queue → **O(1)**.)*
> ⚠️ **Don't pattern-match the complexity.** Day 23: first wrote #102 as "O(h)/O(1)" (the DFS reflex), then re-derived to O(n)/O(n). **Re-derive every complexity; never recall it from a neighbouring problem.**

### BFS reappears in: #102, #199, #103 (zigzag), #515 (max per level), #542 (grid BFS), #994 (rotting oranges)

## Complexity
- **Time: O(n)** for a full traversal — every node visited exactly once.
- **Space: O(h)** — the call stack holds one frame per level, where `h` = height.
  - balanced tree → `h ≈ log n` → **O(log n)**
  - skewed tree (a linked list) → `h = n` → **O(n)** worst case
- **"Recursion is free" is wrong.** If it recurses, it costs stack space. Always say O(h) and name the worst case.
- BFS space is **O(w)** (widest level) → worst **O(n)**.

## What DFS actually means *(the word, taught Day 22)*
**DFS = Depth-First Search:** go as deep as you can down one branch before backing up. Your #104 fully explores the **entire left subtree** before touching `node.right`. **Recursion on a tree IS DFS** — the call stack *is* the "go deep, then back up" mechanism. Its sibling is **BFS** (level by level, with a `deque`).
**`dfs` is just a conventional function name.** No magic — it could be `helper` or `go`.

## Your gotchas
- **`.val` vs `.left`/`.right`** (M-021 → **blocker B-5**) — #226 attempt 1 swapped the *values*, which (a) only mirrors one level and (b) crashes on any leaf via `node.left.val` when `node.left` is `None`. **Swap the pointers.**
- **Being in scope does not mean being relevant** (M-021, Day 22). In the res-drill he reached for `left`/`right` to *count nodes* — but those hold **heights**. They were sitting right there, looking useful. **Before you use a variable, say what it is actually holding.**
- **Missing `self.`** on recursive calls inside a class method (M-020) — `self.invert(...)`, not `invert(...)`. **The test: did I attach it with `self.x = ...` in `__init__`, or is it a method of this class? Yes → `self.`; parameter or local → bare.** `self.node.left` is nonsense — `node` is a *parameter*, it lives on no object. Full write-up: **[python-classes.md](python-classes.md)**.
- **Need a value that survives across recursive calls?** (a running max, a counter, a result list) — a local **can't**; each call gets its own copy. Attach it to the object: `self.diameter = 0`. **local = one per call · `self.` = one per object.** This is exactly how #543 works.
- **The `None` guard IS the base case** (B-4). Every tree function starts with `if root is None`. Skipping it doesn't just break an edge case — it breaks the recursion.
- **"return 0" isn't a failure signal.** An empty tree genuinely *has* depth 0. The base case returns the true answer for the smallest input, not an error code.
- **Don't trace the recursion in your head.** Assume the recursive call returns the correct answer for its subtree, and just write how to combine. Trace only to debug.
