# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        clr = [0] * n
        graph = [[] for _ in range(n)]

        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        def dfs(cur, par):
            clr[cur] = par

            for neb in graph[cur]:
                if clr[neb] == par:
                    return False
                elif clr[neb] == 0:
                    if not dfs(neb, -par):
                        return False
            return True

        for i in range(n):
            if clr[i] == 0:
                if not dfs(i, 1):
                    # print('sd', clr)
                    return False
        
        # print("j", clr)
        
        return True