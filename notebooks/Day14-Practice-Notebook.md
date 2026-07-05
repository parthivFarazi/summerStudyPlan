# Day 14 — Practice Notebook

**Week 2 · Day 14 — July 5, 2026**
**Topic:** Block 1 — 3 reviews (#33, #20, #125, blank screen). Block 2 — NEW: Min Stack (#155), first **class**.
**New concept:** Python classes (`class` / `__init__` / `self` / methods). **New technique:** two-stack Min Stack.

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Warm-up — reflexes (2/2)
1. Search the **left** half → `right = mid - 1` ✅ (M-012 opposite-wall).
2. End of Valid Parentheses → return whether the stack is empty ✅ (`return not stack`).

---

## Block 1 — Due re-solves (all PASS)

### Review 1 — Search in Rotated (#33) ✅ PASS (1d → 3d)
All four pointer directions correct this time — **M-012 inversion fixed**, reproduced cold the day after learning the hardest problem in the plan. Traced `0→4`, `3→-1`, `5→1`. O(log n) / O(1). Variable audit clean.

### Review 2 — Valid Parentheses (#20) ✅ PASS (1d → 3d)
All 3 of yesterday's bugs gone: `append(char)`, `aDict[char]` lookup, `return len(stack) == 0`. Clean cold. O(n) / O(n).

### Review 3 — Valid Palindrome (#125) ✅ PASS (3d → 7d) — B-1 blocker problem
Clean: correct `clean` variable throughout (the historic slip), correct `.isalnum()` spelling, two-pointer `while left < right`. Traced all three incl. the empty string. O(n) / O(n). A real B-1 win on the exact problem that kept it red for five sessions.

---

## Pre-teach — Python classes (first one)
- **class** = blueprint; **instance** = one object built from it (`c = Counter()` makes one).
- **`__init__(self)`** = setup; runs on creation; build the starting data here.
- **`self`** = *this* instance — the object to the **left of the dot** when a method is called. `self.count` lives on the instance (persists; every method can see it); a bare `count` would vanish when the method ends.
- **methods** take `self` first: `def push(self, val):` — but you call `obj.push(5)` and Python passes `self` automatically.
- Cemented "instance" with two independent counters (each has its own `count`).

---

## Block 2 — Min Stack (#155), first class

**Challenge:** `getMin()` in O(1) — can't scan. **Technique:** two lists — a value stack + a min-stack whose top is always the current minimum.

**His good questions:**
- *"Why not a single min variable (O(1) space)?"* → it breaks on `pop`: if you pop the current min, a lone variable can't recover the previous min without an O(n) scan. The min-stack remembers the min at every level, so pop restores it in O(1). O(n) space is the price of O(1) pop **and** getMin.
- Reached for the **conditional-push** optimization (only push to minStack on a new min) and used `<=` for duplicate mins — both correct, and more space-efficient than always-push.

**Bugs (fixed):**
1. push compared `val <= self.stack[-1]` — but `self.stack[-1]` is `val` (just appended) → always true, and the wrong list. Fixed to `self.minStack[-1]` (the current min). **Wrong-container slip — M-004 family (`self.stack` vs `self.minStack`).**
2. Guard needed the **empty** case `len(self.minStack) == 0` (first push), not `> 0` (that's "non-empty" — backwards).
3. Class named `Stack` → should be `MinStack` (LeetCode interface).

**Final (correct):**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val):
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
    def pop(self):
        popped = self.stack.pop()
        if self.minStack[-1] == popped:
            self.minStack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minStack[-1]
```
Verified `push 5,3,7 → getMin 3`; `pop, pop → getMin 5`; + a duplicate-min case. **All ops O(1)**, space O(n).

---

## Takeaways

**Wins:** three clean cold reviews — #33 (M-012 fix stuck), #20 (first stack), #125 (the blocker problem) — plus a working first **class** and a genuinely smart space question.

**Keeper — classes:** blueprint vs instance; `self` = the object before the dot; `self.x` persists on the instance.

**B-1 status — honest:** #125 was clean, but `self.stack`/`self.minStack` on #155 is the same wrong-container family → blocker **stays active** one more session (need a fully clean session *including* the new problem). Was premature to close it.

**Precision watch:** with lookalike names (`stack` / `minStack`), the variable audit still earns its keep.

**Spaced-review queue (after today):**
- #875 (carry-over, due Jul 4), #153, #155 → **Jul 6**
- #121 → Jul 7; #33, #20, #167, #11 → Jul 8; #3 → Jul 9; #704, #74, #1, #217 → Jul 10; #242, #49 → Jul 11; #125 → Jul 12; #347 → Jul 21; #238 → Jul 23

**Next session (Day 15):** reviews due (#875, #153, #155); **new** — Eval Reverse Polish Notation (#150) + Daily Temperatures (#739, **monotonic stack** — store indices).
