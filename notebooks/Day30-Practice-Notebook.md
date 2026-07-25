# Day 30 — 2026-07-25 — Interleave review + #79 Word Search (grid DFS) *(planned Jul 24; ran Jul 25)*

> **Sprint Week 5 → Day 30** (folder `Week 5/Day 30/`).
> **Headline: the reset-causes have migrated. Every *older* named facet held — #1046's un-negate-on-the-way-out finally landed (the one twice-identical repeat is CLOSED), #211's ownership + all three Day-29 slips fixed, #199's enqueue direction fixed. The three resets all landed on the *newest* pattern (backtracking, <1 week old). That's exactly the shape you want: you stop missing old things; the fragility is only ever on the freshest material. And B-7 got its 2nd clean session → CLEARED.**

---

## B-7 micro-drill (warm-up)
Ran the ownership check-question again (nested-function called **bare** vs class-method called **`self.`**). He answered it cleanly — *"you have to call `self.expand` but `dfs` is good as it is"* — the bare-nested-def vs `self.`-method distinction is solid. Combined with the reviews below where every ownership site was correct first-draft, **this is B-7's 2nd clean session → CLEARED** (drops to a standing habit).

## Block 1 — Interleave (mixed, unlabeled — name the pattern first · 3 PASS / 3 reset)

The three that PASSED are the story of the day — **every one of them reset on a *named* cause on a previous day, and every one of those named causes held today:**

### #1046 Last Stone Weight — ✅ PASS → 3d
**The un-negate finally landed.** `heapq` max-heap via negation, and the return is **`-maxHeap[0]`** — the exact `return maxHeap[0]` miss that reset it on **Day 27 AND Day 29** (the sprint's one twice-identical repeat). Correct on the first draft today. **M-027's one stubborn repeat is closed.** Bank the rule that fixed it: *negate going in → un-negate at the return.*

### #211 Add & Search Words — ✅ PASS → 3d
The hardest problem in the queue, and all three Day-29 reset facets are gone: **`TrieNode()`** with the constructor parens, **`for child in node.children`** iterating keys correctly, and the **`return False`** after the wildcard loop all present first-draft. Ownership (`self.root`, `node.isEnd`, bare `dfs`) correct — the B-7 facet held on the exact problem that fired it.

### #199 Right Side View — ✅ PASS → 3d
The Day-29 cause — flipping the enqueue order without flipping the "keep" — is fixed: enqueue and keep are consistent, returns the right view. Root guard + O(n) space (the Day-28 causes) still held.

### #78 Subsets · #90 Subsets II · #46 Permutations — ❌ all 3 RESET → 1d
All three backtracking reviews reset. **This is the honest read, not a dodge:** backtracking is the newest pattern (first taught Day 28, #90/#46 only Day 29), and the resets clustered *entirely* here while every older named facet held. The pattern is <1 week old and still fragile — expected, and it's exactly where the spaced-repetition ladder should be spending resets right now. These stay at 1d and get re-drilled; they'll climb as the shape sets.

**Block 1 theme — the costume closet is empty on the OLD facets.** `self.`/ownership, `curr3`, guard, BFS space, box channel, enqueue direction, and now the #1046 un-negate — every previously-named reset-cause was correct first-draft. **The resets have fully migrated to the newest material.** That's the signal that the drills work: you don't miss the same thing twice anymore.

---

## Block 2 — #79 Word Search (grid DFS + in-place backtracking) — NEW

Started with the spec, because you flagged you didn't understand the question first (good instinct — never code an unread problem). **The problem:** given a grid of characters and a `word`, return whether the word can be traced through **adjacent (up/down/left/right)** cells, each cell used **at most once** per path.

### The shape (grid DFS)
```python
def wordSearchGrid(self, board, word):
    def dfs(row, col, i):
        if i == len(word):                 # matched the whole word → success
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False                   # off the grid
        if board[row][col] != word[i]:
            return False                   # this cell doesn't match word[i]
        temp = board[row][col]
        board[row][col] = "#"              # MARK visited (in place)
        found = (dfs(row+1, col, i+1) or dfs(row-1, col, i+1)
                 or dfs(row, col+1, i+1) or dfs(row, col-1, i+1))   # 4 directions
        board[row][col] = temp             # UN-MARK (the backtrack)
        return found
    for r in range(len(board)):            # every cell is a candidate start
        for c in range(len(board[0])):
            if dfs(r, c, 0):
                return True
    return False
# Time O(r · c · 4^L), Space O(L)   (L = len(word))
```

### What he derived / the good questions asked
- **"When is the un-marking done?"** — after all four neighbor calls return, restore `board[row][col] = temp`. Same choose/explore/**un-choose** shape as the rest of backtracking; here the "board" is the shared mutable state and `"#"` is the mark.
- **"How do you know it's not out of the grid?"** — the bounds check is the base case: `row`/`col` `< 0` or `>= len`. It runs *before* indexing, so no crash.
- **"Do I binary-search for where the word starts?"** — no. Just a double `for` loop over every cell; wrong starts bail immediately on the first-letter mismatch. That double loop is the `r·c` in the complexity.
- **Space O(L)?** — yes. The only memory is the **call stack**, one frame per matched letter, up to `L` deep. Marking in place means no separate `visited` set. So O(L), not O(r·c).

### Two nudges (M-027 flavor — one site on the final pass)
1. Neighbor line first came out `down, up, right, right` — **duplicated right, dropped left.** Fixed to include `dfs(row, col-1, i+1)`.
2. Outer loop was `if dfs(0, 0, 0)` inside the `r`/`c` loop — **launched every search from the top-left**, ignoring the loop variables. Fixed to `dfs(r, c, 0)` so each cell gets its turn.

Both were wire-it-up slips, not concept gaps — structure (base cases, mark/un-mark pair, complexity) was correct cold. **Grid-DFS is now the 4th backtracking shape and the bridge into graphs** (an implicit graph where neighbors = adjacent cells).

---

## Wins
- **The one twice-identical repeat (#1046 un-negate) is CLOSED** — correct first-draft after two identical Day-27/Day-29 misses.
- **Every older named reset-cause held** — resets migrated entirely to the newest pattern.
- **B-7 CLEARED** (2nd clean session) — ownership is now a standing habit.
- **Grid DFS built cold** with clean structure; the bridge to graphs is in place.

## Blockers after today
- **No drill-now blocker.** B-7 cleared → standing habit. All of B-1…B-7 now clear.
- **👁 M-027 (one site on the final pass)** — still the through-line (the two #79 nudges were this flavor), but the one *repeat* is now closed. Watch, drill = the final read-through.
- **👁 Backtracking fragility** — the newest pattern; #78/#90/#46 reset. Not a blocker, just young. Re-drill on the ladder.

## Times
Interleave (not all timed) — #1046, #211, #199 clean cold; #78/#90/#46 reset on backtracking facets. #79 taught + built in Block 2.

## Spaced-review changes
PASS→3d: **#211, #1046, #199.** Reset→1d: **#78, #90, #46.** New→1d: **#79.** Jul 26 = REST. Next: **Day 31 — new material (Intervals or Backtracking cont.) + continue draining the reset/1d backtracking cluster.**
