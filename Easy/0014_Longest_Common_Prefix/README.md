# LeetCode 14 - Longest Common Prefix

## Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Example

Input:
["flower", "flow", "flight"]

Output:
"fl"

## Approach

1. Take the first string as the initial prefix.
2. Compare it with every remaining string.
3. If the current word does not start with the prefix, remove the last character from the prefix.
4. Continue until the prefix matches.
5. Return the prefix.

## Complexity

Time Complexity: O(S)

Where S is the total number of characters that may be examined.

Space Complexity: O(1)

## Algorithm

```text
prefix = first string

for every remaining word:
    while word does not start with prefix:
        remove the last character from prefix

return prefix