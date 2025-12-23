# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(0, min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            else:
                res += first[i]
        return res
