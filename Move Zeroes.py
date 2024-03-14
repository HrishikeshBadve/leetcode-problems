"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example:-
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if(nums[i]==0):
                for j in range(i+1,len(nums)):
                    if(nums[j]!=0):
                        temp=nums[i]
                        nums[i]=nums[j]
                        nums[j]=temp
                        break
