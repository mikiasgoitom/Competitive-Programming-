# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        dirs = {
            1: [(0, -1), (0, 1)], 
            2: [(-1, 0), (1, 0)], 
            3: [(0, -1), (1, 0)], 
            4: [(0, 1), (1, 0)],  
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)], 
        }
        opposite = {(0,1):(0,-1), (0,-1):(0,1), (1,0):(-1,0), (-1,0):(1,0)}

        qu = deque([(0,0)])
        visited = set([0,0])

        while qu:
            # print(qu)
            r, c = qu.popleft()
            if (r, c) == (n-1, m-1):
                return True
            for gr, gc in dirs[grid[r][c]]:
                nr, nc = r + gr, c + gc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    if opposite[(gr,gc)] in dirs[(grid[nr][nc])]:
                        qu.append((nr, nc))
                        visited.add((nr, nc))
        return False