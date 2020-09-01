#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            rev = target - val
            if rev in d:
                return [d[rev], i]
            else:
                d[val] = i
# @lc code=end

