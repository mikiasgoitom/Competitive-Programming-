# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapify(heap)

        for i in range(0, len(heights) - 1):
            # heappush
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                heappush(heap, diff)
            else:
                continue
            
            if len(heap) > ladders:
                num = heappop(heap)
                if bricks - num < 0:
                    return i
                else:
                    bricks -= num
        
        return len(heights) -  1