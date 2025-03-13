# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # fac = 1
        ans = 0
        
        while n > 0:
            ans += n // 5
            n //= 5
        return ans
