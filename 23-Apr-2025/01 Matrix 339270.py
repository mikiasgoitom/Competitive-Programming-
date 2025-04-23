# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return (0 <= r < m) and (0 <= c < n)

        moves = lambda r, c: [
            (r + gr, c + gc) for gr, gc in dirc if inbound(r + gr, c + gc)
        ]

        src = []

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    src.append((r, c))

        qu = deque(src)
        visited = set(src)
        count = 0

        while qu:

            for _ in range(len(qu)):
                cur_r, cur_c = qu.popleft()
                neb = moves(cur_r, cur_c)

                if mat[cur_r][cur_c] != 0:
                    mat[cur_r][cur_c] = count

                for nr, nc in neb:

                    if (nr, nc) not in visited:
                        qu.append((nr, nc))
                        visited.add((nr, nc))

            count += 1

        return mat