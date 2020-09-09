#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is "":
            return []
        d = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno',
        '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        mx = len(digits)
        for ch1 in d[digits[0]]:
            self.backtrack(ch1,1,res,mx,d,digits)
        
        return res
    
    def backtrack(self, ch1, s, res, mx, d, digits):
        if s == mx:
            res.append(ch1)
            return
        for ch2 in d[digits[s]]:
            tmp = ch1+ch2
            self.backtrack(tmp, s+1, res, mx, d, digits)
        

# @lc code=end

