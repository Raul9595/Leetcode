#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0 and matrix[k][j] != float('inf'):
                            matrix[k][j] = float('inf')
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0 and matrix[i][k] != float('inf'):
                            matrix[i][k] = float('inf')
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
# @lc code=end

