# Explanation — Valid Parentheses

## Approach

This problem is solved using a **Stack**.

A stack follows **LIFO (Last In, First Out)**, which is exactly what we need because the most recently opened bracket must be closed first.

## Algorithm

1. Create an empty stack.
2. Create a mapping between closing and opening brackets:
   - `)` → `(`
   - `]` → `[`
   - `}` → `{`
3. Traverse the string from left to right.
4. If the current character is an opening bracket, push it onto the stack.
5. If it is a closing bracket:
   - If the stack is empty, return `False`.
   - Check whether the top of the stack matches the expected opening bracket.
   - If it does not match, return `False`.
   - Otherwise, pop the opening bracket.
6. After processing the entire string, return `True` only if the stack is empty.

## Example

For:

`([{}])`

The stack changes like this:

```text
(       → push
([      → push
([{     → push
([      → match } with {
(       → match ] with [
        → match ) with (