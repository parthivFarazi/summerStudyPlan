# LeetCode Roadmap — Front-Loaded for the Aug 20 Pivot

*Projected from your real progress through Day 8 (Jun 28). Heavy learning is pulled into the summer; fall is maintenance. Built on [FAANG-Prep-Plan](./FAANG-Prep-Plan.md) + [Learning-Science Playbook](./Learning-Science-Playbook.md).*

## The Aug 20 pivot (read first)

Fall semester starts **Aug 20** and your time collapses. New-pattern learning is the cognitively expensive part, so it **all gets front-loaded into the summer**; once classes start you shift to low-effort maintenance while you interview.

**The hard truth about pace:** at your current ~1 problem/day you would *not* finish even the core before Aug 20. The sprint below assumes you **~double to 2/day, 6 days a week** — which is realistic *because it's summer and you have the hours now.* This is the single most important change.

| | Summer Sprint (now → Aug 19) | Fall Maintenance (Aug 20 →) |
|---|---|---|
| Pace | **2 new/day, 6 days/wk** (push 7 when you can) | ~2–3 new/**week** |
| Focus | Acquire every pattern + start depth | Spaced review, mocks, pick off Hards |
| Why | You have time + max bandwidth | Classes + live interviews eat the day |

**What that buys you by Aug 20:** all **66 core patterns** done + ~**13 depth** problems. The remaining ~36 (mostly the **Hards + weighted-graph algorithms**) move to fall — which is correct anyway: Hards land better on a solid base, and the +21-day spaced reviews of your August problems naturally fall across September, so fall review runs itself.

> **Accelerators if you want more margin:** add the 7th day (~+6 problems/wk), or push 3/day on easy clusters (linked-list/tree/bit-manip basics). Every extra summer rep is one you don't have to find during midterms.

---

## How to read each day

- **Block 1 — Review (~10 min):** re-solve the *due* problems cold. ⚠️ **The specific "Block 1 — Review" problems named in the daily tables below are a stale Jun-28 projection — do NOT use them.** Always pull the actual due items from the live **`review/QUEUE.md`** (the single source of truth; it shifts with every pass/fail, so it's the only accurate schedule). Nothing is ever skipped — the ladder resurfaces every problem on its own timer. If none are due, free-pick your weakest.
- **Block 2 — New (~40–60 min in sprint):** the day's new problem(s). Timer on, narrate aloud, then close everything and re-implement from scratch.
- **Interleave day** (every 6th session): mixed *unlabeled* set — trains pattern-spotting. **Mock day** (from Aug): add a timed think-aloud round.

---

## Days 1–8 — completed ✅ (the foundation, before the sprint)

These pre-sprint days built the base patterns + Big-O fluency. Full write-ups live in [`notebooks/`](../notebooks/).

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 1 | Jun 19 | — (first day) | **Arrays & Hashing** — Two Sum (#1, E) · Contains Duplicate (#217, E) | `dict`/`set`; `range(len(x))`; `return` vs `print` | O(1) hash lookup; O(n) |
| 2 | Jun 20 | Two Sum; Contains Duplicate | **Arrays & Hashing** — Valid Anagram (#242, E) · Group Anagrams (#49, M) | `Counter`; sorted-string / char-count key | O(n); group-by-key |
| 3 | Jun 20 | Anagrams | **Arrays & Hashing** — Top K Frequent (#347, M) | bucket sort (list of buckets) | O(n) time + space (derived it himself) |
| 4 | Jun 22 | Bucket sort (cold) | **Arrays & Hashing** — Product of Array Except Self (#238, M) | prefix/suffix passes | O(n) time, O(1) extra |
| 5 | Jun 24 | Product (cold) | **Two Pointers** — Valid Palindrome (#125, E) · Two Sum II (#167, M) | `while`/`elif`; `.lower()`/`.isalnum()` | O(n); O(n) space when cleaning a string |
| 6 | Jun 26 | Interleave: Contains Dup · Two Sum · Product | **Two Pointers** — Container With Most Water (#11, M) | `left`/`right` pointers; move-the-shorter-wall | O(n) greedy |
| 7 | Jun 26 | Warm-up retrieval | **Sliding Window** — Best Time to Buy/Sell (#121, E) | running-min + best-profit (2 vars) | O(n) |
| 8 | Jun 28 | Valid Palindrome (decay caught) | **Sliding Window** — Longest Substring No Repeat (#3, M) | set + shrink-from-left | O(n) amortized |

> **Currently:** **Day 21 ✅ done (Jul 13)** — recursion taught from scratch + first Trees (#226, #104). **Day 22 (Jul 14) is next.** ⚠️ **LRU Cache (#146) is rescheduled to Day 24 (Jul 16)** — see the Week 3 note.

---

# PART 1 — Summer Sprint  ·  Day 9 → Aug 19

*6 days/week (rest Sundays). Dates are real; Day numbers are the backbone if you shift a day.*

### Sprint Week 1 · Jun 29–Jul 4  (Day 9–14)
*Focus: Binary Search, Stack*

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 9 | Jun 29 | Valid Anagram; Group Anagrams (+1) | **Binary Search** — Binary Search (#704, E)<br>**Binary Search** — Search a 2D Matrix (#74, M) | while left<=right; mid=(l+r)//2<br>2D index matrix[r][c]; divmod | O(log n) — halving intuition<br>O(log(m·n)) |
| 10 | Jun 30 | Top K Frequent; Best Time to Buy/Sell | **Binary Search** — Koko Eating Bananas (#875, M) | math.ceil; helper def | Binary search on the ANSWER |
| 11 | Jul 1 | Product of Array Except Self; Longest Substring No Repeat | **Binary Search** — Find Min in Rotated Array (#153, M) | compare mid vs right | O(log n) on rotated invariant |
| 12 | Jul 2 | **Interleave** — mixed unlabeled set | — | name the *pattern* first | state complexity unprompted |
| 13 | Jul 3 | Container With Most Water; Koko Eating Bananas | **Binary Search** — Search in Rotated Array (#33, M)<br>**Stack** — Valid Parentheses (#20, E) | compound and/or conditions<br>list as stack .append/.pop; pair dict | O(log n)<br>O(n) time, O(n) stack space |
| 14 | Jul 4 | Best Time to Buy/Sell; Find Min in Rotated Array | **Stack** — Min Stack (#155, M) | class w/ two lists; tuples | O(1) per op |

### Sprint Week 2 · Jul 6–Jul 11  (Day 15–20)
*Focus: Stack, Two Pointers, Sliding Window, Arrays & Hashing, Linked List*

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 15 | Jul 6 | Longest Substring No Repeat | **Stack** — Eval Reverse Polish Notation (#150, M)<br>**Stack** — Daily Temperatures (#739, M) | int() cast; negatives<br>store INDICES on stack | O(n)<br>Monotonic stack → amortized O(n) |
| 16 | Jul 7 | Binary Search; Search a 2D Matrix (+2) | **Two Pointers** — 3Sum (#15, M)<br>**Sliding Window** — Longest Repeating Char Replace (#424, M) | sort + skip duplicates; nested 2-ptr<br>Counter; track max freq | O(n²)<br>Window-validity O(n) |
| 17 | Jul 8 | Koko Eating Bananas; Min Stack | **Arrays & Hashing** — Longest Consecutive Sequence (#128, M)<br>**Arrays & Hashing** — Encode and Decode Strings (#271, M) | set membership; only-start check<br>length-prefix encoding | Why it's O(n) not O(n²)<br>O(n) |
| 18 | Jul 9 | **Interleave** — mixed unlabeled set | — | name the *pattern* first | state complexity unprompted |
| 19 | Jul 10 | 3Sum; Longest Repeating Char Replace | **Linked List** — Reverse Linked List (#206, E)<br>**Linked List** — Merge Two Sorted Lists (#21, E)<br>**Linked List** — Linked List Cycle (#141, E) | ListNode; prev/curr/next reassign<br>dummy-node pattern<br>fast/slow pointers | O(n) O(1); iter vs rec<br>O(n+m)<br>Floyd's, O(n) O(1) |
| 20 | Jul 11 | Search in Rotated Array; Valid Parentheses (+2) | **Linked List** — Reorder List (#143, M)<br>**Linked List** — Remove Nth Node From End (#19, M) | find middle + reverse + merge<br>two-pointer gap of n | O(n)<br>O(n) one pass |

### Sprint Week 3 · Jul 13–Jul 18  (Day 21–26)
*Focus: Linked List, Trees, Tries, Heap*

> **⚠️ Schedule change (made Day 21, Jul 13):** Day 21's hour went to **teaching recursion from scratch** instead of LRU Cache, so **#146 moved from Day 21 → Day 24**, which was the only day in the week with no Block-2 problems. Days 22, 23, 25, 26 are unchanged; the Aug 20 target is unaffected.

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 21 ✅ | Jul 13 | 6 due (protocol) | **Recursion — taught from scratch** (call stack, base case, `fact`/`power`/`sumOfValues` drills)<br>**Trees** — Invert Binary Tree (#226, E)<br>**Trees** — Maximum Depth of Tree (#104, E)<br><sub>⤷ **LRU Cache (#146) MOVED → Day 24**</sub> | base case + recursive case; the call stack<br>TreeNode; recurse + swap POINTERS<br>recursive depth; max() | —<br>O(n), O(h)<br>O(n), O(h) stack |
| 22 | Jul 14 | Two Sum; Contains Duplicate (+5) | **Trees** — Diameter of Binary Tree (#543, E)<br>**Trees** — Same Tree (#100, E)<br>**Trees** — Lowest Common Ancestor (BST) (#235, M) | helper returns height<br>parallel recursion<br>BST-property navigation | O(n)<br>O(n)<br>O(h) |
| 23 | Jul 15 | Valid Anagram; Group Anagrams (+4) | **Trees** — Level Order Traversal (#102, M)<br>**Trees** — Validate BST (#98, M) | BFS w/ collections.deque<br>recurse w/ (low,high) bounds | O(n)<br>O(n) |
| 24 | Jul 16 | **Interleave** — mixed unlabeled set | ⚠️ **Linked List — LRU Cache (#146, M)** — *rescheduled from Day 21* (the Day-21 hour went to teaching recursion, which is load-bearing for Trees/Backtracking/Graphs/DP). Day 24 is the only day with Block-2 slack, so #146 lands here. **Do not skip it — it's the last unplaced core problem.** | dict + doubly-linked list (or `OrderedDict`); dummy head/tail | O(1) get/put |
| 25 | Jul 17 | Product of Array Except Self; Diameter of Binary Tree (+2) | **Trees** — Kth Smallest in BST (#230, M)<br>**Tries** — Implement Trie (#208, M) | in-order traversal<br>nested dict / TrieNode | O(h+k)<br>O(L) per op |
| 26 | Jul 18 | Valid Palindrome; Two Sum II (+5) | **Tries** — Design Add & Search Words (#211, M)<br>**Heap** — Kth Largest in a Stream (#703, E)<br>**Heap** — Last Stone Weight (#1046, E) | DFS with '.' wildcard<br>heapq; min-heap size k<br>max-heap via negation | O(L) avg<br>O(log k) per add<br>O(n log n) |

### Sprint Week 4 · Jul 20–Jul 25  (Day 27–32)
*Focus: Heap, Backtracking, Intervals*

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 27 | Jul 20 | Container With Most Water; Reorder List (+1) | **Heap** — K Closest Points to Origin (#973, M)<br>**Heap** — Kth Largest in Array (#215, M) | heap with tuple keys<br>heapq.nlargest; quickselect | O(n log k)<br>O(n log k); QS O(n) avg |
| 28 | Jul 21 | Best Time to Buy/Sell; LRU Cache (+4) | **Backtracking** — Subsets (#78, M)<br>**Backtracking** — Combination Sum (#39, M) | backtrack template; path[:] copy<br>recursion w/ start index | O(n·2ⁿ)<br>O(2^t) |
| 29 | Jul 22 | Longest Substring No Repeat; Diameter of Binary Tree (+5) | **Backtracking** — Permutations (#46, M)<br>**Backtracking** — Word Search (#79, M) | used-set / swap<br>grid DFS + visited backtrack | O(n·n!)<br>O(m·n·4^L) |
| 30 | Jul 23 | **Interleave** — mixed unlabeled set | — | name the *pattern* first | state complexity unprompted |
| 31 | Jul 24 | Koko Eating Bananas; Subsets (+1) | **Intervals** — Insert Interval (#57, M)<br>**Intervals** — Merge Intervals (#56, M) | list building; comparisons<br>sort(key=lambda x:x[0]) | O(n)<br>O(n log n) |
| 32 | Jul 25 | Find Min in Rotated Array; Kth Smallest in BST (+3) | **Intervals** — Non-overlapping Intervals (#435, M)<br>**Intervals** — Meeting Rooms (#252, E) | greedy by end time<br>sort + overlap check | O(n log n)<br>O(n log n) |

### Sprint Week 5 · Jul 27–Aug 1  (Day 33–38)
*Focus: Graphs, 1-D DP*

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 33 | Jul 27 | Design Add & Search Words; Kth Largest in a Stream (+1) | **Graphs** — Number of Islands (#200, M)<br>**Graphs** — Clone Graph (#133, M) | grid DFS/BFS; mark visited<br>hashmap old→clone + DFS | O(m·n)<br>O(V+E) |
| 34 | Jul 28 | Search in Rotated Array; Valid Parentheses (+4) | **Graphs** — Rotting Oranges (#994, M)<br>**Graphs** — Course Schedule (#207, M) | multi-source BFS; levels<br>adjacency list; cycle detect | O(m·n)<br>Topological, O(V+E) |
| 35 | Jul 29 | Min Stack; Subsets (+3) | **Graphs** — Course Schedule II (#210, M)<br>**Graphs** — Connected Components (#323, M) | Kahn's: indegree + queue<br>union-find intro | O(V+E)<br>≈O(V+E) |
| 36 | Jul 30 | **Interleave** — mixed unlabeled set | — | name the *pattern* first | state complexity unprompted |
| 37 | Jul 31 | 3Sum; Longest Repeating Char Replace (+2) | **1-D DP** — Climbing Stairs (#70, E)<br>**1-D DP** — Min Cost Climbing Stairs (#746, E)<br>**1-D DP** — House Robber (#198, M) | bottom-up; two rolling vars<br>dp array<br>rob/skip recurrence; 2 vars | O(n) — overlapping subproblems<br>O(n)<br>O(n) |
| 38 | Aug 1 | Longest Consecutive Sequence; Encode and Decode Strings (+4) | **1-D DP** — Longest Palindromic Substring (#5, M)<br>**1-D DP** — Decode Ways (#91, M) | expand-around-center<br>dp w/ 1- & 2-digit checks | O(n²)<br>O(n) |

### Sprint Week 6 · Aug 3–Aug 8  (Day 39–44)
*Focus: 1-D DP, 2-D DP, Greedy*

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 39 | Aug 3 | Non-overlapping Intervals; Meeting Rooms | **1-D DP** — Coin Change (#322, M)<br>**1-D DP** — Maximum Product Subarray (#152, M) | dp table; float('inf')<br>track min AND max | O(amount·coins)<br>O(n) |
| 40 | Aug 4 | Reverse Linked List; Merge Two Sorted Lists (+6) | **1-D DP** — Word Break (#139, M)<br>**1-D DP** — Longest Increasing Subsequence (#300, M) | dp + word set<br>dp O(n²) → O(n log n) | O(n²·m)<br>both bounds |
| 41 | Aug 5 | Reorder List; Remove Nth Node From End (+4) | **2-D DP** — Unique Paths (#62, M)<br>**2-D DP** — Longest Common Subsequence (#1143, M) | 2D grid dp / 1D rolling<br>2D table | O(m·n)<br>O(m·n) |
| 42 | Aug 6 | **Mock + Interleave** — timed think-aloud round | — | name the *pattern* first | state complexity unprompted |
| 43 | Aug 7 | Diameter of Binary Tree; Same Tree (+3) | **2-D DP** — Edit Distance (#72, M)<br>**Greedy** — Maximum Subarray (#53, M) | 2D table; 3 transitions<br>Kadane's; reset running sum | O(m·n)<br>O(n) |
| 44 | Aug 8 | Level Order Traversal; Validate BST (+5) | **Greedy** — Jump Game (#55, M)<br>**Greedy** — Gas Station (#134, M) | greedy farthest reach<br>total + running tank | O(n)<br>O(n) |

### Sprint Week 7 · Aug 10–Aug 15  (Day 45–50)
*Focus: Greedy, Bit Manip, 1-D DP, 2-D DP, Graphs*

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 45 | Aug 10 | Longest Palindromic Substring; Decode Ways | **Greedy** — Partition Labels (#763, M)<br>**Bit Manip** — Single Number (#136, E)<br>**Bit Manip** — Number of 1 Bits (#191, E) | last-occurrence map<br>XOR (^)<br>n & (n-1); shifts | O(n)<br>O(n) O(1)<br>O(1) (32 bits) |
| 46 | Aug 11 | Kth Smallest in BST; Implement Trie (+4) | **Bit Manip** — Counting Bits (#338, E)<br>**1-D DP** — House Robber II (#213, M) ⟂depth | dp + bit relation<br>split into two linear cases | O(n)<br>variant fluency |
| 47 | Aug 12 | Design Add & Search Words; Kth Largest in a Stream (+5) | **1-D DP** — Palindromic Substrings (#647, M) ⟂depth<br>**1-D DP** — Partition Equal Subset Sum (#416, M) ⟂depth | expand-around-center count<br>0/1 knapsack as bool set | variant fluency<br>variant fluency |
| 48 | Aug 13 | **Mock + Interleave** — timed think-aloud round | — | name the *pattern* first | state complexity unprompted |
| 49 | Aug 14 | Subsets; Combination Sum (+2) | **2-D DP** — Buy/Sell Stock w/ Cooldown (#309, M) ⟂depth<br>**2-D DP** — Coin Change II (#518, M) ⟂depth | state-machine dp<br>counting-combinations dp | variant fluency<br>variant fluency |
| 50 | Aug 15 | Permutations; Word Search (+4) | **2-D DP** — Target Sum (#494, M) ⟂depth<br>**Graphs** — Max Area of Island (#695, M) ⟂depth | dp w/ offset / dict memo<br>DFS returning a count | variant fluency<br>variant fluency |

### Sprint Week 8 · Aug 17–Aug 19  (Day 51–53)
*Focus: Graphs, Backtracking, Trees*

| Day | Date | Block 1 — Review | Block 2 — New | New Python / skill | Big-O |
|----|----|----|----|----|----|
| 51 | Aug 17 | Jump Game; Gas Station | **Graphs** — Pacific Atlantic Water Flow (#417, M) ⟂depth<br>**Graphs** — Graph Valid Tree (#261, M) ⟂depth | reverse DFS from borders<br>union-find / edge count | variant fluency<br>variant fluency |
| 52 | Aug 18 | Insert Interval; Merge Intervals (+5) | **Backtracking** — Subsets II (#90, M) ⟂depth<br>**Backtracking** — Palindrome Partitioning (#131, M) ⟂depth | sort + skip dup branch<br>substring + isPalindrome | variant fluency<br>variant fluency |
| 53 | Aug 19 | Non-overlapping Intervals; Meeting Rooms (+4) | **Backtracking** — Letter Combos of Phone (#17, M) ⟂depth<br>**Trees** — Balanced Binary Tree (#110, M) ⟂depth | digit→letters map<br>(height, balanced) tuple | variant fluency<br>variant fluency |

> **Aug 20 checkpoint:** you've acquired every core pattern and started the depth track. If you're behind here, that's fine — finish the *core* first; depth and Hards are built for fall.

---

# PART 2 — Fall Maintenance  ·  Aug 20 → interviews

*Classes + live interviews now. ~2–3 new problems/week, but daily-ish spaced review. No rigid dates — this is a queue you pull from. Your season runs Aug–Jan, so you keep sharpening the whole time.*

**Weekly rhythm (≈3–4 short sessions):**

- **Every session:** 1–2 spaced re-solves that are due (August's problems keep surfacing via the +21 schedule).
- **1×/week:** interleaved mixed set (random patterns, unlabeled).
- **1–2×/week:** timed think-aloud mock (Pramp / interviewing.io).
- **Spare capacity:** pull the next item from the queue below — depth first, then Hards.
- **Behavioral, in parallel:** 6–8 STAR stories, rehearsed aloud.

### Queue A — finish the depth problems (do these first)

| Pattern | Problem | Skill it drills |
|---|---|---|
| Trees | Subtree of Another Tree (#572) | compose sameTree |
| Trees | Right Side View (#199) | BFS last node per level |
| Trees | Count Good Nodes (#1448) | DFS passing max-so-far |
| Trees | Construct Tree (Pre+Inorder) (#105) | index maps; recursion |
| Linked List | Copy List w/ Random Pointer (#138) | hashmap old→new |
| Linked List | Add Two Numbers (#2) | carry handling; divmod |
| Linked List | Find the Duplicate Number (#287) | Floyd's on array |
| Heap | Task Scheduler (#621) | Counter + max-heap + queue |
| Heap | Design Twitter (#355) | heap-merge feeds |
| Greedy | Jump Game II (#45) | BFS-like level greedy |
| Greedy | Hand of Straights (#846) | Counter + sorted keys |
| Intervals | Meeting Rooms II (#253) | min-heap of end times |
| Stack | Car Fleet (#853) | sorted(zip()); reverse |
| Sliding Window | Permutation in String (#567) | fixed window; 26-counts |
| Arrays & Hashing | Valid Sudoku (#36) | defaultdict(set); tuples |
| Bit Manip | Missing Number (#268) | XOR / Gauss sum |
| Bit Manip | Reverse Bits (#190) | shift and build |

### Queue B — the canonical Hards + weighted-graph algorithms
*The ~19 Hards that recur, plus Dijkstra / Bellman-Ford / MST / topo-sort that the core path didn't cover. One solid pass each; revisit only what a target company is known to ask.*

| Pattern / Algorithm | Problem | Why it's on the list |
|---|---|---|
| Arrays / Two Pointers | Trapping Rain Water (#42) | two-ptr + monotonic stack; everywhere |
| Sliding Window | Minimum Window Substring (#76) | the canonical hard window |
| Sliding Window | Sliding Window Maximum (#239) | monotonic deque; FAANG staple |
| Linked List | Merge k Sorted Lists (#23) | heap-merge; hard staple |
| Linked List | Reverse Nodes in k-Group (#25) | pointer-surgery favorite |
| Trees | Binary Tree Maximum Path Sum (#124) | the classic tree-DP hard |
| Trees | Serialize & Deserialize Tree (#297) | design-y tree hard |
| Trie + Backtracking | Word Search II (#212) | the headline trie hard |
| Backtracking | N-Queens (#51) | canonical backtracking hard |
| Heap | Find Median from Data Stream (#295) | two-heaps; recurs often |
| Graph — BFS | Word Ladder (#127) | shortest-path-on-implicit-graph |
| Graph — Topo Sort | Alien Dictionary (#269) | topo-sort hard FAANG loves |
| Graph — Dijkstra | Network Delay Time (#743) | weighted shortest path (new) |
| Graph — Bellman-Ford | Cheapest Flights w/ K Stops (#787) | shortest path w/ constraints |
| Graph — MST | Min Cost to Connect Points (#1584) | Prim's / Kruskal's (new) |
| Graph — Union-Find | Redundant Connection (#684) | cements union-find |
| 2-D DP | Longest Increasing Path in Matrix (#329) | DFS + memo on a grid |
| 2-D DP | Burst Balloons (#312) | interval DP — the feared one |
| 2-D DP | Regular Expression Matching (#10) | string DP; classic hard |

---

## You're "ready for any company" when you can

Solve a random unseen **Medium in 25–35 min while talking**; state **time + space complexity unprompted**; **name the pattern within 2 minutes**; and **recover gracefully when stuck**. The common Hards no longer surprise you, and you have the graph/DP vocabulary to reason through a novel one. No prep guarantees 100% on every prompt — the goal is to make misses rare.

**Counts:** core 66 → +30 depth → +19 Hards = **115 problems**, each mastered 2–3× spaced. Front-load the first ~79 before Aug 20; the rest is fall.

*Generated 2026-06-28. A projection — your notebooks override it. Tell me if a week slips or a pattern bites and I'll re-compress.*