class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while(k>len(nums)):
            k=k-len(nums)
        if(len(nums)!=1):    
            res = []
            for i in range (len(nums)-k, len(nums)):
                res.append(nums[i])
            
            for j in range (len(nums)-k):
                res.append(nums[j])
        
            nums[:] = res
        
