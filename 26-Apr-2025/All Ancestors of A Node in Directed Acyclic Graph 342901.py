# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
        
        src = []

        for i in range(n):
            if indeg[i] == 0:
                src.append(i)
        
        qu = deque(src)
        ans = [set() for _ in range(n)]
        while qu:
            node = qu.popleft()

            for neb in graph[node]:
                ans[neb].update(ans[node])
                ans[neb].add(node)
                indeg[neb] -= 1
                if indeg[neb] == 0:
                    qu.append(neb)

        
        return [sorted(rs) for rs in ans]
