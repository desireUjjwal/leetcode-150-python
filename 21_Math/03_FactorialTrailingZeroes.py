# 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
