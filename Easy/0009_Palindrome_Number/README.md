# LeetCode 9 - Palindrome Number

## Problem

Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

A palindrome number reads the same forward and backward.

### Examples

- `121` → `True`
- `123` → `False`
- `-121` → `False`
- `10` → `False`

## Approach

We reverse the number mathematically instead of converting it into a string.

1. If `x` is negative, return `False`.
2. Store the original value of `x`.
3. Extract the last digit using `% 10`.
4. Add the digit to the reversed number.
5. Remove the last digit using `// 10`.
6. Compare the reversed number with the original number.

## Key Formula

```python
digit = x % 10
reverse = reverse * 10 + digit
x = x // 10