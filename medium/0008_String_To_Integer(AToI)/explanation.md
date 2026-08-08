# Explanation — String to Integer (atoi)

## Main Idea

The problem is basically a controlled string scan.

We process the string in this order:

```text
Spaces → Sign → Digits → Apply Sign → Check Range
```

## Example

Consider:

```text
s = "   -42abc"
```

### 1. Skip spaces

The first three characters are spaces, so we move the index forward.

```text
   -42abc
      ↑
```

### 2. Check the sign

We find `-`, so:

```python
sign = -1
```

Then move to the next character.

### 3. Read digits

We start with:

```python
num = 0
```

For `4`:

```text
num = 0 * 10 + 4
num = 4
```

For `2`:

```text
num = 4 * 10 + 2
num = 42
```

The next character is `a`, which is not a digit, so we stop.

### 4. Apply the sign

```text
num = 42 * -1
num = -42
```

### 5. Check the 32-bit range

The valid range is:

```text
-2147483648 ≤ num ≤ 2147483647
```

Since `-42` is inside the range, the final answer is:

```text
-42
```

## Important Formula

To construct a number digit by digit:

```python
num = num * 10 + int(s[i])
```

For example, constructing `123`:

```text
0 → 1 → 12 → 123
```

## Edge Cases

| Input               |        Output |
| ------------------- | ------------: |
| `"42"`              |          `42` |
| `"   -42"`          |         `-42` |
| `"4193 with words"` |        `4193` |
| `"words and 987"`   |           `0` |
| `"+"`               |           `0` |
| `"-"`               |           `0` |
| `"91283472332"`     |  `2147483647` |
| `"-91283472332"`    | `-2147483648` |
