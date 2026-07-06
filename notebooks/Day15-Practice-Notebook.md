# Day 15 — Practice Notebook

**Week 2 · Day 15 — July 6, 2026**
**Topic:** Block 1 — 3 reviews (#875, #153, #155, blank screen). Block 2 — NEW: Eval RPN (#150) + Daily Temperatures (#739, **monotonic stack**).
**New concepts:** monotonic stack; short-circuit evaluation; `int()` cast; `int(a/b)` truncation-toward-zero.

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Warm-up — reflexes (2/2)
1. Min Stack push-to-minStack condition: `len(minStack) == 0 or val <= minStack[-1]` ✅.
2. Koko searches the **eating-speed** range (the answer space), not the array ✅.

---

## Block 1 — Due re-solves

### Review 1 — Koko (#875) ❌ FAIL → reset 1d  *(M-015 recurrence)*
Bug: converging search (`while left < right`, `right = mid`) but with a tracked `answer = 0` returned instead of `left`. On `piles=[30,11,23,4,20], h=5` (answer 30) the loop converged to the top of the range **without ever entering the `else`**, so `answer` stayed `0` and leaked out. Fixed → `return left`. **Same bug as #153 on Day 12.**

### Review 2 — Find Min in Rotated (#153) ❌ FAIL → reset 1d  *(M-017)*
Bug: converging `else` used `right = mid - 1` instead of `right = mid`, **discarding the candidate min**. Failed `[3,1,2]` (returned 3, min is 1). Fixed → `right = mid`.

**Consolidation — the converging-search checklist (drilled after two misses):**
1. `while left < right` (strict `<`)
2. keep-candidate side → `right = mid` (**never `mid - 1`**)
3. `return nums[left]` (convergence point, **never a tracked `answer`**)
*Miss any one and it breaks — which is exactly what happened twice today.*

### Review 3 — Min Stack (#155) ✅ PASS (1d → 3d)
Clean: `MinStack` named right, `self.minStack[-1]` correct (yesterday's wrong-container slip **gone**), all O(1). B-1-positive.

---

## Block 2 — NEW

### New 1 — Evaluate RPN (#150)
Stack: push numbers, on an operator pop two and combine. **Pre-taught:** `int(token)` cast; operator-vs-number detection; `int(a/b)` truncates toward zero (Python `//` floors — wrong for negatives).
**Bug:** operand order on non-commutative ops — popped `a` (top) then `b`, computed `a - b` / `int(a/b)`, but the *second* pop is the LEFT operand. `["4","13","5","/","+"]` gave `5/13=0` instead of `13/5=2`. Fixed by popping `b` then `a` → `a op b`. O(n)/O(n).

**Final (correct):**
```python
stack = []
for token in tokens:
    if token in ("+", "-", "*", "/"):
        b = stack.pop()
        a = stack.pop()
        if token == "+":   stack.append(a + b)
        elif token == "-": stack.append(a - b)
        elif token == "*": stack.append(a * b)
        elif token == "/": stack.append(int(a / b))
    else:
        stack.append(int(token))
return stack[-1]
```

### New 2 — Daily Temperatures (#739) — MONOTONIC STACK
**Pre-taught:** monotonic stack — a stack of **indices** kept in decreasing-temperature order; the double lookup `temps[stack[-1]]`. Scan once with `i`; while today is warmer than the top day, pop and record `answer[j] = i - j`. Each index pushed/popped once → amortized O(n).

**Bugs (found via nudges, fixed himself):**
1. `else` popped the **whole** stack (`while len(stack) != 0`) → over-popped taller days. Failed `[5,3,4]` (set `answer[0]=2` when `4 < 5`). Fix: while must check `temps[stack[-1]] < temps[i]`.
2. Empty-stack crash: `while temps[stack[-1]] < temps[i] and len(stack) != 0` accesses `stack[-1]` **before** the guard → IndexError on `[2,1,5]`. **Short-circuit evaluation:** in `A and B`, `A` runs first; the guard must be `A`. Fix: `while len(stack) != 0 and temps[stack[-1]] < temps[i]`.

**Final (correct):**
```python
answer = [0] * len(temperatures)
stack = []
for i in range(len(temperatures)):
    if len(stack) <= 0 or temperatures[stack[-1]] >= temperatures[i]:
        stack.append(i)
    else:
        while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
            popped = stack.pop()
            answer[popped] = i - popped
        stack.append(i)
return answer
```
Verified `[2,1,5]→[2,1,0]`, `[5,3,4]→[0,1,0]`, `[73,74,75,71,69,72,76,73]→[1,1,4,2,1,1,0,0]`. O(n)/O(n). *(Optional cleanup for later: the `if/else` collapses into just the `while` + a push.)*

---

## Takeaways

**Theme of the day: converging binary search is fragile for me.** Two resets (#875 tracked-answer, #153 `mid-1`), same family. Checklist now memorized: `< → right = mid → return nums[left]`.

**New tools:** monotonic stack (indices, amortized O(n)); short-circuit evaluation (guard first); `int()` cast; `int(a/b)` truncation.

**Coaching note:** from Day 16 on, **less spoon-feeding** — Parthiv derives the solution; I guide with questions + minimal hints, still pre-teaching genuinely new syntax.

**B-1:** clean on names today (#155 correct `self.minStack`) — 1st of 2 clean-on-names sessions needed to clear (Day 14 broke the streak). Blocker stays active.

**Spaced-review queue (after today):**
- #875 (reset), #153 (reset), #121, #150 (new), #739 (new) → **Jul 7**
- #33, #20, #167, #11 → Jul 8; #3 → Jul 9; #155 → Jul 9; #704, #74, #1, #217 → Jul 10; #242, #49 → Jul 11; #125 → Jul 12

**Next session (Day 16):** reviews due (heavy — #875, #153, #121, #150, #739); **new** — 3Sum (#15, two pointers: sort + skip duplicates) + Longest Repeating Character Replacement (#424, sliding window: Counter + track max freq).
