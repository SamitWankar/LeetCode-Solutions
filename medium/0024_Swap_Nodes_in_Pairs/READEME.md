# LeetCode 24 — Swap Nodes in Pairs

## Problem

Swap every two adjacent nodes in a linked list and return the resulting list.

The nodes themselves must be rearranged; their values should not simply be exchanged.

## Example

```text
Input:
1 → 2 → 3 → 4

Output:
2 → 1 → 4 → 3
```

For an odd number of nodes:

```text
Input:
1 → 2 → 3 → 4 → 5

Output:
2 → 1 → 4 → 3 → 5
```

## Solution

The solution uses a dummy node and three pointers:

* `prev`
* `first`
* `second`

The links are rearranged to swap each pair.

## Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

## Files

```text
solution.py       → Python solution
explanation.md    → Detailed explanation
README.md         → Problem overview
```

## LeetCode

**Problem:** 24 — Swap Nodes in Pairs

**Difficulty:** Medium

**Topic:** Linked List
