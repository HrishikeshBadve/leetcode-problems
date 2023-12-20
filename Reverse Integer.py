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
        rev=0
        k=0
        if x<0:
            x=abs(x)
            k=1
        while x>0:
            temp=x%10
            rev=(rev*10)+temp
            x=x//10
        if k==1:
            rev=-rev
        if rev < pow(-2,31) or rev> pow(2,31)-1:
            return 0
        return rev
