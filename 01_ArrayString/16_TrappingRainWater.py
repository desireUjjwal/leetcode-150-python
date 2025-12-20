# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

  class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        maxHeight = height[0]
        for i in range(1, n-1):
            maxHeight = max(maxHeight, height[i-1])
            left[i] = maxHeight
        maxHeight = height[-1]
        for i in range(n-2, 0, -1):
            maxHeight = max(maxHeight, height[i+1])
            right[i] = maxHeight
        totalArea = 0
        for i in range(1, n-1):
            if min(left[i], right[i]) - height[i] > 0:
                totalArea += min(left[i], right[i]) - height[i]
        return totalArea


# Space Optimised
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = height[0]
        right = height[-1]
        i = 0
        j = n - 1
        totalArea = 0
        while i < j:
            if left <= right:
                i += 1
                left  = max(left, height[i])
                totalArea += left - height[i] 
            else:
                j -= 1
                right = max(right, height[j])
                totalArea += right - height[j]
        return totalArea

        
