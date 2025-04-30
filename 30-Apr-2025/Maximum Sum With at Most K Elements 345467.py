# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        possible = []
        for i in range(len(grid)):
            temp = [0] * len(grid[0])
            
            for j in range(len(grid[i])):
                temp[j] = -(grid[i][j])
            
            heapify(temp)
            lmt = limits[i]

            for _ in range(lmt):
                possible.append(heappop(temp))
        
        heapify(possible)
        holder = []
        
        for _ in range(k):
            holder.append(heappop(possible))
        
        ans = [-1 * num for num in holder]
        
        return sum(ans)