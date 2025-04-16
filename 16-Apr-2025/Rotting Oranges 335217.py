# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        sources = []
        m, n = len(grid), len(grid[0])
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    sources.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        # print("ddd", fresh)
        qu = deque(sources)
        count = 0
        inbound = lambda r, c: True if (0 <= r < m and 0 <= c < n) else False
        while qu:
            count += 1
            qsz = len(qu)
            for _ in range(qsz):
                nr, nc = qu.popleft()

                for gr, gc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    rr = nr + gr
                    cc = nc + gc
                    if inbound(rr, cc) and grid[rr][cc] == 1:
                        # print(inbound(rr, cc), rr, cc)
                        grid[rr][cc] = 0
                        fresh -= 1
                        qu.append((rr, cc))
        # print(fresh)
        if len(sources) > 0 and fresh == 0:
            return count - 1
        elif fresh == 0:
            return 0
        else:
            return -1
        
                    
                
        

                
