# LeetCode 88 - Merge Sorted Array

## Problem

We are given two sorted arrays:

- `nums1`
- `nums2`

`nums1` has enough empty space at the end to store all elements of `nums2`.

We need to merge both arrays into `nums1` in sorted order.

### Example

Input:

nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

Output:

[1,2,2,3,5,6]

---

## Approach

We use the **two-pointer approach**.

Instead of starting from the beginning, we start from the **end** of both arrays.

We use three pointers:

- `i` → last valid element of `nums1`
- `j` → last element of `nums2`
- `k` → last available position in `nums1`

Initially:

```text
i = m - 1
j = n - 1
k = m + n - 1