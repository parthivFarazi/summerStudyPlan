# Big-O & complexity  (knowledge file)

**Status:** ongoing training · **Mastery: 4/5** *(Day 22: called O(h) unprompted, and self-corrected O(n)→O(1) on the bounded-alphabet map)*

You state **time AND space before coding**, then we correct. Complexity = the work actually done, *including inside loops and hidden operations*.

## What you've internalized
- The ladder: O(1) < O(log n) < O(n) < O(n log n) < O(n²).
- **Amortized analysis** (Day 8): a forward-only pointer shared across iterations makes a nested-looking loop O(n), not O(n²) — each element enters/leaves once.
- **Space is not free** (Day 5): building a new string/list/dict that scales with input is **O(n) space**, even if you "only loop once."
- **Hidden costs** (Day 3): a `sorted()` inside the loop made Group Anagrams O(n·k log k), not O(n).
- **The recursion call stack is real memory** (Day 21, self-corrected unprompted): if it recurses, it costs space.
- **Bounded ≠ n** (Day 22): a dict keyed by lowercase letters holds **at most 26 entries, ever** → **O(1)**, not O(n).

## The three complexity sentences to have ready

**1. Tree recursion → always O(h), never "O(n)" flat.**
> *"O(h) space — the call stack holds one frame per level. Balanced → O(log n). Skewed → O(n) worst case."*
Same sentence for **every** tree recursion. *(An iterative descent — e.g. #235 BST — has **no call stack** → **O(1)**.)*

**2. Bounded structures → O(1).**
> *"O(1) space — the map holds at most 26 entries since the input is lowercase letters. If it were full Unicode, it'd be O(k) for the character set."*

**3. Output doesn't count.**
`answer`/`result` is **required output**, not "extra" space you chose. Say **"O(1) auxiliary"**; if asked *"including the output?"*, then quote it separately.

## `sorted()` vs `.sort()` *(Day 22)*

| | Returns | Mutates input? | Space |
|---|---|---|---|
| `sorted(nums)` | **a new sorted list** | no | **O(n)** — the copy |
| `nums.sort()` | **`None`** | yes, in place | **O(1)** from your code |

> ### ⚠️ `alist = nums.sort()` sets `alist = None`.
> Then `alist[i]` → `TypeError: 'NoneType' object is not subscriptable`. **It doesn't optimize your space — it crashes your program.**

**The Python rule underneath it:**
> **Methods that MUTATE return `None`. Functions that BUILD a new object return the object.**

| Mutates → returns `None` | Builds new → returns it |
|---|---|
| `nums.sort()` | `sorted(nums)` |
| `nums.reverse()` | `reversed(nums)` |
| `nums.append(x)` | `nums + [x]` |
| `d.update(other)` | `{**d, **other}` |

So **`x = nums.append(5)` is always a bug** — same family.

**"In-place" ≠ zero memory.** Every sort needs scratch space:
- Heapsort → O(1) · Quicksort → O(log n) (recursion stack) · **Timsort (Python's) → O(n) worst case**

**Interview line:** *"I sort in place, so my own space is O(1); Python's sort itself is O(n) worst case."*
**Bonus line:** *"I'll sort in place for O(1) space — is it okay if I mutate the input?"* → shows you know it's a **trade**, not a free win.

## Gotchas to keep correcting
- Guessing **O(1) space** when you actually allocate a structure that grows with input (M-005).
- Forgetting to count the cost of operations *inside* a loop (M-006).
- Confusing "values vs indexes" when reasoning about what the loop touches (M-021 → **blocker B-5**).
- Saying **"O(log n)"** for a tree/BST when you mean **O(h)** — a BST built from sorted input is a linked list, and `h = n`. **Always name the worst case.**
