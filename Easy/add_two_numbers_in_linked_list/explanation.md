# Add Two Numbers - Detailed Explanation

## Understanding the Problem

The numbers are stored in reverse order.

Example:

Linked List 1

2 → 4 → 3

represents

342

Linked List 2

5 → 6 → 4

represents

465

Adding both numbers

342 + 465 = 807

The answer should also be stored in reverse order.

Output

7 → 0 → 8

---

# Dry Run

Input

l1

2 → 4 → 3

l2

5 → 6 → 4

carry = 0

---

## First Iteration

Current digits

2 and 5

Calculation

2 + 5 + 0 = 7

carry = 0

digit = 7

Result List

7

Move both pointers

l1

4 → 3

l2

6 → 4

---

## Second Iteration

Current digits

4 and 6

Calculation

4 + 6 + 0 = 10

carry = 1

digit = 0

Result List

7 → 0

Move both pointers

l1

3

l2

4

---

## Third Iteration

Current digits

3 and 4

Calculation

3 + 4 + carry(1)

= 8

carry = 0

digit = 8

Result List

7 → 0 → 8

Both linked lists end.

carry is also 0.

Loop stops.

---

# Why Do We Use a Dummy Node?

Initially, we do not have a result linked list.

Instead of handling the first node separately, we create a dummy node.

Initially

dummy

0

After first digit

dummy

0 → 7

After second digit

dummy

0 → 7 → 0

After third digit

dummy

0 → 7 → 0 → 8

The first node (0) is not part of the answer.

Therefore we return

dummy.next

which points to

7 → 0 → 8

---

# Why Do We Need Carry?

Suppose

8 + 7 = 15

We cannot store 15 inside one node.

Store

5

Carry

1

The carry is added in the next iteration.

---

# Why Use

carry = total // 10

Integer division gives the carry.

Example

15 // 10 = 1

28 // 10 = 2

---

# Why Use

digit = total % 10

Modulo returns the last digit.

Example

15 % 10 = 5

28 % 10 = 8

---

# Loop Condition

```python
while l1 or l2 or carry: