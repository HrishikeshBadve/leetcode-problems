"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example:
Input: s = "leetcode"
Output: 0
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        for i in s:
            hashmap[i]=1
        for i in s:
            hashmap[i]+=1
        for i in range(len(s)):
            if(hashmap[s[i]]==2):
                return i
        return -1
        
