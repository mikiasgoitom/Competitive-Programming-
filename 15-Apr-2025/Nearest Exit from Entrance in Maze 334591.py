# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        neb = lambda r, c: [
            (a, b) for a, b in [
                (r + 1, c), (r-1, c), (r, c + 1), (r, c - 1)
            ] if 0 <= a < m and 0 <= b < n
        ]

        print(neb(0, 0))

        qu = deque([entrance])
        chk = neb(*entrance)
        flag = False
        for nr, nc in chk:
            if maze[nr][nc] == '.':
                flag = True

        if not flag:    
            return -1

        step = 0
        visited = set()
        finished = False
        while qu:

            qsz = len(qu)
            step += 1
            for _ in range(qsz):
                cr, cc = qu.popleft()
                maze[cr][cc] = '#'
                movs = neb(cr, cc)
                # print(cr, cc, step)
                for nr, nc in movs:
                    if maze[nr][nc] == '.':
                        if len(neb(nr, nc)) != 4:
                            finished = True
                            # print("rrr", nr, nc, maze[nr][nc])
                            return step
                        maze[nr][nc] = '#'
                        qu.append((nr, nc))
            # print("ss", qu)
        return -1 if not finished else step
        """
        [
            ["+",".","+","+","+","+","+"],
            ["+",".","+",".",".",".","+"],
            ["+",".","+",".","+",".","+"],
            ["+",".",".",".","+",".","+"],
            ["+","+","+","+","+",".","+"]
            ]
        
        """
                

                    




