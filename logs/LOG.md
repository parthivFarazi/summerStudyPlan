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

<!-- Append Day 10+ below. Format: ## Day N — YYYY-MM-DD — topic / problems / [tags] -->
