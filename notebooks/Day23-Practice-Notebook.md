# Day 23 — Practice Notebook
**Date:** 2026-07-15 · **Week 4** · Block B — Trees / BFS
**Session:** 7 reviews + 4 new problems (#102, #199, #110 + BFS taught)

---

## Block 1 — Reviews (7 due, all full re-solves)

### #271 — Encode/Decode Strings · **reset ×2 → PASS** · 9:19

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
            while s[j] != "#":          # ✅ THE BUG THAT RESET THIS TWICE IS GONE
                j = j + 1
            l = int(s[i:j])
            i = j + 1
            word = ""
            for n in range(l):
                word += s[i]
                i = i + 1
            answer.append(word)
        return answer

# O(n) time and space · 9:19
```

**PASS → 3d.** The canary cleared. `while s[j] != "#"` — compares the **character**, not the index. Multi-digit lengths (`"12#..."`) and the empty-string case (`"0#"`) both handled. **He went slower (9:19) on the problem that had beaten him twice — correct instinct.**

**This is B-5's first clean rep.** One more and the blocker drops.

---

### #242 — Valid Anagram · **reset → PASS** · 4:05

```python
if len(s) != len(t):        # ✅ guard present — he wrote "Please do not forget the length check" in his own comment
    return False

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

# O(n) time and O(1) space · 4:05
```

**PASS → 3d.** Guard present, **O(1) space** carried over from yesterday unprompted. **B-4's first clean rep.**

---

### #543 — Diameter · 1d → **PASS** · 5:01

```python
def diameter(self, root):
    self.res = 0
    def dfs(node):
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
    dfs(root)
    return self.res
# O(n) time, O(h) space · 5:01
```
**PASS → 3d.** Cold, correct. Box outside, `dfs` nested (no `self.`), `self.res` before the return, children captured. Every load-bearing detail survived overnight.

---

### #100 — Same Tree · 1d → **PASS** · 5:45

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
# O(n) time, O(h) space · 5:45
```
**PASS → 3d.** Base cases in the right order (`and` before `or`).

---

### #235 — LCA of BST · 1d → **FAIL (reset)** · 3:26

```python
# ❌ First draft — DIRECTION INVERTED (his comment even says the right thing!)
while node is not None:
    if node.val > p.val and node.val > q.val:
        node = node.right                        # ❌ both smaller → should go LEFT
    elif node.val < p.val and node.val < q.val:
        node = node.left                         # ❌ both larger → should go RIGHT
    else:
        return node
```

His own comment read *"if both are on left then go left, if both on right, go right"* — **correct. The code did the opposite.** On `p=0, q=4` (both smaller than root 6) it walked **right** into the big numbers, ran to `None`, returned `None`.

**FAIL → reset 1d.** Needed the trace handed to him. **This is B-6, 4th occurrence, same problem two days running** (#704, #33, #235 Day 22, #235 Day 23).

**The corrected code:**
```python
if node.val < p.val and node.val < q.val:
    node = node.right
elif node.val > p.val and node.val > q.val:
    node = node.left
else:
    return node
```

#### 🔑 The root-cause fix — write the comparison TARGET-first

The inversion keeps happening because he writes the condition **node-first** (`node.val > p.val`) and then has to **mentally flip it** — *"node bigger than p ⇒ p is smaller ⇒ p goes left"* — and the flip is where he inverts.

> **STOP FLIPPING. Put the target on the LEFT of the comparison so the direction word matches:**
> ```python
> if p.val > node.val and q.val > node.val:    # "p, q are BIGGER" → RIGHT
>     node = node.right                        #    the word 'bigger' ↔ 'right', same order
> elif p.val < node.val and q.val < node.val:  # "p, q are SMALLER" → LEFT
>     node = node.left
> ```
> Read aloud: *"p is bigger than node → go right."* **Nothing left to flip.**
> **General rule: `target > node → right`. `target < node → left`.** (Array BS: `target > nums[mid] → left = mid+1`.)

**B-6's drill is now concrete: write comparisons target-first.**

---

### #141 — Linked List Cycle · 1d → **PASS** · 4:46

```python
slow = head
fast = head
while fast is not None:
    if fast.next is not None:
        fast = fast.next.next
    else:
        fast = fast.next
    slow = slow.next
    if fast == slow and fast is not None:       # ✅ guarded the None==None trap
        return True
return False
# O(n) time, O(1) space · 4:46
```

**PASS → 3d.** The subtle case — **single node, no cycle** — makes both pointers `None`, and `None == None` is `True`; his `and fast is not None` guard is the only thing saving it. **He guarded it. B-4 behavior.**

**Idiomatic form to adopt** (guard lives in the loop condition, one place — also the skeleton for #876 and #142):
```python
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

---

### #143 — Reorder List · 1d → **FAIL (reset)** · 12:41

**Phases 1 & 2 correct** (find-middle with fast/slow, `mid.next = None` cut, reverse second half). **Phase 3 was the wrong merge:**

```python
# ❌ He imported #21 Merge Two Sorted Lists wholesale — a VALUE comparison
while curr1 is not None and curr2 is not None:
    if curr1.val <= curr2.val:       # ❌ reorder doesn't care about values at all
        ...
# also: curr2 = rev  →  NameError, there's no 'rev' (it's 'prev')
```

On `1→2` + `4→3` this produced `1→2→4→3`; expected `1→4→2→3`.

**FAIL → reset 1d.** **His own diagnosis nailed it:** *"I just dumped what I practiced for merging and instinctively used the sort value checker."*

#### 🔑 The lesson — recognizing the pattern gets you the SKELETON, not the BODY

| | **#21 Merge Sorted** | **#143 Reorder** |
|---|---|---|
| What picks the next node? | **the values** (`if curr1.val <= curr2.val`) | **nothing — strictly alternate** |
| Are values relevant? | yes, the whole point | **explicitly forbidden to touch** |

**The tell was in the problem statement:** *"you may not modify the values of the nodes."* **When a problem says values don't matter, a value comparison is a red flag.** This is **M-009** — carrying assumptions across problems without re-deriving.

**Corrected phase 3 (strict alternation):**
```python
curr1 = head
curr2 = prev            # the reversed second half
dummy = ListNode()
curr3 = dummy
while curr1 is not None and curr2 is not None:
    curr3.next = curr1;  curr1 = curr1.next;  curr3 = curr3.next
    curr3.next = curr2;  curr2 = curr2.next;  curr3 = curr3.next
if curr1 is not None:
    curr3.next = curr1
elif curr2 is not None:
    curr3.next = curr2
# O(n) time, O(1) space
```

---

### Block 1 scoreboard — 5 of 7

| Problem | Result | Rung |
|---|---|---|
| #271 Encode/Decode | ✅ **Pass** — `s[j]` bug dead | reset → **3d** |
| #242 Valid Anagram | ✅ **Pass** — guard present | reset → **3d** |
| #543 Diameter | ✅ Pass, cold | 1d → **3d** |
| #100 Same Tree | ✅ Pass | 1d → **3d** |
| #235 LCA BST | ❌ **Fail** — direction inverted **again** (B-6, 4th) | **reset 1d** |
| #141 Cycle | ✅ Pass — guarded `None==None` | 1d → **3d** |
| #143 Reorder | ❌ **Fail** — imported #21's value merge (M-009) | **reset 1d** |

**Both blocker problems (#271, #242) came back clean — one clean rep each on B-4 and B-5.** Both failures were *imported templates / inverted direction* — execution, not concept.

---

## Block 2 — BFS (Breadth-First Search) — new

### 🔑 Taught in isolation first (he asked — "pretty hard for me to visualise")

**BFS visits the tree level by level, top-to-bottom, left-to-right** — the opposite of DFS's dive-deep.

**Why a queue, not recursion:** recursion uses the call stack (**LIFO**). Level-order needs **FIFO** — the node seen *first* (leftmost) is processed *first*.

**The deque as a line at a coffee shop:**
```
   front  ← people LEAVE here (popleft)
   back   ← people JOIN here  (append)
```
- `q.append(x)` — join the **back**
- `q.popleft()` — leave the **front**  ← **O(1)** (a list's `pop(0)` is O(n) — shifts everything; silently makes BFS O(n²))

**Popping = "it's your turn":** you pull a node off the front, **use it** (read its value into the answer), then **put its children at the back** for their turn later.

**Step-by-step trace** on:
```
        3
       / \
      9   20
         /  \
        15   7
```
| Step | Action | Line (front→back) | Output |
|---|---|---|---|
| start | root in | `[3]` | |
| 1 | pop 3, add 9,20 | `[9, 20]` | 3 |
| 2 | pop 9 (leaf) | `[20]` | 3, 9 |
| 3 | pop 20, add 15,7 | `[15, 7]` | 3, 9, 20 |
| 4 | pop 15 (leaf) | `[7]` | 3, 9, 20, 15 |
| 5 | pop 7 (leaf) | `[]` | 3, 9, 20, 15, 7 |

Level order falls out of FIFO for free.

### 🔑 The `level_size` freeze — the one real trick

> **At the top of each `while` round, the queue contains EXACTLY one complete level and nothing else.** After processing level 0 (`3`), the line is `[9, 20]` = exactly level 1. After level 1, `[15, 7]` = exactly level 2.

So `len(q)` at the top of the round = the size of the current level. **Freeze it before the inner loop:**

```python
while q:
    level_size = len(q)          # freeze — the line right now IS one level
    for _ in range(level_size):  # pop exactly that many
        node = q.popleft()
        ...
        if node.left:  q.append(node.left)    # kids to the back for NEXT round
        if node.right: q.append(node.right)
```

**Why freeze (the part he didn't get, resolved by tracing both versions):** inside the loop you `append` the next level's kids, so **`len(q)` grows while you loop.** If you read it live via `for _ in range(len(q))`, the loop never stops at the level boundary — it bleeds into the next level and the grouping collapses back to a flat stream. Capture the count *before* appending so the fence can't move.
*(Aside: Python's `range(len(q))` actually evaluates once anyway — but write `level_size = len(q)` to state intent and to be safe in `while` conditions / other languages.)*

---

### #102 — Level Order Traversal · **SOLVED** ✅

> Values level by level, as a list of lists.

```python
from collections import deque

if root is None:
    return []

q = deque()
q.append(root)

answer = []
while q:
    level_size = len(q)
    level = []
    for i in range(level_size):
        node = q.popleft()
        level.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    answer.append(level)
return answer
```
**Code correct first try** → `[[3],[9,20],[15,7]]`. Guard, freeze, children-right, level appended after the inner loop drains.

**Complexity — he FIRST wrote "O(h) time, O(1) space" (pattern-matched from DFS), then re-derived correctly:**
- **Time O(n)** — every node popped/processed exactly once.
- **Space O(n)** — no call stack; the **queue** is the cost, and at the bottom level of a full tree it holds ~**n/2** nodes.

### 🔑 DFS vs BFS space — the guaranteed follow-up
| | Time | Space | Governed by |
|---|---|---|---|
| **DFS** (recursion) | O(n) | **O(h)** — call stack, one frame per level of DEPTH | tree's **height** |
| **BFS** (queue) | O(n) | **O(n)** — queue holds the widest level (~n/2) | tree's **width** |
> **DFS space = height. BFS space = width.** Level info costs O(n).

---

### #199 — Right Side View · **SOLVED** ✅

> The rightmost node of each level, top to bottom.

```python
from collections import deque

if root is None:
    return []

q = deque()
q.append(root)

answer = []
while q:
    level_size = len(q)
    level = []
    for i in range(level_size):
        node = q.popleft()
        level.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    answer.append(level[-1])        # last node popped in a level = rightmost
return answer
# O(n) time, O(n) space
```
**PASS** → `[1,3,4]`. One-line change from #102 (`level[-1]`). Stated complexity correctly.
*(Micro-opt, not needed: you only use `level[-1]`, so you could track just the last value or key off `if i == level_size - 1` and drop the per-level list.)*

---

### #110 — Balanced Binary Tree · **SOLVED** ✅ (box pattern transferred)

> Balanced iff for **every** node, `|left height − right height| ≤ 1`.

**The design question (same as #543):** at each node you need **two** things — your **height** (for the parent) and **is-this-balanced** (a boolean). Two facts, one return channel → **the boolean goes in a box.** *He reasoned this out himself:* *"the 'is it balanced' question is a boolean but the parent needs a number... it has to go in a box outside."*

```python
def isBalancedTree(self, root):
    self.res = True
    def dfs(node):
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        self.res = abs(left - right) <= 1 and self.res     # only-ever-falsify
        return 1 + max(left, right)
    dfs(root)
    return self.res
# O(n) time, O(h) space
```
**Correct, cold.** The update line `... <= 1 and self.res` is the **"only ever falsify"** move — once `self.res` is `False`, `X and False` stays `False`, so a later balanced node can't erase an earlier failure. **The analog of #543's `max`. He got the safety property without being told.**

**Complexity O(h)** — correctly went *back* to O(h) (DFS call stack) after the two BFS problems. **Three different space complexities stated correctly in one block: DFS O(h), BFS O(n), iterative-BST O(1).** That discrimination is the fix for yesterday's "imported the wrong template."
*(Footnote: doesn't short-circuit — visits all nodes even after finding imbalance. The `-1` sentinel version bails early; know it as the "can you optimize?" answer.)*

---

## Day 23 — takeaways

**The theme flipped from yesterday, and it's worth naming.** Yesterday he lost to imported templates. Today in Block 2 he **re-derived every complexity from scratch instead of recalling** — and got all three right, across three different traversal shapes.

**But Block 1 shows the imported-template failure mode is still live:**
- **#235 — inverted BST direction, 4th time, same problem.** → **fix: write comparisons TARGET-first** so there's nothing to flip.
- **#143 — imported #21's value-comparison merge into a problem that forbids touching values.** → **pattern recognition gives the skeleton, not the body; re-derive what decides each step.**

**Wins that matter:** both blocker problems (#271, #242) came back clean — first clean rep on **B-4** and **B-5**. BFS learned solidly. Box pattern transferred to a brand-new problem (#110).

### The reflexes (say them out loud before submitting)
1. **Box or contents?** — and *what does this variable actually hold?*
2. **Is it guarded?** — *empty? single? none-found? lengths equal? is this None?*
3. **Am I looping where I should loop?**
4. **Which side can still contain the answer?** — **write the comparison target-first** (B-6)
5. **What decides the next step IN THIS PROBLEM?** — don't paste a template; re-derive the body (M-009)

### Times
| Problem | Time |
|---|---|
| #271 | 9:19 |
| #242 | 4:05 |
| #543 | 5:01 |
| #100 | 5:45 |
| #235 | 3:26 (fail) |
| #141 | 4:46 |
| #143 | 12:41 (fail) |

### Patterns banked
- **BFS / level-order** — deque, FIFO, freeze `level_size`. → #102, #199, #103, #515, #542
- **BFS space = width (O(n)), DFS space = height (O(h))**
- **Box pattern transfers** — #110 (balanced) reuses #543's structure

---

## ⚠️ Schedule notes → Day 24

- **#98 Validate BST was NOT done today** (roadmap had it for Day 23; we did #199 + #110 instead — 3 problems, strong picks). **#98 rescheduled → Day 25**, where it clusters naturally with #230 Kth Smallest in BST (both BST, and #98 is the direct application of the *subtree-wide invariant* taught Day 22).
- **Day 24 (Jul 16) = LRU Cache (#146)** — the last unplaced core problem, plus interleave reviews. Queue rebalanced to keep Jul 16 at **6** despite the reset pile-up.
- Jul 16–18 were clustering heavily; stable 7d items fuzzed forward across Jul 18–20. No day over 8.

## Next session → **Day 24**
1. **Interleave + reviews (~6, mixed unlabeled where possible):** resets **#235, #143** first (fragile — full re-solve), then #739, #206, #21, #19.
2. **New — the big one:** **LRU Cache (#146)** — `dict` + doubly-linked list (dummy head/tail), O(1) get/put. Pre-teach the doubly-linked node and the hashmap-points-to-nodes idea in isolation first.
3. **Standing habits:** target-first comparisons (B-6) · box or contents · is it guarded · re-derive the body, don't paste (M-009) · complexity out loud, time AND space.
