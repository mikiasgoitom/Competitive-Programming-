# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] 

        def inbound(row, col): 
            return (0 <= row < len(grid) and 0 <= col < len(grid[0])) 

        def dfs(grid, row, col): 
            if grid[row][col] == "0": 
                return 

            grid[row][col] = "0" 

            for go_row, go_col in directions: 
                new_row = row + go_row 
                new_col = col + go_col 

                if inbound(new_row, new_col) and grid[new_row][new_col] == "1": 
                    dfs(grid, new_row, new_col)
            # return
        
        num_ilands = 0 
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == "1":
                    num_ilands += 1 
                    dfs(grid, row, col) 
        print("d",grid)
        return num_ilands