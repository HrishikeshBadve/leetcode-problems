"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:-
Input: nums = [1,2,3,1]
Output: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set=set(nums)
        if len(nums_set)==len(nums):
            return False
        else:
            return True
