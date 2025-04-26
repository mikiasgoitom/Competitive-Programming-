# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = [[] for _ in range(n)]

        for pre, course in prerequisites:
            graph[course].append(pre)
        
        prereq_map = {}

        def dfs(node):
            if node not in prereq_map:
                prereq_map[node] = set()
                for neb in graph[node]:
                    prereq_map[node] |= dfs(neb)
                prereq_map[node].add(node)
            return prereq_map[node]

        for i in range(numCourses):
            dfs(i)

        # print(prereq_map)
        res = []
        for u, v in queries:
            res.append(u in prereq_map[v])
        
        return res