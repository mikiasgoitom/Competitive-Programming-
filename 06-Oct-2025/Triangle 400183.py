# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        rows = len(triangle)
        mx_cols = len(triangle[-1])

        def dfs(i, j):
            if i >= rows or j >= len(triangle[i]):
                return float('inf')

            if i == rows - 1:
                return triangle[i][j]
            
            if (i, j) not in memo:
                memo[(i,j)] = min(dfs(i + 1, j + 1), dfs(i + 1, j)) + triangle[i][j]
            
            return memo[(i, j)]
        
        return dfs(0, 0)