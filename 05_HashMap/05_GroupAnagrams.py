# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            res[key].append(word)
        return list(res.values())

# Optimized time complexity but it may take extra space depending on the test cases
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26  # for storing from a to z

            for c in word:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(word)
        return list(res.values())
            
