# Day 25 — Practice Notebook
**Date:** 2026-07-17 · **Week 5** · Block B — BST / Tries
**Session:** 5 reviews + 3 new (#98 Validate BST, #230 Kth Smallest, #208 Trie — first Trie)

---

## Block 1 — Reviews (5 due, 2 of 5)

**Rough block — 3 resets — but all surface (API names + pointer slips), not comprehension. The three drilled behaviors (`self.`, return, dict-sync) all held clean.**

### #146 — LRU Cache · 1d (brand new) → **RESET** · 35:16

Full blank-screen rebuild of the hardest problem. **The three flagged behaviors held on the first draft:**
- **`self.` — perfect** throughout (`self.remove`, `self.addFront`, `self.adict`; no spurious `self.` on params) → **B-7's first clean rep.**
- **`return node.val` — present** → B-3 held.
- **Dict sync — correct in BOTH overwrite and eviction paths** → M-024 (yesterday's miss) stuck.

**Three bugs, needed hints → reset:**
1. **`addFront` did only 2 of its 4 pointer reassignments** (set `node.next` + `head.next`, missed both backward pointers). The real logic bug.
2. `self.head = Node()` — `Node.__init__` needs `(key, value)` → `Node(0, 0)`.
3. `del self.adict(oldNode.key)` — parens instead of brackets → `del self.adict[oldNode.key]`.

**The fix for bug 1 (a keeper):** *when you write a pointer-surgery helper, count the pointers.* Inserting one node between two others touches **4** pointers (2 forward, 2 backward); `remove` touches **2**. If the helper has fewer lines than that, it's incomplete. **Verified correct after fixes** (spec + overwrite + cap-1 + 3000 randomized trials vs OrderedDict).

### #102 — Level Order · 1d → **RESET** · 10:52
Algorithm **perfect** (guard, freeze `len(q)`, drain level, push children, append). Two API-recall crashes:
- `from * import deque` → **`from collections import deque`**
- `q.popfront()` → **`q.popleft()`**

Reset (wouldn't run). Pure memorization now — the algorithm is owned.

### #199 — Right Side View · 1d → **PASS** · 4:24
Correct (`level[-1]`), both API names right this time. **And reconstructed the optimized variant from a glimpse** — track a single `level` value overwritten each iteration (the last write = rightmost), dropping the per-level list. Real retention. **PASS → 3d.**

### #226 — Invert · 3d → **RESET** · 5:52
**Bug: swapped two LOCAL variables (`left`, `right`) instead of `node.left`/`node.right`.** The locals held the recursion's return values; shuffling them does nothing to the tree. Needed the trace → reset.
**Named it:** this is the **container-vs-contents** family (B-5, just cleared) in a new costume — *"am I changing the object's field, or just a local?"* Fixed by assigning to `node.left`/`node.right`. (Also: named the helper `bfs` when it's DFS; and the `left =`/`right =` lines became dead assignments.) **RESET → 1d.**

### #104 — Max Depth · 3d → **PASS** · 2:34
Clean, `self.` correct, return present. **PASS → 7d.**

| Problem | Result | Rung |
|---|---|---|
| #146 LRU | ❌ Reset — incomplete `addFront` + 2 syntax | reset → 1d |
| #102 Level Order | ❌ Reset — `deque` import + `.popleft()` | reset → 1d |
| #199 Right Side View | ✅ Pass — + optimized variant | 1d → **3d** |
| #226 Invert | ❌ Reset — swapped locals, not `node.left/right` | reset → 1d |
| #104 Max Depth | ✅ Pass | 3d → **7d** |

> **The one real signal:** #226 (swapped locals) and #146 (incomplete `addFront`) are the **same shape** — pointer/field assignments that don't do what you think. The reflex: *"am I mutating the object's field, or just a local copy?"* · *"count the pointers."*

---

## Block 2 — New material (3 problems, all ✅)

### #98 — Validate BST ✅ — passing constraints DOWN

The payoff of the Day-22 insight (invariant is **subtree-wide, not parent-child**). Parent-only checking is the #1 wrong answer.

**The mechanism (taught): recurse with a `(low, high)` range.** Each node must satisfy `low < node.val < high`. Going **left** tightens `high` to `node.val`; going **right** raises `low` to `node.val`. The bound **propagates down** — so `4` under `8` under `5` still carries the lower bound `5` and gets caught.

```python
def isValidBST(self, root):
    def valid(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return valid(root, float('-inf'), float('inf'))
# O(n) time, O(h) space
```
He filled in all six bounds correctly once the range idea landed.

> 🔑 **New tool: passing state DOWN through parameters.** #104/#543 pass answers **up** (via return); #98 passes context **down** (via arguments). Both are DFS. This reappears in backtracking. *(He asked "are we using DFS here?" — yes; the traversal is unchanged, the new thing is the direction of information flow.)*

### #230 — Kth Smallest in BST ✅ — in-order = sorted

> 🔑 **In-order traversal (`left → node → right`) of a BST visits nodes in SORTED order.** So k-th smallest = k-th node visited in-order.

**Big call-stack teaching moment** — he got stuck on *"5 is already queued right, how does 4 come before 5?"* Resolved by tracing the stack frame-by-frame: **5 is NOT queued — its frame is PAUSED at step 1 (`inorder(node.left)`) and cannot visit itself until its entire left subtree drains.** `4` lives inside `3`'s subtree, so it's visited during 5's not-yet-finished left recursion. **The node visits itself BETWEEN its left and right calls** — that's why the left subtree always comes first.

**His solution (list version, correct):**
```python
def kthSmallest(self, root, k):
    self.res = []
    def inorder(node):
        if node is None:
            return None
        inorder(node.left)
        self.res.append(node.val)
        inorder(node.right)
    inorder(root)
    return self.res[k-1]
# O(n) time, O(n) space
```
**Space correction:** he first said O(h); the list holds all n values → **O(n)** (M-005 reflex — a structure that scales with input dominates the call stack). Self-corrected.

**The optimization (taught, for the interview follow-up):** track `self.count`/`self.answer`, increment at each visit, record when `count == k`. Best case **O(h + k) time, O(h) space**. Key mechanic he didn't know: **"stopping" a recursion isn't one `return` — it's setting a flag every frame checks** so they all bail as the stack unwinds (reappears in backtracking).

### #208 — Implement Trie ✅ — FIRST TRIE (new data structure, clean first try)

Pre-taught the structure in isolation (per the new-data-structure rule). Key ideas that landed via his own questions:
- **The character is NOT stored in the node — it's the KEY in the parent's `children` dict.** (His question: *"don't I need a `self.val`?"* → no; the edge label is the dict key, like `d['p']="hi"` doesn't store `'p'` in `"hi"`.)
- **`is_end` vs `children` are independent** — a node can both end a word AND have longer children (`app` inside `apple`).
- **`search` vs `startsWith` are the same walk** — only the last line differs (`return node.is_end` vs `return True`).
- His own synthesis: *"a Trie is nodes attached to dictionaries, like LRU but each node has its OWN children dict, and nodes only reach their own children"* — exactly right; that's why every op starts at `self.root`.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        return True
```
**Complexity:** insert/search/startsWith all **O(L) time**; **insert O(L) space** (may create L nodes), search/startsWith **O(1) space** (walk only). The "≤26 keys" fact is the *branching factor* (keeps each step O(1)), not the op's space.
**Verified:** LeetCode example + 1000 randomized trials vs a reference set — all PASS. Clean first try, no bugs.

---

## Day 25 — takeaways

**Block 2 was strong: three new problems, all correct, one a brand-new data structure built clean.** He's now derived or absorbed: passing state *down* (#98), in-order = sorted + the call-stack "why" (#230), and the nested-dict Trie (#208).

**Block 1 (3 resets) was surface, not comprehension:**
- #102 — two API names (`from collections import deque`, `.popleft()`).
- #146 — rebuilt end-to-end; bugs were incomplete pointer surgery + 2 syntax; **all three drilled behaviors clean.**
- #226 — the one real slip: swapping locals instead of the node's fields.

**The precision drill is working on the flagged items** (`self.`, return, dict-sync all held). **The live signal:** pointer/field assignment slips — #226 (locals vs `node.left/right`) and #146 (incomplete `addFront`). Same reflex fixes both: ***"am I mutating the object's field or a local? · count the pointers."***

### Times
| Problem | Time |
|---|---|
| #146 | 35:16 (reset) |
| #102 | 10:52 (reset) |
| #199 | 4:24 |
| #226 | 5:52 (reset) |
| #104 | 2:34 |

### Banked
- **BST: passing bounds down** (#98) · **in-order = sorted** (#230) · **flag-to-stop-a-recursion** (early exit)
- **Trie** — new data structure: nested dicts of nodes, char = the key, `is_end` flag; insert/search/startsWith
- **Pointer-surgery discipline:** count the pointers; mutate the field, not a local

---

## Next session → **Day 26**
1. **Reviews (queue-driven):** the 3 resets come back — **#146, #102, #226** (1d) — plus #199, #543/#271/etc. per QUEUE. **#146: count the pointers in `addFront`. #226: mutate `node.left/right`, not locals. #102: `from collections import deque`, `.popleft()`.**
2. **New (roadmap Day 26):** **Design Add & Search Words (#211)** — Trie + `.` wildcard (DFS over children); **Heap** — Kth Largest in a Stream (#703), Last Stone Weight (#1046). Pre-teach `heapq` (min-heap, and max-heap via negation) in isolation.
3. **Habits (out loud before submit):** count the pointers / mutate the field not a local · the `self.` test · does it return? · both structures in sync · complexity time AND space.
