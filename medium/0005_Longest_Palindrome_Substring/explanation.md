# Explanation

## Intuition

Instead of checking every possible substring, observe that every palindrome has a center.

There are two possible centers:

### Odd Length

```text
racecar

   e
```

### Even Length

```text
abba

 ↑ ↑
```

Therefore, for every index in the string, we check both possibilities.

---

## Expand Around Center

We create a helper function:

```python
expand(left, right)
```

The function keeps expanding outward while:

- `left` is inside the string.
- `right` is inside the string.
- Both characters are equal.

When expansion stops, it returns the starting and ending indices of the palindrome.

---

## Main Idea

For every index:

- Find the largest odd palindrome.
- Find the largest even palindrome.
- Compare both with the current longest palindrome.
- Update the answer if needed.

Finally, return the substring using the stored indices.

---

## Example

Input

```text
babad
```

Iteration:

```
i = 0 → "b"

Longest = "b"
```

```
i = 1 → "bab"

Longest = "bab"
```

```
i = 2 → "aba"

Same length as "bab"
```

```
i = 3 → "a"
```

```
i = 4 → "d"
```

Final Answer

```text
bab
```

---

## Why Expand Around Center?

Brute Force:

- Generate every substring.
- Check whether it is a palindrome.

Time Complexity:

```
O(n³)
```

Expand Around Center:

- Visit every possible center once.
- Expand only while characters match.

Time Complexity:

```
O(n²)
```

This makes the solution much faster while using constant extra space.

---

## Key Learning

- Every palindrome has a center.
- Check both odd and even centers.
- Store only the longest palindrome found.
- Return the substring using the saved indices.