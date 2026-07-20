# Heap / Priority Queue

**Status:** learning (started Day 26, 2026-07-18) · **Mastery: 2/5** · Block B
**First problems:** #703 Kth Largest in a Stream, #1046 Last Stone Weight — both built + verified.

## In one line
A container that keeps the **minimum instantly accessible** while staying cheap to insert into and remove from. **NOT recursion** — iterative, backed by a library.

## Reach for it when
- "k-th largest / k smallest", "top k", "k closest"
- Repeatedly pull the largest (or smallest) thing, mutate, put back (#1046)
- A streaming feed where you need a running top-k (#703)
- Merge k sorted lists; Dijkstra; scheduling by priority

## Why not just sort?
- **Sorted list:** min is free, but every insert shifts elements → O(n).
- **Unsorted list:** insert is free, but finding the min → O(n) scan.
- **Heap:** peek min **O(1)**, push **O(log n)**, pop min **O(log n)**. It doesn't fully sort — just enough that the min is always on top.

## `heapq` — the Python API (operates on a plain list)
```python
import heapq
h = []
heapq.heappush(h, x)     # TWO args: the heap FIRST, then the item
heapq.heappop(h)         # ONE arg: the heap. Removes & returns the MIN.
h[0]                     # peek the min — O(1). (h[1], h[2]... are NOT sorted.)
heapq.heapify(lst)       # turn a plain list into a heap IN PLACE — O(n)
```
- **`heapq` is a MIN-heap.** `heappop` always gives the smallest.
- **`h[0]` is the min; the rest of the list is not ordered.** Only the top is guaranteed.

## 🔑 Max-heap: the negation trick
No max-heap in `heapq`. **Store negatives, negate back when you read.**
```python
heapq.heappush(h, -x)      # push the negative
val = -heapq.heappop(h)    # pop the most-negative (= largest), negate back
```

## 🔑 The "min-heap of size k" pattern (#703 Kth Largest)
To track the **k-th largest**, keep a **min-heap holding only the k largest** seen so far.
Then `h[0]` — the smallest of the top k — **IS the k-th largest.**
```python
def add(self, val):
    heapq.heappush(self.h, val)       # push
    if len(self.h) > self.k:
        heapq.heappop(self.h)         # trim: pop the smallest (falls off the top-k)
    return self.h[0]                  # the cutoff = the answer
# add: O(log k) time, O(k) space
```
**Why a MIN-heap (not max):** you need the **cutoff** between "top k" and "everyone else" — that's the *smallest* of your k, i.e. `h[0]`. It's both the answer and the thing you evict. *(He built a verbose case-split version; push-and-trim above is the clean idiom.)*

## #1046 Last Stone Weight — max-heap
```python
h = [-s for s in stones]
heapq.heapify(h)                       # O(n)
while len(h) > 1:
    a = -heapq.heappop(h)              # largest
    b = -heapq.heappop(h)              # 2nd largest  (a >= b)
    if a != b:
        heapq.heappush(h, -(a - b))
return -h[0] if h else 0
# O(n log n) time, O(n) space
```

## Complexity
- push / pop: **O(log n)** · peek `h[0]`: **O(1)** · `heapify`: **O(n)**.
- "min-heap of size k" ops: **O(log k)**; whole streaming pass O(n log k).
- Space: **O(n)** (or O(k) if you cap the heap at size k).

## Your gotchas (Day 26 — all new-API friction)
- **`heappush` needs the heap first** — wrote `heapq.heappush(x)` / `heapq.heappush(-num)` (missing `h`) **three times**. `heappush(h, x)`, always.
- **`heappop` takes ONLY the heap** — wrote `heapq.heappop(h, num)` with a stray second arg. `heappop(h)`.
- **A plain list is not a heap** — call `heapq.heapify(lst)` first, or build it with pushes. `self.h = nums` alone leaves `h[0]` as arbitrary `nums[0]`.
- **Sign flips (max-heap)** — negate on push AND negate back on every read; easy to drop one.
