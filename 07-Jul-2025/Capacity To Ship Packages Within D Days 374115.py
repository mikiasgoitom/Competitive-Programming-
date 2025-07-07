# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight =  max(weights)

        def validator(cap):
            days_needed = 1
            total = 0
            
            for w in weights:

                if total + w > cap:
                    total = 0
                    days_needed += 1

                total += w

            return days_needed <= days

        low, high = max_weight, sum(weights)

        while low <= high:
            mid = (high + low) // 2

            if validator(mid):
                high = mid - 1 
            else:
                low = mid + 1
        
        return low