# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

sys.setrecursionlimit(10**7)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
            
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        
        # print(dp)
        return dp[n]

        # def dp(n):
        #     if n == 0:
        #         return 0
        #     elif n == 1 or n == 2:
        #         return 1
            
        #     if n not in memo:
        #         memo[n] = dp(n - 3) + dp(n - 2) + dp(n - 1)
        #     return memo[n]
        
        # return dp(n)
        