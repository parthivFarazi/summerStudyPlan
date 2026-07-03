# Study Log — event layer (append-only)

> One dated entry per session. Never edited after writing. Keep struggles, dead ends, and confusion *in* — they're the most valuable data. Tags: `[STRUGGLE] [INSIGHT] [NEEDS_RECALL]`. New entries go at the **bottom**.

---

## Day 1 — 2026-06-19 — Python on-ramp + Big-O
Source: NeetCode (Arrays & Hashing). Two Sum (#1), Contains Duplicate (#217).
Hashmap/set for O(1) lookup [INSIGHT] — a dict kills the nested-loop scan. Slips: `range(x)` vs `range(len(x))`, and `nums.add` vs `seen.add` [STRUGGLE].

## Day 2 — 2026-06-20 — Frequency counting + group-by-key
Valid Anagram (#242), Group Anagrams (#49) — first Medium, reproduced clean from memory [INSIGHT]. Group by a canonical key (sorted string / char-count).

## Day 3 — 2026-06-20 — Bucket sort
Top K Frequent (#347) via bucket sort; derived time + space O(n) yourself [INSIGHT]. Got overloaded with Python idioms mid-session [STRUGGLE] → set the **pre-teach rule** (one new concept in isolation first). Product of Array Except Self deferred to Day 4.

## Day 4 — 2026-06-22 — Prefix/suffix + first spaced re-solves
Reproduced bucket sort cold (re-solve = method working). Product of Array Except Self (#238) via prefix/suffix products, incl. the O(1)-extra-space upgrade; derived complexity yourself. Slips: forgot `return` [STRUGGLE]; `for item in list` ordering.

## Day 5 — 2026-06-24 — Two Pointers
Taught `while`, `elif`. Palindrome + Two Sum II (#167, sorted). Reproduced the O(1) Product solution cold. Spotted that the basic palindrome fails on real input → extended to full Valid Palindrome (#125) with `.lower()`/`.isalnum()`. Slips: guessed O(1) space — it's O(n) when you build a cleaned string [STRUGGLE]; `.append[x]` brackets.

## Day 6 — 2026-06-26 — First interleaved review + greedy
Interleaved (unlabeled): Contains Duplicate, Two Sum, Product — all correct; correctly chose hashmap for *unsorted* Two Sum [INSIGHT]. Container With Most Water (#11) — nailed the "move the shorter wall" greedy insight yourself. Slips: skipped verbalizing the pattern before coding; used `i`/`j` instead of `left`/`right` [STRUGGLE].

## Day 7 — 2026-06-26 — Sliding Window (running-state), start of Week 2
Best Time to Buy/Sell Stock (#121). First attempt over-engineered (4 vars + time guards, buggy) → reframed to running-min + best-profit, 2 vars [INSIGHT]: keep the minimum necessary state. Verbalized patterns in warm-up ✅. Dropped the anagram length check, re-added [STRUGGLE].

## Day 8 — 2026-06-28 — Sliding Window (variable-size)
Longest Substring Without Repeating (#3) through self-driven iteration: clear-set (wrong) → shrink-from-left → +maxLen (correct). Taught **amortized analysis** (forward-only pointer ⇒ O(n), not O(n²)) [INSIGHT]. Slips: carried `k log k` from Group Anagrams (no sort here) [STRUGGLE]; under-read the spec ("alphanumeric only"). Spaced review caught real decay on Valid Palindrome (had dropped cleaning + reintroduced an infinite loop) [NEEDS_RECALL] → reset to 1d. Good: correctly called Valid Palindrome O(n) space — the Day-5 correction stuck.

## Day 9 — 2026-06-29 — Binary Search (new) · #704, #74
Block 1 reviews: Longest Substring (#3) **PASS** with unprompted amortized O(n) reasoning [INSIGHT]; Valid Palindrome (#125) **FAIL** again — compared `s` instead of the cleaned string [STRUGGLE][NEEDS_RECALL] → reset to 1d (root cause: wrong-variable reference, **M-004 now 2×**). Binary Search (#704): inverted the discard direction first (**M-012**), fixed after reasoning *small→right / big→left*. Search a 2D Matrix (#74): correct first try via the **virtual-flattened index** (`mid//cols`, `mid%cols`), complexity stated unprompted [INSIGHT]. Hit the **2-new/day sprint pace**.

## Day 10 — 2026-06-30 — Binary search ON THE ANSWER · Koko #875
Block 1 (5 re-solves): #704, #74, #347, #121 all **PASS** clean; **#125 Valid Palindrome** — the recurring wrong-variable bug (M-004) **did NOT recur** (pre-empt worked ✅), but a fresh typo `.isalum`→`.isalnum` keeps it red [NEEDS_RECALL]. **Koko (#875):** learned to search the *answer space* — speed `[1, max(piles)]`, hours = Σ`ceil(p/k)`, monotonic. Took 3 tries on the boundary logic: returned only on `==` → `None` on an early finish; then returned on `==` too eagerly → wrong on `[21],h=3` (got 8, answer 7); fixed with `h >= hours` → record + shrink + return `result` [INSIGHT] (**M-013**: never return on an exact match in a find-minimum search). All 6 test cases pass. O(n·log k)/O(1). (Day-10 = single new problem per roadmap.)

## Day 11 — 2026-07-01 — Find Min in Rotated Sorted Array (#153) + variable-audit drill
Block 1 (4 due): first pass had TWO wrong-variable slips — #125 `strs` vs `s`, #167 `nums` vs `numbers` (#875 Koko + #11 Container clean). That's **M-004 recurrence 3 → escalated to BLOCKERS**; introduced the **"variable audit before submit"** drill → fixed both instantly → all 4 clean, and **#125 finally green** after 5 sessions [INSIGHT]. #153: derived the `mid` vs `nums[right]` invariant himself; tripped on `while left <= right` + `right = mid` → **infinite loop** (**M-014**), fixed with strict `<` + `return nums[left]` [INSIGHT]. Verified 7/7. O(log n)/O(1). Also retired the roadmap's stale review column — reviews now come only from `QUEUE.md`.

## Day 12 — 2026-07-02 — Interleave day (#238, #3, #153) + variable-audit drill
Mixed unlabeled set, name-the-pattern-first; no new problem. Warm-up 3/3 reflexes clean (`.append()`, converging `<`, record-and-shrink). **#238 Product** ✅ correct, O(n)/O(1)-extra, prefix/suffix — but named it "iteration of lists" → corrected to **prefix & suffix products**; audit caught `appened`→`append` (M-004/B-1, needed a nudge) [STRUGGLE]. **#3 Longest Substring** ✅ correct, unprompted amortized O(n), audit clean [INSIGHT]. **#153 Find Min Rotated** — correct invariant + both loop reflexes, but regressed from Day 11's `return nums[left]` to tracking `answer = 0` → returned 0 on `[2,1]` and single-element `[5]` (**M-015**); found it by tracing, self-fixed back to `return nums[left]` [STRUGGLE][NEEDS_RECALL] → **reset to 1d**. Keeper: in a converging search the exit index IS the answer — no tracked candidate. Pattern names 2/3 crisp.

## Day 13 — 2026-07-03 — Binary-search reviews + Search in Rotated (#33) + first Stack (#20)
Block 1 (3 due, all **PASS**): #704 ✅ (slip: `for`→`while`, M-016, self-owned); #74 ✅ clean (flattened index); **#153 ✅ retest of the Day-12 fail — `return nums[left]`, no tracked answer; M-015 lesson stuck** [INSIGHT]. Block 2 new: **#33 Search in Rotated** — hardest yet; built which-half-is-sorted + the nested range-test himself [INSIGHT], but inverted ALL FOUR pointer updates (**M-012 recurrence 2**) → fixed on "pointer = opposite wall from direction" [STRUGGLE]; O(log n)/O(1). **#20 Valid Parentheses — first STACK** (pre-taught LIFO list): 3 bugs ironed out — empty-arg `append`, dict looked up the popped opening not the current closing, and a bare `return True` (band-aided with `len(s)<2` before landing on `return len(stack)==0`) [STRUGGLE]; O(n)/O(n). New pattern file: `stack.md`. No wrong-*name* slip today; B-1 audit still active.

<!-- Append Day 14+ below. Format: ## Day N — YYYY-MM-DD — topic / problems / [tags] -->
