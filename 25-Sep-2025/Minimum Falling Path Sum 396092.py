# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dp(i, j):
            if i >= len(matrix) or j >= len(matrix[0]) or j < 0:
                return float('inf')

            if i == len(matrix) - 1 and 0 <= j < len(matrix[0]):
                return matrix[i][j]

            if (i, j) not in memo:
                memo[(i, j)] = min(dp(i + 1, j), dp(i + 1, j - 1), dp(i + 1, j + 1)) + matrix[i][j]
            
            return memo[(i, j)]
        
        ans = float('inf')
        for i in range(len(matrix[0])):
            ans = min(ans, dp(0, i))
        
        # print(memo)
        return ans