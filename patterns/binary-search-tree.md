# Binary Search Tree (BST)

**Status:** learning (started Day 22, 2026-07-14) · **Mastery: 2/5** · Block B
**Prereqs:** [trees](trees.md) (recursion, DFS) · [binary-search](binary-search.md) (the halving idea)

## In one line
**Compare, then pick ONE side.** The ordering invariant lets you throw away half the tree without looking at it.

## The invariant — this is the whole data structure

> **For every node: everything in its LEFT subtree is smaller. Everything in its RIGHT subtree is larger.**
> **Not just the immediate children — the ENTIRE subtree, recursively.**

```
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \     /
         4   7   13
```
At `8`: left `{3,1,6,4,7}` all < 8 ✓ · right `{10,14,13}` all > 8 ✓
At `3`: left `{1}` ✓ · right `{6,4,7}` ✓ — **holds at every node.**

## Why it exists: it turns a tree into binary search

Find `13`: at `8` → `13 > 8`. **Everything smaller than 8 lives left, so 13 CANNOT be there.** Discard the entire left subtree. Go right. At `10` → right. At `14` → left. **Found — 3 comparisons.**

Never visited `3, 1, 6, 4, 7`. **Eliminated without visiting**, because the invariant *guaranteed* they couldn't hold the answer.

**Same idea as #704.** In an array you halve by **index**; in a BST you halve by **branching**. → **O(h)** — and `h = log n` when balanced.

**Hitting `None` means the value is DEFINITIVELY ABSENT** — not "not found yet." Every step eliminated the only region it could have been in.

## The move to internalize

| | |
|---|---|
| **Ordinary binary tree** | No information → **must explore BOTH children** (#104, #226, #543 all recurse left *and* right) |
| **BST** | The invariant tells you which side → **compare and pick ONE.** Never explore both. |

**If you find yourself recursing into both children of a BST, ask why — you're probably wasting the invariant.**

## Reach for it when
- The problem *says* "binary search tree" — that word is the whole hint
- Search / insert / delete a value
- Lowest common ancestor (#235)
- Validate a BST (#98)
- Kth smallest (#230) — **in-order traversal of a BST yields SORTED order**

## Templates

### Search — O(h) time, O(1) space (iterative)
```python
while node is not None:
    if target < node.val:
        node = node.left            # target is smaller → it can only be left
    elif target > node.val:
        node = node.right
    else:
        return node                 # found
return None                         # ran off the tree → definitively absent
```

### #235 — Lowest Common Ancestor
```python
while node is not None:
    if p.val < node.val and q.val < node.val:      # both STRICTLY smaller
        node = node.left
    elif p.val > node.val and q.val > node.val:    # both STRICTLY larger
        node = node.right
    else:
        return node                                # they SPLIT → this is the answer
```
**O(h) time · O(1) space** — no recursion, so **no call stack**. One path down.

**Why the split is immediately the answer** (no backtracking):
Step **left** and the subtree holds only values **< node** → **you lose `q` forever.**
Step **right** and it holds only values **> node** → **you lose `p`.**
**You cannot go deeper without abandoning one of them ⇒ you are standing on the deepest node containing both.**

**The equality case handles itself.** If `p.val == node.val`: `p.val < node.val` is False *and* `p.val > node.val` is False → **falls into `else` → returns `node`** ✅ (a node is an ancestor of itself).
> **The STRICTNESS (`<`, `>` — never `<=`, `>=`) is what lets equality escape into the `else`.**
> **Two narrow gates. Everything that fits neither gate is the answer.**

## Complexity
- **Search / insert / LCA: O(h) time.** Balanced → **O(log n)**. Degenerate chain → **O(n)**.
- **Iterative descent: O(1) space** — no call stack. *(Recursive version: O(h).)*
- ⚠️ **A BST is NOT automatically O(log n).** Insert `1,2,3,4,5` in order and you get a linked list. `h = n`. **Always say "O(h), which is O(log n) balanced and O(n) worst case."** (Self-balancing trees — AVL, red-black — are what actually guarantee `log n`; not needed for these problems.)

## Your gotchas
- **Direction inversion (M-012 → blocker B-6).** `node.val > p.val` means **`p` is SMALLER**, so `p` lives **LEFT**. Day 22: walked **right**. **Say the sentence before writing the branch: *"Which side can still contain the answer? Go there."***
- **The descent is a LOOP (M-018).** Day 22: reassigned `node = node.left` inside a bare `if/elif/else` and fell off the bottom of the function → returned `None`. **Moving a pointer once is not traversing. Wrap it in `while node is not None`.**
- **The invariant is SUBTREE-WIDE, not parent-child.** This is invalid:
  ```
          5
         / \
        3   7
           / \
          4   8      ← 4 < 5, but it sits in 5's RIGHT subtree
  ```
  `4`'s parent is `7` and `4 < 7`, so **locally it looks fine.** It isn't. **Checking only immediate children is the #1 wrong answer to #98 (Validate BST)** — the real solution passes a `(min, max)` range down.
  **And it's fatal, not cosmetic:** search that tree for `4` — you stand at `5`, see `4 < 5`, go **left**, and never find it, though it's sitting right there. **The invariant is a promise the search relies on. Break it and search silently lies.**
- **In-order traversal of a BST is sorted.** `left → node → right`. That's the trick behind #230 and one solution to #98. Worth remembering before you reach for anything clever.
