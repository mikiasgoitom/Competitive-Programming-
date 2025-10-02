# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * (2) for _ in range( len(prices) + 1 )]
        dp[1][1] = -prices[0]
        
        # print(dp)
        for day in range(2, len(prices) + 1):
            for sell in range(2):
                if sell == 0:
                    dp[day][sell] = max(dp[day - 1][sell], dp[day - 1][sell + 1] + prices[day - 1])
                else:
                    dp[day][sell] = max(dp[day - 1][sell], dp[day - 2][sell - 1] - prices[day - 1])
        # print(dp)
        return dp[len(prices)][0]
        """ memo = {}

        def dfs(i, sell):
            if i >= len(prices):
                return 0
            
            if (i, sell) not in memo:
                opt1, opt2 = 0, 0
                if sell:
                    opt1 = dfs(i + 2, not sell) + prices[i]
                else:
                    opt2 = dfs(i + 1, not sell) - prices[i]
                opt3 = dfs(i + 1, sell)
                memo[(i, sell)] = max(opt1, opt2, opt3)
            
            return memo[(i, sell)]
        
        return dfs(0, False)
 """