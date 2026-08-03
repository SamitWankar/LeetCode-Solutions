# 3. Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the **longest substring** without repeating characters.

A **substring** is a contiguous sequence of characters.

### Example 1

**Input:**
```text
s = "abcabcbb"
```

**Output:**
```text
3
```

**Explanation:**

The longest substring without repeating characters is `"abc"`.

---

### Example 2

**Input:**
```text
s = "bbbbb"
```

**Output:**
```text
1
```

---

### Example 3

**Input:**
```text
s = "pwwkew"
```

**Output:**
```text
3
```

The longest substring is `"wke"`.

---

## Approach

This problem is solved using the **Sliding Window** technique.

- Use two pointers (`left` and `right`) to represent the current window.
- Use a `set` to store characters currently inside the window.
- Expand the window by moving the `right` pointer.
- If a duplicate character is found, shrink the window from the left until all characters become unique again.
- Update the maximum window length after each valid expansion.

---

## Algorithm

1. Create an empty set.
2. Initialize `left = 0` and `max_length = 0`.
3. Traverse the string using the `right` pointer.
4. While the current character already exists in the set:
   - Remove the leftmost character from the set.
   - Move the `left` pointer forward.
5. Add the current character to the set.
6. Update the maximum length.
7. Return the maximum length.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Python Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
```