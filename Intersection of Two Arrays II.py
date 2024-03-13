class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        if (len(nums1)<len(nums2)):
            for i in nums1:
                for j in nums2:
                    if(i==j):
                        res.append(i)
                        nums2.remove(j)
                        break
        else:
            nums2set=set(nums2)
            for i in nums2:
                for j in nums1:
                    if(i==j):
                        res.append(i)
                        nums1.remove(j)
                        break
        return res
