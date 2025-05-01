# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        n = len(matrix)

        while low < high:
            mid = (high + low) // 2

            count = 0
            for row in matrix:
                count += bisect_right(row, mid)
                # print(bisect_right(row, mid))
            
            if count < k:
                low = mid + 1
            else:
                high = mid
            
        return low
