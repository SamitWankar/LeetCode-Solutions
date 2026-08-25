class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_count, close_count):
            # Base case: current string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still have opening parentheses available
            if open_count < n:
                backtrack(
                    current + "(",
                    open_count + 1,
                    close_count
                )

            # Add ')' only if there is an unmatched '('
            if close_count < open_count:
                backtrack(
                    current + ")",
                    open_count,
                    close_count + 1
                )

        # Start with an empty string
        backtrack("", 0, 0)

        return result