# Explanation — Find the Index of the First Occurrence in a String

## Problem

Given two strings `haystack` and `needle`, find the index of the first occurrence of `needle` in `haystack`.

If `needle` does not occur in `haystack`, return `-1`.

## Approach

We check every possible starting position in `haystack`.

At each index `i`, we take a substring having the same length as `needle`:

```python
haystack[i:i + len(needle)]
```

Then we compare that substring with `needle`.

* If they are equal, return `i`.
* Otherwise, continue to the next index.
* If no match is found, return `-1`.

## Example

```text
haystack = "sadbutsad"
needle = "sad"
```

Indexes:

```text
s a d b u t s a d
0 1 2 3 4 5 6 7 8
```

At index `0`:

```text
" sad " == "sad"
```

So we return:

```text
0
```

## Complexity

### Time Complexity

`O(n × m)` in the worst case, where:

* `n` = length of `haystack`
* `m` = length of `needle`

### Space Complexity

`O(m)` for the temporary substring comparison.
