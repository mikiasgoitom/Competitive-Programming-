# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # height_diffs = []
        # for i in range(1, len(heights)):
        #     if heights[i] - heights[i-1] > 0:
        #         height_diffs.append((heights[i] - heights[i-1], i))
        
        # print("diffs",height_diffs)
        heap = []
        heapify(heap)
        ans = len(heights) - 1

        for i in range(0, len(heights) - 1):
        
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heappush(heap, diff)
                
            if len(heap) > ladders:
                num = heappop(heap)
                if bricks - num < 0:
                    return i
                else:
                    bricks -= num
        
        return (ans)