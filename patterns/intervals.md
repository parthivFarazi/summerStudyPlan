# Intervals

**Status:** learned Day 31 (2026-07-26) · **Mastery: 2/5** · Block B
*(2/5 = derived and implemented both shapes correctly, but needed heavy guidance on the primitive and the sweep. Bump on the 1d/3d reps.)*

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

## Still to come
#435 Non-overlapping Intervals (greedy by **end**) · #252/#253 Meeting Rooms (sort + overlap check / heap of ends) — Day 32.
