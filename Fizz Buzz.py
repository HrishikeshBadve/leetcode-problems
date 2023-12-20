"""
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Example:-
Input: n = 3
Output: ["1","2","Fizz"]
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [0]*(n)
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5==0:
                res[i]="FizzBuzz"
            elif (i+1)%3==0:
                res[i]="Fizz"
            elif (i+1)%5==0:
                res[i]="Buzz"
            else:
                res[i]=str(i+1)
        return res
