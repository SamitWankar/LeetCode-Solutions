# 6. Zigzag Conversion

## Problem Statement

Given a string `s` and an integer `numRows`, arrange the characters of the string in a zigzag pattern across the given number of rows. After writing the characters in this pattern, read the rows one by one to form the final string.

### Example 1

**Input:**
```text
s = "PAYPALISHIRING"
numRows = 3
```

**Zigzag Pattern:**

```text
P   A   H   N
A P L S I I G
Y   I   R
```

**Output:**

```text
"PAHNAPLSIIGYIR"
```

---

### Example 2

**Input:**

```text
s = "PAYPALISHIRING"
numRows = 4
```

**Zigzag Pattern:**

```text
P     I     N
A   L S   I G
Y A   H R
P     I
```

**Output:**

```text
"PINALSIGYAHRPI"
```

---

## Approach

Instead of creating the actual zigzag pattern, we simulate the movement between rows.

1. Create one empty string for each row.
2. Start from the first row.
3. Add each character to the current row.
4. Move downward until reaching the last row.
5. Reverse direction and move upward until reaching the first row.
6. Continue this process until all characters are processed.
7. Join all rows together to obtain the final answer.

---

## Algorithm

1. If `numRows == 1` or `numRows >= len(s)`, return the original string.
2. Create a list of empty strings, one for each row.
3. Initialize:
   - `currentRow = 0`
   - `goingDown = False`
4. Traverse every character in the string.
5. Append the character to `rows[currentRow]`.
6. If the current row is the first or last row, reverse the direction.
7. Move to the next row based on the current direction.
8. Join all rows and return the result.

---

## Complexity Analysis

**Time Complexity:** `O(n)`

- Every character is visited exactly once.

**Space Complexity:** `O(n)`

- The rows store all characters of the input string.

---

## Key Concepts

- String Simulation
- Direction Change
- Traversing Rows
- String Concatenation