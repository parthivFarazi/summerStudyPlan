# Day 5 — Practice Notebook

**Week 1 · Day 5 — June 24, 2026**
**Topic:** New pattern — **Two Pointers** (+ the `while` loop); spaced re-solves
**Solved:** Palindrome check, Two Sum II (sorted)

> Format: my **raw answers** verbatim, then the **correction / coaching notes**.

---

## Block 1 — Warm-up retrieval (cold)

### Product of Array Except Self — ✅ (reproduced the O(1)-space version!)
```python
answer = []
leftRun = 1
for i in range(len(nums)):
    answer.append(leftRun)
    leftRun = leftRun * nums[i]
rightRun = 1
for j in range(len(nums) - 1, -1, -1):
    answer[j] = answer[j] * rightRun
    rightRun = rightRun * nums[j]
return answer
# O(n) time, O(1) space
```
**Correction:** Perfect — and from memory you produced the *optimized* in-place version, not the easier two-array one. Complexity correct.

### Valid Anagram — ✅ (counting version, all edge cases)
```python
if len(s) != len(t):
    return False
tracker = {}
for letter in s:
    if letter in tracker:
        tracker[letter] += 1
    else:
        tracker[letter] = 1
for letter in t:
    if letter not in tracker or tracker[letter] <= 0:
        return False
    else:
        tracker[letter] -= 1
return True
# O(n) time, O(n) space
```
**Correction:** Perfect — length check + the `not in / <= 0` guard. Complexity correct.

### Top K Frequent (bucket sort) — ✅ logic, one recurring bug
```python
# ...counts + bucket fill correct...
answer = []
for j in range(len(bucket) - 1, 0, -1):
    for num in bucket[j]:
        answer.append[num]      # BUG (2nd time): brackets
        if len(answer) == k:
            return answer
# O(n) time, O(n) space
```
**Correction:** Logic + complexity correct. Recurring bug: `answer.append[num]` → `answer.append(num)`.
> **Rule to burn in:** `()` *calls* a method (doing something → `.append(x)`); `[]` *indexes* (grabbing by position → `nums[0]`).

---

## Block 2 — Two Pointers (new pattern)

**Tools taught first:**
- **`while` loop** — repeats while a condition is true; *you* must move the variables or it loops forever (unlike `for`, which auto-advances).
- **Two-pointer pattern** — two index variables; classic form is `left` at the front, `right` at the back, moving toward each other. Great for symmetry checks and sorted-array pair search. Usually O(n) time, O(1) space.

**Problem — Palindrome check** (clean lowercase string).

**Attempt 1 (raw) — infinite loop:**
```python
left = 0
right = len(s) - 1
while left < right:
    if s[left] != s[right]:
        return False
    else:
        continue           # BUG: never moves the pointers -> infinite loop
return True
```
**Correction:** Structure + complexity right (O(n)/O(1)), but `continue` jumps to the top *without* moving `left`/`right` → hangs forever. Exactly the `while`-loop gotcha.

**Attempt 2 (raw) — ✅ fixed it himself:**
```python
left = 0
right = len(s) - 1
while left < right:
    if s[left] != s[right]:
        return False
    else:
        left += 1
        right -= 1
return True
```
**Correction:** Correct. (Minor: the `else` is optional since the `if` returns — the moves could sit right after the `if`.)

---

## Block 3 — Two Sum II (sorted array)

**Idea taught:** on a *sorted* array, the sum tells you which pointer to move — too small → move `left` up; too big → move `right` down. No hashmap → O(1) space (vs the unsorted Two Sum, which needed O(n)).

**Attempt 1 (raw) — the "clock" idea:**
```python
left = 0; right = len(numbers) - 1; clock = 0
answer = []
while left < right:
    if numbers[left] + numbers[right] == target:
        answer.append(left); answer.append(right); return answer
    else:
        if clock == 0:
            left += 1; clock = 1
        else:
            right -= 1; clock = 0
```
**Correction:** Creative, but it moves pointers *blindly* and **ignores the sorted order**, so it misses answers. Failing case `numbers=[1,2,3,4,5], target=8` (answer `[2,4]`): the clock walks past `3+5` and returns nothing.

**Attempt 2 (raw) — ✅ comparison-driven, correct:**
```python
left = 0
right = len(numbers) - 1
answer = []
while left < right:
    if numbers[left] + numbers[right] < target:
        left = left + 1
    elif numbers[left] + numbers[right] > target:
        right = right - 1
    else:
        answer.append(left)
        answer.append(right)
        return answer
# O(n) time, O(1) space
```
**Correction:** Correct. Good use of **`elif`** (checks the next condition only if the previous ones were false — cleaner than nested if/else).

---

## Block 3b — Valid Palindrome (the real problem; my own edge-case catch)

**My catch:** the clean-string palindrome fails on realistic input like `"Was it a car or a cat I saw?"` (capitals, spaces, punctuation) — which *should* be `True`. That's the actual LeetCode "Valid Palindrome": consider only alphanumeric characters, ignore case.

**New tools taught:**
- `.lower()` → lowercases (`"W".lower()` → `"w"`).
- `.isalnum()` → `True` if the char is a letter or digit (`" ".isalnum()` → `False`).
- Building a string by concatenation: start `clean = ""`, then `clean = clean + char`.

**Solution (raw) — ✅ correct:**
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
```

**Complexity:**
- **Time: O(n)** — one pass to clean + one two-pointer pass.
- **Space: O(n)** — ⚠️ *I first guessed O(1); that's wrong.* Building `clean` creates a new string of up to `n` chars → O(n) extra. The original palindrome was O(1) only because it used two pointers and read the input **in place**. **Creating a new structure that scales with the input = O(n) space.**
- *Advanced note (revisit later):* repeated `clean = clean + char` can be O(n²) worst-case (strings are immutable; each `+` copies). Cleaner: collect chars in a list and `"".join(...)`. Same "hidden cost inside a loop" theme as the `sorted()` in Group Anagrams.

**O(1)-space version (future rep):** skip non-alphanumeric chars *inside* the two-pointer loop and compare `.lower()` on the fly — no new string needed.

---

## Takeaways
**Pattern learned:** **Two Pointers** — (a) converge from both ends to check symmetry (palindrome); (b) comparison-driven search on a *sorted* array (Two Sum II). Usually O(n) time, O(1) space.

**New tools:** `while` loop, `elif`, `.lower()`, `.isalnum()`, string-building by concatenation.

**Precision habits:**
1. `.append(x)` with **parentheses**, never `.append[x]`. (`()` = call/do; `[]` = index/grab.)
2. In a `while` loop, **move your variables yourself** — `continue` does *not* advance them.
3. Use the structure you're given — a *sorted* array means the sum tells you which pointer to move.
4. **Space complexity:** creating a new structure (list/string/dict) that scales with the input is **O(n) space** — not O(1). In-place pointers are O(1); a new `clean` string is O(n).

**Wins:** reproduced the optimized Product solution cold; learned a whole new pattern; fixed both of today's bugs yourself after one nudge.

**Spaced-review queue (re-solve cold):**
- Two Sum, Contains Duplicate → **June 26**
- Valid Anagram, Group Anagrams, Top K Frequent → **June 27**
- Product of Array Except Self → **June 25**, **June 29**
- **Palindrome (basic + Valid Palindrome), Two Sum II** → **June 27**, **July 1**

**Next session (Day 6):** warm-up, then more Two Pointers (e.g., Container With Most Water) + first interleaved mixed review of Week 1 patterns.
