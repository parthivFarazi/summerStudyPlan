# Stack

**Status:** learned (Day 13–14) · **Mastery: 2/5** · Block A

## In one line
LIFO (last-in, first-out) structure for matching, undo, or 'nearest greater/smaller' scans. In Python it's just a **list** — only ever touch the end.

## Reach for it when
- Matching pairs / nested structure (parentheses, tags)
- 'Next greater/warmer' element → monotonic stack
- Evaluate expressions (RPN)
- Need to remember the most recent unresolved thing (LIFO)

## Python ops (list as stack)
```python
stack = []
stack.append(x)    # push onto the top (end)
top = stack.pop()  # remove AND return the top
peek = stack[-1]   # look at the top without removing
if not stack:      # True when empty  (same as len(stack) == 0)
    ...
```

## Template — matching / Valid Parentheses (#20)
```python
pairs = {")": "(", "]": "[", "}": "{"}   # closing → opening
stack = []
for ch in s:
    if ch not in pairs:          # opening → push
        stack.append(ch)
    else:                        # closing → the top must be its match
        if not stack or stack.pop() != pairs[ch]:
            return False
return not stack                 # valid ONLY if nothing is left unclosed
```

## Template — Min Stack (#155): O(1) minimum via a second stack
Keep a parallel `minStack` whose top is always the current min (conditional push saves space):
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:   # <= keeps duplicate mins
            self.minStack.append(val)
    def pop(self):
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
    def top(self):    return self.stack[-1]
    def getMin(self): return self.minStack[-1]
```
- Why not a single min variable? Popping the current min can't recover the previous min without an O(n) scan; the min-stack holds the min at every level. O(n) space buys **O(1) pop + getMin**.
- Compare to **`self.minStack[-1]`**, not `self.stack[-1]` (after append that's `val` itself) — wrong-container slip, M-004. (Day 14)

## Complexity
- Time **O(n)** (one pass). Space **O(n)** for the stack (worst case: all openings).

## Your gotchas
- **Empty-stack guard:** a closing bracket when the stack is empty ⇒ invalid — never `pop()` an empty stack. (Day 13)
- **End-state is part of correctness:** after the loop, leftover items = unclosed ⇒ `return not stack` (or `len(stack) == 0`), not a bare `return True`. Don't patch it with a length/shape band-aid (`len(s) < 2`) — the stack already carries the answer. (Day 13)
- **Look up the CURRENT item:** map the closing `ch` you're on → `pairs[ch]`, compare to the popped top. Don't look up the popped opening (`pairs[x]` → KeyError; keys are closings). (Day 13)
