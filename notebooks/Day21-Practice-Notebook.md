# Day 21 — Practice Notebook
**Date:** 2026-07-13 (Monday) · **Week 4 folder / Sprint Week 3** · **Phase:** Summer Sprint, Block B

> **The milestone day.** You learned **recursion** from zero — traced it, wrote it, understood the call stack — and then solved your first two **Tree** problems off the template. This is the single highest-leverage hour of the sprint so far: Trees, Backtracking, Graphs and DP are *all* recursion. It cost you LRU Cache (#146), which is now rescheduled to **Day 24**.

---

## Block 1 — Reviews (6 due, protocol order: resets → 1d → 3d → oldest)

| # | Problem | Rung | Result | Time | What happened |
|---|---|---|---|---|---|
| 1 | Daily Temperatures (#739) | reset 1d | ✅ **PASS** | 6:55 | **Reset cleared.** The `while stack and ...` guard was back — the exact thing that failed it last time. |
| 2 | Reverse Linked List (#206) | 1d | ✅ **PASS** | 2:03 | Clean. `prev`/`curr`/`nxt` reassignment fluent now, and **`return prev` was there** (that's the B-3 miss from Day 19 — fixed). |
| 3 | Merge Two Sorted Lists (#21) | 1d | ✅ **PASS** | 5:57 | Correct. One typo (`! =`), self-caught. Dummy + tail pattern is solid. |
| 4 | **3Sum (#15)** | 3d | ❌ **FAIL → reset 1d** | 12:21 | **Regression:** used `if nums[left] == nums[left+1]: left += 1` for dedup instead of `while`. A single `if` skips *one* duplicate; a run of three identical values still slips through. Dedup is a **loop**, not a check. |
| 5 | Longest Consecutive Sequence (#128) | 3d | ✅ **PASS** | 8:03 | The only-start check (`if n-1 not in numSet`) is internalized. Correctly said O(n), not O(n²). |
| 6 | **Encode/Decode Strings (#271)** | 3d | ❌ **FAIL → reset 1d** | 11:45 | Three bugs: compared the **index** to `"#"` instead of the **character** (`s[j]`), forgot `i = j + 1` to jump past the decoded chunk, and read the length/content in the wrong order. |

**Rolled forward (not reached, budget hit):** #125, #704.

### The two failures share one root cause
Both were **execution slips, not comprehension gaps** — you knew the algorithm in both cases and narrated it correctly before coding. That's your standing weakness: *first-draft precision*. The good news is it's the most trainable thing on the list. The pre-submit audit exists for exactly this:

> **"Does it return? Are the edges guarded? Am I looping where I should be looping? Is this an index or a value?"**

`#271`'s "index vs. char" bug is a **sibling of the node-vs-value bug** you then hit on #226 an hour later. Same shape: *you reached for the container instead of the thing inside it.* Worth naming, because it will keep showing up.

---

## Block 2 — RECURSION (taught from scratch)

You said: *"I think it is best you drill me on recursion first cause it looks really confusing."* Correct instinct — this is a new **mental model**, not new syntax, and every remaining pattern depends on it.

### The idea

A recursive function **calls itself on a smaller version of the problem.** Every one has exactly two parts:

```python
def f(problem):
    if <smallest possible case>:   # BASE CASE — the stopping condition
        return <the answer for it>
    return <combine me with>  f(smaller problem)   # RECURSIVE CASE
```

**Without the base case it never stops** → `RecursionError`. The base case is not optional decoration; it is what makes the whole thing terminate.

### The call stack (the part that clicked)

Calls **stack up** — nobody returns until the deepest one returns. `fact(4)`:

```
fact(4) → 4 * fact(3)        ← waiting
          fact(3) → 3 * fact(2)   ← waiting
                    fact(2) → 2 * fact(1)   ← waiting
                              fact(1) → 1   ← BASE CASE, returns
                    fact(2) = 2 * 1  = 2    ← now unwinds
          fact(3) = 3 * 2  = 6
fact(4) = 4 * 6 = 24
```

**Down** = the calls pile up. **Up** = the answers come back. You traced this correctly.

### Drills you did

1. **Trace `fact(4)` by hand** → ✅ correct, all four frames.
2. **Write `power(base, exp)` from scratch** → ✅ correct:
   ```python
   def power(base, exp):
       if exp == 0:
           return 1
       return base * power(base, exp - 1)
   ```
3. **`sumOfValues(node)` on a tree** — this one exposed a real misconception. You wrote `return 2 + sumOfValues(left) + sumOfValues(right)`, reasoning that a node has two children.

   > **The fix:** the constant in front is **what THIS node contributes**, not how many children it has. A node contributes its own **value**:
   > ```python
   > return node.val + sumOfValues(node.left) + sumOfValues(node.right)
   > ```
   > Ask "*what does this one node add to the total?*" — for a sum it's `node.val`; for a **count** it's `1`; for **depth** it's `1` (one level). That reframing is what made #104 easy ten minutes later.

### The two flavors of tree recursion

| Flavor | You do | Return value | Example |
|---|---|---|---|
| **Compute & combine** | ask the children for answers, merge them | the answer | #104 Max Depth |
| **Do work & mutate** | change this node, then recurse to change the rest | usually the root | #226 Invert |

---

## Block 2 — New problems (Trees)

### #104 — Maximum Depth of Binary Tree (Easy) ✅

```python
def maxDepth(self, root):
    if root is None:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

- **Base case:** an empty tree has depth **0**. (You asked *"what do you mean by return 0?"* — an empty tree isn't an error, it's a tree with zero levels. That IS its answer.)
- **Recursive case:** the depth of this tree = **1** (for me) + the depth of my **deeper** child.
- **Complexity:** **O(n) time** — every node visited once. **O(h) space** — the call stack holds one frame per level, worst case a skewed tree → **O(n)**.

> You initially said "O(1) space", then corrected yourself unprompted: *"So if it is stacked up like that it is taking up space therefore, O(n) space also."* — **exactly right, and you got there yourself.** The call stack is real memory. This is the space reflex working.

### #226 — Invert Binary Tree (Easy) ✅

**Attempt 1 (wrong):** you swapped the **values**:
```python
temp = node.left.val
node.left.val = node.right.val   # ❌
```
Two problems: (a) swapping the two children's values only flips *one level* — the grandchildren stay put, so the tree isn't mirrored; and (b) if `node.left` is `None` (any leaf!), `node.left.val` **crashes**. That's a dropped edge-guard — **B-4** again.

**Attempt 2 (correct)** — swap the **pointers**, which carries each entire subtree with it:
```python
def invert(self, node):
    if node == None:
        return None
    temp = node.left
    node.left = node.right
    node.right = temp
    self.invert(node.left)     # ← self. required (M-020)
    self.invert(node.right)
    return node
```

- `.left` / `.right` hold **nodes**; `.val` holds a **value**. Reassigning `.left` moves a whole subtree. Reassigning `.val` moves one number. **Node vs. value — this is your recurring blind spot.**
- **`self.`** on the recursive calls, because it's a method on the class (**M-020**, second occurrence — first was `self.minStack` on #155).
- Python shortcut you'll see: `node.left, node.right = node.right, node.left` does the swap with no `temp`.
- **Complexity:** **O(n) time**, **O(h) space** (worst **O(n)**).

---

## Post-session concept: **when does `self.` go in front?** *(you asked — this one is load-bearing)*

> *"Why are we not doing `self.node.left = self.node.right`? How do I know when to actually include `self.`?"*

### `self` is not a magic prefix — it's a variable

When Python runs `sol.invertTree(root)`, it quietly passes the object in as the first argument. So inside the method, **`self` is just a name pointing at your `Solution` object** — no different from `node` being a name pointing at a TreeNode.

Which means **two different objects are in play**:

| Name | Points at | What lives on it |
|---|---|---|
| `self` | the **Solution** object | its methods — `invertTree`, `maxDepth`, any helper |
| `node` | a **TreeNode** object | `.val`, `.left`, `.right` |

**The dot means "go inside *this* object."** So the only question is ever: **whose thing is it?**

- `invert` is a method **on the Solution** → reach it with **`self.invert(...)`**. Bare `invert(...)` makes Python hunt for a standalone global function by that name → `NameError`.
- `left` is an attribute **on the TreeNode** → reach it with **`node.left`**.
- **`self.node.left` is nonsense**: it says *"go inside Solution, find an attribute called `node`"* — but `node` is a **parameter**, a local name that exists only for this call. It was never stored on the object. → `AttributeError`.

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

### Why Min Stack (#155) was different

```python
class MinStack:
    def __init__(self):
        self.minStack = []          # ← ATTACHED to the object here

    def push(self, val):
        self.minStack.append(val)   # so every method reaches it through self
```

`__init__` **stores** the list on the object, so all methods can find it later. A parameter like `node` is never stored — it arrives, gets used, and vanishes when the call returns.

### ✅ The test (memorize this)

> **For any name `x`: did I attach it with `self.x = ...` in `__init__`, or is it a method defined in this class?**
> **Yes → `self.x`.  ·  No (it's a parameter or a local variable) → bare `x`.**

**Your check — you got it right, including the two you correctly left alone:**

| | `self.`? | Why |
|---|---|---|
| `self.maxDepth(root.left)` | **yes** | a method on the class ✅ |
| `root.left` | no | `root` is a **parameter** — a different object |
| `leftDepth` | no | a **local variable**, made with a plain `=` |

### The sentence to keep
> **`self.` is a lookup mechanism, not an importance marker.** It literally means *"look for this name inside the object I was called on."*
>
> **local = one per call.  ·  `self.` = one per object.**

### Where this bites next — **#543 Diameter (tomorrow)**
You'll need a value that **survives across recursive calls** (the running max diameter). A local can't do that — every call gets its own private copy. So you'll do exactly what Min Stack did: `self.diameter = 0`, and every call in the recursion reads and writes **the same one**. That's the whole reason `self.` exists.

---

## Mistakes logged today

| Ref | What | Lesson |
|---|---|---|
| **M-020** (recur. 2) | Missing `self.` on the recursive calls in `invert` | Inside a class method, calling another method on the same object is **`self.method()`** |
| **M-011 / B-4** | `node.left.val` on a leaf → crash (#226 attempt 1) | Edge scan before submitting: *"is this None?"* |
| **M-018-adjacent** | #15 dedup used `if` instead of `while` | Skipping a **run** of duplicates is a loop |
| *(new, watch)* | #271 compared the **index** to `"#"`, not `s[j]` | Index vs. value — the same confusion as node vs. value |

## Blocker status
- **B-3 (forgetting `return`) — ✅ CLEARED.** Every function you wrote today returned its answer (8 for 8: six reviews + #104 + #226). Two clean sessions in a row (Day 20 + Day 21). **Keep "does it return?" as a standing pre-submit habit** — it re-escalates if it comes back.
- **B-4 (dropping edge-guards) — 🟡 still active.** #739's guard was back (good), but #226 attempt 1 would have crashed on every leaf. **0 of 2 clean.** Pre-submit edge scan stays.

---

## Complexity scorecard
| Problem | Your call | Verdict |
|---|---|---|
| #128 | O(n), not O(n²) | ✅ unprompted, with the reason |
| #104 | O(n) time; O(1) → **self-corrected to O(h)/O(n)** | ✅ — the correction is the win |
| #226 | O(n) time, O(h) space | ✅ |

---

## Next session — **Day 22 (Jul 14)**
1. **Block 1 (~7 due):** the two resets first (**#15**, **#271**), then #1, #217, #875, #19, #125, plus the new #104/#226 at 1d. Time-box 30–40 min; verbal tier for the 21d items.
2. **Block 2 — new (Trees, all off today's template):** **Diameter of Binary Tree (#543)**, **Same Tree (#100)**, **Lowest Common Ancestor in a BST (#235)**.
3. **⚠️ Standing reminder: LRU Cache (#146) is now on Day 24 (Jul 16).** It's the last unplaced core problem — don't let it drift.
4. **Habits:** does it return? · **edges guarded (B-4)?** · **node vs. value / index vs. value** · dedup needs a `while` · space reflex includes the **call stack**.
