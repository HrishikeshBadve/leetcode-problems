"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:-
Input: nums = [2,2,1]
Output: 1
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            sampleset = set(nums)
            sumnums = 0
            for i in range(len(nums)):
                sumnums+=nums[i]
            sumset = sum(sampleset)
            temp = (2*sumset) - sumnums
            return temp
            
