# Day 27 — 2026-07-21 — Heap depth (#973 K Closest, #215 Kth Largest) + 7 reviews

> **Sprint Week 4 → Day 27** (folder `Week 5/Day 27/`, since `Week = ⌈27/6⌉ = 5`).
> Scheduled for Jul 20 but that day was skipped (Jul 19 was the rest day); this session ran Jul 21. Pace note below.
> **Headline: both twice-reset problems recovered CLEAN, and #235 cleared B-6 — the last drill-now blocker. Every blocker ever escalated (B-1…B-7) is now clear.**

---

## Block 1 — Reviews (7 due-fragile worked · 4 PASS / 3 reset)

Ordered resets → 1d → 3d canary. Full re-solves from a blank screen. The 6 stable 3d items also due today (#146, #226, #98, #230, #199, #271) were **rolled forward** (overflow — 13 due vs an ~8 cap; see QUEUE).

### 1. #102 Level Order Traversal — ✅ PASS (5:48) — reset ×2 cleared → 3d
Twice-reset, both times on **dropped None-guards** (B-4). This time both were present on the first draft.

His code (verbatim):
```python
from collections import deque
if root is None:
    return []
q = deque()
q.append(root)
answer = []
while q:
    level_len = len(q)
    level = []
    for i in range(level_len):
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        level.append(node.val)
    answer.append(level)
return answer
```
**Coaching:** root-None guard ✓, child guards ✓, `level_len` frozen before the inner loop (the BFS trap) ✓, `popleft` for O(1) ✓, every branch returns. Space reasoning correct and unprompted: peak memory = the widest level (~n/2 in a perfect tree) → **O(n)**. Footnote: `if node.left:` is safe because a TreeNode is always truthy; don't carry that to `if node.val:` where a real `0` would betray you. **O(n)/O(n).**

### 2. #208 Implement Trie — ✅ PASS (7:50) — reset ×2 cleared → 3d
Twice-reset on the **dropped `isEnd` terminal line** (M-026). Present on first draft this time.
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True          # ← the line that reset it twice, present unprompted
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        return node.isEnd          # returns the flag, not a bare True → distinguishes word from prefix
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        return True
```
**Coaching:** clean. `search` returns `node.isEnd` (exact word vs prefix), `startsWith` returns True. **M-026 first clean rep.** insert/search/startsWith O(L); space O(L) insert, O(1) others.

### 3. #211 Add & Search Word (wildcard DFS) — ❌ RESET → 1d
Algorithm came out **cold and correct** (huge step up from 5 bugs on Day 26). Failed on **two ownership NameErrors**, both the "whose thing is it?" family:
- `return isEnd` → should be `return node.isEnd`
- `return dfs(0, root)` → should be `return dfs(0, self.root)`

Needed a categorial nudge ("two crashes, same family — an attribute without its owner"). Then fixed both instantly. Final:
```python
def search(self, word):
    def dfs(index, node):
        if index == len(word):
            return node.isEnd
        if word[index] != '.':
            if word[index] not in node.children:
                return False
            else:
                return dfs(index + 1, node.children[word[index]])
        else:
            answer = False
            for child in node.children.values():
                answer = answer or dfs(index + 1, child)   # `or` short-circuits; return False only after the loop
            return answer
    return dfs(0, self.root)
```
**Why reset:** first draft didn't run + needed a hint. **This reopens the B-7 watch** (the `self.` / ownership rule that cleared Day 26). Add *"whose thing is every attribute?"* to the out-loud scan. Complexity: addWord O(L); search worst **O(N)** (all-dots input walks the trie), space **O(L)** = call-stack depth (space reflex landed).

### 4. #703 Kth Largest in a Stream — ✅ PASS (8:44) → 3d
```python
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.h = []
        for num in nums:
            heapq.heappush(self.h, num)
        while len(self.h) > self.k:
            heapq.heappop(self.h)
    def add(self, val):
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            if val > self.h[0]:
                heapq.heappop(self.h)
                heapq.heappush(self.h, val)
        return self.h[0]
```
**Coaching:** clean. Every reference **owned** (`self.k`, `self.h`) — the exact thing #211 dropped — and `heappush(self.h, val)` has both args (Day-26 arg friction gone). **Complexity precision drilled:** the heap is pinned at size k forever → `add` is **O(log k)**, not O(log n). O(k) space. *(The `self.` consistency here, one problem after the `self.root` miss, shows the slip is first-draft **variance**, not a gap — which is why the out-loud scan catches it.)*

### 5. #1046 Last Stone Weight — ❌ RESET → 1d (three nudges)
Stated "negate" out loud, then **wrote a plain min-heap** — plan/code disconnect (M-009 family). Three corrections:
1. No negation at all (`heappush(h, num)`) → pops the two *lightest*, not heaviest.
2. Typo `heapq.heapop` (crash) → `heappop`.
3. `return h[0]` returned the *negated* survivor → `return -h[0]`.

Final:
```python
import heapq
h = []
for num in stones:
    heapq.heappush(h, -num)
while len(h) > 1:
    heavy = -heapq.heappop(h)
    light = -heapq.heappop(h)
    diff = abs(heavy - light)
    if diff > 0:
        heapq.heappush(h, -diff)
return -h[0] if len(h) == 1 else 0
```
**The lesson (new, M-027):** *negation is a **touch-every-boundary** transform* — it must hit the value on the way **in** (push), on the way **out** (pop), and on the **final read** (return). He got 0 of 3, then 2, then 3. **O(n log n)/O(n).**

### 6. #235 Lowest Common Ancestor of a BST — ✅ PASS (2:27) → 7d — **B-6 CLEARS**
The B-6 canary. Stated the rule **target-first** first (no mental flip), then coded exactly that:
```python
node = root
while node:
    if q.val > node.val and p.val > node.val:
        node = node.right
    elif q.val < node.val and p.val < node.val:
        node = node.left
    else:
        return node
```
**Coaching:** target-first, no inversion; `while node:` loop present (no fall-off like Day 22); split returns the node. **Day 24 was clean rep 1; this is rep 2 → B-6 (inverted search direction) CLEARED.** It beat him 4× and reset #235 two days running; the mechanical fix (comparison target-first) held cold. **O(h) time (worst O(n), balanced O(log n)) / O(1) space** (iterative — no call stack).

### 7. #110 Balanced Binary Tree — ❌ RESET → 1d
The **code was clean and correct** — but he first stated the box channel **backwards** ("the return is always a boolean") and needed a Socratic walk to "return carries the **height**, the box holds the boolean." Recovered instantly, then coded flawlessly:
```python
def isBalancedTree(self, root):
    if root is None:
        return True
    self.res = True
    def dfs(node):
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left - right) > 1:
            self.res = False
        return 1 + max(left, right)
    dfs(root)
    return self.res
