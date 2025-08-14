# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # return sum(informTime)
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append( i)
        
        candi = []
        visited = set()
        def dfs(node, infotime):
            if not graph[node]:
                candi.append(infotime)
            visited.add(node)
            
            for neb in graph[node]:
                if neb not in visited:
                    dfs(neb, infotime + informTime[node])
       
        dfs(headID, 0)
        return max(candi)