# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        clr = [0 for _ in range(n)]
        path = {}
        ans = []

        def topsort(node, step):

            if clr[node] == 1:
                # print(path, step, node, "sds", step - path[node])
                ans.append(step - path[node])
                return 
            path[node] = step
            step += 1
            clr[node] = 1
            neb = edges[node]
            if neb != -1 and clr[neb] != 2:
                topsort(neb, step)
            clr[node] = 2
            del path[node]
            return
        
        for i in range(n):
            if clr[i] == 0:
                topsort(i, 0)
        print(ans)
        if ans:
            return max(ans)
        else:
            return -1
                
                
