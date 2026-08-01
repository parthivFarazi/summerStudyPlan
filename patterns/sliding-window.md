# Sliding Window

**Status:** learned (Days 7–8, 16) · **Mastery: 3/5** · Block A

## In one line
A moving window over a sequence that maintains *running state*; expand the right edge, shrink the left to keep the window valid.

## Reach for it when
- Contiguous subarray/substring with a constraint (longest/shortest/at-most-k distinct).
- A "running" max/min/sum as you scan.
- You'd otherwise recompute over overlapping ranges.

## Sub-techniques you've done
- Running-state form — Best Time to Buy/Sell Stock (#121): track running-min + best-profit (just 2 vars).
- Variable-size window — Longest Substring Without Repeating (#3): set + shrink-from-left.
- **Freq-map + validity rule — Longest Repeating Char Replacement (#424): window OK while `(len - maxFreq) <= k`; `maxFreq = max(count.values())`; dict capped at 26 → O(1) space.**

## Template
```python
left = 0
state = ...                      # the minimum you need (a set, a count, a running min)
for right in range(len(s)):
    # include s[right] in state
    while not_valid(state):
        # remove s[left] from state
        left += 1
    answer = max(answer, right - left + 1)
```

## Complexity
O(n) by **amortized analysis** — each element is added once and removed at most once; forward-only pointers ⇒ not O(n²).

## Your gotchas (from the log)
- **Keep the minimum necessary state** — Day 7 you over-engineered with 4 vars + time-guards; the answer was 2 vars.
- Don't carry assumptions across problems — Day 8 you imported `k log k` from Group Anagrams (there's no sort here).
- **Read the spec/example** for work you must do (e.g., "alphanumeric only" = real work).

---

## Fixed-size window + frequency compare (#567) — *🎯 Mock #1, Day 36*

**The tell:** *"does some substring of `s2` contain exactly the letters of `s1`?"* — the window length never changes. **That's a fixed-size window**, which is simpler than the grow/shrink kind: both pointers move together, every step.

### The trap: comparing windows the expensive way

The obvious comparison is *"sort both and check equality."* It is **correct and it will be rejected.**

```python
while right <= len(s2):
    key1 = "".join(sorted(s1))          # ⚠️ loop-INVARIANT, recomputed every step
    key2 = "".join(sorted(s2[left:right]))
    if key1 == key2: return True
    left += 1; right += 1
```

Let `m = len(s1)`, `n = len(s2)`. The loop runs `n − m + 1` times and each pass sorts `m` characters twice ⇒ **`O((n − m)·m log m)`, worst case `O(n² log n)`** — not the `O(n log n)` it looks like. Measured at the constraint ceiling (`len ≤ 10⁴`):

| version | time |
|---|---|
| as written | **5.67 s** ⛔ TLE |
| `key1` hoisted out of the loop | 2.80 s ⛔ still TLE |
| `O(n)` rolling frequency count | **0.001 s** ✅ |

> **Two separate lessons, and they are different.** **(1)** Anything that doesn't depend on the loop variable belongs **outside** the loop — hoisting `key1` alone halves the runtime for free. **(2)** Even hoisted, sorting *inside* a loop is the wrong shape. **Price the body of every loop you write.** *(M-006 — third occurrence, after Group Anagrams on Day 3 and Longest Substring on Day 8.)*

### The `O(n)` version — the window changes by exactly TWO characters

```python
def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False
    a = ord('a')
    need = [0]*26
    window = [0]*26
    for ch in s1: need[ord(ch)-a] += 1

    for i, ch in enumerate(s2):
        window[ord(ch)-a] += 1                       # the character ENTERING
        if i >= len(s1):
            window[ord(s2[i-len(s1)])-a] -= 1         # the character LEAVING
        if window == need: return True
    return False
```

**You never rebuild the count.** One character enters on the right and one leaves on the left, so the update is `O(1)`. The comparison is over **26 slots — a bounded map is `O(1)`**, not `O(m)`.

**Complexity:** `O(n)` time · **`O(1)` space** (26 counters, independent of input size).

> **The general move: when a window slides, ask what actually CHANGED.** Almost never the whole window — usually two things. Rebuilding state you could have updated is the most common way a correct sliding-window solution becomes too slow. Kin to `#3` and `#424`, where the same reasoning gives you the `O(n)` bound.

### Related
`#242 Valid Anagram` is this comparison without the window. `#438 Find All Anagrams in a String` is the same code returning every index instead of a boolean.
