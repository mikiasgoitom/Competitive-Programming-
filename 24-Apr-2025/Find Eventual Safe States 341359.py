# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdeg = [0] * n
        clr = [0] * n

        for i in range(n):
            outdeg[i] = len(graph[i])
        # print(outdeg)
        stk = []

        def dfs(node):
            if clr[node] == 1:
                return False
            
            if outdeg[node] == 0:
                return True

            clr[node] = 1
            for neb in graph[node]:
                if clr[neb] == 2:
                    continue
                elif clr[neb] == 1:
                    return False
                    
                if clr[neb] == 0:
                    rt = dfs(neb)
                    if not rt:
                        return False
                        
            clr[node] = 2
            return True
        
        stk = []
        for i in range(n):
            if dfs(i):
                stk.append(i)
        
        return stk




