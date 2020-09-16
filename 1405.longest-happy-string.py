#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
from collections import OrderedDict
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a<3 and b<3 and c<3:
            return 'a'*a + 'b'*b +'c'*c
        
        res = ''
        n = 'a'*a + 'b'*b +'c'*c
        cnt = Counter(n)
        
        for i in range(a+b+c):
            if len(res)<2 or (len(res)>=2 and res[-1] != res[-2]):
                ch = max(cnt, key=cnt.get)
                res+=ch
                cnt[ch]-=1
            else:
                for key, val in cnt.items():
                    if key!=res[-1] and val!=0:
                        res+=key
                        cnt[key]-=1
                        break
        return res
# @lc code=end

