# Day 29 — 2026-07-23 — Backtracking cont. (#90 Subsets II, #46 Permutations) + 8 reviews + B-7 drill

> **Sprint Week 5 → Day 29** (folder `Week 5/Day 29/`).
> **Headline: the drills are working — every *previously-named* reset-cause was correct on the first draft. 5/8 reviews passed; the 3 resets were fresh facets (one repeat: #1046's return-negation). And recursion — his weakest area — is visibly moving: he DERIVED Permutations from scratch.**

---

## B-7 micro-drill (warm-up)
Ownership fragments (bare vs `self.` vs `object.`). Surfaced that the real gap is the **nested-function (called bare) vs class-method (called `self.`)** distinction — and his understanding is sound (he correctly flagged my question was ambiguous). **B-7 is an execution slip, not a knowledge gap** — so the fix is the final read-through, not re-teaching the rule.

## Block 1 — Reviews (8 fragile · 5 PASS / 3 reset)

### #211 Add & Search Word — ❌ RESET (21:11)
**Ownership HELD** (`self.root`, `node.isEnd`, bare `dfs` — the drill worked on that facet!). But **3 other precision slips**: `self.root = TrieNode` (missing `()`), `for child in node.children` (keys, not `.values()`), dropped `return False` after the wildcard loop. Same disease (first-draft completeness), fresh costumes. Still the hardest problem.

### #1046 Last Stone Weight — ❌ RESET
Two bugs: `heapq.heappop(-maxHeap)` (negated the *list*), and **`return maxHeap[0]` not `-maxHeap[0]` — the SAME return-negation that reset it on Day 27.** The one *repeat* of the sprint. **Bank it: negate going in → un-negate at the return.**

### #110 Balanced Binary Tree — ✅ PASS (3:06) → 3d
Box channel correct: helper returns the height, `self.res` is the boolean. *(The Day-27 "wobble" was my fuzzy "box" terminology — his model was right all along.)* Nitpick: method named `isValidBST` (copy-paste leftover) — should be `isBalanced`.

### #973 K Closest Points — ✅ PASS (6:42) → 3d
`x*x` (no XOR), tuple unpack, correct direction, pop-then-push holds size k. First cold re-solve, clean.

### #215 Kth Largest in Array — ✅ PASS (3:20) → 3d
`len()` check present, every ref `minHeap` — both Day-27 bugs gone.

### #143 Reorder List — ✅ PASS (6:32) → 3d
Both `curr3 = curr3.next` correct — the exact `curr`/`curr3` typo that reset it Day 28 is gone. Traces to `1→4→2→3`.

### #199 Right Side View — ❌ RESET
Guard + O(n) space fixed (the Day-28 causes cleared!). But **flipped the enqueue to right-then-left without flipping the "keep"** → returned the LEFT view. Needed a level-2 trace to catch it. *(Fix: flip enqueue → flip the keep.)*

### #146 LRU Cache — ✅ PASS → 3d
Cold rebuild, everything clean (dict-sync M-024, 4-pointer `addFront` M-025, `self.` throughout, space **O(capacity)**). One `self.` missing on `remove(lru)` which he confirmed was a **paste drop** — the sibling branch had `self.remove` correct, corroborating. Counted PASS.

**Block 1 theme — the named checks HELD.** `self.` (#211, #146), `curr3` (#143), guard+space (#199), box (#110) — every prior reset-cause was correct on the first draft. The 3 resets were the hardest problem + fresh facets. **The costume closet is emptying. B-7 held → 1 clean session (clears after 1 more).**

---

## Block 2 — Backtracking cont. (both ✅)

### #90 Subsets II — extend #78 with dedup
Derived *why* duplicates arise (two equal values are interchangeable: `[2]` via "take 1st, skip 2nd" = "skip 1st, take 2nd"). **Fix: `nums.sort()` + in the SKIP branch, walk `i` past all copies** before recursing; the TAKE branch is untouched, so `[2,2]` still comes from take-take. Great question mid-teach: "how will you get `[2,2]` then?" → because reuse-via-consecutive-takes lives in the take branch. **Built 2 animators** (skip-copies step-through + a **decision-tree that draws itself** — the tree viz made the two-level skip jump concrete). O(n·2ⁿ)/O(n). Clean cold.

### #46 Permutations — DERIVED FROM SCRATCH
Coach initially dumped the skeleton; Parthiv pushed back ("are you forgetting what you have to do?"). **Restarted concept-first, Socratic** — and he derived the whole structure himself:
- permutation = fill slots, each slot picks any **unused** element (contrast subsets' take/skip).
- track used with a **`seen` set**; skip if `in seen`.
- his index-based first attempt couldn't produce `[2,1]` (only builds in original order) + crashed on `nums[i]` out of range → he saw the flaw via trace.
- reframed to **for-loop over ALL nums, no index**, choose/recurse/un-choose with BOTH undos (`path.pop()` + `seen.remove()`).
```python
res, path, seen = [], [], set()
def backtracking():
    if len(path) == len(nums): res.append(path.copy()); return
    for num in nums:
        if num in seen: continue
        seen.add(num); path.append(num)
        backtracking()
        popped = path.pop(); seen.remove(popped)
backtracking(); return res
```
O(n·n!)/O(n). First permutation, built cold from reasoning — in his hardest area.

**Coaching self-note [FEEDBACK]:** leading with the code skeleton was the wrong move (he called it out). Concept-first + Socratic is what unlocked the derivation. Reinforces COACHING #1/#9 — **teach the model first, never lead with the skeleton.**

---

## Roadmap note
#90 Subsets II is actually a **Day-52** item, slotted early by mistake (banked, not wasted). Today's roadmap item #46 Permutations done. **#79 Word Search carries to Day 30** (grid DFS + backtracking — the bridge to graphs).

## Wins
- **Every previously-named reset-cause held first-draft** — the drills are landing.
- **Recursion is moving** — Subsets II cold, Permutations derived from scratch.
- B-7 held (1 clean session).

## Blockers after today
- **B-7 — drill-now, 1 of 2 clean** (held on #211 & #146). One more clean clears it.
- **M-027 (one site on final pass)** — the through-line. **#1046 return-negation is the one *repeat* (Day 27 + Day 29 identical)** → un-negate on the way out.

## Times
#211 21:11 · #1046 4:46 · #110 3:06 · #973 6:42 · #215 3:20 · #143 6:32 · #199 4:40 · #146 12:36.

## Spaced-review changes
PASS→3d: #110, #973, #215, #143, #146. Reset 1d: #211, #1046, #199. New 1d: #90, #46. **Backlog exceeds cap Jul 24–25 — apply overflow rule live.** Next: **Day 30 — interleave + #79 Word Search.**
