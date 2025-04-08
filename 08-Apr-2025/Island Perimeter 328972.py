# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        def dfs(grid, row, col):
            visited[row][col] = 1

            sides = 0
            for go_row, go_col in directions:
                new_row = row + go_row
                new_col = col + go_col
                if (not inbound(new_row, new_col)) or (not grid[new_row][new_col]):
                    sides += 1
            
            for go_row, go_col in directions:
                new_row = row + go_row
                new_col = col + go_col
                                
                if inbound(new_row, new_col) and (not visited[new_row][new_col]) and grid[new_row][new_col]:
                    sides += dfs(grid, new_row, new_col)
            
            return sides
        
        num_ilands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(row, col, num_ilands)
                if not visited[row][col] and grid[row][col]:
                    num_ilands += dfs(grid, row, col)
                    
        
        return num_ilands
            
        