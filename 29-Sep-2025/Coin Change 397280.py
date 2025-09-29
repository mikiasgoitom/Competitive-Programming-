# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for rem_amount in range(amount + 1):
            for coin in coins:
                if rem_amount >= coin:
                    dp[rem_amount] = min(dp[rem_amount], dp[rem_amount - coin] + 1)

        # print(dp)
        ans = dp[amount]
        if ans == float('inf'):
            return -1
        return ans