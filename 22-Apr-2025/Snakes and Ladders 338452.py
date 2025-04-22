# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        n2 = n**2
        pgd = [0] * (n2+1)
        
        revers = False
        i = 1
        for r in range(n-1, -1, -1):
            row = range(n) if not revers else range(n-1, -1, -1)
            for c in row:
                val = board[r][c]
                pgd[i] = (i, val if val > 0 else None)
                i += 1
            revers = not revers
        
        que = deque([pgd[1]])
        steps = 0
        visited = set([1])

        while que:

            for _ in range(len(que)):
                cur = que.popleft()

                if cur[0] == n2:
                    return steps
                
                for i in range(1, 7):
                    nxt = cur[0] + i
                    if nxt > n2:
                        break
                    else:
                        jump = pgd[nxt][1] if pgd[nxt][1] else nxt
                        if jump not in visited:
                            que.append(pgd[jump])
                            visited.add(jump)
    
            steps += 1


        return -1
                


"""
[
    [-1,-1,19,10,-1],
    [2,-1,-1,6,-1],
    [-1,17,-1,19,-1],
    [25,-1,20,-1,-1],
    [-1,-1,-1,-1,15]
]
"""