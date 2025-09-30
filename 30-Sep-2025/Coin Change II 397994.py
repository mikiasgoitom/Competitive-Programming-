# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, amt):
            if amt == 0:
                return 1
            
            if amt < 0:
                return 0
            
            if i >= len(coins):
                return 0

            if (i, amt) not in memo:
                memo[(i, amt)] = dfs(i, (amt - coins[i])) + dfs(i + 1, amt)
            return memo[(i, amt)]
        
        return dfs(0, amount)