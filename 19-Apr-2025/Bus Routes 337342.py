# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        src = []
        graph = defaultdict(set)
        if source == target:
            return 0

        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].add(i)

        # print(graph)
       
        que = deque()
        visited_s = set([source])
        visited_r = set()

        for i in graph[source]:
            que.append((i, 1))
            visited_r.add(i)

        buses = 0
        # print(que)
        while que:
            rut_i, buses = que.popleft()

            # print("r", rut_i, len(routes))
            for stop in routes[rut_i]:
                if stop == target:
                    return buses
                elif stop in visited_s:
                    continue
                # print(stop, rut_i)
                visited_s.add(stop)
                # for stops in 
                for nrut_i in graph[stop]:
                    if nrut_i in visited_r:
                        continue
                    else:
                        # print("ds", nrut_i, buses + 1)
                        que.append((nrut_i, buses + 1))
                        visited_r.add(nrut_i)
        

        return -1

                



    