```
**Why reset:** a recall miss on the box pattern (return-channel vs box), and the box pattern is **recursion-heavy — his slowest area (rule 9)** — so it earns another near-term rep. Comprehension is fine; it's a recall wobble (M-028). **O(n)/O(h).**

---

## Block 2 — New: Heap depth (both solved with guidance)

### #973 K Closest Points to Origin — solved → enters QUEUE at 1d
Pre-taught **heapq with tuple keys** in isolation (heap orders by first element, then second as tiebreaker → push `(distance, index)`).

Design work was his: proposed a **min-heap of all**, I asked him to trace "pop down to k on a min-heap keeps the *farthest* k" → he flipped to a **max-heap of size k via negation**. `h[0]` = the farthest kept = the boundary.

Three first-draft bugs (all found via categorial nudges):
1. **`dist = x^2 + y^2`** — `^` is **XOR** in Python, not power. `3^2 == 1`. Use `x*x + y*y` or `x**2`. *(Silent — computes garbage, doesn't crash.)*
2. `if -dist > maxHeap[0]:` — `maxHeap[0]` is a **tuple**; compared int to tuple → TypeError. Fixed by unpacking `kthNegDis, index = maxHeap[0]`.
3. **Missing `heappop`** in the else branch → heap grew past k (breaks both correctness and the O(log k) claim).

Final:
```python
import heapq
maxHeap = []
for i in range(len(points)):
    x, y = points[i][0], points[i][1]
    dist = (x * x) + (y * y)
    if len(maxHeap) < k:
        heapq.heappush(maxHeap, (-dist, i))
    else:
        kthNegDis, index = maxHeap[0]
        if -dist > kthNegDis:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-dist, i))
answer = []
for negDist, index in maxHeap:
    answer.append(points[index])
