# 0020 - Valid Parentheses

## Problem

Given a string `s` containing only the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

A valid string satisfies:

1. Every opening bracket has a corresponding closing bracket.
2. Brackets close in the correct order.
3. Every closing bracket matches the most recent opening bracket.

## Approach

Use a stack.

- Push every opening bracket onto the stack.
- For every closing bracket:
  - Check that the stack is not empty.
  - Check whether the top of the stack is the matching opening bracket.
  - Pop the opening bracket.
- At the end, the stack must be empty.

## Complexity

- Time: O(n)
- Space: O(n)

## Key Concept

Stack - LIFO (Last In, First Out)