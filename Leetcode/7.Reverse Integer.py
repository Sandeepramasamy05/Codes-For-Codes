class Solution(object):
    def reverse(self, x):
        MIN_INT = -2**31         # -2147483648
        MAX_INT = 2**31 - 1      # 2147483647

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10             # IMPORTANT: integer division

        rev = rev * sign

        # overflow check
        if rev < MIN_INT or rev > MAX_INT:
            return 0

        return rev
