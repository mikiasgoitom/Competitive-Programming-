# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        src = []
        m, n = len(isWater), len(isWater[0])

        for r in range(len(isWater)):
            for c in range(len(isWater[0])):
                if isWater[r][c] == 1:
                    src.append((r, c))
        
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(r, c):
            return (0 <= r < m) and (0 <= c < n)

        moves = lambda r, c: [
            (r + gr, c + gc) for gr, gc in dirc if inbound(r + gr, c + gc)
        ]

        qu = deque(src)
        visited = set(src)
        val = 0
        while qu:

            for _ in range(len(qu)):
                r, c = qu.popleft()
                isWater[r][c] = val
                neb = moves(r, c)
                for nr, nc in neb:
                    if (nr, nc) not in visited:
                        qu.append((nr, nc))
                        visited.add((nr, nc))
            val += 1
        
        return isWater

