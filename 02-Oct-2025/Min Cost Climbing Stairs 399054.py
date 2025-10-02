# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i not in memo:
                memo[i] = min(dfs(i + 1), dfs(i + 2)) + cost[i]

            return memo[i]
        return min(dfs(0), dfs(1))