class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # If there is only one row (or the string is shorter than the number of rows),
        # no zigzag pattern can be formed.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an empty string for each row.
        rows = [""] * numRows

        # Start from the first row.
        currentRow = 0

        # Direction of movement.
        # False = moving up
        # True = moving down
        goingDown = False

        # Process each character in the string.
        for char in s:

            # Add the character to the current row.
            rows[currentRow] += char

            # Change direction if we are at the first or last row.
            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown

            # Move to the next row.
            if goingDown:
                currentRow += 1
            else:
                currentRow -= 1

        # Combine all rows into one string.
        return "".join(rows)