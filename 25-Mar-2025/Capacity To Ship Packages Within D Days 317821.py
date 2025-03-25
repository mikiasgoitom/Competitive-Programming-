# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def capacityChecker(self, capacity, weights, days):
        accum = 0
        num_d = 1
        for right in range(len(weights)):
            if accum + weights[right] > capacity:
                accum = weights[right]
                num_d += 1
            else:
                accum += weights[right]
        return num_d <= days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        print(low, high)
        while low <= high:
            mid = (high + low) // 2
            if self.capacityChecker(mid, weights, days):
                high = mid - 1
            else:
                low = mid + 1
        return low
        