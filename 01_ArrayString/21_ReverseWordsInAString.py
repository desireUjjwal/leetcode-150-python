# 51. Reverse Words in a String

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ""
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
            if i != 0:
                res += " "
        return res
