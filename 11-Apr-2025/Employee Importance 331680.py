# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employee: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        print(employee[0].id)
        for i in range(len(employee)):
            graph[employee[i].id].append(employee[i].subordinates)
            graph[employee[i].id].append(employee[i].importance)

        visited = set()
        # print(graph)
        def dfs(node):
            visited.add(node)

            tot = graph[node][1]

            for neb in graph[node][0]:
                # print(neb)
                if not neb in visited:
                    tot += dfs(neb)
            
            return tot
        
        return dfs(id)

