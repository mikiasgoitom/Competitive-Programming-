# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0] * n
        def dfs(cur_ver, visited):
            if cur_ver == destination:
                return True

            visited[cur_ver] = 1

            for neighbour in graph[cur_ver]:
                if not visited[neighbour]:
                    if dfs(neighbour, visited):
                        return True
            return False
            
        return dfs(source,visited)