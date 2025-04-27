# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indeg = [0] * n
        if n <= 2:
            return list(range(n))
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        # print(adj)

        src = []

        for i in range(n):
            if indeg[i] == 1:
                src.append(i)
        
        qu = deque(src)
        order = []

        while qu:
            for _ in range(len(qu)):
                node = qu.popleft()
                for neb in adj[node]:
                    indeg[neb] -= 1
                    if indeg[neb] == 1:
                        qu.append(neb)
            order.append(list(qu))
        res = []
        for lt in order:
            if lt:
                res.append(lt)
     
        return sorted(res[-1])
            