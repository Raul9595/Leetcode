#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findParent(self, parents, i):
        if parents[i] == -1:
            return i
        return self.findParent(parents, parents[i])

    def findCircleNum(self, M: List[List[int]]) -> int:
        num = len(M)
        parent = [-1]*num
        
        for i in range(num):
            for j in range(num):
                if M[i][j] == 1 and i<j:
                    x_par = self.findParent(parent, i)
                    y_par = self.findParent(parent, j)
                    if x_par != y_par:
                        parent[y_par] = x_par
        
        return len([item for item in parent if item==-1])
# @lc code=end

