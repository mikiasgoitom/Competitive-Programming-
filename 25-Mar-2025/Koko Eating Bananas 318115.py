# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def eatingRate(self, rate, piles, hour):
        num_h = 0
        for pile in piles:
            num_h += math.ceil(pile/rate)
        return num_h <= hour
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (high + low) // 2
            if self.eatingRate(mid, piles, h):
                high = mid - 1
            else:
                low = mid + 1
        return low