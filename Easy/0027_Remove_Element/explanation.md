# Explanation — Remove Element

## Approach

We use the **two-pointer technique**.

* `i` is used to traverse the entire array.
* `k` keeps track of the position where the next valid element should be placed.
* If `nums[i]` is not equal to `val`, we copy it to `nums[k]` and increment `k`.
* At the end, `k` represents the number of elements that are not equal to `val`.

## Example

Given:

```text
nums = [3, 2, 2, 3]
val = 3
```

We skip both `3`s and keep both `2`s.

The array becomes:

```text
[2, 2, ...]
```

The function returns:

```text
2
```

Therefore, the first `2` elements are the valid result.

## Why This Works

Every element that is different from `val` is moved toward the beginning of the array.

The elements after index `k - 1` do not matter because the problem only considers the first `k` elements.

## Complexity

* **Time Complexity:** `O(n)` — we traverse the array once.
* **Space Complexity:** `O(1)` — no extra array is created.

## Key Concept

The important idea is to **overwrite unwanted elements with valid elements** instead of actually deleting elements from the array.
