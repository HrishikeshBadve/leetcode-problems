"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(needle not in haystack):
            return -1

        for i in range(len(haystack)):
            if(haystack[i]==needle[0]):
                temp = haystack[i:i+len(needle)]
                if(temp==needle):
                    return i
        return -1
