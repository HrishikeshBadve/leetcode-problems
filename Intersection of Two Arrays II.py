"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must 
appear as many times as it shows in both arrays and you may return the result in any order.

Example:-
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums1:
            for j in nums2:
                if(i==j):
                    res.append(i)
                    nums2.remove(j)
                    break
        
        return res
