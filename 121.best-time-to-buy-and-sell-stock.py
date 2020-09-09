#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        diff = 0
        mn = prices[0]
        mx = prices[0]
        for i in prices[1:]:
            if i == mn or i == mx:
                continue
            if i < mn:
                mn = i
                mx = i
            elif i > mx:
                mx = i
                diff = max(diff, mx - mn)

        return diff


# @lc code=end

