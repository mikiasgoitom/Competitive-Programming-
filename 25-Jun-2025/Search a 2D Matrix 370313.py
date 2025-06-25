# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mtx = [-10**5] + matrix + [10**5]
        
        def bs_r():
            low, high = 0, len(matrix) - 1
            while low <= high:
                mid = (high + low) // 2
                if matrix[mid][-1] == target:
                    return 'found'
                elif matrix[mid][-1] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
        def bs_cl(idx):
            low, high = 0, len(matrix[0]) - 1
            while low <= high:
                mid = (high + low) // 2
                if matrix[idx][mid] == target:
                    return True
                elif matrix[idx][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        temp = bs_r()
        if temp == 'found':
            return True
        elif len(matrix) <= temp:
            return False
        return bs_cl(temp)
        
