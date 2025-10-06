# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """ memo = {}
        rows = len(triangle)

        def dfs(i, j):
            if i >= rows or j >= len(triangle[i]):
                return float('inf')

            if i == rows - 1:
                return triangle[i][j]
            
            if (i, j) not in memo:
                memo[(i,j)] = min(dfs(i + 1, j + 1), dfs(i + 1, j)) + triangle[i][j]
            
            return memo[(i, j)]
        
        return dfs(0, 0) """
        dp = []
        for i in range(len(triangle)):
            dp.append([0] * (i + 1))

        for j in range(len(triangle[-1])):
            dp[-1][j] = triangle[-1][j]

        # print(dp)
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r]) -1 , -1, -1):
                dp[r][c] = min(dp[r + 1][c + 1], dp[r+1][c]) + triangle[r][c]
        
        return dp[0][0]