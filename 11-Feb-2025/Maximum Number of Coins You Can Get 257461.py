# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True) 
        n = len(piles)
        me = 1
        ans = 0
        iter = n // 3
        while iter > 0:
            ans += piles[me]
            me += 2
            iter -= 1
        return ans

