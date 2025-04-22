# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        # exi
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
        print(graph)

        
        def dfs(node, d):
            if node == d:
                return 1 
            visited.add(node)
            for neb, val in graph[node]:
                if neb not in visited:
                    rt = dfs(neb, d)
                    print(rt)
                    if rt != -1:
                        rt *= val
                        return rt
            return -1
        res = []
        for s, d in queries:
     
            if s in graph and d in graph:
                visited = set()
                res.append(dfs(s, d))
            else:
                res.append(-1)
        return res
