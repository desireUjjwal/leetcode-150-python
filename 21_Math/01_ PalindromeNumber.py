# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        num = x
        while num != 0:
            dig = num % 10
            num = num // 10
            reverse = reverse * 10 + dig
        if(reverse == x):
            return True
        else:
            return False
