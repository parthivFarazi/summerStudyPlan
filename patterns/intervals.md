# Intervals

**Status:** learned Day 31 · extended Day 32 (#435, #252) · **all four clean Day 33** · **Mastery: 3/5** · Block B
*(3/5 and staying there on purpose. Day 33 returned #57 in 6:06, #435 in 4:50 and #252 in 2:13, all first-draft from a blank screen — but those are the four problems he was TAUGHT. Rehearsed performance is not mastery; 4/5 needs a novel interval problem cold. #253 is the test.)*

## In one line
Get the list sorted by **start**, then sweep left to right comparing each interval against **the one that's been growing** — merge into it, or put down a new one.

## Reach for it when
- Inputs are `[start, end]` ranges
- Merge / insert / count overlaps
- "Minimum rooms / max overlap" → sort + heap of ends
- Scheduling problems

---

## The primitive — memorise this, everything else is bookkeeping

For `[a, b]` and `[c, d]`:

```python
overlap = (b >= c) and (d >= a)
```

**Say it as a sentence:** *"I reach at least as far as you start, and you reach at least as far as I start."* Both must hold.

**How to derive it if you forget** *(this is the move worth keeping — Day 31)*: don't enumerate the ways two intervals **can** overlap — that's four clauses and four chances to typo. Enumerate the ways they **can't**. Two segments miss each other only if one is entirely left of the other, so there are exactly **two** cases:

```python
no_overlap = (b < c) or (d < a)
overlap    = not that  =  (b >= c) and (d >= a)
```

**`>=` not `>` — touching counts.** `[1,3]` and `[3,5]` merge into `[1,5]`, because returning them separately would share the point 3 and the output wouldn't be non-overlapping. Identical intervals also need `>=`.

> **The general lesson, beyond intervals:** when a condition has many positive cases, count the negative cases instead and negate. Fewer comparisons, fewer typos.

---

## Shape 1 — insert one interval into a sorted list (#57)

**Input guarantee:** already sorted by start **and** non-overlapping. So **no sort needed → `O(n)`.**

One pass. Every existing interval falls in exactly one of three buckets relative to `newInterval = [a,b]`, current = `[c,d]`:

| bucket | test | action |
|---|---|---|
| entirely **before** | `d < a` | append it, move on |
| **overlapping** | `b >= c and d >= a` | **don't append.** Grow: `newInterval = [min(a,c), max(b,d)]` |
| entirely **after** | `c > b` | append `newInterval` **first**, then this one and all the rest |

**Two traps:**
- **Ordering in the "after" bucket** — `newInterval` goes in *before* the current interval, or the output isn't sorted.
- **The terminal append.** If the loop ends without ever hitting "after," `newInterval` was never placed. Needs one unconditional append after the loop. *(The "before everything" case handles itself — the "after" branch fires on the very first interval.)*
- **If you use a flag instead of an early return, gate the branch with it** — otherwise the "after" branch re-appends `newInterval` once per remaining interval. *(Day 31 first-draft bug, self-found.)*

**Complexity:** `O(n)` time · `O(n)` output space, `O(1)` auxiliary.

---

## Shape 2 — merge a whole list into itself (#56)

**Input guarantee: NONE.** Not sorted, overlaps allowed. **That's the entire difference from #57** — and it costs you the sort.

**The representation is the insight:** there's no `newInterval` variable. The growing interval **is `answer[-1]`** — the last thing you put down. Appending does *not* finalise it; you reach back and stretch its right edge.

| step | current | `answer[-1]` | overlap? | action |
|---|---|---|---|---|
| 1 | `[1,3]` | *empty* | — | guard: just append |
| 2 | `[2,6]` | `[1,3]` | yes | stretch to `[1,6]` — `[2,6]` never enters `answer` |
| 3 | `[8,10]` | `[1,6]` | no | append; it becomes the new `answer[-1]` |
| 4 | `[15,18]` | `[8,10]` | no | append |

**Compare against `answer[-1]`, NOT the previous interval in the input.** On `[[1,10],[2,3],[4,5]]`, comparing `[4,5]` to the previous *input* interval `[2,3]` says "no overlap" and wrongly appends `[4,5]` — but `[1,10]` had already absorbed `[2,3]`, and `[4,5]` sits inside it. `answer[-1]` carries the accumulated end; the previous input interval doesn't.

**The sort buys you "the left edge never moves."** Sorted by start ⇒ `a <= c` always ⇒ `min(a,c)` is always just `a`. Only the right edge needs `max`.

`intervals.sort()` with no key is correct — Python compares lists element-wise, so it sorts by start (ties broken by end, harmless). Be able to *say* that rather than looking lucky. `sort(key=lambda x: x[0])` is the explicit equivalent.

**Complexity:** `O(n log n)` time — **the sort dominates.** Space `O(n)` either way: `O(n)` output, and **`O(n)` auxiliary for the sort itself** — Python's Timsort is not free.

> **Bank this:** when you add a sort, add its **space** as well as its time. Stating `O(1)` space next to an `O(n log n)` sort is the classic miss. *(Day 31.)*

---

## Complexity summary

| Problem | Time | Space | Why |
|---|---|---|---|
| #57 Insert Interval | `O(n)` | `O(n)` out / `O(1)` aux | input pre-sorted — no sort |
| #56 Merge Intervals | `O(n log n)` | `O(n)` | no guarantees — must sort; Timsort is `O(n)` aux |

**The #57 vs #56 contrast is the whole pattern:** identical sweep, and the only difference is what the input promised you.

## Your gotchas
- **Read the guarantees before deciding the complexity.** On Day 31 I misread #56 as sorted because the example *happened* to be sorted by start. The statement gives no promise. Check the statement, not the example.
- **Vocabulary:** "the previous interval" is ambiguous and the wrong reading of it is a real bug. Say **"the last one in the answer"** or **"the growing one."**
- Guard the empty-`answer` case before touching `answer[-1]`.
- `answer[-1] = temp` replaces `answer.pop()` + `answer.append(temp)` — one site instead of two (M-027).

---

## Shape 3 — greedy: keep the most, remove the fewest (#435, #252) · *Day 32*

**These stop being "sweep and merge" and become GREEDY.** Named form: **interval scheduling / activity selection.**

> Sort so the best candidate comes first, then sweep once taking anything that doesn't conflict with what you've already taken. **Never look back, never reconsider.**

Two moving parts, always: **a sort key that makes "best" mean "first"**, and **one variable holding the last thing you committed to.**

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
        if b > c:            # conflicts with what we KEPT
            count += 1       # drop current; ref UNCHANGED
        else:
            ref = interval   # keep it; it becomes the reference
return count
```

**Sort by END, not start — and know why.** Keep the interval that frees the timeline soonest. Sorting by start breaks it: the earliest-starting interval might run to 100 and block everything behind it.

**The criterion is "ends later", not "overlaps more."** Sweeping left to right you can't see the future, so "overlaps with the rest" is unusable. **"Ends later" is a purely LOCAL check that predicts the global property.** That's the heart of every greedy: *when a global property is expensive to check, find a local one that predicts it.*

**⚠️ The bug that got written first, twice now:** comparing against the interval **physically adjacent** in the array instead of the last one you **KEPT**. Fails on `[[1,3],[2,4],[3,5]]` — gives 2, should be 1, because `[2,4]` is used as a comparison partner and then deleted. **Identical to #56's `answer[-1]` bug.** Rule: **the reference is what survived, never what's next to you.**

**#435 asks HOW MANY, not WHICH.** Nothing gets removed — you just count. That kills the `pop()`-in-a-loop idea (`O(n²)`, plus mutating while iterating skips elements) before it starts.

**#252 Meeting Rooms** is the same sweep, returning `False` on the first conflict instead of counting. Sorting by end works here too: if no adjacent-by-end pair overlaps, no non-adjacent pair can either.

> **⚠️ Day 33 — know what you got away with on #252.** In **#435** the sort-by-END is load-bearing: sort by start and the answer is wrong. In **#252 it is not** — sorting by start works equally well *(verified against brute force on 300,000 random cases under LeetCode's `start < end` constraint)*.
>
> **Why the difference: #435 SKIPS intervals, #252 never does.** In #435 you drop a conflicting interval and keep sweeping, so `ref` diverges from "the previous element in the array" — and that gap is the bug that has bitten twice. **#252 returns `False` on the first conflict**, so nothing is ever skipped, so `ref` *is* always the previous element and the trap cannot fire.
>
> **Do not file this as "sort by end for interval problems."** File it as: **the sort key exists to make the greedy choice come first — and if you never skip, there is no greedy choice to protect.**
>
> *(Degenerate zero-length meetings would break the sort-by-end version on ties; LeetCode guarantees `start < end`, so it does not arise. Worth knowing the guarantee is doing work for you.)*

### Greedy vs sliding window *(asked Day 32)*

| | Sliding window | Greedy |
|---|---|---|
| State is about | a **range** (`left`, `right`) | a **commitment** (last thing taken) |
| Do things leave? | **Yes** — `left` advances and state is removed | **No** — every decision is final |
| Examples | #3, #424 | #11, #121, #435, #252 |

**The tell: does anything ever get removed from consideration after being added?** Yes → window. Every decision final → greedy.

---

## Complexity summary

| Problem | Time | Space | Why |
|---|---|---|---|
| #57 Insert Interval | `O(n)` | `O(n)` out / `O(1)` aux | input pre-sorted — no sort |
| #56 Merge Intervals | `O(n log n)` | `O(n)` | must sort; Timsort is `O(n)` aux |
| #435 Non-overlapping | `O(n log n)` | `O(n)` | sort by end; output is one integer |
| #252 Meeting Rooms | `O(n log n)` | `O(n)` | sort; output is one boolean |

## Method names — get them right
`insert` · `merge` · `eraseOverlapIntervals` · `canAttendMeetings`. *(Renamed all of these on Day 32 — the thing already has a name.)*

## Still to come
#253 Meeting Rooms II (heap of end times — minimum rooms) · #1851 Minimum Interval to Include Each Query.
