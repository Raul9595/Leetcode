#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        pos = {}
        for i, val in enumerate(s):
            d[val]+=1
            pos[val] = i
        
        for key, val in d.items():
            if val == 1:
                return pos[key]
        return -1
# @lc code=end

