# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def bfs(node):
            qu = deque([node])
            nodes = 0
            edges_count = 0

            while qu:
                cur = qu.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                nodes += 1
                edges_count += len(graph[cur])
                
                for neb in graph[cur]:
                    if neb not in visited:
                        qu.append(neb)
            # print("sadf", nodes, edges_count // 2)
            return nodes, edges_count // 2
                

        count = 0
        for u in range(n):
            if u not in visited:
                v, e = bfs(u)
                if e == ((v * (v - 1)) // 2):
                    # print(e, v, u)
                    count += 1
        return count
