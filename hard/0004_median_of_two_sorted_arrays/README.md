# 0004. Median of Two Sorted Arrays

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n`, return the median of the two sorted arrays.

The overall run time complexity must be **O(log(m + n))**.

---

## Example 1

**Input**

```text
nums1 = [1,3]
nums2 = [2]
```

**Output**

```text
2.0
```

**Explanation**

Merged array:

```text
[1,2,3]
```

Median = **2**

---

## Example 2

**Input**

```text
nums1 = [1,2]
nums2 = [3,4]
```

**Output**

```text
2.5
```

**Explanation**

Merged array:

```text
[1,2,3,4]
```

Median = **(2 + 3) / 2 = 2.5**

---

## Approach

Instead of merging both arrays, we use **Binary Search** on the smaller array.

The idea is to divide both arrays into two halves such that:

* Every element on the left side is less than or equal to every element on the right side.
* The left side contains exactly half of the total elements.

For every partition, we compare only four boundary elements:

* `leftX`
* `rightX`
* `leftY`
* `rightY`

If:

```text
leftX <= rightY
```

and

```text
leftY <= rightX
```

then we have found the correct partition.

Once the correct partition is found:

* If the total number of elements is odd, the median is the maximum element on the left side.
* If the total number of elements is even, the median is the average of the maximum element on the left side and the minimum element on the right side.

---

## Algorithm

1. Perform binary search on the smaller array.
2. Calculate the required number of elements on the left side.
3. Compute partitions in both arrays.
4. Find the four boundary values.
5. Check whether the partition is valid.
6. If valid, calculate the median.
7. Otherwise, move the partition left or right.

---

## Time Complexity

```text
O(log(min(m, n)))
```

where:

* `m` = length of `nums1`
* `n` = length of `nums2`

---

## Space Complexity

```text
O(1)
```

No extra array is created.
