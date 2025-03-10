# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        # print(ceil(n/2), floor(n/2))
        half_n = self.my_pow(x, n//2)
        if n % 2 == 0:
            return half_n * half_n
        else:
            return x * half_n * half_n
        # return self.my_pow(x, ceil(n/2)) * self.my_pow(x, floor(n/2))
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.my_pow(x, (n*-1))
        else:
            return self.my_pow(x, n)
        # if n == 0:
        #     return 1
        # elif n % 2 == 0:
        #     twice = self.myPow(x, n/2)
        #     return twice * twice
        # elif n < 0:
        #     return 1 / x * self.myPow(x, n+1)
        # else:
        #     return x * self.myPow(x, n-1)
