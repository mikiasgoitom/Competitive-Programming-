# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
               matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            matrix[r].reverse()
        