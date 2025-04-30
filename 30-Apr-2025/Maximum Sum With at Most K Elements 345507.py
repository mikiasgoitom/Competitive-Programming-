# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        possible = []
        
        for i, arr in enumerate(grid):
            for j, elt in enumerate(arr):
                heappush(possible, (-elt, i))
        
        count = 0
        res = 0
        
        while count < k:
            elt, idx = heappop(possible)

            if limits[idx] <= 0:
                continue
            limits[idx] -= 1
            count += 1
            res += elt
            
        return -res
