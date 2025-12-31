# 202. Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# --> Starting with any positive integer, replace the number by the sum of the squares of its digits.
# --> Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# --> Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    def sumOfSquare(self, n: int) -> int:
        squaredAddition = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            squaredAddition += digit
            n = n // 10
        return squaredAddition
        

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquare(n)

            if n == 1:
                return True
        return False
