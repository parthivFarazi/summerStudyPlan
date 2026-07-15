# Day 22 — Practice Notebook
**Date:** 2026-07-14 · **Week 4** · Block B — Trees
**Session:** 8 reviews + 3 new problems (#543, #100, #235)

---

## Block 1 — Reviews (8 due)

### #15 — 3Sum · **reset → PASS** · 2:35... *(7:35)*

```python
# Pattern: two pointer, but one is pinned down. Sort nums first then do the two pointer.
# Be careful about the two duplicate checkers.

answer = []
alist = sorted(nums)

for i in range(len(alist)):
    if i > 0 and alist[i] == alist[i - 1]:
        continue

    target = 0 - alist[i]

    left = i + 1
    right = len(alist) - 1

    while left < right:
        if alist[left] + alist[right] == target:
            answer.append([alist[i], alist[left], alist[right]])
            left = left + 1
            right = right - 1
            while left < right and alist[left] == alist[left - 1]:
                left = left + 1
        elif alist[left] + alist[right] > target:
            right = right - 1
        elif alist[left] + alist[right] < target:
            left = left + 1

return answer

# O(n^2) time, O(n) space · 7:35
```

**PASS.** The Day-21 failure cause — dedup written as an `if` instead of a `while` — did **not** recur. The `while` was there.

**Why only `left` needs deduping:** a unique `left` value, with a fixed pin `i` and therefore a fixed `target`, forces a unique `right`. Skipping duplicate `left`s is sufficient.

---

### 🔑 Deep dive — `sorted()` vs `.sort()` (this was the real lesson of the review block)

He said space was **O(n)**, correctly. Probe: *where does the O(n) come from?* → `alist = sorted(nums)`. ✅

Probe 2: *what if you used `nums.sort()` instead?* → he said "space stays the same." ✗

| | Returns | Mutates input? | Space |
|---|---|---|---|
| `sorted(nums)` | **a new sorted list** | no | **O(n)** — the copy |
| `nums.sort()` | **`None`** | yes, in place | **O(1)** from your code |

**So `alist = nums.sort()` sets `alist = None`** → `alist[i]` → `TypeError: 'NoneType' object is not subscriptable`. It doesn't optimize the space; it crashes the program.

**The Python rule underneath it:**

> **Methods that mutate return `None`. Functions that build a new object return the object.**

| Mutates in place → returns `None` | Builds new → returns it |
|---|---|
| `nums.sort()` | `sorted(nums)` |
| `nums.reverse()` | `reversed(nums)` |
| `nums.append(x)` | `nums + [x]` |
| `d.update(other)` | `{**d, **other}` |

So `x = nums.append(5)` is *always* a bug — same family as `x = nums.sort()`.

**"In-place" ≠ zero memory.** Every sort needs scratch space of its own:
- Heapsort → O(1)
- Quicksort → O(log n) (recursion stack)
- **Timsort (what Python actually uses) → O(n) worst case** (merges runs through a temp buffer)

**Interview line:** *"I sort in place, so my own space is O(1); Python's sort itself is O(n) worst case."*
**Bonus line:** *"I'll sort in place for O(1) space — is it okay if I mutate the input?"* — shows you know it's a trade, not a free win.

**Output doesn't count.** `answer` is required output, so it isn't "extra" space. Say **O(1) auxiliary**; if asked "including output?", it's O(number of triplets).

---

### #271 — Encode/Decode Strings · **reset → FAIL (reset again)** · 8:37

```python
class Endecode:
    def encode(self, strs):
        answer = ""
        for word in strs:
            answer += str(len(word)) + "#" + word
        return answer

    def decode(self, s):
        answer = []
        i = 0
        while i < len(s):
            j = i
            while j != "#":        # ❌ BUG — j is an INDEX, "#" is a CHAR
                j = j + 1
            l = int(s[i:j])
            i = j + 1
            word = ""
            for n in range(l):
                word += s[i]
                i = i + 1
            answer.append(word)
        return answer

# O(n) time and space · 8:37
```

**FAIL → reset to 1d.**

**The bug:** `while j != "#"` compares an **index** to a **character**. `0 != "#"` is always true → the loop runs `j` off the end of the string.

**The fix:** `while s[j] != "#":`

**Why this one stings:** *this is the exact cause #271 was reset for last time.* Logged Day 21 as **index-vs-char**. Same slip, same problem, second time. It is **M-021 — container vs. contents.**

> **The reflex: "is this the box, or what's in the box?"**
> `j` is the box. `s[j]` is what's in it.
> `i` vs `nums[i]` · `node` vs `node.val` · same question every time.

Encode was correct. Approach, encoding scheme, and pointer plan were all right — **this was a precision slip, not a comprehension gap.**

---

### #242 — Valid Anagram · **FAIL (reset)** · 3:11

```python
# ❌ First draft — missing the length guard

adict = {}
for char in s:
    if char not in adict:
        adict[char] = 1
    else:
        adict[char] += 1

for char in t:
    if char not in adict or adict[char] <= 0:
        return False
    else:
        adict[char] -= 1

return True
```

**Counterexample that kills it:** `s = "aab"`, `t = "ab"` → every char of `t` is found, returns `True`. Wrong — different lengths, not an anagram.

**The fix:**

```python
if len(s) != len(t):
    return False
```

**FAIL → reset to 1d.** Needed the counterexample handed to him — by the contract, a hint = a fail.

**Root cause: B-4, the open blocker.** *"Lengths equal?"* is **literally on his own pre-submit checklist.* Knew the algorithm cold, wrote it in 3 minutes, shipped without running the scan.

**Complexity correction — the good news.** He said O(n) space; probed on the constraint (*lowercase English letters*) → **at most 26 keys, ever** → **O(1)**.

> **Interview line:** *"O(1) space — the map holds at most 26 entries since the input is lowercase letters. If it were full Unicode, it'd be O(k) for the character set."*
> **Bounded by the alphabet, not by `n`.**

---

### #226 — Invert Binary Tree · **PASS** · 2:32

```python
def treeInvert(self, node):
    if node == None:
        return None

    temp = node.left
    node.left = node.right
    node.right = temp

    self.treeInvert(node.left)
    self.treeInvert(node.right)

    return node

# O(n) time, O(h) space · 2:32
```

**PASS → 3d.** The Day-21 crash (`node.left.val` on a leaf) is gone — the `None` guard is there, and he swaps **pointers**, not values.

**Space probe → the O(h) framing landed:**
- Space here = the **recursion call stack**, one frame per level → **O(h)**.
- Balanced: `h = log n` → **O(log n)**
- Degenerate chain: `h = n` → **O(n)**

> **Say it as: "O(h) — O(n) worst case, O(log n) balanced."** Same sentence for *every* tree recursion.

---

### #104 — Maximum Depth · **PASS** · 3:23

```python
def maxDepth(self, node):
    if node == None:
        return 0
    return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

# O(n) time and O(h) space where worst case is O(n) and balanced tree is O(log n)
```

**PASS → 3d.** Carried the O(h) framing over **unprompted**, one problem after learning it. The space reflex is sticking.

---

### #125 — Valid Palindrome · **PASS** · 4:45

```python
astr = ""
for char in s:
    if char.isalnum():
        astr += char.lower()

left = 0
right = len(astr) - 1

while left < right:
    if astr[left] != astr[right]:
        return False
    else:
        left = left + 1
        right = right - 1
return True

# O(n) time and space · 4:45
```

**PASS → 21d (verbal tier from now on).**

**Edge handled without prompting:** a string with **no alphanumeric characters** (`" ."`) → `astr = ""` → `left=0`, `right=-1` → loop never runs → returns `True`. Correct: empty *is* a palindrome.

**The O(1)-space follow-up** (interviewers always ask): don't build the string — two pointers walk `s` directly, skipping non-alphanumerics in place, comparing `s[left].lower()` to `s[right].lower()`.
⚠️ **The skip must be a `while`, not an `if`** — `"a,,,,b"` has a *run* of junk. And guard `left < right` inside those inner loops.

---

### Verbal tier — #1 Two Sum, #217 Contains Duplicate

Both **PASS → 60d.** Complexity right on both (O(n)/O(n)).

**But he stated both approaches in the wrong order** — "add it to the set, *then* check" — which, as literally described, is broken:

- **#217, `[1,2,3,4]`:** add `1` → check "is `1` in the set?" → yes, you just put it there → returns `True`. No duplicates exist.
- **#1, `[3,3], target=6`:** insert `{3:0}` → check complement `3` → found at index 0 → returns `[0,0]`. Self-paired.

**The invariant:** **check first, then insert.** The map/set holds **only what you've already passed** — never the element you're standing on. That's what makes self-pairing impossible.

He had the right model and *described it imprecisely*. **In an interview the interviewer only has what you say.** Say the loop body in the order it executes.

**Also worth noting — good instinct:** he asked *"is Two Sum sorted?"* before answering. That question **is** the fork:
- **#1 unsorted → hash map**
- **#167 sorted → two pointers**

---

### Block 1 scoreboard

| Problem | Result | Rung |
|---|---|---|
| #15 3Sum | ✅ Pass — dedup `while` held | 1d → **3d** |
| #271 Encode/Decode | ❌ **Fail** — index-vs-char (M-021, 2nd time on this problem) | **reset 1d** |
| #242 Valid Anagram | ❌ **Fail** — missing length guard (B-4) | **reset 1d** |
| #226 Invert Tree | ✅ Pass | 1d → **3d** |
| #104 Max Depth | ✅ Pass — O(h) unprompted | 1d → **3d** |
| #125 Valid Palindrome | ✅ Pass | 7d → **21d** |
| #1 Two Sum | ✅ Verbal | 21d → **60d** |
| #217 Contains Duplicate | ✅ Verbal | 21d → **60d** |

**6 of 8.** **Both failures were execution slips, not knowledge gaps.** He knew every algorithm and lost both on a guard he had already written down.

---

## Block 2 — New material

### 🔑 The new mental model: **"the box outside the recursion"**

*(Taught in isolation before #543 — he asked for it, correctly.)*

Every recursion so far answered **one** question, and the return value **was** the answer (#104: return the height → the root's height *is* the answer).

Now: **what if the thing your parent needs and the thing you want to know are different numbers?**

At any node you have **two** distinct facts:

1. **What you owe your parent.** Your parent is computing *its* height, so it needs *your* height. **The return channel is spoken for.** You have no choice.
2. **What you actually want.** e.g. `left_height + right_height` — the longest path *bending at this node*. Your parent doesn't care and can't use it.

**You can't return both.** So the second one goes in **a box that lives outside the recursion** — every node peeks in on its way up and overwrites it if it beat the record. At the end, you read the box.

> **`dfs` returns what the PARENT needs. `res` collects what YOU need.**

#### Why the box is *mandatory*, not a convenience

```
        1
       /
      2
     / \
    3   4
   /     \
  6       7
```

True diameter = `6→3→2→4→7` = **4 edges**. It **bends at node 2** and never touches the root.

At the root: `left_height=3`, `right_height=0` → `3 + 0 = 3`. **Wrong.**

Why? All the root ever receives from `dfs(node2)` is a **single number** — `3`, the height. That number has **no memory** of the fat path running *across* node 2. **The fact cannot fit through the return pipe.** So node 2 writes `4` to the box on its way up, and the root never needs to know.

#### The Python syntax (this is what actually blocked him)

```python
def diameter(root):
    res = 0
    def dfs(node):
        ...
        res = max(res, left + right)   # ❌ UnboundLocalError
```

**Assigning** to `res` inside `dfs` makes Python treat `res` as a **brand-new local** belonging to `dfs` — so the `res` on the right-hand side doesn't exist yet.

Two fixes:

```python
self.res = 0                  # Option A — attribute (use this on LeetCode)
self.res = max(self.res, ...)

nonlocal res                  # Option B — reach out to the enclosing scope
res = max(res, ...)
```

#### The 6-slot anatomy

```python
class Solution:
    def someProblem(self, root):
        self.res = 0                  # 1. the box — OUTSIDE the recursion

        def dfs(node):                # 2. the helper
            if node is None:
                return 0              # 3. base case

            left  = dfs(node.left)    # 4. collect what the children owe you
            right = dfs(node.right)

            self.res = ???            # 5. UPDATE THE BOX (on the way back up)

            return ???                # 6. RETURN what your PARENT needs

        dfs(root)                     # 7. kick it off — DISCARD the return value
        return self.res               # 8. read the box — THAT is the answer
```

**Only slots 5 and 6 ever change.** Slot 6 = *"what does my parent need?"* Slot 5 = *"what did I learn here that nobody upstream will ever hear about?"*

**Line 7 feels wrong the first time** — you call a function and throw its answer away. But you're not calling it *for* its answer. You're calling it **for the side effect**: it walked the whole tree and filled the box.

---

### 🔑 Sidebar: what "DFS" actually means

He asked. Fair — the term had never been taught.

**DFS = Depth-First Search:** go as deep as you can down one branch before backing up. His own #104 fully explores the **entire left subtree** before touching `node.right`. **He'd been writing DFS since Day 21 without the word.**

- **Recursion on a tree IS DFS** — the call stack *is* the "go deep, then back up" mechanism.
- Its sibling is **BFS** (breadth-first, level by level) — Day 23.
- **`dfs` is just a conventional function name.** No magic. Could be `helper`, `go`, `height`.

---

### Warm-up drill — wiring only *(count the nodes using the box)*

Deliberately trivial algorithm so the only thing being practiced is the plumbing.

**His attempts:**
1. `self.res += left + right` → on a 3-node tree gives **2**. ✗
2. `self.res += 1 + left + right` → gives **5**. ✗

**Why both fail:** `left` and `right` hold **heights**, not counts. He kept bolting them onto the line **because they were sitting right there in scope, looking useful.**

> **Being in scope doesn't mean being relevant.** Before using a variable, ask what it is actually holding.
> **M-021 again — third costume of the day.**

**The answer — `dfs` visits every node exactly once, so:**

```python
self.res = 0

def dfs(node):
    if node is None:
        return 0
    left  = dfs(node.left)
    right = dfs(node.right)
    self.res += 1                  # slot 5 — count THIS node. One term. Nothing else.
    return 1 + max(left, right)    # slot 6 — height, for the parent

dfs(root)
return self.res
```

Two channels, doing completely unrelated jobs. **That's** the pattern.

---

### #543 — Diameter of Binary Tree · **SOLVED** ✅

> Longest path between **any two nodes**, in **edges**. May not pass through the root.

**The trace that makes it click** — `dfs` returns height in **nodes** (`None → 0`, leaf → `1`):

```
      1
     / \
    2   3
   / \
  4   5
```

| Node | `left` | `right` | **`left + right`** ← path bending here | **returns** `1 + max(left,right)` | box `res` |
|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 1 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 |
| 2 | 1 | 1 | **2** ← `4→2→5` | 2 | **2** |
| 3 | 0 | 0 | 0 | 1 | 2 |
| 1 | 2 | 1 | **3** ← `4→2→1→3` | 3 | **3** |

**Answer = 3** — that's the **box**, not the return value.

```python
def diameter(self, root):

    self.res = 0

    def dfs(node):

        if node == None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        self.res = max(self.res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return self.res

# O(n) time, O(h) space (O(n) worst, O(log n) balanced)
```

**Correct first try, and he stated the complexity cold.**

**Two subtle things he got right:**

1. **`dfs(node.left)`, not `self.dfs(node.left)`** — `dfs` is a *nested function*, not a method. But `self.res` **does** need `self` (it's an attribute). He threaded that needle unprompted.
   > **Nested helper → no `self`. Class method → `self`.**
2. **`self.res = max(...)` comes BEFORE the `return`** — the box is written **on the way back up**, after the children report. Write it before the recursive calls and `left`/`right` don't exist yet.

**The insight *he* spotted, and it's the important one:**

```python
# plain DFS (#104) — recursive calls inlined, used once
return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

# res-pattern — calls CAPTURED in variables, used TWICE
left  = dfs(node.left)
right = dfs(node.right)
self.res = max(self.res, left + right)   # use #1
return 1 + max(left, right)              # use #2
```

> **The moment a child's result feeds both the box and the return, capture it in a variable.**
> Inline them and you'd call `dfs(node.left)` twice — **re-walking the whole subtree**, blowing O(n) up to exponential. That's a correctness-of-complexity issue, not style.

**Same pattern reappears in:** #110 Balanced Binary Tree, #124 Max Path Sum, Longest Univalue Path.

---

### #100 — Same Tree · **SOLVED** ✅

> Two roots `p`, `q`. `True` iff structurally identical **and** same values everywhere.

**First instinct (caught before coding):** *"do I check `p.left.val == q.left.val`?"*

❌ **`None.val` → `AttributeError`.** That is **exactly** the Day-21 #226 crash, same shape (B-4).

> **Stop looking down at your children's values. Compare the node you're standing on, and let the recursion handle the children.**
> **The base case is where `None` gets handled — so nobody ever has to peek ahead.**

**The crux he found himself** — which base case?

| Scenario | Correct answer |
|---|---|
| **A:** `p = None`, `q = None` | `True` — two empty trees are identical |
| **B:** `p = None`, `q = Node(5)` | `False` — structurally different |

- `if p is None or q is None: return False` → breaks **A** (returns False; should be True)
- `if p is None and q is None: return True` → breaks **B** (falls through → touches `p.val` → **crash**)

**Neither alone works. Each handles what the other misses. You need both:**

```python
if p is None and q is None:
    return True          # ← the `and` check MUST come first
if p is None or q is None:
    return False         # ← by now, "not both None", so `or` means EXACTLY ONE
```

**Order is load-bearing.** Flip them and two empty trees return `False`.
*(He first wrote it nested — `if (or): if (and): True else: False` — which is **logically correct**, just less flat.)*

**Second confusion — "doesn't it just `return True` after the value gate?"**

Counterexample:
```
p:   1        q:   1
    /              \
   2                2
```
Both roots `= 1`, neither `None` → passes the gate → returns `True`. **But these trees differ.**

> **Passing the value gate proves the two NODES match. It proves nothing about what's below them.**
>
> **Reframe: `isSameTree(p, q)` means "is the ENTIRE SUBTREE at `p` identical to the entire subtree at `q`?"** Not "do these two nodes match." So `True` requires **all three**: values match **AND** left subtrees identical **AND** right subtrees identical.

```python
def isSameTree(self, p, q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    left = self.isSameTree(p.left, q.left)
    right = self.isSameTree(p.right, q.right)

    return left and right

# O(n) time and O(h) space where O(n) worst and O(log n) balanced
```

**No box needed — and he made that call himself, correctly.**
> **You only need `res` when the return channel is already spoken for.** Here it isn't: the thing you want to know ("are these identical?") **is** the thing you hand your parent. One question, one channel. **No box.**

**Notes:** `self.isSameTree(...)` **does** take `self` — it's a class method, not a nested helper. Also: short-circuits — the instant any pair mismatches, `False` propagates up without exploring the rest. `n` = nodes in the **smaller** tree.

**Style:** use **`is None`**, not `== None`. Both work; `is` is the correct identity check and interviewers notice.

---

### 🔑 New data structure: **Binary Search Tree** *(taught cold — he'd never met it)*

An ordinary binary tree has **no rules** about placement. A BST adds exactly one:

> **For every node: everything in its LEFT subtree is smaller. Everything in its RIGHT subtree is larger.**
> **Not just the immediate children — the ENTIRE subtree, recursively.**

```
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \     /
         4   7   13
```

At `8`: left = `{3,1,6,4,7}` all < 8 ✓ · right = `{10,14,13}` all > 8 ✓
At `3`: left = `{1}` ✓ · right = `{6,4,7}` ✓ — **holds at every node.**

#### Why anyone cares — it turns a tree into binary search

Find `13`: at `8` → `13 > 8`, and **everything smaller than 8 lives left**, so `13` **cannot be there** → **throw away the entire left subtree.** Go right. At `10` → right. At `14` → left. **Found. Three comparisons.**

He never visited `3`, `1`, `6`, `4`, `7` — **eliminated without visiting**, because the invariant *guaranteed* they couldn't hold the answer.

**Same idea as #704 Binary Search.** In an array you halve by **index**; in a BST you halve by **branching**. → **O(h)**, and `h = log n` when balanced.

**Searching for something absent (`5`):** `8`→left, `3`→right, `6`→left, `4`→right → **`None`**. Hitting `None` means the value is **definitively absent** — not "not found yet." Every step eliminated the only region it could have been in.

#### The move to internalize

| | |
|---|---|
| **Ordinary binary tree** | No information → **must explore BOTH children.** (#543, #104, #226 all recurse left **and** right.) |
| **BST** | The invariant tells you which side → **compare and pick ONE.** Never explore both. |

#### The validity trap *(he got this right)*

```
        5
       / \
      3   7
         / \
        4   8      ← NOT a valid BST
```

`4`'s parent is `7`, and `4 < 7`, so **locally it looks fine**. But `4` sits in the **right subtree of `5`**, and `4 < 5`. ✗

> **The invariant is subtree-wide, not parent-child.** Checking only immediate children is the #1 wrong answer to "validate a BST" (**#98**, coming).

**And why it's fatal:** search this broken tree for `4` — you stand at `5`, see `4 < 5`, go **left**, and never find it, though it's sitting right there. **The invariant is a promise the search algorithm relies on. Break it and search silently lies.**

---

### #235 — Lowest Common Ancestor of a BST · **SOLVED** ✅

> Deepest node with **both** `p` and `q` in its subtree. A node can be an ancestor of itself.

**Standing at any node, there are exactly three situations:**

1. **Both `p` and `q` smaller** → both live left → **go left**
2. **Both `p` and `q` larger** → both live right → **go right**
3. **They split** (one smaller, one larger — or one of them *is* this node) → **THIS NODE IS THE ANSWER. Return it.**

**Why case 3 is immediate — no backtracking** *(his first instinct was "move back up to find where they meet")*:

At node `6`, with `p=2` (smaller) and `q=8` (larger):
- **Go left to `2`?** That subtree contains only values **< 6**. **You just lost `q` forever.**
- **Go right to `8`?** Only values **> 6**. **You just lost `p`.**

> **You cannot go deeper without abandoning one of them. So you are standing on the deepest node containing both. The split IS the signal — stop and return.**

**The equality case handles itself — for free:**

```python
if p.val < node.val and q.val < node.val:      # both STRICTLY smaller
elif p.val > node.val and q.val > node.val:    # both STRICTLY larger
else:                                          # everything else → the answer
```

If `p.val == node.val`: condition 1 is `6 < 6` → False. Condition 2 is `6 > 6` → False. **Falls into `else` → returns `node`.** ✅

> **The strictness (`<`, `>`, never `<=`/`>=`) is what lets equality escape into the `else`.**
> **Two narrow gates — and everything that fits neither gate is the answer.**

#### The two bugs on the first draft

```python
# ❌ Draft
if node.val > p.val and node.val > q.val:
    node = node.right                          # BUG 1 — directions INVERTED
elif node.val < p.val and node.val < q.val:
    node = node.left
else:
    return node
                                               # BUG 2 — no loop! Runs ONCE, then
                                               #   falls off the bottom → returns None
```

**Bug 1 — inverted direction.** `node.val > p.val` means `p` is **smaller**, so `p` lives **left** — but he walked **right**, into the big numbers. *(Same family as M-012: moving toward the half that cannot contain the target.)*

**Bug 2 — moved the pointer, then stopped.** He reassigned `node` and never looked at the new one. **The descent is a LOOP.**
*(Third `if`-where-a-`while`-belongs of the day: #15's dedup, #125's skip, now this.)*

#### Final

```python
while node is not None:
    if node.val < p.val and node.val < q.val:
        node = node.right
    elif node.val > p.val and node.val > q.val:
        node = node.left
    else:
        return node

# O(h) time where h = log n for balanced and h = n for worst, O(1) space
```

**Complexity — he caught the important thing himself:** **O(1) space.** No recursion → **no call stack.** One path down, no branching. First tree problem today that *isn't* O(h) space.

> **This IS binary search** — same skeleton as #704, except you halve the space by **following a pointer** instead of moving an index.

---

## Day 22 — what to take away

**The whole day had one theme, and it wasn't trees.**

Every single failure was **first-draft precision**, not comprehension. He derived the diameter box-pattern, the Same-Tree base cases, and the LCA split-rule **himself**. He then lost points on:

- comparing an **index** to a character (`j` vs `s[j]`) — **M-021**
- reaching for `left`/`right` **heights** to count **nodes** — **M-021, again**
- dropping the **length guard** on #242 — **B-4**, a guard on his own checklist
- writing an **`if`** where a **`while`** belongs — **three separate times**
- **inverting the descent direction** in a BST

> **He knows the algorithms. He is losing to his own first draft.**

### The three reflexes — run them out loud before submitting

1. **"Box or contents?"** — `j` vs `s[j]` · `i` vs `nums[i]` · `node` vs `node.val`. **And: being in scope doesn't mean being relevant.**
2. **"Is it guarded?"** — *empty? single? none-found? lengths equal? is this `None`?*
3. **"Am I looping where I should loop?"** — **skipping a run is a `while`. A descent is a `while`. A scan is a `while`.**

### Patterns banked

- **The box outside the recursion** — *helper returns what the parent needs; a variable outside collects what you actually want.* → #543, #110, #124
- **Binary Search Tree** — *compare and pick ONE side; never explore both.* → #235, #98, #700, #701
- **DFS** — the name for what he'd already been doing since Day 21.

### Times

| Problem | Time |
|---|---|
| #15 3Sum | 7:35 |
| #271 Encode/Decode | 8:37 |
| #242 Valid Anagram | 3:11 |
| #226 Invert Tree | 2:32 |
| #104 Max Depth | 3:23 |
| #125 Valid Palindrome | 4:45 |

---

## Next session → **Day 23**

1. **Reviews:** #271 + #242 (resets, fragile) · #543 / #100 / #235 (1d, brand new) · #141, #143 (1d) · #20, #424 (3d). Verbal: none new.
2. **New:** **BFS / level-order traversal** — #102 Binary Tree Level Order, #199 Right Side View. (`deque`, freeze the level size first.) Plus **#110 Balanced Binary Tree** — reuses today's box pattern.
3. **Standing habits:** box-or-contents · edges guarded · **`if` vs `while`** · complexity out loud first, time **and** space.

⚠️ **LRU Cache (#146) is still parked on Day 24 (Jul 16).** Last unplaced core problem. Do not let it drift.
