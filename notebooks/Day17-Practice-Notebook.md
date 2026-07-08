# Day 17 — Practice Notebook

**Week 2 · Day 17 — July 8, 2026**
**Topic:** Block 1 — 3 reviews (#150, #15, #424). Block 2 — NEW: Longest Consecutive Sequence (#128) + Encode/Decode Strings (#271).
**Theme of the day:** space-complexity reflex (a *new structure that scales* = O(n)); length-prefix encoding; amortized O(n) via an only-start gate.

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Warm-up — B-2 pre-empt
`for i in range(len(nums))` ✅ — range/len order automatic. (Review-heavy day: 8 due → ran the 3 fragile 1d items, rolled #33/#20/#121/#167/#11 to Day 18 interleave.)

---

## Block 1 — Due re-solves

### #150 Evaluate RPN ✅ PASS (1d → 3d)
Clean: operand order (`b` then `a`), `int(a/b)` truncation. **Called space O(1) → corrected to O(n)** (the stack scales — M-005). Time O(n).

### #15 3Sum ❌ FAIL → reset 1d  *(M-018)*
Had every piece (sort, pin, target `-nums[i]`, both dedup levels) but **omitted the `while left < right` wrapper** — the if/elif/elif ran once per `i` and jumped on, so the two pointers never swept. Fixed on a nudge. Also called space O(1) → O(n) (`sorted()` copy). Needs another rep.

### #424 Longest Repeating Char Replacement ✅ PASS (1d → 3d)
Clean, and **correctly called space O(1)** — the dict is capped at 26 (bounded, doesn't scale), unlike the stack/sorted-copy. Good distinction. Time O(n).

---

## Block 2 — NEW (less-spoon-feeding; he derived both)

### #128 Longest Consecutive Sequence
**Approach (his, with nudges):** O(n) rules out sorting → use a **set** for O(1) membership. Key insight: only start counting at a **run-start** (a number `x` where `x-1` isn't in the set), then count **forward** (`x+1, x+2, …`). Worked out the **amortized O(n)** himself (each number is forward-walked once total, so the loop-in-loop is O(n), not O(n²) — same lesson as sliding window).
**Bug:** inner `while num + i not in seen` (inverted) → fixed to `in seen`.
```python
seen = set(nums)
maxRun = 0
for num in nums:
    if num - 1 not in seen:          # run-start gate
        i = 1
        while num + i in seen:
            i += 1
        maxRun = max(maxRun, i)
return maxRun
```
O(n) amortized time, O(n) space (the set scales — correctly identified).

### #271 Encode and Decode Strings
**Insight (his):** can't use any delimiter (strings may contain it) → **length-prefix**: `len#string`, and `decode` reads by **count**, not by hunting a delimiter (so a `#` inside a string is harmless). Class with no `__init__` (no state to carry — contrast Min Stack).
**Bugs worked through:** encode omitted the word, then overwrote instead of accumulating → `answer += str(len(word)) + "#" + word`. decode: `i` reset inside the loop → moved `i = 0` out; single-digit `int(s[i])` → read all digits to `#` via a `j` pointer + slice `s[i:j]`; `j = i` reset must be **inside** the loop.
```python
class Codec:
    def encode(self, strs):
        answer = ""
        for word in strs:
            answer += str(len(word)) + "#" + word
        return answer
    def decode(self, s):
        aList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            aStr = ""
            for n in range(l):
                aStr += s[i]
                i += 1
            aList.append(aStr)
        return aList
```
O(N) time; space: encode O(1) extra (output excluded — he reasoned this himself ✅), decode O(n) via the temp `aStr`.

---

## Takeaways

**Space-complexity reflex (M-005, recurrence 2):** three times today he said "O(1)" for something O(n) (stack, sorted copy, encoded string) and corrected each on a beat. **But improving** — he nailed #424's O(1) (bounded dict) unprompted and reasoned #271-encode's O(1)-extra (output excluded) correctly. The rule solidifying: *new structure that scales with input = O(n); bounded (≤26) or the returned output = doesn't count.*

**#15 reset:** forgot the `while` wrapper on the two-pointer — 3Sum isn't fully consolidated yet, so it comes back at 1d (M-018).

**New patterns:** #128 = set + only-start gate + forward count (amortized O(n)); #271 = length-prefix, decode-by-count.

**B-2 (range/len):** clean today (`range(len(nums))`, `range(len(s))`) — 1 of 2 to clear.

**Spaced-review queue (after today):**
- **Day 18 = interleave** (no new): rolled #33, #20, #121, #167, #11 + due Jul 9 (#155, #3, #15 reset, #128, #271)
- #875, #153, #739, #1, #217 → Jul 10; #704, #74 → Jul 10; #242, #49 → Jul 11; #150, #424 → Jul 11; #125 → Jul 12; #347 → Jul 21; #238 → Jul 23

**Next session (Day 18):** **Interleave day** — mixed, unlabeled set (clears the review backlog). Name the pattern first; state complexity unprompted (esp. space!). No new problem.
