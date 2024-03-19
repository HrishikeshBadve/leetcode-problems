"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Example:-
Input: x = 123
Output: 321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            str1 = str(x)
            str1=str1[::-1]
            x=int(str1)
        else:
            x=abs(x)
            str1 = str(x)
            str1=str1[::-1]
            x=int(str1)
            x=-x
        if(x>=pow(-2,31) and x<=pow(2,31)-1):
            return x
        else:
            return 0
