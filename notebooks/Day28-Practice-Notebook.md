# Day 28 — 2026-07-22 — Backtracking from scratch (#78 Subsets, #39 Combination Sum) + 6 reviews

> **Sprint Week 5 → Day 28** (folder `Week 5/Day 28/`).
> **Second session of the day** (ran right after Day 27) — this makes up the skipped Jul 20.
> **Spacing call:** did NOT re-drill the 5 items done hours earlier on Day 27 (#211/#1046/#110/#973/#215) — re-solving minutes later tests short-term memory, not retention. Pulled genuinely-due reviews instead (last seen days ago).
> **Headline: Block 1 exposed the sharpest signal yet — reconstruct-correct-then-lose-ONE-site. Block 2: first backtracking, understood via a hand-trace + an interactive call-stack animator.**

---

## Block 1 — Reviews (6 real spaced reps · 3 PASS / 3 reset)

### 1. #271 Encode/Decode Strings — ✅ PASS (8:38) → 7d
Length-prefix (`len + "#" + word`); decode with a two-pointer scan. **The container-vs-index bug that reset this twice is GONE** — inner loop is `while s[j] != "#"` (compares the *character*). Round-trips correctly with `#` inside a word and multi-digit lengths. **O(n)/O(1) beyond output.**

### 2. #143 Reorder List — ❌ RESET → 1d
The 3-phase algorithm was **flawless** — find-middle (slow/fast, cut `mid.next=None`), reverse 2nd half, **alternate-merge with NO value comparison** (the M-009 lesson from Day 23 held; he said "there is no requirement"). But the submitted draft **crashed on a `NameError`**: `curr3 = curr.next` — `curr` doesn't exist, should be `curr3`. Not self-caught.
**Reset:** a first draft that doesn't run is a reset. The fix: a "does every variable exist / is every name right?" read-through (M-027 family). **O(n)/O(1).**

### 3. #226 Invert Binary Tree — ✅ PASS (3:47) → 7d
Swapped the **fields** (`node.left`/`node.right`) via `temp`, not locals — the Day-25 reset cause, didn't recur (M-025 held). Base case guarded, returns node. **O(n)/O(h).**

### 4. #98 Validate BST — ✅ PASS (11:59) → 7d
Bounds `(low, high)` passed down; strict chained `low < node.val < high`; left tightens high, right raises low; `-inf`/`inf` seed. Correctly rejects `[5,1,4,...]`. Held from Day 25. **O(n)/O(h).**

### 5. #199 Right Side View — ❌ RESET → 1d
BFS itself clean (`rightVal` overwritten each level → last node). But **two slips, both of which he got RIGHT on #102 the day before**: (a) **dropped the root-None guard** → `node.val` crash on an empty tree (B-4), and (b) **called space O(1)** — the deque holds a whole level → **O(n)** (M-005). Real decay, surfaced by a genuine spaced rep — exactly why we didn't waste reps re-drilling the just-done items. **O(n)/O(n).**

### 6. #146 LRU Cache — ❌ RESET → 1d (cold rebuild, 15:38)
Built the whole thing cold, and the **drilled parts HELD**: dict synced in every path (M-024), `addFront` all 4 pointers in a safe order (M-025), `remove` unlinks both, `self.` correct at **5 of 6** sites. The one miss: **`remove(lru)` instead of `self.remove(lru)`** in the eviction branch → `NameError`. **B-7 recurrence — 2nd day running (after #211 on Day 27).**

**Block 1 theme — every reset was ONE site missed on the final pass:** `curr`/`curr3` (#143), dropped guard (#199), missing `self.` (#146). The machinery is drilled and holds; the gap is a final read-through. **B-7 → re-escalated to drill-now.**

---

## Block 2 — BACKTRACKING taught from scratch (new pattern #12)

He was **"lost from the start"** → threw out the code and rebuilt fully concrete (rule 9, go slow):
1. **Listed all subsets of `[1,2]` by hand** — `[], [1], [2], [1,2]`.
2. **Reframed each as take/skip decisions** — `[1]` = "take 1, skip 2."
3. **Decision tree** — binary branch per element; leaves = answers.
4. **The choose → explore → un-choose skeleton**, hand-traced frame-by-frame (path grows `[]→[1]→[1,2]`, records, pops back).
He then **traced the skip-1 side himself correctly** → the mechanism landed.

### #78 Subsets — ✅ (derived by hand-trace)
```python
def subsets(self, nums):
    self.res = []; self.path = []
    def backtrack(i):
        if i == len(nums):
            self.res.append(self.path.copy()); return
        self.path.append(nums[i]); backtrack(i + 1); self.path.pop()   # take
        backtrack(i + 1)                                                # skip
    backtrack(0); return self.res
```
Two bugs, both self-fixed on a nudge: `stack()` → `[]`, and the skip branch `backtrack(i)` → `backtrack(i+1)`. **Complexity taught: O(n·2^n) time** (2^n subsets, each O(n) to copy) **/ O(n) space** (depth = n).

### #39 Combination Sum — taught with heavy scaffolding + the animator
His attempt tangled the state: used `self.total` with `+=` but **no undo** (`-=`), and the take branch used `backtrack(i+1)` — **losing the reuse**. Taught the clean template:
```python
def combinationSum(self, candidates, target):
    res, combo = [], []
    def backtrack(i, total):
        if total == target: res.append(combo.copy()); return
        if total > target or i == len(candidates): return
        combo.append(candidates[i])
        backtrack(i, total + candidates[i])   # TAKE — STAY on i (reuse)
        combo.pop()
        backtrack(i + 1, total)               # SKIP — i+1
    backtrack(0, 0); return res
```
**Two big ideas:** (1) carry `total` as a **parameter** → it auto-unwinds on return, no `-=`; (2) **reuse = TAKE stays on `i`**. Base cases: success (`==target`, records) split from overshoot (`>target`, discards).

**Built an interactive call-stack animator** (`backtracking-stack-animator` artifact) for `[2,3]`, target 4. Stepping through push/pop of frames is what unlocked **how a `return` unwinds** — it cascades up through frames with nothing left (the skip is their last line) and **halts at the first frame with work left** (a take-frame still owes its pop + skip). This finally made recursion unwinding concrete [INSIGHT].

**Complexity contrast (his question, well-caught):** Subsets O(n·2^n)/O(n) vs Combination Sum **O(N^(T/M+1))/O(T/M)** — because **reuse decouples depth from n** (deepest path = "take the smallest over and over" = target/smallest, unrelated to how many distinct candidates there are).

---

## The day's theme
Reconstruction is excellent; the loss is a **single site on the final pass** — the one habit worth building above all others now is a deliberate final read-through (every name real & owned, every guard present, every multi-site change complete).

## Wins
- **Recursion, his weakest area, moved** — derived Subsets by hand, and got from "lost from the start" to explaining stack-unwinding.
- #271 container bug cleared; #226 field-mutation held; #98 bounds held.

## Blockers after today
- **B-7 (self./ownership) → DRILL-NOW** (re-escalated, 2 days running). Micro-drill next 2–3 sessions.
- **M-027** (one site on final pass) — the through-line. B-4 (#199 guard) + M-005 (#199 BFS space) fired. M-028, M-026 watches.

## Times
#271 8:38 · #143 ~7:40 · #226 3:47 · #98 11:59 · #199 ~5:52 · #146 15:38.

## Spaced-review changes
Advanced: #271/#226/#98 → 7d. Reset 1d: #143/#199/#146. New 1d: #78/#39 (backtracking). The 5 deferred Day-27 items sit due Jul 23 (now properly spaced). Next: **Day 29 — Backtracking cont.** (#90 Subsets II / #40 Combination Sum II, or #46 Permutations).
