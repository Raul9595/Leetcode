#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, end, curr):
            res.append(curr)
            for i in range(start, end):
                backtrack(i+1, end, curr+[nums[i]])
        
        backtrack(0, len(nums), [])
        return res
# @lc code=end

