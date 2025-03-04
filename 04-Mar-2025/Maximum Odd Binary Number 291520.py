# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        size = len(s)
        count_1s = s.count('1')
        if count_1s == 1:
            return "0" * (size-1) + "1"  
        else:
            return "1" * (count_1s-1) + "0" * (size-count_1s) + "1"