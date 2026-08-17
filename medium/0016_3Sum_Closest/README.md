# 16. 3Sum Closest

## Problem

Given an integer array `nums` of length `n` and an integer `target`,
find three integers in `nums` such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

## Example

Input:

nums = [-1, 2, 1, -4]
target = 1

Output:

2

## Approach

1. Sort the array.
2. Fix one element using index `i`.
3. Use two pointers:
   - `left = i + 1`
   - `right = n - 1`
4. Calculate the current three-number sum.
5. Update `closest` if the current sum is closer to the target.
6. If the sum is smaller than the target, move `left`.
7. If the sum is greater than the target, move `right`.
8. If the sum equals the target, return immediately.

## Complexity

Time Complexity: O(n²)

Space Complexity: O(1)