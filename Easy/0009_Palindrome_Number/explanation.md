# Explanation - Palindrome Number

## Problem Understanding

We are given an integer `x`.

We need to check whether the number is the same when read from left to right and right to left.

### Examples

```text
121 → 121 → Palindrome
123 → 321 → Not Palindrome
-121 → Not Palindrome
10 → 1 → Not Palindrome
```

---

## Approach

We can solve this problem by **reversing the number mathematically**.

We don't need to convert the number into a string.

The main idea is:

1. If the number is negative, return `False`.
2. Store the original number in a variable.
3. Extract the last digit using `% 10`.
4. Add that digit to the reversed number.
5. Remove the last digit using `// 10`.
6. Compare the reversed number with the original number.

---

## Important Formula

To get the last digit:

```python
digit = x % 10
```

To add the digit to the reversed number:

```python
reverse = reverse * 10 + digit
```

To remove the last digit:

```python
x = x // 10
```

---

## Step-by-Step Example

Let's take:

```text
x = 121
```

First, store the original value:

```python
original = 121
reverse = 0
```

### Iteration 1

```text
x = 121
```

Get the last digit:

```text
121 % 10 = 1
```

Update reverse:

```text
reverse = 0 * 10 + 1
        = 1
```

Remove the last digit:

```text
121 // 10 = 12
```

---

### Iteration 2

```text
x = 12
```

Get the last digit:

```text
12 % 10 = 2
```

Update reverse:

```text
reverse = 1 * 10 + 2
        = 12
```

Remove the last digit:

```text
12 // 10 = 1
```

---

### Iteration 3

```text
x = 1
```

Get the last digit:

```text
1 % 10 = 1
```

Update reverse:

```text
reverse = 12 * 10 + 1
        = 121
```

Remove the last digit:

```text
1 // 10 = 0
```

Now the loop stops because:

```text
x = 0
```

---

## Final Comparison

We have:

```text
original = 121
reverse  = 121
```

Therefore:

```python
return reverse == original
```

returns:

```text
True
```

So `121` is a palindrome.

---

## Why Do We Store `original`?

Inside the loop, we continuously modify `x`:

```python
x = x // 10
```

Eventually, `x` becomes `0`.

Therefore, we cannot compare:

```python
reverse == x
```

Instead, we save the original number before modifying it:

```python
original = x
```

Then we compare:

```python
reverse == original
```

---

## Negative Numbers

A negative number cannot be a palindrome.

For example:

```text
-121
```

Its reverse would not be the same number.

Therefore:

```python
if x < 0:
    return False
```

---

## Complete Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return reverse == original
```

---

## Complexity Analysis

### Time Complexity

```text
O(log₁₀(x))
```

The loop runs once for each digit in the number.

For example, a 3-digit number requires approximately 3 iterations.

### Space Complexity

```text
O(1)
```

We only use a few variables such as `original`, `reverse`, `digit`, and `x`.

---

## Key Takeaways

* `% 10` gives the last digit.
* `// 10` removes the last digit.
* `reverse * 10 + digit` builds the reversed number.
* Save the original number before modifying `x`.
* Compare `reverse` with `original` to determine whether the number is a palindrome.
