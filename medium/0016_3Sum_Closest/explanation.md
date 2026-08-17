# Explanation

## Brute Force

The brute-force approach checks every possible combination of three
numbers.

This requires three nested loops:

O(n³)

This is inefficient for large inputs.

## Optimized Approach

We first sort the array.

After sorting, we fix one element and use two pointers for the
remaining two elements.

For each `i`:

- `left = i + 1`
- `right = len(nums) - 1`

We calculate:

current_sum = nums[i] + nums[left] + nums[right]

Then we compare its distance from the target:

abs(current_sum - target)

If this distance is smaller than the previous best distance, we update
`closest`.

### Pointer Movement

If:

current_sum < target

we need a larger sum, so:

left += 1

If:

current_sum > target

we need a smaller sum, so:

right -= 1

If:

current_sum == target

the difference is zero, which is the best possible result, so we can
return the target immediately.

## Initial Closest Value

We initialize:

closest = nums[0] + nums[1] + nums[2]

This is simply a valid three-element sum used as the initial comparison
value. It is not necessarily the final answer.

## Complexity

Sorting takes O(n log n).

The two-pointer search takes O(n²).

Therefore, the overall time complexity is:

O(n²)

The algorithm uses O(1) extra space apart from the sorting
implementation.