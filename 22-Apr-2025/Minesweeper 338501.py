# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        direction = [(0,1), (0,-1), (-1,0), (1, 0), (1,1), (-1,-1), (-1,1), (1,-1)]
        
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        moves = lambda r, c: [
            (r + gr, c + gc) for gr, gc in direction if inbound(r + gr, c + gc)
        ]

        def adj_mine(r, c):
            count_mine = 0
            chks = moves(r, c)

            for gr, gc in chks:
                if inbound(gr, gc):
                    if board[gr][gc] == 'M' or board[gr][gc] == 'X':
                        count_mine += 1

            return 'B' if count_mine == 0 else str(count_mine)
        
        def bfs(r, c):
            qu = deque([(r, c)])
            visited = set([(r, c)])
            while qu:
                for _ in range(len(qu)):
                    cur_r, cur_c = qu.popleft()
                    board[cur_r][cur_c] = adj_mine(cur_r, cur_c)
                    changes = moves(cur_r, cur_c)

                    if board[cur_r][cur_c] == 'B':
                        for nr, nc in changes:
                            if inbound(nr, nc):
                                if board[nr][nc] == 'E' and (nr, nc) not in visited:
                                    qu.append((nr, nc))                        
                                    visited.add((nr, nc))

        clk_r, clk_c = click

        if board[clk_r][clk_c] == 'M':
            board[clk_r][clk_c] = 'X'
    
        elif board[clk_r][clk_c] == 'E':
            bfs(clk_r, clk_c)
        
        return board
