# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in redEdges:
            graph[u].append((v, 'r'))
        
        for u, v in blueEdges:
            graph[u].append((v, 'b'))

        ans = [-1] * n
        qu = deque([(0, 'r', 0), (0, 'b', 0)])
        visited = set([(0, 'r', 0), (0, 'b', 0)])
        path = {}

        while qu:
            cur, clr, accum = qu.popleft()
            
            if ans[cur] == -1:
                ans[cur] = accum
            else:
                ans[cur] = min(ans[cur], accum)
            
            for nxt, nxt_clr in graph[cur]:
                if (nxt, nxt_clr) not in visited and clr != nxt_clr:
                    qu.append((nxt, nxt_clr, accum + 1))
                    visited.add((nxt, nxt_clr))
            
        return ans

        