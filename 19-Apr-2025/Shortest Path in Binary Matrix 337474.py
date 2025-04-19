# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rgsz, cgsz = len(grid) - 1, len(grid[0]) - 1
        if grid[0][0] != 0 or grid[rgsz][cgsz] != 0:
            return -1
        
        dirc = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

        moves = lambda r, c:[
            [r + gr, c + gc] for gr, gc in dirc if 0 <= r + gr <= rgsz and 0 <= c + gc <= cgsz 
        ]
        target = (rgsz, cgsz)
        que = deque([(0, 0)])
        visited = set([(0,0)])
        count = 0
        found = False
        while not found and que:
            for _ in range(len(que)):
                cr, cc = que.popleft()
                if (cr, cc) == target:
                    found = True
                    break
                
                for r, c in moves(cr,cc):
                    if (r, c) not in visited and grid[r][c] == 0:
                        que.append((r, c))
                        visited.add((r, c))
            count += 1
        
        if found:
            return count
        else:
            return -1

        
                    