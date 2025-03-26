# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def validMinute(time):
            rem = cars
            for rank in ranks:
                rem -= floor((time/rank)**0.5)
            return rem <= 0
        low, high = 1, 10**14

        while low <= high:
            mid = (high + low) // 2
            # print(mid)
            if validMinute(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low