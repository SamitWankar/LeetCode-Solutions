# Explanation - Zigzag Conversion

## Intuition

The main challenge is understanding the zigzag movement.

Instead of drawing the zigzag, we keep track of the row where the next character should be placed.

Example:

```
P   A   H   N
A P L S I I G
Y   I   R
```

Each row stores its own characters.

```
Row 0 : PAHN
Row 1 : APLSIIG
Row 2 : YIR
```

Finally, joining all rows gives:

```
PAHNAPLSIIGYIR
```

---

## Step-by-Step

### Step 1

Create one empty string for each row.

```python
rows = [""] * numRows
```

Example:

```
["", "", ""]
```

---

### Step 2

Start from the first row.

```python
currentRow = 0
```

---

### Step 3

Maintain the movement direction.

```python
goingDown = False
```

- `True` → Moving Down
- `False` → Moving Up

---

### Step 4

Process every character.

```python
for char in s:
```

Append the character to the current row.

```python
rows[currentRow] += char
```

---

### Step 5

Whenever we reach the top or bottom row, reverse the direction.

```python
if currentRow == 0 or currentRow == numRows - 1:
    goingDown = not goingDown
```

---

### Step 6

Move to the next row.

```python
if goingDown:
    currentRow += 1
else:
    currentRow -= 1
```

---

### Step 7

Join all rows.

```python
return "".join(rows)
```

---

## Dry Run

Input

```
s = "PAYPALISHIRING"
numRows = 3
```

| Character | Row |
|-----------|-----|
| P | 0 |
| A | 1 |
| Y | 2 |
| P | 1 |
| A | 0 |
| L | 1 |
| I | 2 |
| S | 1 |
| H | 0 |
| I | 1 |
| R | 2 |
| I | 1 |
| N | 0 |
| G | 1 |

Final rows:

```
Row 0 : PAHN
Row 1 : APLSIIG
Row 2 : YIR
```

Final answer:

```
PAHNAPLSIIGYIR
```

---

## Why does this work?

We never create the actual zigzag matrix.

Instead, we only remember:

- Current row
- Current direction

Whenever we reach:

- First row → Start moving down.
- Last row → Start moving up.

This correctly simulates the zigzag traversal while keeping the implementation simple and efficient.

---

## Complexity

**Time Complexity:** `O(n)`

Each character is processed once.

**Space Complexity:** `O(n)`

The rows together store all characters from the input string.