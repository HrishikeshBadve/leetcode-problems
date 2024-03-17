"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example:
Input: n = 27
Output: true
Explanation: 27 = 3^3
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        if(n==1):
            return True
        
        max_power = 1
        while (max_power < n):
            max_power *= 3
        

        return max_power == n