return answer
```
**O(n log k) / O(k).** Bright spot: the **negated comparison stayed pointed the right way** — B-6 skill transferring off #235.

### #215 Kth Largest Element in an Array — solved → enters QUEUE at 1d
Recognized it's the **#703 engine**: min-heap of size k, `h[0]` = kth largest. (Briefly said "max heap, negate," self-corrected to min-heap.) Two bugs:
1. `if maxHeap < k:` — compared the **list** to an int (TypeError). Needs `len(maxHeap)`.
2. Renamed `maxHeap → minHeap` but **missed one occurrence** (`heappush(maxHeap, ...)` straggler → NameError).

Final:
```python
import heapq
minHeap = []
for num in nums:
    if len(minHeap) < k:
        heapq.heappush(minHeap, num)
    else:
        if num > minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, num)
return minHeap[0]
```
**O(n log k) / O(k).** *Quickselect (O(n) average, partition-recursion) deliberately deferred to next session — recursion-heavy, not to be rushed (rule 9).*

---

## The theme of the day — the disease moved to the "edit" level

Every reset and every Block-2 bug was **one meta-mistake (M-027): a transform/edit that must touch multiple sites, and the first draft missed a site.**
- **Negation** (#1046) — 3 boundaries (in/out/return), got 0 then 2 then 3.
- **Rename** (#215) — one straggler left un-renamed.
- **Ownership** (#211) — an attribute written without its owner, ×2 (`self.root`, `node.isEnd`).
- **Paired op** (#973) — evict+add, wrote the add, dropped the evict.

The algorithm was right in his head every time. **New highest-leverage habit: when you apply a change, enumerate every site it must land, and confirm each one.** This sits next to the existing "walk the op to the end" scan.

## Wins
- **#102 and #208** — both twice-reset — back **clean, dropped line present on first draft.** The whole thesis (name the check → it clears) working.
- **B-6 CLEARED** (#235 target-first, rep 2). The last drill-now blocker. **All of B-1…B-7 now clear.**
- **B-6 skill transferred** to #973's negated comparison — real, not memorized.
- **#703** — every reference owned, heapq args correct.

## Blockers / watches after today
- **B-6 (search direction) — CLEARED** ✅ (moves to resolved/dormant).
- **B-7 (`self.` / ownership) — WATCH REOPENED** (#211 `self.root` + `node.isEnd`). M-020 recurrence 4.
- **M-027 (multi-site change incomplete) — NEW**, fired 3× today (#1046, #215, #973). One rep from a blocker.
- **M-028 (box-pattern channel recall) — NEW** (#110). Recursion-heavy (rule 9).
- **M-009 (plan/code disconnect)** — #1046 "said negate, wrote min-heap" is kin; watchlist.
- Still on watch: B-4 (guards), B-3 (returns), M-026 (terminal line) — none fired today.

## Complexity scorecard (stated first, every problem)
All correct or self-corrected: #102 O(n)/O(n) · #208 O(L) · #211 O(N)/O(L) · #703 **O(log k)** (drilled off O(log n)) · #1046 O(n log n)/O(n) · #235 O(h)/O(1) · #110 O(n)/O(h) · #973 O(n log k)/O(k) · #215 O(n log k)/O(k). **Space reflex strong** — call-stack depth on #211, size-k on the heaps.

## Times (stopwatch)
#102 5:48 · #208 7:50 · #211 ~6:41 (+ fix) · #703 8:44 · #1046 ~3:18 (+ 3 fixes) · #235 2:27 · #110 6:44.

## Pace
Jul 20 (Day 27) was skipped; ran Jul 21. **30 days to the Aug 20 pivot; all core done — only depth patterns remain**, so one missed day is absorbable. The one real cost: the review queue stacked up (6 items rolled from Jul 20 onto Jul 21's 7) — rebalanced in QUEUE, and the 3d wave will crest near the cap through ~Jul 25. Next new: **Backtracking** starts Day 28.

## Spaced-review changes (see QUEUE for the full fuzzed schedule)
- **Advanced:** #102 → 3d (Jul 24) · #208 → 3d (Jul 24) · #703 → 3d (Jul 24) · #235 → 7d (Jul 28).
- **Reset to 1d (Jul 22):** #211, #1046, #110.
- **New at 1d (Jul 22):** #973, #215.
- **Rolled forward (unworked overflow):** #146, #226 → Jul 23 · #98, #230 → Jul 24 · #271, #199 → Jul 22.
