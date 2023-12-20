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
            
