# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        def heapify_down(heap, current):
            child_l = 2 * current + 1
            child_r = 2 * current + 2
            n = len(heap)

            swaped_by = None
            if child_r < n:
                if heap[current] < heap[child_l] and heap[child_l] >= heap[child_r]:
                    heap[child_l], heap[current] = heap[current], heap[child_l]
                    swaped_by = child_l
                elif heap[current] < heap[child_r]:
                    heap[child_r], heap[current] = heap[current], heap[child_r]
                    swaped_by = child_r
            elif child_l < n:
                if heap[current] < heap[child_l]:
                    heap[child_l], heap[current] = heap[current], heap[child_l]
                    swaped_by = child_l
            if swaped_by:
                heapify_down(heap, swaped_by)

        def heapify(piles):

            for i in range((len(piles)//2) - 1, -1, -1):
                heapify_down(piles, i)
        
        def solve(piles):
            heapify(piles)
            for _ in range(k):
                piles[0] = ceil(piles[0] / 2)
                heapify_down(piles, 0)
        solve(piles)
        return sum(piles)