# 5. Longest Palindromic Substring

## Problem

Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same forward and backward.

### Example 1

```text
Input: s = "babad"

Output: "bab"

Explanation:
"aba" is also a valid answer.
```

### Example 2

```text
Input: s = "cbbd"

Output: "bb"
```

---

## Approach

This solution uses the **Expand Around Center** technique.

Every palindrome has a center.

- Odd-length palindromes have one center.
- Even-length palindromes have two centers.

For every index:

1. Expand considering the current character as the center.
2. Expand considering the gap between two characters as the center.
3. Keep updating the longest palindrome found.

---

## Algorithm

1. Initialize `start` and `end` to store the longest palindrome.
2. Create an `expand()` function that expands while characters match.
3. Iterate through every character.
4. Find both odd and even palindromes.
5. Update the longest palindrome if a longer one is found.
6. Return the substring from `start` to `end`.

---

## Time Complexity

**O(n²)**

Each character can expand up to `n` positions.

---

## Space Complexity

**O(1)**

Only a few variables are used.