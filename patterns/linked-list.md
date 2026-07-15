# Linked List

**Status:** learned (Day 19–20) · **Mastery: 4/5** *(Day 24: LRU Cache built + verified)* · Block B

## In one line
Pointer surgery: a chain of nodes (`val` + `next`); manipulate by carefully rewiring `.next`. Dummy nodes, fast/slow pointers, in-place reversal.

## The 5 core moves (drill these first on any LL problem)
```python
# BUILD:    a = ListNode(5); a.next = ListNode(10)
# TRAVERSE: curr = head
#           while curr: ... curr = curr.next        # stops at None
# ACCESS:   head.val, head.next.val, head.next.next.val
# DELETE b: a.next = a.next.next                    # skip b (node→node, no .val)
# INSERT x: x.next = a.next; a.next = x             # ORDER: stash before overwrite
```
**Golden rule: node vs value.** `.next` links **nodes**; `.val` reads a **value**. When rewiring `.next`, both sides are nodes — never `.val`. And a node reference **is** the whole rest of the chain.

## Reach for it when
- Reverse / reorder / merge nodes
- Detect a cycle → fast/slow (Floyd's)
- 'Nth from the end' → two pointers with a gap
- O(1) extra space required on a list

## Template — reverse (#206)
```python
prev, curr = None, head
while curr:
    nxt = curr.next      # stash the rest BEFORE overwriting
    curr.next = prev     # flip this link backward
    prev = curr; curr = nxt   # slide both forward
return prev              # new head
```
- Only 2–3 pointers, reused, that WALK the list. n links flipped (O(n) time), fixed handles (O(1) space).

## Template — dummy + tail (build/merge #21)
```python
dummy = ListNode(); tail = dummy
while list1 and list2:
    if list1.val <= list2.val:
        tail.next = list1; list1 = list1.next
    else:
        tail.next = list2; list2 = list2.next
    tail = tail.next
tail.next = list1 if list1 else list2   # attach the whole leftover in one line
return dummy.next
```
- `dummy` = throwaway starter so the first attach needs no special case; real head is `dummy.next`. `tail` = handle on the end where you splice.

## Template — Floyd's fast/slow (cycle #141)
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```
- Cleaner than the manual guard: `while fast and fast.next` both prevents `fast.next.next` crashing AND avoids the `None == None` false positive.

## Template — find middle (fast/slow) + Reorder (#143), Remove Nth (#19)
**Find middle** — same fast/slow as Floyd's, new job (no cycle needed): when `fast` falls off the end, `slow` is at the middle.
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next; fast = fast.next.next   # slow ends at the middle
```
**Reorder List (#143)** = compose in place: find middle → `second = slow.next; slow.next = None` (**CUT — halves don't auto-detach**) → reverse `second` → merge the two halves alternately. O(1) space.
**Remove Nth from end (#19)** = two-pointer **gap of n** + dummy: advance `fast` n steps, then move both till `fast` hits the end; `slow` (from a dummy) lands just before the target → `slow.next = slow.next.next`. One pass.

## 🔑 Doubly-linked list + hashmap — the design combo *(Day 24, #146 LRU Cache)*

**The doubly-linked node** adds a **backward** pointer:
```python
class Node:
    def __init__(self, key, val):
        self.key = key      # store the KEY too — needed to delete from the dict at eviction
        self.val = val
        self.prev = None    # ← the backward pointer
        self.next = None
```
**Why `prev`:** to remove a node you're *holding*, you splice its neighbours together — you need to reach **both**. `node.next` gives one; **`node.prev` gives the other.** Singly-linked → you'd walk from head to find the predecessor → O(n). With `prev`, removal is **O(1)**:
```python
def remove(node):
    node.prev.next = node.next
    node.next.prev = node.prev
```
**Dummy head & tail sentinels** — two permanent fake nodes at the ends. Real nodes always live *between* them, so **every real node is guaranteed a `prev` and a `next`** → `node.prev.next` can never hit `None` → **the `if node.prev is None` edge cases vanish.** Convention: next-to-head = MRU, next-to-tail = LRU.
```python
def insert_front(node):          # stitch node in right after head (MRU)
    temp = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = temp
    temp.prev = node
```

**Why two structures (the whole point of LRU):** a **dict alone** has O(1) lookup but O(n) eviction (must *find* the LRU); an **ordered list alone** has O(1) eviction but O(n) lookup. **Each is O(1) at what the other is O(n) at → use both.** The **dict maps `key → Node`**; lookup is O(1), and once you hold the node, remove/insert_front are O(1). Full working class + verification in `notebooks/Day24-Practice-Notebook.md`.

**Design-problem instinct (M-024):** when one abstraction is backed by **two** structures, **every mutation must touch both** — overwrite repoints `dict[key]`; eviction does `remove(node)` *and* `del dict[node.key]`. Forgetting the second is the design-level version of container-vs-contents.

## Complexity
Traverse/reverse/merge/cycle: **O(n)** (or O(n+m)) time, **O(1)** space (rewire in place; dummy is O(1)).
**LRU (#146):** `get`/`put` **O(1)**, space **O(capacity)** (bounded by cache size — not the number of ops; two different "n"s, be explicit).

## Your gotchas (from the log)
- **node vs value** — `.val` when rewiring `.next` (Day 19, multiple times).
- **`self.` confusion** — both directions inside a class (**M-020 → blocker B-7**): dropped `self.` on `self.minStack` (#155, Day 19) and on `self.remove(node)` calls (#146, Day 24); *added* a spurious `self.` to a **parameter** (`self.node`, #146, Day 24). **The test:** attached via `self.x=` in `__init__` OR a method of this class → `self.`; parameter/local → bare. See [python-classes.md](python-classes.md).
- **Reorder merge is ALTERNATION, not value comparison** (M-009) — #143 forbids touching values; don't paste #21's `if a.val <= b.val` body. #21 compares values, #143 strictly alternates. Same skeleton, opposite body.
- **Floyd's `None == None` false positive** — guard with `while fast and fast.next` (or `and fast != None`). (Day 19)
- Reverse/insert: **stash `nxt` BEFORE overwriting** `curr.next`, or you strand the rest.
