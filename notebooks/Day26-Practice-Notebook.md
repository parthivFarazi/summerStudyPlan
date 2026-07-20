# Day 26 — Practice Notebook
**Date:** 2026-07-18 · **Week 5** · Block B — Tries / Heaps
**Session:** 6 reviews + 3 new (#211 Trie-wildcard, #703 + #1046 Heap — first Heaps)
*(Last session of Sprint Week 3; Jul 19 = rest. Next session Day 27, Jul 20.)*

---

## Block 1 — Reviews (6 due, 4 of 6)

**Both pointer-surgery resets from Day 25 came back FIXED. Today's two fails were a different facet — dropped required lines.**

### #146 — LRU Cache · reset → **PASS** · 16:10
Full blank-screen rebuild, **all four pointers in `addFront` this time** (M-025 fix held), `self.` clean, return present, dict synced. Verified vs OrderedDict (3000 trials). **Down from 35 min to 16.** → **3d.**
*(Complexity nit: said "O(n) space" — it's **O(capacity)**.)*

### #102 — Level Order · reset → **FAIL** · 7:38
Two API names fixed (`from collections import deque`, `.popleft()`). **But dropped BOTH None-guards he had on Day 23** — the root-`None` check and `if node.left/right` before enqueuing → `None` gets enqueued → `node.val` crashes. Needed the trace. **B-4 (edge guards) recurring** — it cleared Day 24. → **stays reset 1d.**

### #226 — Invert · reset → **PASS** · 5:54
**Swapped `node.left`/`node.right` (the fields), not locals** — M-025 fix held. First try, no hints. → **3d.** *(Still named the helper `bfs`; it's DFS — cosmetic.)*

### #98 — Validate BST · 1d → **PASS** · 4:16
Bounds correct (left tightens high, right raises low), first try. → **3d.**

### #230 — Kth Smallest · 1d → **PASS** · 4:34
Wrote the **optimized early-stop version** (flag every frame checks) unprompted — better than yesterday's list version. Verified vs 2000 random BSTs. → **3d.**
> **⚠️ Coach error, logged for honesty:** my stated example said `k=3 → 5`; the correct answer is **4** (in-order 1,3,4 → 3rd is 4). His code was right; my annotation was wrong (also wrong in the Day-25 note). Owned it.

### #208 — Implement Trie · 1d → **FAIL** · 7:13
**Forgot `node.isEnd = True` at the end of `insert`** → every search returns False. Needed the hint. → **stays reset 1d.**
*(Complexity: it's per-op **O(L)**, not "O(n)"; insert O(L) space, search/startsWith O(1).)*

| Problem | Result | Rung |
|---|---|---|
| #146 LRU | ✅ Pass — 4 pointers, verified | reset → **3d** |
| #102 Level Order | ❌ Fail — dropped both None-guards (B-4) | reset → 1d |
| #226 Invert | ✅ Pass — mutated fields | reset → **3d** |
| #98 Validate BST | ✅ Pass | 1d → **3d** |
| #230 Kth Smallest | ✅ Pass — optimized, unprompted | 1d → **3d** |
| #208 Trie | ❌ Fail — forgot `isEnd = True` | reset → 1d |

> **The theme moved.** The pointer-surgery slips (M-025) that reset #146/#226 yesterday are **fixed** — both passed. **Today's two fails are a new facet of the same precision disease: dropping a required line** — None-guards (#102) and the `isEnd` end-marker (#208). Same fix: **walk the operation to its end before submitting — "guard written? end marked? does every branch return?"**

---

## Block 2 — New material (3 problems, all solved w/ guidance)

### #211 — Add and Search Words — Trie + `.` wildcard (DFS)

**The conceptual leap (his, unprompted):** a `.` can't pick one edge, so **try ALL children and succeed if any subtree matches** — that's DFS/backtracking, which is why a plain one-pointer walk no longer works.

```python
def search(self, word):
    def dfs(index, node):
        if index == len(word):
            return node.isEnd
        if word[index] != ".":
            if word[index] not in node.children:
                return False
            return dfs(index+1, node.children[word[index]])
        else:
            for child in node.children.values():
                if dfs(index+1, child):
                    return True
            return False
    return dfs(0, self.root)
```
**Recursion visualized (per his request):** built two step-through animations — one syncing the trie + word-pointer + executing code line, and one showing the **call stack push/pop/backtrack** on `search(".at")` over `{bad, cat}` (first child `b` fails → both frames pop → root's loop tries `c` → succeeds). This is what finally made wildcard backtracking click. **He asked me to always go slow on recursion-heavy topics → logged as COACHING rule #9.**

**Execution had FIVE bugs (his profile):** `addWord` missing `isEnd` (again, same as #208), base-case off-by-one (`len-1`), missing `return` in the normal branch, wildcard returning on the first child, wildcard not returning `answer`. The DFS *idea* was right every time; the **first draft leaked required lines** (returns, isEnd). Verified vs brute force (3000 queries).
**Complexity:** addWord O(L); search O(L) no-wildcard, worst O(N nodes) all-dots; space O(L) recursion depth.

### 🔑 Heaps — pre-taught in isolation (first Heap; NOT recursion — a breather)

A heap keeps the **min instantly accessible** while staying cheap to insert/remove: **peek O(1), push O(log n), pop O(log n)**. Python's `heapq` operates on a plain list:
```python
heapq.heappush(h, x)     # TWO args: heap, then item
heapq.heappop(h)         # ONE arg; removes & returns the MIN
h[0]                     # peek min, O(1) (rest of list NOT sorted)
heapq.heapify(lst)       # plain list → heap in place, O(n)
```
**`heapq` is a MIN-heap.** For a **max-heap, negate** on push and negate back on pop.

### #703 — Kth Largest in a Stream — min-heap of size k

**The design (taught slowly, he was stuck at first):** keep a **min-heap holding only the k largest** numbers. Then `h[0]` — the smallest of the top-k — **IS the k-th largest.** On `add`: push, and if size > k, pop the min (which is both the answer boundary and the thing to evict). **Min-heap because you need the *cutoff* between top-k and the rest at your fingertips**, not the max.

```python
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.h = []
        for num in nums:
            heapq.heappush(self.h, num)     # (or self.h=nums; heapq.heapify(self.h) — O(n))
        while len(self.h) > k:
            heapq.heappop(self.h)
    def add(self, val):
        if len(self.h) == self.k:
            if val > self.h[0]:
                heapq.heappop(self.h); heapq.heappush(self.h, val)
            return self.h[0]
        else:
            heapq.heappush(self.h, val)
            return self.h[0]
```
`add` = **O(log k)** time, O(k) space. Verified vs brute force (1000 trials, incl. empty start).
**Bugs:** `heapq.heappush(num)` missing the heap; `heapq.heappop(self.h, num)` with an extra arg — pure `heapq` API-arg confusion.

### #1046 — Last Stone Weight — max-heap via negation

```python
def lastStoneWeight(self, stones):
    h = []
    for num in stones:
        heapq.heappush(h, -num)
    while len(h) > 1:
        stone1 = -heapq.heappop(h)      # largest
        stone2 = -heapq.heappop(h)      # 2nd largest
        difference = abs(stone1 - stone2)
        if difference > 0:
            heapq.heappush(h, -difference)
    return -h[0] if len(h) == 1 else 0
```
**O(n log n)** time, O(n) space. Clean sign-handling; only bug was `heapq.heappush(-num)` missing the heap again (3rd time today). Verified vs brute force (3000 trials).

---

## Day 26 — takeaways

**Block 2 continues strong: 3 solved, first Heaps banked, and the wildcard-DFS is the deepest recursion he's handled — the animations were the unlock.** Block 1: 4/6, both Day-25 pointer resets recovered.

**The precision tax moved facet again:**
- ✅ **M-025 pointer surgery FIXED** — #146 (4 pointers), #226 (mutate the field).
- ✅ **B-7 `self.` clean** on the #146 rebuild → clears (2 consecutive clean sessions).
- ❌ **New facet: dropping a required line** — None-guards (#102, B-4 recurred), `isEnd` end-marker (#208, #211), and `return`s (#211). Plus `heapq` arg-count friction (×3, new-API).

**Same root, new clothes: first-draft completeness.** The one scan that fixes all of it: **before submitting, walk the operation top to bottom — guard present? end marked? every branch returns? all args passed?**

### Banked
- **Trie + wildcard DFS** (#211) — a `.` branches into all children; recursion backtracks.
- **Heaps** (new pattern) — `heapq` min-heap, negation for max-heap; **min-heap-of-size-k** for "k-th largest" (#703); max-heap for "repeatedly take the largest" (#1046).
- **Recursion is his slowest area → always visualize the stack (COACHING #9).**

### New standing instruction
**COACHING rule #9 — go slow on recursion-heavy concepts; visualize the call stack.** *(given today.)*

---

## Next session → **Day 27 (Jul 20)** — *(Jul 19 is a rest day)*
1. **Reviews (6 due):** resets **#102, #208** first (**#102: root-None + child-None guards; #208: `node.isEnd = True`**), then new **#211, #703, #1046** (1d), and **#235** (B-6 canary — target-first, the pending 2nd clean test).
2. **New (roadmap Day 27):** **Heap** — K Closest Points to Origin (#973), Kth Largest in Array (#215, quickselect option).
3. **Habits (out loud before submit):** **walk the op to the end — guard? end-marker? does it return? all args?** · `heappush(h, x)` takes the heap first · complexity time AND space.
