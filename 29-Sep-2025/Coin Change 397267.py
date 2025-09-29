# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return float('inf')
            
            if remain in memo:
                return memo[remain]

            memo[remain] = float('inf')
            
            for coin in coins:
                if remain >= coin:
                    memo[remain] = min(memo[remain], dfs(remain - coin) + 1)  
                    # print(memo[remain])         
            
            return memo[remain]
        
        ans = dfs(amount) 
        if ans == float('inf'):
            return -1
        else:
            return ans
