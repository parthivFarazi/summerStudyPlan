# Heap / Priority Queue

**Status:** learning (started Day 26, 2026-07-18) · **Mastery: 3/5** · Block B
**Problems:** #703 Kth Largest in a Stream, #1046 Last Stone Weight (Day 26) · **#973 K Closest Points, #215 Kth Largest in Array (Day 27)** — all built + verified.

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

## 🔑 Tuple keys — sort the heap by a computed value *(Day 27)*
`heapq` orders tuples by the **first element, then the second as a tiebreaker**. Push `(key, payload)` and the heap sorts by `key` for free. Put a **unique tiebreaker** (like an index `i`) second so it never has to compare the payloads (e.g. two `[x,y]` points at equal distance).
```python
heapq.heappush(h, (dist, i))     # ordered by dist; ties break on i
```

## 🔑 "Max-heap of size k" for k-CLOSEST / k-smallest *(#973)*
To keep the **k smallest** (closest), use a **max-heap of size k** (via negation): `h[0]` = the *largest* kept = the boundary. A point beats the boundary ⇒ evict, add.
```python
maxHeap = []
for i, (x, y) in enumerate(points):
    d = x*x + y*y                        # NOT x^2 — ^ is XOR
    heapq.heappush(maxHeap, (-d, i))     # push then trim = simplest
    if len(maxHeap) > k:
        heapq.heappop(maxHeap)           # pops most-negative = farthest
return [points[i] for (nd, i) in maxHeap]
# O(n log k) time, O(k) space
```
⚠️ **Min-heap-of-all keeps the FARTHEST k** if you pop to size k — the opposite. For k-smallest with a size-k heap you need a **max**-heap.

## "Min-heap of size k" for k-LARGEST *(#215 — the #703 engine)*
```python
minHeap = []
for num in nums:
    if len(minHeap) < k:
        heapq.heappush(minHeap, num)
    elif num > minHeap[0]:
        heapq.heappop(minHeap); heapq.heappush(minHeap, num)
return minHeap[0]              # smallest of the k largest = kth largest
# O(n log k) / O(k)  ·  (quickselect O(n) avg — later)
```

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
- **Sign flips (max-heap)** — negate on push AND negate back on every read; easy to drop one. **Negation is a *touch-every-boundary* transform (M-027):** push `-x`, pop `-…`, `return -h[0]` — miss any one and it's silently wrong (#1046 needed all three).
- **`^` is XOR, not power** *(Day 27, #973)* — `x^2` = `x XOR 2`, NOT `x²`. Doesn't crash, computes garbage. Use `x*x` or `x**2`.
- **`h[0]` on a tuple heap is a TUPLE** — unpack/compare the field you want (`nd, i = h[0]`), don't compare a scalar to the whole tuple.
- **Size-k: min vs max by which end you evict** — k-largest → min-heap (evict smallest); k-smallest/closest → max-heap (evict largest).
