# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        cost_size = len(costs)
        for i in range(cost_size):
            diff.append((costs[i][1] - costs[i][0], i))

        diff.sort()

        min_cost = 0
        mid = cost_size // 2
        for i in range(cost_size):
            if i < mid:
                min_cost += costs[diff[i][1]][1]
            else:
                min_cost += costs[diff[i][1]][0]
        return min_cost