# Tries (Prefix Trees)

**Status:** learning (started Day 25, 2026-07-17) · **Mastery: 2/5** · Block B
**First problem:** #208 Implement Trie — built clean cold, verified vs a reference set (1000 trials).

## In one line
A tree of characters where each **path from the root spells a prefix**; words that start the same share the same early nodes. Built for **prefix** questions a hash set can't answer.

## Reach for it when
- "starts with" / prefix search / autocomplete
- Store a dictionary of words and query membership **and** prefixes
- Wildcard word search (#211 — `.` matches any char → DFS over children)
- Word Search II (#212 — Trie + grid DFS)

## The structure — nested dicts of nodes

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_end = False     # does a COMPLETE word end at this node?

class Trie:
    def __init__(self):
        self.root = TrieNode()  # empty node = the empty prefix; every op starts here
```

**🔑 The character is NOT a field on the node — it's the KEY in the parent's `children` dict.**
`parent.children['p'] = child` — the `'p'` lives as the dict key; the child node stores no character (no `self.val`). Its identity comes from *how you reached it*. (Just like `d['p'] = "hi"` doesn't put `'p'` inside `"hi"`.)

**🔑 `is_end` and `children` are independent.** A node can BOTH end a word AND have longer children — e.g. `app` ends inside `apple`. Without `is_end` you couldn't tell a stored word from a mere prefix.

## The three operations — all start at `self.root`, walk char by char

```python
def insert(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()   # create the edge if missing
        node = node.children[char]             # step down
    node.is_end = True                         # mark the end

def search(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            return False                       # edge missing → not stored
        node = node.children[char]
    return node.is_end                         # ← must ACTUALLY end here

def startsWith(self, prefix):
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        node = node.children[char]
    return True                                # ← path existing is enough
```

**🔑 `search` and `startsWith` are the SAME walk — only the last line differs:**
`search` returns `node.is_end` (a word must *end* here); `startsWith` returns `True` (any path through the prefix means some word has it).

## Complexity (word/prefix length `L`)
- **insert:** O(L) time · **O(L) space** (may create up to L new nodes)
- **search / startsWith:** O(L) time · **O(1) space** (walk only, no allocation)
- The "≤ 26 children per node" fact is the **branching factor** — it's what keeps each step's dict lookup O(1). It is *not* the operation's space.

## Mental model (his own, Day 25)
*"A Trie is nodes attached to dictionaries — like LRU, but each node has its OWN `children` dict, and a node only ever reaches its own children."* Exactly right — there's no back/sideways pointer, which is **why every operation must start at `self.root`.**

## 🔑 #211 Add & Search Words — the `.` wildcard = DFS *(Day 26)*
`addWord` is identical to `insert`. `search` gains a `.` that matches any one char. A normal letter follows **one** edge; a `.` **can't pick** — so try **all** children and succeed if **any** subtree matches. That branching is why a plain one-pointer walk no longer works — you need recursion (DFS), which **backtracks** when a child fails.
```python
def search(self, word):
    def dfs(index, node):
        if index == len(word):
            return node.isEnd
        if word[index] != ".":
            if word[index] not in node.children:
                return False
            return dfs(index+1, node.children[word[index]])   # one edge
        else:
            for child in node.children.values():              # try ALL children
                if dfs(index+1, child):
                    return True                               # any match wins
            return False
    return dfs(0, self.root)
```
- **Time:** O(L) with no wildcard (one path); worst case with many `.`s it fans out — up to **O(N)** total nodes visited. **Space:** O(L) recursion depth.
- **On the call stack (the thing that clicks slowly):** a `.` pushes a whole sub-search for the first child, waits for it to **fully return**, and if it's False, the frames **pop back** to the `.`'s frame and the `for`-loop tries the next child — stack goes deep, collapses, goes deep again. A normal letter never backs up; only the `.` does.

## Your gotchas
- **`addWord`/`insert` must end with `node.isEnd = True`** — dropped it on #208 and #211 (M-026). The op isn't done when the loop ends.
- **Every branch of `dfs` must `return`** — #211 dropped the return on the normal branch and didn't return `answer` from the wildcard loop (M-001). Walk each branch to its end.
- **Base case is `index == len(word)`**, not `len(word) - 1` — off-by-one stops one char early.
