#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr, start, end, t):
            if t == 0:
                res.append(curr[:])
            elif t > 0:
                for i in range(start, end):
                    backtrack(curr+[candidates[i]], i, end, t-candidates[i])

    
        backtrack([], 0, len(candidates), target)
        return res
# @lc code=end

