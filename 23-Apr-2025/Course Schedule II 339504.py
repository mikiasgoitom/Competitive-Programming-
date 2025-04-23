# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            indegree[c1] += 1
        
        # 
        
        src = [n for n in range(numCourses) if indegree[n] == 0]
        # print(src)

        qu = deque(src)
        course_order = []
        while qu:
            # print(qu, indegree)
            for _ in range(len(qu)):
                crs = qu.popleft()
                course_order.append(crs)

                for neb in graph[crs]:
                    indegree[neb] -= 1
                    if indegree[neb] == 0:
                        qu.append(neb)
        
        return course_order if len(course_order) == numCourses else []