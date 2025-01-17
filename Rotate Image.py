"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example:-
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        #Transpose
        for i in range (len(matrix)):
            for j in range(i+1,len(matrix)):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                
        #Swapping columns
        for i in range ((len(matrix)+1)/2):
            for j in range(len(matrix)):
                temp=matrix[j][i]
                matrix[j][i]=matrix[j][len(matrix)-1-i]
                matrix[j][len(matrix)-1-i]=temp
