#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, end, curr):
            if curr not in res:
                res.append(curr)
            for i in range(start, end):
                backtrack(i+1, end, curr+[nums[i]])
        
        nums.sort()
        backtrack(0, len(nums), [])
        return res
# @lc code=end

