# Day 19 — Practice Notebook

**Week 3 (folder Week 4) · Day 19 — July 10, 2026**
**Topic:** Block 1 — 5 reviews (new review protocol). Block 2 — first **Linked Lists**: Reverse (#206), Merge Two Sorted (#21), Cycle (#141) — plus a full **linked-list basics drill** in between.

> Format: my **raw answers** verbatim, then the **correction / coaching notes**. First session on the new review protocol (budget ~6–8, verbal tier, fuzzed dates).

---

## Block 1 — Due re-solves (5, ordered resets → 1d → 3d → oldest)

- **#20 Valid Parentheses ✅ PASS (reset cleared, 1d → 3d)** — empty-stack guard back; `")("` → False.
- **#155 Min Stack ✅ PASS (3d → 7d)** — correct two-stack logic, but **dropped `self.` on `minStack` twice** in the push condition (`len(minStack)` / `minStack[-1]`) → NameError; fixed on nudge. *Reflex: inside a class method, instance data is always `self.x`.* (M-004 family — B-1 is cleared, but re-watch.)
- **#875 Koko ❌ FAIL → reset 1d** — `left = 0` instead of `left = 1`; on `piles=[1]`, `mid=0` → `math.ceil(1/0)` **division by zero**. Converging logic itself was clean. *Eating speed ≥ 1 — respect the valid lower bound.* (**M-019**)
- **#153 Find Min ✅ PASS (3d → 7d)** — clean, `right = mid`, `return nums[left]`.
- **#121 Best Time ✅ PASS (7d → 21d)** — running-min + best-profit, 2 vars. **Now graduates to the VERBAL tier.**

---

## Linked-list foundation (Parthiv asked for it — he'd been under-drilled)

Pre-taught `ListNode` (val/next), traversal, None-termination. Built an **interactive reversal-stepper widget** (2 handles walk, links flip). Then, after he flagged that reverse/merge assumed too much, ran a **basics drill** — this was the turning point of the day:

1. **Build:** `head = ListNode(5); head.next = ListNode(10); curr = head.next; curr.next = ListNode(15)`.
2. **Traverse:** `curr = head; while curr: total += curr.val; curr = curr.next`.
3. **Access:** `head.val`, `head.next.val`, `head.next.next.val`.
4. **Delete** (a→b→c ⇒ a→c): `curr.next = curr.next.next`.
5. **Insert** (a→b, splice x): `x.next = curr.next; curr.next = x` — **order matters** (stash before overwrite).

**The recurring lesson all day: node vs value.** `.next` links **nodes**; `.val` reads a **value**. When rewiring `.next`, both sides are nodes — never `.val`.

---

## Block 2 — NEW (linked lists)

### #206 Reverse Linked List ✅
```python
prev = None
curr = head
while curr != None:
    store = curr.next     # stash the rest BEFORE overwriting
    curr.next = prev      # flip
    prev = curr           # slide
    curr = store          # slide
return prev
```
Derived it after the widget clicked (2–3 pointers that *walk*, not one per node). **Slip: forgot `return prev`** → **M-001 recurrence 3 → escalated to blocker B-3.** O(n)/O(1).

### #21 Merge Two Sorted Lists ✅
Dummy + tail (`curr3`); compare-and-splice `while list1 and list2`; attach leftover in ONE line (`curr3.next = curr1 if curr2 is None else curr2`); `return dummy.next`. **Big idea he learned: a node reference IS the whole rest of the chain** — so the leftover attaches wholesale. O(n+m)/O(1).

### #141 Linked List Cycle ✅ — Floyd's fast/slow
```python
fast = head
slow = head
while fast != None:
    if fast.next != None:
        fast = fast.next.next
    else:
        fast = fast.next
    slow = slow.next
    if fast == slow and fast != None:   # guard the None==None false positive
        return True
return False
```
Reasoned out "two runners at different speeds must meet on a loop" himself. **Bug: `fast == slow` fired on `None == None`** (single node, no cycle → false True); fixed with the `and fast != None` guard. O(n)/O(1).

---

## Takeaways

**The basics drill was the smartest move of the day** — going from "linked lists are completely new" to build/traverse/access/delete/insert as reflexes, *then* solving reverse/merge/cycle. Lesson for the system: **for a brand-new data structure, drill the fundamental ops in isolation BEFORE manipulation problems.**

**New pattern — Linked List:** node vs value; `.next` rewiring; the reversal pointer-dance; dummy+tail for building; Floyd's fast/slow.

**Precision slips (execution gap, the #1 focus):** forgot `return` (M-001 → B-3), missing `self.` (#155), `left=0` boundary (#875 reset, M-019). All fixed on nudges — the theme is first-draft precision.

**Next session (Day 20):** reviews due, then **Linked List Mediums** — Reorder List (#143), Remove Nth Node From End (#19, two-pointer gap).
