# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            front = i+1
            back = len(nums) - 1
            while(front < back):
                sum = nums[i] + nums[front] + nums[back]
                if(sum < 0):
                    front += 1
                elif(sum > 0):
                    back -= 1
                else:
                    result.append([nums[i], nums[front], nums[back]])
                    while(front < back and nums[front] == nums[front+1]):
                        front += 1
                    while(front < back and nums[back] == nums[back-1]):
                        back -= 1
                    front += 1
                    back -= 1 
        return result
                
            
        
        
