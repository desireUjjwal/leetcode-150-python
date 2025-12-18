238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        ans = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        for i in range(0, n):
            ans[i] = prefix[i] * postfix[i]
        return ans
# Space Optimized
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        postfix = 1
        for i in range(n-2, -1, -1):
            postfix *= nums[i+1]
            ans[i] = ans[i] * postfix
        return ans

        
