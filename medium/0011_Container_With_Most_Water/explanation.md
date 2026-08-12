# Container With Most Water — LeetCode 11

## Problem

Given an integer array `height`, where each element represents the height of a vertical line, find two lines that together with the x-axis form a container that holds the most water.

## Approach — Two Pointers

We use two pointers:

* `left` starts at the first element.
* `right` starts at the last element.

For every pair of lines, calculate the area using:

`area = min(height[left], height[right]) * (right - left)`

The shorter line determines the maximum possible water height because water would overflow over the shorter wall.

After calculating the area:

* If the left line is shorter, move `left` forward.
* Otherwise, move `right` backward.

We continue until `left` and `right` meet.

## Why Move the Shorter Pointer?

Suppose:

`height[left] < height[right]`

The left line is limiting the water height. If we move the right pointer, the width decreases while the limiting left height remains the same or could still be smaller.

Therefore, moving the shorter pointer gives us a chance to find a taller line and increase the area.

## Algorithm

1. Set `left = 0`.
2. Set `right = len(height) - 1`.
3. Set `max_area = 0`.
4. While `left < right`:

   * Calculate the current area.
   * Update `max_area`.
   * Move the pointer corresponding to the shorter height.
5. Return `max_area`.

## Example

Input:

`height = [1,8,6,2,5,4,8,3,7]`

The maximum area is:

`49`

This is obtained using the lines with heights `8` and `7`.

## Complexity

### Time Complexity

`O(n)`

Each pointer moves through the array at most once.

### Space Complexity

`O(1)`

Only a few variables are used.
