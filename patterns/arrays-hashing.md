# Arrays & Hashing

**Status:** learned (Days 1–3, 17) · **Mastery: 3/5** · Block A

## In one line
Trade space for time: a hash map/set gives **O(1) lookup**, frequency counting, or grouping by a canonical key — usually to kill a nested-loop scan.

## Reach for it when
- "Have I seen X before?" / dedupe → **set**.
- Counting occurrences → **dict / `collections.Counter`**.
- Grouping items that share something (anagrams) → **group by a canonical key** (sorted string, char-count tuple).
- You're about to write an O(n²) "for each, scan the rest" → a hash usually makes it O(n).

## Sub-techniques you've done
- Hashmap/set lookup — Two Sum (#1), Contains Duplicate (#217)
- Frequency counting — Valid Anagram (#242)
- Group-by-canonical-key — Group Anagrams (#49)
- Bucket sort — Top K Frequent (#347) — derived O(n) yourself
- Prefix/suffix products — Product of Array Except Self (#238), incl. O(1)-extra-space
- **Set + only-start gate — Longest Consecutive Sequence (#128): `x-1 not in set` starts a run → count forward; amortized O(n)**
- **Length-prefix encoding — Encode/Decode Strings (#271): `len#string`; decode reads by COUNT, not by hunting a delimiter**

## Template
```python
seen = set()
for x in nums:
    if target - x in seen:   # O(1) lookup
        return True
    seen.add(x)              # touch the RIGHT container
```

## Complexity
Hash ops O(1) average; whole scan O(n) time. Building the dict/set = **O(n) space**.

## Your gotchas (from the log)
- Touch the **right container**: `seen.add(x)`, not `nums.add(x)`.
- A hidden `sorted()` adds `k log k` per element — Group Anagrams is O(n·k log k), not O(n).
- Use exact names (`nums`, not `num`); `range(len(x))`, not `range(x)`.
