#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for j in range(len(nums)-2):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            target = (-nums[j])
            d = {}
            for i, val in enumerate(nums[j+1:]):
                rev = target - val
                if rev in d:
                    res.add((-target, rev, val))
                else:
                    d[val] = i
        return map(list, res)
# @lc code=end

