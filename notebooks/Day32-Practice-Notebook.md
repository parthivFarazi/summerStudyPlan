# Day 32 — Practice Notebook
**Monday, 2026-07-27** · Week 6 · **Reviews (3/6) + Intervals continued: #435, #252**

**Times:** #79 **10:06** · #39 **9:33** · #57 **9:57** · #56 **7:20** · #435 *~30 min (est.)* · #252 *~5–10 min (est.)*

---

## Scoreboard

| Target | Result |
|---|---|
| Block 1 reviews | **3 / 6** — #56, #704, #33 pass · #79, #39, #57 reset |
| **2 new problems** (#435, #252) | ✅ both built |
| Complexity before code | ✅ every problem |
| Scan run before submit | ❌ — see *The scan didn't run* |
| 30-min Block 1 box | ❌ blown (36:56 of solve time) → #146 moved to Jul 28 |

---

# Coaching change — rule 12

Opened the session by posting the entire day: every block, both new problems, the whole review list. He stopped it:

> *"Don't just dump. You are supposed to be my teacher. Let's go with it one by one."*

**Correct, and now `COACHING.md` rule 12.** The run-sheet is for pre-session setup, not the opening message. One thing, then wait. He should only ever see what he's working on right now. **Dumping the plan is a form of spoon-feeding** — it hands him the map instead of making him walk it.

---

# Block 0 — warm-up

Asked for the overlap primitive cold. He didn't recognise the *name* ("what do you mean by overlap condition?"), but once the question was concrete — *two intervals `[a,b]` and `[c,d]`, one boolean test* — it came straight back as `c <= b and a <= d`. Same test as yesterday with both comparisons flipped.

**The label was missing; the knowledge wasn't.** Same shape as M-029.

---

# Block 1 — Reviews (3/6)

## #79 Word Search — ❌ FAIL · 10:06

Complexity `O(m·n·4^L)` / `O(L)` auxiliary, with the convention, unprompted.

**Both Day-30 nudges held:** all four directions present (Day 30 dropped **left**), and `dfs(r, c, 0)` inside the loop (Day 30 had `dfs(0,0,0)`). Base-case order correct too — `i == len(word)` **before** the bounds check, which matters: the successful match lands at `dfs(3,2,5)`, out of bounds, and returns `True` only because the length check fires first.

**Fail cause — he peeked at his notes for the mark/un-mark idiom, and volunteered that.** [STRUGGLE] Nobody would have caught it; the code was correct. Self-reporting a lapse is worth more to the system than the pass would have been.

```python
temp = board[row][col]
board[row][col] = "#"     # choose
...                       # recurse 4 directions
board[row][col] = temp    # un-choose
```

**The binding that should stop this needing notes:** that pair **is** choose/un-choose — the same `path.append()` / `path.pop()` he owns cold in Subsets and Permutations. Grid DFS isn't a fifth mechanism; it's the same skeleton where the board *is* the path, and `temp` exists only because a cell holds a letter that has to be given back, whereas a list just pops.

Name: the method is `exist`, not `wordSearch`.

## #39 Combination Sum — ❌ FAIL · 9:33

Complexity `O(n^(T/M+1))` / `O(T/M)` — correct. **Flagged low confidence in advance and said he'd report if stuck** — a better move than yesterday's confirm-seeking.

**The bug — a prune written backwards:**

```python
if i == len(candidates) or target > total:   # ✗ backwards
    return
```

Intent: *stop when I've overshot.* What it says: *stop when I haven't got there yet.* True at the root call, so `backtrack(0, 0)` returned instantly and `res` came back **empty**. Fixed to `total > target`.

**Same family as B-6 (target-first in BST): knows which two things to compare, puts them the wrong way round.**

> **New check, say it out loud:** *"This prune kills the branch when ___."* Fill the blank in **English** first, then read the code and confirm it says the same thing. Here: "when the running total has gone past target" → `total > target`.

Fail because I pointed at the specific line and expression. Method name `combinationSum` was **correct**.

## #57 Insert Interval — ❌ FAIL · 9:57

**The whole loop was right. The post-loop `if not isInserted: answer.append(newInterval)` was gone.**

His own comment said *"Make sure to have the isInserted boolean."* He declared it, set it, checked it inside the loop — and never used it for the one thing it exists for. On `[[1,3],[6,9]]` + `[10,12]`, `newInterval` vanishes.

**This is M-026 (dropped terminal line), and it's item two on his own scan** — *"Terminal line/mark written?"*

> **So the scan didn't fail. It didn't run.** Saying it and running it against the code in front of you are different acts, and the difference is three failures today.

Still owes the space convention: `O(1)` auxiliary, `O(n)` output.

## #56 Merge Intervals — ✅ PASS · 7:20 *(down from 26:24)*

Traced on five cases including unsorted input, full containment, touching, empty. Correct.

```python
intervals.sort(key=lambda x: x[0])
answer = []
for interval in intervals:
    if len(answer) == 0:
        answer.append(interval)
    else:
        c, d = interval
        a, b = answer[-1]
        if c > b:
            answer.append(interval)
        else:
            answer[-1] = [a, max(b, d)]
return answer
```

**Both of yesterday's corrections applied unprompted:** [INSIGHT]

- `answer[-1] = [...]` instead of `pop()` + `append()` — one site, not two.
- **`[a, ...]` instead of `min(a, c)`** — and not just deleted, *understood*: the sort guarantees the left edge never moves. That was a question he didn't answer yesterday.

Name: `merge`, not `mergeInterval`.

## 🗣 #704 Binary Search — ✅ PASS → 21d

`left <= right`, `mid = (left+right)//2`, both shifts ±1, both complexities. Whole thing in 30 seconds.

Slip: *"return the mid value cause that is the index."* **`mid` IS the index; the value is `nums[mid]`.** B-5 family, container vs contents.

## 🗣 #33 Search in Rotated Sorted Array — ✅ PASS → 21d

Had the key insight — **one half is always sorted; work out which, then check whether the target lies inside it** — plus `left <= right` and the `-1` fallthrough.

For the next full solve: he said *"if `nums[left]` is **less than** `nums[mid]`."* It needs `<=`. With two elements, `left` and `mid` are the same index and strict `<` sends you down the wrong branch.

## Box enforcement

Four full solves = **36:56 of solve time**, over the hard 30-minute box. **#146 LRU Cache → Tue Jul 28**, dated in the queue, not rolled vaguely. Beyond the rule, the real reason: **his first one-draft deserves a clean run**, not the tail of an overrun block after three failures.

---

# Block 2 — NEW: #435 and #252

## #435 Non-overlapping Intervals — built *(~30 min est.)*

**Two of yesterday's lessons applied without prompting:** [INSIGHT]

- **Read the spec, not the example.** Saw that `[1,2]` and `[2,3]` touching is *not* an overlap here, so the comparison needs strict `>`. That's the exact mistake he made yesterday on #56's guarantees.
- **`O(n)` space with the sort as the reason** — M-032 from yesterday.

### Deriving the greedy

First instinct: *"if it overlaps, get rid of it"* — but **which one?** Given `[[1,10],[2,3],[4,5]]` to work by hand, he got that removing `[1,10]` is better, and offered two reasons:

1. *"because 10 > 3"* — **the criterion.**
2. *"because it overlaps with the rest"* — **a consequence, not a criterion.** Sweeping left to right you only see two intervals at a time; you can't know how many future ones something will hit.

> **"Ends later" is a purely local check that stands in for "will block more things later."** An interval reaching to 10 shuts out everything starting before 10; one reaching to 3 shuts out almost nothing. **When a global property is expensive to check, find a local one that predicts it.** That's the shape of every greedy.

### The `pop` detour that paid off

He asked whether `alist.pop(i)` removes by index (yes; also `pop()` = last, `del a[i]` = by index no return, `a.remove(v)` = **by value**). Flagged the two hazards — `pop` is `O(n)` so in a loop it's `O(n²)`, and mutating while iterating skips elements. From that he got there himself:

> *"Oh I don't even need to get rid of them, I just have to keep a count."*

**The problem asks how many, not which ones.** Nothing to mutate, no shifting indices, no `O(n²)`.

### 🔴 The reference bug — and MY error

His first version compared **physically adjacent** pairs after sorting by end. It failed on:

```
[[1,3], [2,4], [3,5]]      →  his: 2      correct: 1
```

At `i=2`, `[3,5]` was compared against `[2,4]` — **which was about to be deleted.** Once it's gone, `[3,5]`'s real neighbour is `[1,3]`, and those merely touch.

> **[FEEDBACK] This one is mine.** I told him the backward sweep was sound, after checking two examples and giving a plausible-but-insufficient argument ("if adjacent don't overlap, non-adjacent can't"). **Two passing tests plus a nice-sounding reason is exactly what I'd spent two days telling him isn't verification.** Own it, log it, and remember that the coach is not exempt from the rule.

**The fix is a thing he already owns:** compare against **the last one you decided to KEEP**, not the one physically next to you. Identical to #56, where the reference had to be `answer[-1]` — and where the counter-example was also a containment case. Here it's one variable, not a list, because you only need the last kept interval.

He flipped to a **forward** sweep unprompted:

```python
intervals.sort(key=lambda x: x[1])      # sort by END
count = 0
ref = []

for interval in intervals:
    if len(ref) == 0:
        ref = interval
    else:
        c, d = interval
        a, b = ref
        if b > c:              # overlaps what we kept
            count += 1         # remove current; ref UNCHANGED
        else:
            ref = interval     # keep it; it becomes the reference
return count
```

Verified on six cases. `O(n log n)` / `O(n)`. Name: `eraseOverlapIntervals`.

### The pattern, named

**Greedy — specifically interval scheduling / activity selection.**

> Sort so the best candidate comes first, then sweep once taking anything that doesn't conflict with what you've already taken. Never look back, never reconsider.

Two moving parts, always: **a sort key that makes "best" mean "first"**, and **one variable holding what you last committed to.**

He asked whether he'd met this before. He had, unlabelled:

- **#11 Container With Most Water** — move the shorter wall, never revisit.
- **#121 Best Time to Buy/Sell** — a running minimum summarising everything behind you.
- **#56 Merge Intervals** — not greedy (nothing is discarded), but the *reference* mechanic is identical, which is why the same bug appeared in both.

Greedy arrives as a named block **Aug 6–10** (#53, #55, #134, #763).

**And: a greedy needs a sort that makes the locally-best choice also globally safe.** Here that's sorting by **end** — keep the interval that frees the timeline soonest. Sorting by start breaks it: the earliest-starting interval might run to 100 and block everything.

### Greedy vs sliding window *(he asked)*

**Sliding window keeps a live range** — `left` and `right` both move, state is added when `right` advances and **removed** when `left` advances. Things *leave* the window (#3, #424).

**Greedy has no window.** One pointer, forward only, nothing un-counted, one number summarising every decision behind you, every choice final.

> **The tell:** *does anything ever get removed from consideration after being added?* Yes → probably a window. Every decision final → greedy. Both are one pass with `O(n)` state, but **a window is state about a range; a greedy is state about a commitment.**

## #252 Meeting Rooms — built *(~5–10 min est.)*

```python
intervals.sort(key=lambda x: x[1])
ref = []
for interval in intervals:
    if len(ref) == 0:
        ref = interval
    else:
        c, d = interval
        a, b = ref
        if b > c:
            return False
        else:
            ref = interval
return True
```

Verified on the example, a clean pair, touching endpoints (`[[1,5],[5,10]]` → `True`, correct), a single meeting, and empty. `O(n log n)` / `O(n)`.

Sorting by **end** works here too: if no adjacent-by-end pair overlaps, no non-adjacent pair can either.

**Asked whether a `ref` was needed at all** (nothing is removed — the answer is no). His reasoning was sound: a `ref` lets him write `for interval in intervals` instead of `range(len(intervals) - 1)` with `intervals[i+1]`, avoiding an index bound. **Given B-2 is his range/len history, trading a variable for an off-by-one is a good trade, not a lazy one.** Mentioned `zip(intervals, intervals[1:])` as the idiomatic alternative — deliberately not taught today, end of a long session.

---

# The honest read

**All four full solves were FIRST retrievals — problems never reviewed before. Three failed. The one that passed was #56 — the one he struggled with hardest yesterday.** [INSIGHT]

#56 cost 26:24 and three separate explanations to get `answer[-1]` to land. Today: clean, 7:20, both corrections applied unprompted. **#57 went relatively smoothly yesterday and today the terminal append was gone.**

> **Desirable difficulty, in his own data.** The material that felt worst yesterday is the material that stuck. Smooth sessions feel better and retain worse. Worth telling him again when a session feels bad.

**Every failure was completeness, not comprehension** — a missing terminal line, a reversed comparison, an un-recalled idiom. Consistent with the entire log.

**The scan is now the bottleneck, and it's a behaviour not a knowledge gap.** M-026 is item two on his own list and it still got through. **Saying the scan ≠ running the scan against the code in front of you.**

**Improving, and worth naming:** he tested his own backward sweep when asked rather than asking me to confirm (M-030 improving); reached the counting insight himself off the `pop` hazard; flipped to a forward sweep unprompted; self-reported the #79 peek; and told me to stop dumping.

**Still slipping:** method names four sessions running (`exist`→`wordSearch`, `merge`→`mergeInterval`, `insert`→`insertInterval`, `eraseOverlapIntervals`→missing), *"the mid value... that is the index"*, and no stopwatch on new problems for the third session.

---

# Banked rules

1. **Grid DFS's mark/un-mark IS choose/un-choose** — same skeleton, board as the path.
2. **Say what a prune kills, in English, before writing it.** *"Kills the branch when total has gone past target"* → `total > target`.
3. **Compare against the last thing you KEPT**, never the thing physically next to you. (#56 and #435, same bug.)
4. **Greedy = sort so best-is-first + one variable for the last commitment.** Never look back.
5. **A local property that predicts a global one is the heart of a greedy.** "Ends soonest" predicts "blocks least."
6. **Window vs greedy:** does anything ever leave? Window = state about a range; greedy = state about a commitment.
7. **Two passing tests is not a proof** — for him *and* for me.
8. **Saying the scan is not running the scan.**

# Next session — Day 33 (Tue Jul 28) · Graphs, HEAVY ⇒ Block 2 runs first

**Block 2 first (fresh brain):** **Graphs — #200 Number of Islands, #133 Clone Graph.** First contact with a new pattern; budget the pre-teach generously.
**Block 1 (30 min, full solves only):** **#79 · #39 · #57** (resets) · **#435 · #252** (1d). Five full solves is the entire box — every one-draft and verbal moved off Jul 28 to keep it honest.
