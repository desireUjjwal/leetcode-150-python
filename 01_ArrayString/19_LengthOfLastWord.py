# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(" ")
        for i in range(len(lst)-1, -1, -1):
            print(lst[i])
            if len(lst[i]) != 0:
                return len(lst[i])

# Another solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')
        return len(words[-1])
