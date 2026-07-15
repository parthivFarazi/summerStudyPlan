# Day 24 — Practice Notebook
**Date:** 2026-07-16 · **Week 4** · Block B — Design
**Session:** 6 reviews (interleave) + **LRU Cache (#146)** — the last unplaced core problem ✅

---

## Block 1 — Interleave + reviews (6 due, 6 of 6 ✅)

**Clean sweep — and the two that reset yesterday both came back fixed.**

### #235 — LCA of BST · reset → **PASS** · 6:25

```python
node = root
while node:
    if p.val > node.val and q.val > node.val:      # ✅ TARGET-FIRST — no mental flip
        node = node.right
    elif p.val < node.val and q.val < node.val:
        node = node.left
    else:
        return node
# O(h) time, O(1) space · 6:25
```
**PASS → 3d.** The B-6 fix held **on the exact problem that beat him twice.** He wrote it target-first (`p.val > node.val → right`), so there was nothing to invert. **B-6's first clean rep.**

### #143 — Reorder List · reset → **PASS** · 14:20
Phases 1&2 correct (find-middle, cut, reverse). **Phase 3 is now strict alternation — no value comparison** (he wrote in his own plan: *"there is no comparison needs to be done"*). Traced correct on odd (`1→2→3→4→5 → 1→5→2→4→3`) and even (`1→2→3→4 → 1→4→2→3`). **PASS → 3d.** The M-009 lesson landed — re-derived the merge body instead of pasting #21's.

### #19 — Remove Nth from End · **PASS** · 7:26
Two-pointer gap of `n`, dummy handles the remove-the-head edge. **PASS → 3d.**
*(Tighter variant noted: advance `fast` `n+1` steps and `slow` lands on the predecessor — no `prev` needed.)*

### #739 — Daily Temperatures · **PASS** · 8:44
Monotonic stack, **empty-stack guard present in both the `if` and the `while`** (the bug that reset it Day 20). B-4 behavior. **PASS → 7d.**
*(Structural note: both branches end in `stack.append(i)`, so it collapses to "pop-while-smaller, then always append.")*

### #206 — Reverse List · **PASS** · 3:19
Fluent. `return prev` present. **PASS → 7d.**

### #21 — Merge Two Sorted Lists · **PASS** · 5:15
**The interleave payoff:** `#21` and `#143` share a skeleton; here he **took from the smaller value** (`if curr1.val <= curr2.val`), 20 min after **strictly alternating** on #143 — **picked the right body for each without the pattern being named.** That is exactly the discrimination that was missing when he imported the wrong merge on Day 23. **PASS → 7d.**

| Problem | Result | Rung |
|---|---|---|
| #235 LCA BST | ✅ Pass — target-first, no inversion | reset → **3d** |
| #143 Reorder | ✅ Pass — alternation, no value compare | reset → **3d** |
| #19 Remove Nth | ✅ Pass | 1d → **3d** |
| #739 Daily Temps | ✅ Pass — stack guarded | 3d → **7d** |
| #206 Reverse | ✅ Pass | 3d → **7d** |
| #21 Merge | ✅ Pass — right body, unprompted | 3d → **7d** |

**All three open blockers (B-4, B-5, B-6) are now riding clean.** They could all drop after Day 25.

---

## Block 2 — LRU Cache (#146) ✅ — the last unplaced core problem

### 🔑 Taught in layers before any code (design problem, all-new machinery)

**What LRU is:** fixed-size cache; on overflow, evict the **Least Recently Used** item. Desk-of-books mental model — read a book → put it on top; desk full → toss the bottom one.

**The spec:** `get(key)` returns value or -1 **and marks it most-recently-used**; `put(key, value)` inserts/overwrites, marks MRU, evicts LRU if over capacity. **Both must be O(1)** — that single constraint is the whole problem.

**Why the obvious ideas fail (this motivates the design):**
- **Dict alone:** O(1) lookup, but eviction must *find* the LRU key → **O(n) scan.** ❌ (the failure is specifically on `put` when full)
- **Ordered list alone:** O(1) eviction (chop the end), but `get(key)` must *find* the key → **O(n) scan.** ❌
- **Each structure is O(1) at exactly what the other is O(n) at → use BOTH.** Dict for instant lookup, an ordering structure for instant reorder/evict, wired together.

**New machinery — the doubly-linked list.** Adds a **backward** pointer (`node.prev`) to the singly-linked node he already knew.
```python
class Node:
    def __init__(self, key, val):
        self.key = key      # ← stores the KEY too (needed at eviction)
        self.val = val
        self.prev = None    # ← NEW: backward pointer
        self.next = None
```
**Why `prev` matters:** to remove a node you're holding, you splice its neighbors together — you need to reach *both* neighbors. `node.next` gives one; **`node.prev` gives the other.** In a singly-linked list you'd have to walk from head to find the predecessor → O(n). With `prev`, removal is **O(1)**:
```python
node.prev.next = node.next     # "the previous node's next skips over me"
node.next.prev = node.prev
```
> He read the pointer surgery back correctly in plain English — the thing people fumble.

**The dummy head/tail sentinels.** Two permanent fake nodes at the ends. Real nodes always live *between* them, so **every real node is guaranteed a `prev` and a `next`** (worst case, a dummy) → `node.prev.next` can never hit `None` → **the `if node.prev is None` special-cases vanish** (which is his B-4 guard problem, designed away). Convention: **next-to-head = MRU, next-to-tail = LRU (the eviction target).**

**The join:** **the dict maps `key → the Node object`.** Lookup via the dict is O(1); once you hold the node, remove/insert_front are O(1). **This is why Node stores its `.key`:** at eviction you find the LRU node via `tail.prev`, and to also delete it from the dict you need `del self.adict[node.key]` — the node must know its own key or you're back to scanning.

### His build — strong structure, four precision bugs (his exact profile)

**The machinery was all understood.** `insert_front` (4-pointer stitch) and `remove` were structurally correct on the first try. Every bug was first-draft precision:

1. **`self.node` throughout `remove`/`insert_front`** — `node` is a **parameter**, lives on no object → bare `node`, no `self.` **(M-020, the `self.` rule from Day 21).** Self-corrected with the test: *"would it be just node then?"*
2. **`remove(node)` / `insert_front(node)` called without `self.`** — those are **methods of the class** → `self.remove(node)`. **Same rule, opposite direction (M-020).**
3. **`get` fell off the end without `return node.val`** on a hit — returned `None` instead of the value **(M-001 — the return check; B-3 recurrence, first since it cleared Day 21).**
4. **Dual-structure sync (M-024, NEW):** the cache lives in **two** structures and he updated one, forgot the other — twice:
   - overwrite branch: removed old node from the list but **didn't repoint `self.adict[key]`** at the new node → next `get` returns a dead node.
   - eviction: unlinked the LRU node from the list but **didn't `del self.adict[lru.key]`** → the dict grows unbounded.
   - plus an off-by-one: the capacity check ran *before* adding, so it never triggered → fixed to `if len(self.adict) == self.capacity:` **before** the insert.

### Final — verified correct

```python
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.adict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_front(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def get(self, key):
        if key not in self.adict:
            return -1
        else:
            node = self.adict[key]
            self.remove(node)
            self.insert_front(node)
            return node.val

    def put(self, key, value):
        if key in self.adict:
            oldNode = self.adict[key]
            self.remove(oldNode)
            newNode = Node(key, value)
            self.insert_front(newNode)
            self.adict[key] = newNode
        else:
            if len(self.adict) == self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.adict[lru.key]
            newNode = Node(key, value)
            self.adict[key] = newNode
            self.insert_front(newNode)
```
**Complexity: `get` and `put` both O(1); space O(capacity)** (bounded by the cache size — *not* O(n) in the number of operations/keys; two different "n"s in this problem, be explicit).

**Verification (run in sandbox):** spec example ✅ · overwrite-existing-key ✅ · capacity-1 ✅ · get-on-missing ✅ · **2000 randomized trials against `OrderedDict` reference — all PASS.**

---

## Day 24 — takeaways

**A milestone: the last unplaced core problem is done.** All 66-ish core patterns/problems from the roadmap are now covered before Aug 20. What remains is depth (Tries, Heap, Backtracking, Intervals, Graphs, DP) — not core gaps.

**The theme, one more time.** Block 1 was a clean 6/6 with every blocker riding clean. The LRU bugs were *all* first-draft precision on machinery he understood — `self.`, missing return, dual-structure sync. **He built the hardest data structure in the sprint correctly; he just needed the debugging passes to catch the slips.** That is his exact, consistent profile: reasoning strong, first draft imprecise.

**New this session:**
- **B-7 escalated — the `self.` rule (M-020, recurrence 3).** He *knows* the rule (asked for it Day 21, has the test written in `python-classes.md`) but doesn't run it on the first draft. Same shape as B-4. **Drill: run the test on every `X.y` and every bare call inside a class.**
- **B-3 (return) recurrence** — reopened as a watch. One slip, in the hardest problem, but the standing rule says re-escalate on any recurrence. **Pre-submit "does it return?" is mandatory again.**
- **M-024 (NEW) — dual-structure sync.** When data lives in two structures, every mutation must touch **both**. The design-problem version of "container vs. contents."

### Times
| Problem | Time |
|---|---|
| #235 | 6:25 |
| #143 | 14:20 |
| #19 | 7:26 |
| #739 | 8:44 |
| #206 | 3:19 |
| #21 | 5:15 |
| #146 | (design build, ~guided) |

### Machinery banked
- **Doubly-linked list** — backward pointer makes O(1) removal of a held node; dummy sentinels kill the `None` edge cases.
- **Hashmap + linked list combo** — dict for O(1) lookup, list for O(1) order/evict; the dict maps key → node, the node stores its key.
- **Design-problem instinct:** when two structures back one abstraction, keep them in sync on every op (M-024).

---

## Next session → **Day 25**
1. **Reviews (5 due):** #146 (1d, brand new — full re-solve), #102, #199 (1d), #226, #104 (3d). **Run the `self.` test and the return check.**
2. **New:** **Validate BST (#98)** *(deferred from Day 23 — the direct application of the subtree-wide invariant)* · **Kth Smallest in BST (#230)** (in-order traversal is sorted) · **Implement Trie (#208)** (first Trie — pre-teach the nested-dict / TrieNode structure in isolation).
3. **Habits (out loud before submit):** **the `self.` test (B-7)** · **does it return? (B-3)** · both structures in sync (M-024) · target-first comparisons (B-6) · complexity time AND space.
