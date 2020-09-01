#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, end):
            if start == end and nums not in res:
                res.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[i], nums[start] = nums[start], nums[i]
        
        backtrack(0, len(nums))
        return res
# @lc code=end

