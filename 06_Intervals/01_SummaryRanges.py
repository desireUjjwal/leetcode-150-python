# 228. Summary Ranges

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [(str(nums[0]))]

        res = []
        s = ''
        for i in range(len(nums)-1):
            if len(s) == 0:
                s += str(nums[i])
            if (nums[i]+1 == nums[i+1]):
                continue
            else:
                if s == str(nums[i]):
                    res.append(s)
                else:
                    s += "->"
                    s += str(nums[i])
                    res.append(s)
                s = ''
        if nums[-1] == nums[-2] + 1:
            s += "->"
            s += str(nums[-1])
        else:
            s += str(nums[-1])
        res.append(s)
        return res
