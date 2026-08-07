# Reverse Integer - Explanation

## Intuition

To reverse an integer, repeatedly extract its last digit and append it to a new number.

For example:

```
123
```

Step 1

```
digit = 3
reverse = 3
```

Step 2

```
digit = 2
reverse = 32
```

Step 3

```
digit = 1
reverse = 321
```

---

## Algorithm

1. Store whether the number is negative.
2. Convert the number to positive.
3. Initialize `reverse = 0`.
4. Repeat while the number is not zero:
   - Extract the last digit using `% 10`.
   - Append it using:
     ```
     reverse = reverse * 10 + digit
     ```
   - Remove the last digit using `// 10`.
5. Restore the sign if the original number was negative.
6. Check whether the result lies within the 32-bit signed integer range.
7. Return `0` if overflow occurs.

---

## Dry Run

Input

```
x = -456
```

Initially

```
negative = True
x = 456
reverse = 0
```

Iteration 1

```
digit = 6
reverse = 6
x = 45
```

Iteration 2

```
digit = 5
reverse = 65
x = 4
```

Iteration 3

```
digit = 4
reverse = 654
x = 0
```

Restore sign

```
reverse = -654
```

Overflow check

```
-654 lies within the 32-bit range.
```

Final Answer

```
-654
```

---

## Complexity Analysis

**Time Complexity**

```
O(log n)
```

Each digit is processed exactly once.

**Space Complexity**

```
O(1)
```

Only a few variables are used.