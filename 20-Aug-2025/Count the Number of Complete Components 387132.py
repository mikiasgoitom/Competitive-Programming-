# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)

        visited = set()

        def dfs(node, check):
            size = 1
            check.add(node)
            for neb in graph[node]:
                if neb not in check:
                    size += dfs(neb, check)                
            return size
        
        def bfs(node, size):
            qu = deque([node])
            valid = True
            while qu:
                cur = qu.popleft()
                visited.add(cur)

                if size != (len(graph[cur]) + 1):
                    # print("touched1")
                    valid = False

                for neb in graph[cur]:
                    if neb not in visited:
                        qu.append(neb) 
            # print("calprit")
            return valid

        count = 0
        for u in range(n):
            if u not in visited:
                check = set()
                size = dfs(u, check)
                # print(size, visited)
                if bfs(u, size):
                    count += 1
        return count