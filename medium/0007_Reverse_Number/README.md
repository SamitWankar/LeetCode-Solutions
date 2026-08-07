# 7. Reverse Integer

## Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, return `0`.

Assume the environment does not allow storing 64-bit integers.

## Examples

### Example 1

Input:
```
x = 123
```

Output:
```
321
```

### Example 2

Input:
```
x = -123
```

Output:
```
-321
```

### Example 3

Input:
```
x = 120
```

Output:
```
21
```

### Example 4

Input:
```
x = 0
```

Output:
```
0
```

## Approach

1. Check whether the number is negative.
2. Convert it to a positive number.
3. Reverse the digits using modulo (`%`) and integer division (`//`).
4. Restore the negative sign if needed.
5. Check whether the reversed integer lies within the 32-bit signed integer range.
6. Return `0` if it overflows; otherwise return the reversed integer.

## Time Complexity

```
O(log n)
```

## Space Complexity

```
O(1)
```