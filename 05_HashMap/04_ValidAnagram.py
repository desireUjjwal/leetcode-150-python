# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        for c in s:
            countS[c] = 1 + countS.get(c, 0)
        for c in t:
            if c in countS:
                countS[c] -= 1
                if countS[c] < 0:
                    return False
            else:
                return False
        return True
