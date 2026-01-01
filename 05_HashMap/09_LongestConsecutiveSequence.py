# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = set(nums)

        longestSeq = 0
        for n in st:
            if (n-1) not in st: # this condition will let start this while only at the beginning
                seq = 1
                while(n + seq) in st:
                    seq += 1
                longestSeq = max(longestSeq, seq)
        return longestSeq

