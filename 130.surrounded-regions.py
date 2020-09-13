#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def dfs(self, i, j, board):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        if board[i][j] == 'X' or board[i][j] == 1:
            return

        board[i][j] = 1

        self.dfs(i+1, j, board)
        self.dfs(i, j+1, board)
        self.dfs(i-1, j, board)
        self.dfs(i, j-1, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
            
        nR = len(board)
        nC = len(board[0])

        for i in range(nR):
            for j in range(nC):
                if i == 0 or i == nR-1 or j == 0 or j == nC-1 and board[i][j] == 'O':
                    self.dfs(i, j, board)
        
        for i in range(nR):
            for j in range(nC):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(nR):
            for j in range(nC):
                if board[i][j] == 1:
                    board[i][j] = 'O'

        
# @lc code=end

