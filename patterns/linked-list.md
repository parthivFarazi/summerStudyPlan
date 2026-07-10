# Linked List

**Status:** learned (Day 19) · **Mastery: 2/5** · Block B

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

## Complexity
Traverse/reverse/merge/cycle: **O(n)** (or O(n+m)) time, **O(1)** space (rewire in place; dummy is O(1)).

## Your gotchas (from the log)
- **node vs value** — `.val` when rewiring `.next` (Day 19, multiple times).
- **Missing `self.`** on instance attributes inside class methods (#155, Day 19).
- **Floyd's `None == None` false positive** — guard with `while fast and fast.next` (or `and fast != None`). (Day 19)
- Reverse/insert: **stash `nxt` BEFORE overwriting** `curr.next`, or you strand the rest.
