# Python: classes and `self.` — the reference

**Not a pattern — a language concept file.** Started Day 21 (2026-07-13) because `self.` is load-bearing for Trees, Backtracking, Graphs, DP and every design problem (LRU Cache, Min Stack, Trie).

## The one idea

**`self` is not a magic prefix. It's a variable** — a name bound to *the object the method was called on*. When Python runs `sol.invertTree(root)`, it quietly passes the object in as the first argument, and inside the method that argument is called `self`.

So in a typical LeetCode method there are **two different objects** in play:

| Name | Points at | What lives on it |
|---|---|---|
| `self` | the **Solution** object | its methods, and anything set with `self.x = ...` |
| `node` / `root` | a **TreeNode** (or ListNode) | `.val`, `.left`, `.right` / `.next` |

**The dot means "go inside *this* object."** So the only question is: **whose thing is it?**

## ✅ The test

> **For any name `x`: did I attach it with `self.x = ...` in `__init__`, or is `x` a method defined in this class?**
> **Yes → `self.x`.  ·  No (parameter, or a local you just made) → bare `x`.**

```python
class Solution:
    def invert(self, node):          # self = the Solution.  node = a TreeNode.
        if node is None:
            return None
        node.left, node.right = node.right, node.left   # TreeNode's stuff → node.
        self.invert(node.left)                          # Solution's stuff → self.
        self.invert(node.right)
        return node
```

| | `self.`? | Why |
|---|---|---|
| `self.invert(...)` | **yes** | a **method** defined in this class |
| `node.left` | no | `node` is a **parameter** — a *different object* |
| `leftDepth = ...` | no | a **local variable** (plain `=`) |
| `self.minStack` (#155) | **yes** | **attached** to the object in `__init__` |

## The three failure modes

1. **Bare `invert(...)`** when it's a method → Python hunts for a standalone global function → **`NameError`**. *(This was M-020, Day 21, on #226.)*
2. **`self.node.left`** → says *"find an attribute called `node` on the Solution"* — but `node` is a parameter, never stored on the object → **`AttributeError`**. Parameters arrive, get used, and vanish when the call returns.
3. **Bare `minStack`** when it *was* set in `__init__` → **`NameError`**. *(M-020, Day 19, on #155.)*

## Why it matters for recursion

> **local = one per call.  ·  `self.` = one per object.**

Every recursive call gets its **own private copy** of every local variable. So when you need a value that **survives across calls** — a running max, a counter, a result list — a local can't do it. Attach it to the object:

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0            # ONE of these, shared by every call below
        self.height(root)
        return self.diameter

    def height(self, node):
        if node is None:
            return 0
        L = self.height(node.left)
        R = self.height(node.right)
        self.diameter = max(self.diameter, L + R)   # every call updates the SAME one
        return 1 + max(L, R)
```

**That is the whole reason `self.` exists.** (Alternative: a `nonlocal` variable in a nested function — same idea, different mechanism.)

## The sentence to keep
**`self.` is a lookup mechanism, not an importance marker.** It means *"look for this name inside the object I was called on"* — nothing more.
