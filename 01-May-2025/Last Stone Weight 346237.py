# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * num for num in stones]
        heapify(heap)
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)

            if x == y:
                continue
            elif x != y:
                heappush(heap, x-y)
        
        ans = 0
        if heap:
            ans = -heap[0]

        return ans