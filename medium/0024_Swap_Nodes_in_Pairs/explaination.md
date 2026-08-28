# Swap Nodes in Pairs — Explanation

## Problem

Given the head of a linked list, swap every two adjacent nodes and return the modified list.

### Example

Input:

```text
1 → 2 → 3 → 4
```

Output:

```text
2 → 1 → 4 → 3
```

If the list contains an odd number of nodes, the final node remains unchanged.

Example:

```text
1 → 2 → 3 → 4 → 5
```

Output:

```text
2 → 1 → 4 → 3 → 5
```

## Approach

We use three pointers:

* `prev` — node before the current pair
* `first` — first node of the pair
* `second` — second node of the pair

A dummy node is placed before the head. This makes it easier to handle swapping the first pair.

For:

```text
dummy → 1 → 2 → 3
```

we identify:

```text
first = 1
second = 2
```

Then change the links:

```python
prev.next = second
first.next = second.next
second.next = first
```

This changes:

```text
1 → 2 → 3
```

into:

```text
2 → 1 → 3
```

After completing the swap, `prev` is moved to `first`, so we can process the next pair.

## Algorithm

1. Create a dummy node.
2. Point `dummy.next` to `head`.
3. Set `prev = dummy`.
4. Continue while two nodes are available.
5. Store the first and second nodes.
6. Rearrange their `next` pointers.
7. Move `prev` to the end of the swapped pair.
8. Return `dummy.next`.

## Complexity

### Time Complexity

```text
O(n)
```

Every node is processed once.

### Space Complexity

```text
O(1)
```

Only a constant number of pointers are used.

## Key Idea

The important part is not changing the values of the nodes.

We change the **links between the nodes**:

```text
prev → first → second
```

becomes:

```text
prev → second → first
```
