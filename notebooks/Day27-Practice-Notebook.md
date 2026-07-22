# Day 27 — 2026-07-21 — Heap depth (#973 K Closest, #215 Kth Largest) + 7 reviews

> **Sprint Week 4 → Day 27** (folder `Week 5/Day 27/`, since `Week = ⌈27/6⌉ = 5`).
> Scheduled for Jul 20 but that day was skipped (Jul 19 was the rest day); this session ran Jul 21.
> **Headline: both twice-reset problems recovered CLEAN, and #235 cleared B-6 — the last drill-now blocker. Every blocker ever escalated (B-1…B-7) is now clear.**

---

## Block 1 — Reviews (7 due-fragile worked · 4 PASS / 3 reset)

Ordered resets → 1d → 3d canary. Full re-solves from a blank screen. The 6 stable 3d items also due today (#146, #226, #98, #230, #199, #271) were **rolled forward** (overflow — 13 due vs an ~8 cap).

### 1. #102 Level Order Traversal — ✅ PASS (5:48) — reset ×2 cleared → 3d
Twice-reset on **dropped None-guards** (B-4). Both present on the first draft this time.
```python
from collections import deque
if root is None:
    return []
q = deque(); q.append(root)
answer = []
while q:
    level_len = len(q); level = []
    for i in range(level_len):
        node = q.popleft()
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
        level.append(node.val)
    answer.append(level)
return answer
```
Root guard ✓, child guards ✓, `level_len` frozen (the BFS trap) ✓, `popleft` O(1) ✓. Space reasoning unprompted: peak = widest level ~n/2 → **O(n)**. Footnote: `if node.left:` is safe (a TreeNode is always truthy); don't carry that to `if node.val:` where a real `0` betrays you. **O(n)/O(n).**

### 2. #208 Implement Trie — ✅ PASS (7:50) — reset ×2 cleared → 3d
Twice-reset on the dropped `isEnd` line (M-026) — present on first draft this time. `search` returns `node.isEnd` (exact word vs prefix), not a bare `True`. **M-026 first clean rep.** insert/search/startsWith O(L).

### 3. #211 Add & Search Word (wildcard DFS) — ❌ RESET → 1d
Algorithm **cold-correct** (up from 5 bugs Day 26). Failed on **two ownership NameErrors**: `return isEnd` → `node.isEnd`, and `dfs(0, root)` → `dfs(0, self.root)`. Needed a categorial nudge, then fixed instantly.
```python
def search(self, word):
    def dfs(index, node):
        if index == len(word): return node.isEnd
        if word[index] != '.':
            if word[index] not in node.children: return False
            return dfs(index + 1, node.children[word[index]])
        answer = False
        for child in node.children.values():
            answer = answer or dfs(index + 1, child)   # `or` short-circuits
        return answer
    return dfs(0, self.root)
```
**Reset:** first draft didn't run + needed a hint → **reopens B-7 (self./ownership).** Add *"whose thing is every attribute?"* to the scan. search worst O(N) (all-dots), space **O(L)** = call-stack depth.

### 4. #703 Kth Largest in a Stream — ✅ PASS (8:44) → 3d
Every reference **owned** (`self.k`, `self.h`) — the thing #211 dropped — and heapq args correct. **Complexity drilled: `add` is O(log k)** (heap pinned at size k), not O(log n). O(k) space. *(self. consistency here, one problem after the `self.root` miss, shows the slip is first-draft variance, not a gap.)*

### 5. #1046 Last Stone Weight — ❌ RESET → 1d (three nudges)
Said "negate" then **wrote a plain min-heap** (plan/code disconnect). 3 corrections: no negation → `heapop` typo → `return h[0]` not `-h[0]`.
```python
h = []
for num in stones: heapq.heappush(h, -num)
while len(h) > 1:
    heavy = -heapq.heappop(h); light = -heapq.heappop(h)
    if heavy - light > 0: heapq.heappush(h, -(heavy - light))
return -h[0] if len(h) == 1 else 0
```
**Lesson (M-027):** negation is a **touch-every-boundary transform** — in (push), out (pop), final read (return). Got 0 of 3, then 2, then 3. **O(n log n)/O(n).**

### 6. #235 Lowest Common Ancestor of a BST — ✅ PASS (2:27) → 7d — **B-6 CLEARS**
```python
node = root
while node:
    if q.val > node.val and p.val > node.val:   node = node.right
    elif q.val < node.val and p.val < node.val: node = node.left
    else: return node
```
Target-first, no inversion, `while` loop present, split returns the node. **Day 24 clean rep 1; this is rep 2 → B-6 CLEARED.** Beat him 4×, reset #235 two days running; the mechanical fix held cold. **O(h) / O(1)** (iterative).

### 7. #110 Balanced Binary Tree — ❌ RESET → 1d
**Code clean and correct** — but stated the box channel **backwards** ("return is always a boolean"); needed a Socratic walk to "return carries the height, box holds the boolean." Recovered instantly.
```python
if root is None: return True
self.res = True
def dfs(node):
    if node is None: return 0
    left = dfs(node.left); right = dfs(node.right)
    if abs(left - right) > 1: self.res = False
    return 1 + max(left, right)
dfs(root); return self.res
```
**Reset:** recall miss on the box pattern (recursion-heavy — his slowest area, rule 9; M-028). Comprehension fine; recall wobble. **O(n)/O(h).**

---

## Block 2 — New: Heap depth (both solved with guidance)

### #973 K Closest Points to Origin — → QUEUE 1d
Pre-taught **heapq tuple keys**. Design was his: proposed min-heap-of-all, traced that popping to size k keeps the *farthest* k → flipped to **max-heap-of-size-k via negation**. Bugs: **`^` is XOR not power** (`3^2==1`, silent), int-vs-tuple compare (`maxHeap[0]` → unpack), **missing `heappop`** (heap grew past k).
```python
maxHeap = []
for i in range(len(points)):
    x, y = points[i][0], points[i][1]
    dist = (x * x) + (y * y)
    if len(maxHeap) < k:
        heapq.heappush(maxHeap, (-dist, i))
    else:
        kthNegDis, index = maxHeap[0]
        if -dist > kthNegDis:
            heapq.heappop(maxHeap); heapq.heappush(maxHeap, (-dist, i))
return [points[i] for (nd, i) in maxHeap]
```
**O(n log k)/O(k).** Bright spot: negated comparison stayed pointed right — **B-6 skill transferred.**

### #215 Kth Largest Element in an Array — → QUEUE 1d
Recognized the **#703 engine** (min-heap size k). Bugs: `maxHeap < k` (missing `len()`), rename straggler (`maxHeap→minHeap` missed one). **O(n log k)/O(k).** *(Quickselect deferred — recursion-heavy.)*

---

## The theme — the disease moved to the EDIT level (M-027)
Every reset + Block-2 bug = **a multi-site change where the first draft missed a site**: negation (#1046, 3 spots), rename (#215), ownership (#211, 2 spots), evict+add (#973). Algorithm right in his head every time. **Habit: enumerate every site a change must land, confirm each.**

## Wins
- #102 & #208 (both twice-reset) back **clean, dropped line present on first draft.**
- **B-6 CLEARED** (#235 rep 2). All of B-1…B-7 now clear.
- B-6 skill **transferred** to #973's negated compare.

## Blockers after today
- **B-6 CLEARED** ✅. **B-7 WATCH REOPENED** (#211). **M-027 NEW** (×3). **M-028 NEW** (#110).

## Times
#102 5:48 · #208 7:50 · #211 ~6:41 · #703 8:44 · #1046 ~3:18 · #235 2:27 · #110 6:44.

## Spaced-review changes
Advanced: #102/#208/#703 → 3d · #235 → 7d. Reset 1d: #211/#1046/#110. New 1d: #973/#215. Rolled forward: #146/#226/#98/#230/#199/#271.
