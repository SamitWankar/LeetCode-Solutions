
# 12. Integer to Roman

## Problem
Convert an integer into its Roman numeral representation.

### Example 1
Input: num = 3
Output: "III"

### Example 2
Input: num = 58
Output: "LVIII"

### Example 3
Input: num = 1994
Output: "MCMXCIV"

---

## Approach
This solution uses a **Greedy Algorithm**.

- Store Roman values in descending order.
- Store their corresponding symbols.
- Repeatedly subtract the largest possible value.
- Append the matching Roman symbol to the result.

---

## Time Complexity
**O(1)**

Only 13 Roman values exist.

## Space Complexity
**O(1)**