# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        par = {}
        size = defaultdict(lambda : 1)
        vals = 0
        def find(x):
            par.setdefault(x,x)
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(x, y, w):
            x, y = find(x), find(y)
            nonlocal vals
            if x != y:
                vals += w
                if size[x] > size[y]:
                    par[y] = par[x]
                    size[x] += size[y]
                else:
                    par[x] = par[y]
                    size[y] += size[x]                    

        v = []
        sz = len(points)
        for i in range(sz):
            for j in range(i + 1, sz):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]

                v.append((i, j, (abs(x) + abs(y))))

        v.sort(key=lambda x: x[2])

        for u, v, w in v:
                union(u, v, w)
        
        return vals



