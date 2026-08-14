# LeetCode 13 - Roman to Integer

## Problem

Given a Roman numeral string, convert it into an integer.

## Examples

- `III` → `3`
- `LVIII` → `58`
- `MCMXCIV` → `1994`

## Roman Numeral Values

| Symbol | Value |
|--------|-------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

## Approach

We store the Roman numeral values in a dictionary.

For every character:

- If its value is smaller than the value of the next character, subtract it.
- Otherwise, add it.

### Example

For `MCMXCIV`:

```text
M - C + M - X + C - I + V
1000 - 100 + 1000 - 10 + 100 - 1 + 5
= 1994