# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        res = 0
        j = 0
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[j])
                j += 1
            st.add(s[i])
            res = max(res, len(st))
        return res
