# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)

        
        def dfs(node):
            visited.add(node)

            for neb in graph[node]:
                if neb not in visited:
                    dfs(neb)
        
        possible = -1
        for i in range(n):
            visited = set()
            dfs(i)
            if len(visited) == n:
                possible = i
        
        return possible

