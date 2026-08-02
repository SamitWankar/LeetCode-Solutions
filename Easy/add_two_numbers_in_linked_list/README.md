# 2. Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

### Example

Input:

l1 = 2 → 4 → 3

l2 = 5 → 6 → 4

Output:

7 → 0 → 8

Explanation:

342 + 465 = 807

---

## Approach

We traverse both linked lists simultaneously.

For every iteration:

1. Read the current digit from both linked lists.
2. Add both digits along with the carry.
3. Store the last digit of the sum in a new node.
4. Update the carry.
5. Move both linked list pointers forward.

A **dummy node** is used to simplify the creation of the result linked list.

Finally, return `dummy.next` because the dummy node itself is only a placeholder.

---

## Algorithm

1. Create a dummy node.
2. Create a pointer `current` pointing to the dummy node.
3. Initialize `carry = 0`.
4. While either linked list has nodes or carry exists:
   - Read values from both lists (use 0 if a list has ended).
   - Compute the total.
   - Calculate carry using integer division.
   - Create a new node using the remainder.
   - Move the current pointer.
   - Move both linked list pointers.
5. Return `dummy.next`.

---

## Complexity Analysis

**Time Complexity**

O(max(m, n))

where m and n are the lengths of the linked lists.

**Space Complexity**

O(max(m, n))

A new linked list is created to store the result.

---

## Python Solution

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
```