# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        dp = [[0] * (W + 1) for _ in range(len(wt) + 1)]
        res = 0
        for i in range(1, len(wt) + 1):
            for cap in range(1, W + 1):
                # print(cap)
                exc = dp[i - 1][cap]
                inc = 0
                if cap >= wt[i - 1]:
                    inc  = dp[i - 1][cap - wt[i - 1]] + val[i - 1]
                    
                dp[i][cap] = max(exc, inc)
                            
                    
        # print(dp)
        return dp[len(wt)][W]
        # def dp(i, capacity):
        #     if capacity <= 0:
        #         return 0
        #     if i == len(wt):
        #         return 0
            
        #     if (i, capacity) not in memo:
        #         exc = dp(i + 1, capacity)
        #         inc = 0
        #         if capacity >= wt[i]:
        #             inc  = dp(i + 1, capacity - wt[i]) + val[i]
                    
        #         memo[(i, capacity)] = max(exc, inc)
                

        #     return memo[(i, capacity)]
            
        # return dp(0, W)
        # print(memo)