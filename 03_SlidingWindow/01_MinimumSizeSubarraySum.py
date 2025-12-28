# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        j = 0
        minLength = 1e5 + 1
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                minLength = min(minLength, i-j+1)
                sum -= nums[j]
                j += 1
        return minLength if minLength != 1e5 + 1 else 0
