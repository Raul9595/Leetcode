#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, mn, mx):
        if not root:
            return True
        
        if root.val>=mx or root.val<=mn:
            return False

        return self.dfs(root.right, root.val, mx) and self.dfs(root.left, mn, root.val)
# @lc code=end

