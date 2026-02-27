# 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = 1
        for i in range(1, x//2 + 1):
            if i * i <= x:
                ans = i
            else:
                break
        return ans
