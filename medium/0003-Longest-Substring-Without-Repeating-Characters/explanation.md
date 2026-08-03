# Explanation

## Intuition

The goal is to find the longest substring where every character appears only once.

Checking every possible substring would be very slow, so we use the **Sliding Window** technique.

The window expands to include new characters and shrinks whenever a duplicate character is found.

---

## Sliding Window

We maintain two pointers:

- **left** → Start of the current window
- **right** → End of the current window

Example:

```text
abcabcbb
↑
left

↑
right
```

The window always contains **unique characters**.

---

## Data Structure

A **set** is used to store the characters currently inside the window.

Example:

```python
seen = {'a', 'b', 'c'}
```

Checking whether a character exists in a set takes approximately **O(1)** time.

---

## Dry Run

Consider:

```text
s = "abcabcbb"
```

### Step 1

Window:

```text
a
```

Unique characters.

Length = 1

---

### Step 2

Window:

```text
ab
```

Length = 2

---

### Step 3

Window:

```text
abc
```

Length = 3

---

### Step 4

Next character:

```text
a
```

Duplicate found.

Remove characters from the left until the duplicate disappears.

Window becomes:

```text
bca
```

Length remains 3.

---

Continue the same process until the string ends.

The longest valid window has length **3**.

---

## Code Walkthrough

### Create an empty set

```python
seen = set()
```

Stores all characters currently inside the window.

---

### Left pointer

```python
left = 0
```

Marks the beginning of the sliding window.

---

### Maximum answer

```python
max_length = 0
```

Stores the length of the longest valid substring found so far.

---

### Traverse the string

```python
for right in range(len(s)):
```

The `right` pointer expands the window one character at a time.

---

### Remove duplicates

```python
while s[right] in seen:
    seen.remove(s[left])
    left += 1
```

If the current character already exists in the window:

- Remove the leftmost character.
- Move the left pointer.
- Repeat until the duplicate is removed.

---

### Add current character

```python
seen.add(s[right])
```

Insert the current character into the window.

---

### Update answer

```python
max_length = max(max_length, right - left + 1)
```

Current window length is:

```text
right - left + 1
```

Compare it with the previous maximum.

---

### Return answer

```python
return max_length
```

After traversing the entire string, return the longest valid substring length.

---

## Example Visualization

```text
Input:
abcabcbb

Window Expansion

a
ab
abc

Duplicate 'a'

Remove 'a'

Window

bca

Duplicate 'b'

Remove 'b'

Window

cab

Continue...

Maximum Length = 3
```

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

Each character is added to and removed from the set at most once.

---

### Space Complexity

```
O(n)
```

The set stores only the unique characters in the current window.

---

## Key Learning

This problem is a classic example of the **Sliding Window** technique.

It teaches:

- Two-pointer approach
- Efficient window expansion and shrinking
- Using a set for constant-time lookup
- Optimizing from `O(n³)` brute force to `O(n)` using a sliding window