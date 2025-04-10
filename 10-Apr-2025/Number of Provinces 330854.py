# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = [[] for _ in range(len(isConnected))]

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if r != c:
                    if isConnected[r][c] == 1:
                        graph[r].append(c)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for neb in graph[node]:
                if not neb in visited:
                    dfs(neb)
            # return

        provs = 0
        for i in range(len(graph)):
            if not i in visited:
                provs += 1
                dfs(i)
        
        return provs