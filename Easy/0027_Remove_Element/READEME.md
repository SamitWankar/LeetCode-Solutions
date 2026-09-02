# LeetCode 27 — Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.

The order of the remaining elements may be changed.

Return the number of elements in `nums` that are not equal to `val`.

## Example

### Input

```text
nums = [3, 2, 2, 3]
val = 3
```

### Output

```text
2
```

### Explanation

The elements equal to `3` are removed.

The first `2` elements of the modified array are:

```text
[2, 2]
```

## Approach

Use the **two-pointer technique**.

One pointer scans the array while the second pointer keeps track of the position for the next valid element.

```text
i → scans the array
k → position for the next valid element
```

Whenever:

```text
nums[i] != val
```

we copy:

```text
nums[k] = nums[i]
```

and increment `k`.

## Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

## Key Takeaway

Instead of physically deleting elements, we overwrite the unwanted elements and keep the valid elements at the beginning of the array.
