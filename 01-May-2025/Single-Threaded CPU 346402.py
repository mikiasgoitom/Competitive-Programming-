# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
    
        size = len(tasks)

        for i in range(size):
            tasks[i].append(i)
        
        tasks.sort()
        
        heap = []
        heapify(heap)
        till_now = tasks[0][0]
        res = []
        i = 0

        while heap or i < size:
            while i < size and tasks[i][0] <= till_now:
                heappush(heap, (tasks[i][1], tasks[i][2], tasks[i][0]))
                i +=1
            
            if heap:
                min_p_t, ans, started_time= heappop(heap)
                till_now += (min_p_t)
                res.append(ans)
            elif not heap and i < size:
                till_now = tasks[i][0]

        return res

