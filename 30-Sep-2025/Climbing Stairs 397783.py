# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        dp = [0] * (n + 1)
        dp[n] = 1
        # dp[0] = 1

        for i in range(n - 1, -1, -1):
            if i + 2 > n:
                dp[i] = dp[i + 1]
            else:
                # print("touch")
                dp[i] = dp[i + 1] + dp[i + 2]
        
        # print(dp)
        return dp[0]