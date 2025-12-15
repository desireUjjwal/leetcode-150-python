45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxReach = 0
        steps = 0
        farthestReach = 0
        for i in range(n):
            if maxReach + i + 1 >= n:
                return steps
            if nums[i] > maxReach:
                farthestReach = max(farthestReach, nums[i])
            
            if maxReach == 0:
                maxReach = farthestReach
                steps += 1
            maxReach -= 1
            farthestReach -= 1
