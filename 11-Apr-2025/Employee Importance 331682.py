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
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {empl.id: empl for empl in employees}

        print(graph)
        def dfs(node):
            tot = graph[node].importance
            for neb in graph[node].subordinates:
                tot += dfs(neb)
            
            return tot
        
        return dfs(id)

