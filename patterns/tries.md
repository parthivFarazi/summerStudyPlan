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

## Next
- **#211 Add & Search Words** — `search` with a `.` wildcard: at a `.`, you can't pick one edge, so **recurse into ALL children** (DFS). This is where Trie meets tree-DFS.
