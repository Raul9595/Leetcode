#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(numbers):
            rev = target - val
            if rev in d:
                return sorted([i+1, d[rev]+1])
            else:
                d[val] = i
# @lc code=end

