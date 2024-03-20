"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = 1

        res=""
        for i in range(len(strs[0])):
            count=0
            prefix = (strs[0])[:length]
            for string1 in strs:
                if(string1[:length]==prefix):
                    count+=1
            
            if count==len(strs):
                length+=1
                res=prefix
        return res
