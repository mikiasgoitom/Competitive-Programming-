# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)

        def dfs(i, j):
            if i >= m or j < 0 or j >= n:
                return 0
            if i == m - 1 or j == n-1:
                return 1
            
            if (i, j) not in memo:
                if j + 1 < n:
                    memo[(i, j)] += dfs(i, j + 1)
                if i + 1 < m:
                    memo[(i, j)] += dfs(i + 1, j)
            
            return memo[(i, j)]
        
        return dfs(0, 0)