
# Explanation – Integer to Roman

## Idea

Roman numerals have fixed values:

| Value | Symbol |
|------:|:------|
|1000|M|
|900|CM|
|500|D|
|400|CD|
|100|C|
|90|XC|
|50|L|
|40|XL|
|10|X|
|9|IX|
|5|V|
|4|IV|
|1|I|

Instead of checking every possible number, we always choose the **largest value** that fits into the remaining number.

This is called a **Greedy Algorithm**.

---

## Dry Run (1994)

1994

→ 1000 = M

Remaining = 994

→ 900 = CM

Remaining = 94

→ 90 = XC

Remaining = 4

→ 4 = IV

Final Answer = **MCMXCIV**

---

## Why do we use `while`?

We use:

```python
while num >= values[i]:
```

because the same Roman numeral may appear multiple times.

Example:

3000

1000 → M

1000 → M

1000 → M

Result = **MMM**

Using `if` would only add one `M`, which is incorrect.

---

## Algorithm

1. Create value and symbol arrays.
2. Start with an empty string.
3. Traverse the arrays from largest to smallest.
4. While the value fits:
   - Append the symbol.
   - Subtract the value.
5. Return the result.