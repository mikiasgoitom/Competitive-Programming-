# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def check_pow_four(self, n):
        if n < 1:
            return False
        if n == 1:
            return True
        return self.check_pow_four(n / 4)
    def isPowerOfFour(self, n: int) -> bool:
        return self.check_pow_four(n)