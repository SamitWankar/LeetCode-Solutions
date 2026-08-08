class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        num = 0

        # 1. Skip leading spaces
        while i < len(s) and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        # 3. Read digits
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # 4. Apply sign
        num = num * sign

        # 5. Clamp to 32-bit integer range
        num = max(-2147483648, min(num, 2147483647))

        return num