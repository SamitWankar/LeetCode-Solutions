# LeetCode 88 - Merge Sorted Array

## Problem

Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array.

`nums1` has enough space to hold all elements from both arrays.

## Approach

We use the **two-pointer approach from the end**.

- `i` points to the last valid element of `nums1`
- `j` points to the last element of `nums2`
- `k` points to the last position of `nums1`

We compare `nums1[i]` and `nums2[j]` and place the larger value at `nums1[k]`.

Working from the end prevents us from overwriting the existing elements in `nums1`.

## Complexity

- Time: O(m + n)
- Space: O(1)

## Example

Input:

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Output:

[1,2,2,3,5,6]