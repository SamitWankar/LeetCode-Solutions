# Remove Nth Node From End of List

## Problem

Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Example

Input:

1 → 2 → 3 → 4 → 5

n = 2

The 2nd node from the end is 4.

Output:

1 → 2 → 3 → 5

## Approach

We use the two-pointer technique with:

- `slow`
- `fast`

We also create a dummy node before the head.

### Why use a dummy node?

The dummy node makes removing the head easier.

For example:

dummy → 1 → 2 → 3

If we need to remove `1`, we can use the same logic:

slow.next = slow.next.next

### Algorithm

1. Create a dummy node.
2. Set `slow` and `fast` to the dummy node.
3. Move `fast` forward `n` steps.
4. Move both `slow` and `fast` together until `fast.next` is `None`.
5. `slow` will now point to the node immediately before the node we want to remove.
6. Remove the target node using:

slow.next = slow.next.next

7. Return `dummy.next`.

## Example Walkthrough

List:

dummy → 1 → 2 → 3

n = 1

Initially:

slow = dummy
fast = dummy

Move `fast` one step:

dummy → 1 → 2 → 3
          ↑
         fast

Move both pointers until `fast.next` is `None`.

Eventually:

dummy → 1 → 2 → 3
              ↑    ↑
            slow  fast

Now `slow` is at `2`, which is immediately before `3`.

Remove `3`:

slow.next = slow.next.next

Result:

1 → 2

## Complexity

Time Complexity: O(L)

Space Complexity: O(1)

Where `L` is the number of nodes in the linked list.