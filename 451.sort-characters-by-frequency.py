#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = sorted(Counter(s).items(), key=lambda kv:kv[1], reverse=True)
        res = ''
        for i in cnt:
            res+=(i[0]*i[1])
        return res
# @lc code=end

