#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, end):
            if start == end:
                res.append(nums[:])
            for i in range(start, end):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0, len(nums))
        return res
# @lc code=end

