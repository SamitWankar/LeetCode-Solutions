# LeetCode 8 — String to Integer (atoi)

## Problem

Given a string `s`, convert it into a 32-bit signed integer.

The conversion follows these rules:

1. Ignore leading whitespace.
2. Check for an optional `+` or `-` sign.
3. Read consecutive digits.
4. Stop when a non-digit character is encountered.
5. If the result is outside the 32-bit signed integer range, clamp it.

### Examples

```text
"42"           → 42
"   -42"       → -42
"4193 with words" → 4193
"words and 987"  → 0
"+7"           → 7
```

## Approach

We use an index `i` to scan the string.

### Step 1 — Skip spaces

Move `i` forward while the current character is a space.

### Step 2 — Check the sign

Set:

```text
sign = 1
```

If the character is `-`, change the sign to `-1`.

If the character is `+`, keep the sign as `1`.

### Step 3 — Build the number

For every digit:

```text
num = num * 10 + digit
```

For example:

```text
4 → 42 → 425
```

### Step 4 — Apply the sign

```text
num = num * sign
```

### Step 5 — Handle overflow

A 32-bit signed integer has this range:

```text
-2147483648 to 2147483647
```

If the number exceeds this range, return the corresponding boundary value.

## Complexity

**Time Complexity:** `O(n)`

We scan the string at most once.

**Space Complexity:** `O(1)`

We only use a few variables.
