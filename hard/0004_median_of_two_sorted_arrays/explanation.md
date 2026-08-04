# Explanation

## Intuition

A simple solution is to merge both sorted arrays and then find the median.

Although this approach is easy to understand, merging requires **O(m + n)** time, while the problem specifically asks for **O(log(m + n))** time.

To achieve this, we avoid merging the arrays and instead use **Binary Search** on the smaller array.

---

## Key Idea

Imagine placing a partition (`|`) inside both arrays.

Example:

```text
nums1 = [1,2]
nums2 = [3,4]

nums1
1 2 |

nums2
| 3 4
```

Left side:

```text
1 2
```

Right side:

```text
3 4
```

The goal is to find a partition where:

```text
leftX <= rightY
```

and

```text
leftY <= rightX
```

If these conditions are true, then every element on the left is less than or equal to every element on the right.

---

## Why Binary Search?

There are many possible partition positions.

Instead of checking every partition one by one, Binary Search quickly finds the correct partition by eliminating half of the remaining possibilities in each step.

---

## Dry Run

### Input

```text
nums1 = [1,3]
nums2 = [2]
```

After ensuring `nums1` is the smaller array:

```text
nums1 = [2]
nums2 = [1,3]
```

Total elements:

```text
3
```

Left side should contain:

```text
(3 + 1) // 2 = 2
```

Choose partitions:

```text
nums1

2 |

nums2

1 | 3
```

Boundary values:

```text
leftX = 2
rightX = +∞

leftY = 1
rightY = 3
```

Check:

```text
2 <= 3  ✅
1 <= +∞ ✅
```

Correct partition found.

Since the total number of elements is odd:

```text
Median = max(leftX, leftY)

= max(2,1)

= 2
```

---

## Important Points

* Always perform Binary Search on the smaller array.
* The left side must contain exactly:

```text
(m + n + 1) // 2
```

elements.

* Only four boundary values are compared.
* No merged array is created.

---

## Complexity Analysis

### Time Complexity

```text
O(log(min(m, n)))
```

### Space Complexity

```text
O(1)
```

---

## What I Learned

* How Binary Search can be used on partitions instead of values.
* How to find the median without merging two sorted arrays.
* Why checking only four boundary values is sufficient.
* How partition-based Binary Search achieves logarithmic time complexity.
