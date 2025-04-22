# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(image), len(image[0])
        cur_clr = image[sr][sc]

        def inbound(r, c):
            return (0 <= r < m) and (0 <= c < n)

        moves = lambda r, c:[
            (r + gr, c + gc) for gr, gc in dirc if inbound(r + gr, c + gc)
        ]

        visited = set([(sr, sc)])
        qu = deque([(sr, sc)])

        while qu:

            for _ in range(len(qu)):
                r, c = qu.popleft()
                image[r][c] = color

                nebs = moves(r, c)

                for nr, nc in nebs:
                    if (nr, nc) not in visited and image[nr][nc] == cur_clr:
                        qu.append((nr, nc))
                        visited.add((nr, nc))
        
        return image