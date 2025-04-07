# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(cur_ver, visited):
            if cur_ver == destination:
                return True

            visited.add(cur_ver)

            for neighbour in graph[cur_ver]:
                if neighbour not in visited:
                    if dfs(neighbour, visited):
                        return True
            return False
            
        return dfs(source,visited)