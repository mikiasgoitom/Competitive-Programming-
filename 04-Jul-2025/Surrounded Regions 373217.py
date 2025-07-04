# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        def inBound(r, c):
            return 0 <= r < n and 0 <= c < m

        def inBoundery(r,c):
            return (r == 0 or c == 0) or (r == (n - 1) or c == (m - 1))

        dircs = [ (0,1), (1,0), (0,-1), (-1,0)]
        
        def getMove(node):
            r, c = node[0], node[1]
            move = []
            for gr, gc in dircs:
                nr, nc = r + gr, c + gc
                if inBound(nr, nc):
                    move.append((nr, nc))
            return move
          
          
        bcheck_visited = set()
        border_connected = set()

        def borderDfs(node):
            bcheck_visited.add(node)
            move = getMove(node)
            
            for r, c in move:
                if (r,c) not in bcheck_visited and board[r][c] == 'O':
                    border_connected.add((r,c))
                    borderDfs((r,c))


        for r in range(n):
            for c in range(m):
                if (r,c) not in bcheck_visited and board[r][c] == 'O':
                    if inBoundery(r, c):
                        border_connected.add((r,c))
                        borderDfs((r, c))


        for r in range(n):
            for c in range(m):
                if (r,c) not in border_connected and board[r][c] == 'O':
                    board[r][c] = "X"
