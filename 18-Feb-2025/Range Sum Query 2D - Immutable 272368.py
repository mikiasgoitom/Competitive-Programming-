# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        # for r in range(len(self.mat)):
        #     self.mat[r]
        
        last_row = [0 for _ in range(len(self.mat[0]))]
        self.mat.extend([last_row])
        print(self.mat)

        self.prefix = [[0 for _ in range(len(self.mat[0])+1)] for _ in range(len(self.mat)+1)]
        for row in range(len(self.mat)):
            for col in range(len(self.mat[0])):
                self.prefix[row][col] = self.prefix[row-1][col] + self.prefix[row][col - 1] - self.prefix[row-1][col-1] + self.mat[row][col]
        print(self.prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.prefix[row2][col2] - self.prefix[row1 - 1][col2] - self.prefix[row2][col1 - 1] + self.prefix[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)