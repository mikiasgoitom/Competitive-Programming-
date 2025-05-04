# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        gird_size = len(grid)
        vers = gird_size + 1
        tot_ver = vers * vers

        parent = [i for i in range(tot_ver)]
        size = [1] * tot_ver
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        

        def union(u, v):
            x, y = find(u), find(v)

            if x != y:
                if size[y] > size[x]:
                    parent[x] = parent[y]
                    size[y] += size[x]
                else:
                    parent[y] = parent[x]
                    size[x] += size[y]
                return False
            else:
                return True

        edges = []

        for i in range(vers):
            for j in range(vers):
                if (i == 0 or i == (vers-1)) and j + 1 < vers:
                    u = (i * vers) + j
                    v = (i * vers) + (j + 1)
                    union(u, v)

                if (j == 0 or j == vers - 1) and i + 1 < vers:
                    u = (i * vers) + j
                    v = ((i + 1) * vers) + j
                    union(u, v)

        # print(parent, size)

        count_region = 1
        for r in range(gird_size):
            for c in range(gird_size):
                if grid[r][c] == '/':
                    if union(
                        ((r*vers) + c + 1), 
                        (((r + 1) * vers) + c)
                        ):
                        count_region += 1
                elif grid[r][c] == '\\':
                    if union(
                        ((r*vers) + c), 
                        (((r + 1) * vers) + c + 1)
                    ):
                        count_region += 1


        return count_region
                