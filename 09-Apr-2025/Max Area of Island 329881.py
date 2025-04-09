# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_i = 0
        direction = [(0,1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        visited = []

        def dfs(row, col, ara):
            nonlocal visited
            if grid[row][col] == 0:
                return 0 

            visited.append((row, col))
            ara = 1

            for nrow, ncol in direction:
                gorow = nrow + row
                gocol = ncol + col

                if inbound(gorow, gocol) and (gorow, gocol) not in visited and grid[gorow][gocol] == 1:
                    ara += dfs(gorow, gocol, ara)
            
            return ara
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # print("a",visited)
                if (r, c) not in visited and grid[r][c] == 1:
                    max_i = max(max_i, dfs(r, c, 0))
                # print("ara", max_i)
        
        return max_i
