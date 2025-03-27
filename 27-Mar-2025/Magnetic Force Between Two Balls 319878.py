# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(diff):
            num_b = m - 1
            # rem_box = len(position) - 1
            # bigger = 0
            curr = position[0]
            for i in range(1, len(position)):
                if abs(position[i] - curr) >= diff:
                    num_b -= 1
                    curr = position[i]
            return num_b <= 0                

        low, high = 1, (position[-1] - position[0])
        while low <= high:
            mid = (high + low) // 2
            if helper(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
        # print(helper(3))