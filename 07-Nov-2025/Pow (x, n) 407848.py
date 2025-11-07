# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def divide(base, exp):
            res = 1
            while exp > 0:
                if exp % 2 == 1:
                    res *= base
                base *= base
                exp //= 2
            return res
        
        if n < 0:
            return 1 / divide(x, -n)
        else:
            return divide(x, n)