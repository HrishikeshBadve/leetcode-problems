"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 
Example:-
Input: board = 
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
Output: true
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        "Rows"
        for i in board:
            seen = set()
            for j in i:
                if(j!='.'):
                    if j in seen:
                        return False
                    seen.add(j)
                    
        "Columns"
        for i in range (9):
            seen = set()
            for j in range (9):
                if board[j][i] != '.':
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
                    
        "3x3 Boxes"
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen=set()
                for k in range (i,i+3):
                    for l in range (j,j+3):
                        if board[k][l]!='.':
                            if board[k][l] in seen:
                                return False
                            seen.add(board[k][l])
                
        
        
        return True
