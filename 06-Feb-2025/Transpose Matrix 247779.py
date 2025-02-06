# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = [[0  for _ in range(len(matrix))] for _ in range(len(matrix[0])) ] 
        print(mat)
        print(matrix)
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                mat[row][col] = matrix[col][row]
        return mat