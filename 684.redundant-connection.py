#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findParent(self, parents, i):
        if parents[i] == -1:
            return i
        return self.findParent(parents, parents[i])

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [-1] * n
        res = []

        for i in range(n):
            x_par = self.findParent(parents, edges[i][0]-1)
            y_par = self.findParent(parents, edges[i][1]-1)
            if x_par != y_par:
                parents[y_par] = x_par
            else:
                res = edges[i]
        
        return res
# @lc code=end

