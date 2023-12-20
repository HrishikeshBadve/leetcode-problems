"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:-
Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        def sort(st):
            for i in range(len(st)):
                minst=i
                for j in range (i+1,len(st)):
                    if st[j]<st[minst]:
                        minst=j
                temp=st[i]
                st[i]=st[minst]
                st[minst]=temp
        """
        s2=sorted(s)
        t2=sorted(t)
        if(s2==t2):
            return True
        else:
            return False
