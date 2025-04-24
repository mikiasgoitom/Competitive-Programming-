# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for i in range(len(richer)):
            u, v  = richer[i]
            graph[u].append(v)
            indeg[v] += 1        
        
        # print(indeg)
        src = []

        ans = list(range(n))
        for i in range(n):
            if indeg[i] == 0:
                src.append(i)
        
        qu = deque(src)

        while qu:
                node = qu.popleft()
                for neb in graph[node]:
                    if quiet[ans[node]] < quiet[ans[neb]]:
                        ans[neb] = ans[node]
                    indeg[neb] -= 1
                    if indeg[neb] == 0:
                        qu.append(neb)
        
        return ans

