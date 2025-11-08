# Problem: Minimum Time to Collect All Apples in a Tree - https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        gph = [[] for _ in range(n)]
        for eg in edges:
            gph[eg[0]].append(eg[1])
            gph[eg[1]].append(eg[0])

        def dfs(node, parent):
            dist = 0
            for neb in gph[node]:
                if neb != parent:
                    dist += dfs(neb, node)
            
            if node != 0 and (dist != 0 or hasApple[node]):
                dist += 2

            # print(node, dist)

            return dist

        return dfs(0, -1)
