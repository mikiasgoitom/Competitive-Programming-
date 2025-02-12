# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        i = 0
        while i < len(costs) and coins > 0:
            if costs[i] <= coins:
                ans += 1
                coins -= costs[i]
            else:
                break
            i += 1
        return ans