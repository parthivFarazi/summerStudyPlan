# Day 20 — Practice Notebook

**Week 3 (folder Week 4) · Day 20 — July 11, 2026**
**Topic:** Block 1 — 7 reviews (first full run of the new protocol: verbal tier + logged times). Block 2 — Linked List mediums: Reorder List (#143), Remove Nth Node From End (#19).

> Format: raw answers verbatim, then correction/coaching. Times now logged per problem.

---

## Block 1 — Reviews

**Full re-solves (5):**
- **#875 Koko ✅ PASS (reset cleared, 1d → 3d)** — `left = 1` (boundary fixed), converging logic clean, `return left`. **5:54.**
- **#150 Eval RPN ✅ PASS (3d → 7d)** — operand order + `int(a/b)` truncation, `return`. **8:03.**
- **#739 Daily Temps ❌ FAIL → reset 1d** — dropped the empty-stack guard in the `while` **and** forgot `stack.append(i)` after (both clean on Day 15). **M-011** (dropped guard). **9:58.**
- **#167 Two Sum II ✅ PASS (7d → 21d, now verbal)** — two pointers, `+1` 1-indexing. **6:30.**
- **#11 Container ✅ PASS (7d → 21d, now verbal)** — width × min-height, move-the-shorter-wall. **5:43.**

**Verbal recalls (2):**
- **#49 Group Anagrams ✅ (21d → 60d)** — sorted-string key, dict of lists, `list(aDict.values())`. (Complexity note: O(n·k log k), not O(n log n).)
- **#242 Valid Anagram ❌** — recalled the **WRONG pattern** (said two-pointer/palindrome; it's frequency-count) → converted to a full solve → then **dropped the length guard** (the EXACT M-011 bug from Day 7) → reset 1d. *The verbal tier did its job — caught a decayed problem cheaply.*

---

## Block 2 — Linked List mediums

### #143 Reorder List ✅ (strong first attempt)
Composed three owned operations himself: **find middle** (fast/slow, tracked `mid` = prev-of-slow, cut `mid.next = None`) → **reverse the 2nd half** → **alternating merge**. Only bug: a `revCurr`/`reCurr` **name typo** (variable-consistency). In-place, returns `None`. O(n)/O(1).
- Learned: fast/slow finds the middle (same tool as #141, different job — no cycle needed); the space win is doing it all **in place**; you must **explicitly cut** the halves (`slow.next = None`), they don't auto-detach.

### #19 Remove Nth Node From End ✅ (clean first try)
```python
dummy = ListNode(); dummy.next = head
slow = fast = dummy
for i in range(n):
    fast = fast.next            # gap of n
prev = None
while fast != None:
    fast = fast.next; prev = slow; slow = slow.next
prev.next = prev.next.next      # delete slow (prev is one before it)
return dummy.next
```
Two-pointer **gap of n** in one pass; **dummy** handles head-removal cleanly. Traced n=2 on 5-list + edge cases. O(n)/O(1).

---

## Takeaways

**Big jump on linked lists** — #143 (3-part medium) and #19 both essentially self-driven, a day after the basics drill. Composition of fundamentals is landing.

**#1 recurring gap = dropped edge-guards (M-011).** Twice today (#739 empty-guard, #242 length-check — a *literal repeat of Day 7*) → **escalated to blocker B-4**: pre-submit edge-guard check (empty? single? length? none-found?). This is the clearest slice of the "first-draft precision" gap.

**B-3 (forgot `return`):** clean today — every solve returned (or #143 intentionally `None`). 1 of 2 sessions to clear.

**Times logged** (new): 5:54 / 8:03 / 9:58 / 6:30 / 5:43 / 3:13 — solid re-solve pace; will trend these down toward interview speed.

**Spaced-review queue (after today):** #875→3d, #150→7d, #739 reset 1d, #167/#11→21d (verbal), #49→60d, #242 reset 1d; #143 + #19 new at 1d — dates fuzzed.

**Next session (Day 21, roadmap Week 3):** review **Min Stack**; **new** — LRU Cache (#146, Medium), Invert Binary Tree (#226), Max Depth of Tree (#104) → **first Trees** (pre-teach TreeNode + recursion basics first, per the new-data-structure rule).
