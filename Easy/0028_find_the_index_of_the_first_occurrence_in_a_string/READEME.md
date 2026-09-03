# LeetCode 28 — Find the Index of the First Occurrence in a String

**Difficulty:** Easy
**Problem Number:** 28

## Problem

Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`.

Return `-1` if `needle` does not occur in `haystack`.

## Example 1

```text
Input:
haystack = "sadbutsad"
needle = "sad"

Output:
0
```

## Example 2

```text
Input:
haystack = "leetcode"
needle = "leeto"

Output:
-1
```

## Solution

The solution checks each possible starting position in `haystack` and compares the substring with `needle`.

### Files

* `solution.py` — Python solution
* `explanation.md` — Detailed explanation
* `README.md` — Problem overview and solution information

## Complexity

* **Time:** O(n × m)
* **Space:** O(m)
