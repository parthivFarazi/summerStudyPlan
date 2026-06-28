# Day 8 — Practice Notebook

**Week 2 · Day 8 — June 28, 2026**
**Topic:** The real **variable-size Sliding Window** + amortized complexity
**Solved:** Group Anagrams, Valid Palindrome (warm-up) + Longest Substring Without Repeating Characters

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Interleaved warm-up

### Problem A → Group Anagrams (group-by-key)
Final (after fixes):
```python
aDict = {}
for word in strs:
    key = "".join(sorted(word))
    if key in aDict:
        aDict[key].append(word)
    else:
        aDict[key] = [word]
return list(aDict.values())
# O(n · k log k) time, O(n · k) space  (k = longest word)
```
**Fixes:** `"".add(...)` → **`"".join(...)`** (`.add` is for sets; `.join` glues a list into a string). Complexity corrected to **O(n · k log k)** — the `log` attaches to `k` (sorting each word), not `n`.

### Problem B → Valid Palindrome (two pointers + cleaning)
**Decayed from Day 5 — two things dropped, both re-fixed:**
1. **No cleaning** — compared raw chars, so `"A man, a plan..."` failed at `'A' != 'a'`. Re-added `.isalnum()` + `.lower()`.
2. **Infinite loop** — pointers never moved. Re-added `left += 1 / right -= 1`.

Final:
```python
clean = ""
for char in s:
    if char.isalnum():
        clean = clean + char.lower()
left = 0
right = len(clean) - 1
while left < right:
    if clean[left] != clean[right]:
        return False
    else:
        left += 1
        right -= 1
return True
# O(n) time, O(n) space  (correctly called the space O(n) this time)
```

**Spec-reading lesson:** "*considering only alphanumeric characters and ignoring case*" describes the **rules you must implement** (filter non-alphanumeric, lowercase), NOT a promise the input is clean. Read the **example** to disambiguate (`"A man, a plan..."` → True proves you must strip + lowercase). In interviews, ask: "can the input have spaces/punctuation, and ignore case?"

---

## Block 2 — Longest Substring Without Repeating Characters (variable sliding window)

**Problem:** length of the longest substring with all-unique characters.
`"abcabcbb"` → 3 · `"bbbbb"` → 1 · `"pwwkew"` → 3

### Attempt 1 — clear-the-set (wrong)
Idea: on a duplicate, `unique.clear()` and reset count to 0.
**Why it fails:** clearing throws away still-valid characters *and* drops the current char. Failing case `"dvdf"` → returns 2, correct is 3 (`"vdf"`). The window should **shrink from the left only until the duplicate is gone**, keeping the rest — which needs a `left` pointer.

### Attempt 2 — left pointer + shrink, but no max tracking
Window mechanics correct (left pointer, while-shrink, add), but `return right - left + 1` only gives the **final** window. Trace `"abcabcbb"` → returns 1, not 3. Same lesson as the stock problem: **track the running max as you go.**

### Attempt 3 — ✅ correct
```python
left = 0
seen = set()
maxLen = 0
for right in range(len(s)):
    if s[right] not in seen:
        seen.add(s[right])
    else:
        while s[right] in seen:
            seen.remove(s[left])
            left = left + 1
        seen.add(s[right])
    length = right - left + 1
    if length > maxLen:
        maxLen = length
return maxLen
```
Correct on all three examples. (Optional cleanup: the `if/else` is redundant — the `while` does nothing when there's no duplicate, so you can always "while-shrink, then add.")

### Complexity — the key lesson: **amortized analysis**
- **Space: O(n)** ✓ (the set).
- **Time: O(n)** — *not* O(n²), and *not* O(k log k · n) (no sorting here → no `log`; that was Group Anagrams bleeding over).
- **Why O(n):** the `while` is nested in the `for`, but `left` only ever moves **forward** and never resets. So **each character is added to the set once and removed at most once** → ≤ 2n set ops total. Plus the `for`'s n steps → O(n).

> **Rule update:** nested loops multiply to O(n²) **only when the inner loop runs fully each outer step.** If the inner loop advances a *shared, forward-only* pointer, total inner work is bounded by n → O(n). The shape `for right ... while left ...` (left never resets) is the classic O(n) sliding window.

---

## Takeaways
**Pattern:** **variable-size sliding window** — expand `right`; when a constraint breaks, shrink `left` *just enough*; track the best as you go. Tools: a set for window contents, `left` pointer, running `maxLen`.

**Big concepts today:**
1. **Amortized analysis** — a forward-only shared pointer makes a nested loop O(n), not O(n²).
2. **Derive complexity from the actual code** — don't carry over a `log` from a different problem.
3. **Read the spec (and the example) carefully** — "considering only…/ignoring…" = work *you* must do.

**Recurring habits:**
- `.join()` (string) vs `.add()` (set).
- Track the running max as you go (don't return only the final window) — 2nd time (stock problem too).
- Spaced review caught real decay on Valid Palindrome — exactly its purpose.

**Win:** built the hardest pattern so far through self-driven iteration, and justified an amortized O(n).

**Spaced-review queue (re-solve cold):**
- Group Anagrams, Valid Palindrome → next ~**July 1**
- Container With Most Water, Best Time to Buy/Sell → **June 29**, **July 3**
- Top K Frequent, Two Sum, Contains Duplicate, Product, Valid Anagram, Two Sum II → rolling, **~July 1–4**
- **Longest Substring Without Repeating Characters** → **July 1**, **July 5**

**Next session (Day 9):** warm-up, then a new pattern — **Binary Search**.
