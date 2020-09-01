#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, end, curr, t):
            if t == 0:
                res.append(curr[:])
            elif t > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    backtrack(i+1, end, curr+[candidates[i]], t-candidates[i])

        candidates.sort()
        backtrack(0, len(candidates), [], target)
        return res
# @lc code=end

