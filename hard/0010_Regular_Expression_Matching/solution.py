class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def match(i, j):
            # Check if this state is already calculated
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern is finished
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (
                s[i] == p[j] or p[j] == '.'
            )

            # If the next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                result = (
                    match(i, j + 2)
                    or
                    (first_match and match(i + 1, j))
                )
            else:
                # Normal character or '.'
                result = first_match and match(i + 1, j + 1)

            # Store the result
            memo[(i, j)] = result

            return result

        return match(0, 0)