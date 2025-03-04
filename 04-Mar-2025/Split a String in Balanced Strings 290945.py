# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        count_l = 0
        count_r = 0
        ans = 0
        for r in range(len(s)):
                
            if s[r] == 'L':
                count_l += 1
            elif s[r] == 'R':
                count_r += 1
            
            if count_l == count_r:
                ans += 1
                count_l = 0
                count_r = 0
        return ans