#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i, val in enumerate(intervals):
            if res and intervals[i][0]<=res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(val)
        return res
# @lc code=end

