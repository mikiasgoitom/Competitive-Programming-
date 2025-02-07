# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        s_row = 0
        e_row = len(matrix) - 1
        s_col = 0
        e_col = len(matrix[0]) - 1
    
        ans = []
        size = len(matrix[0]) * len(matrix)
        while s_row <= e_row and s_col <= e_col:
            col = s_col

            while col <= e_col:
                ans.append(matrix[s_row][col])
                col+=1
            print(ans, "first")

            s_row += 1
            row = s_row
            while row <= e_row:
                ans.append(matrix[row][e_col])
                row += 1
            print(ans)

            e_col -= 1
            col = e_col

            if s_row <= e_row :
                while col >= s_col:
                    ans.append(matrix[e_row][col])
                    col -= 1
                print(ans, "third")

                e_row -= 1
            row = e_row

            if s_col <= e_col:
                while row >= s_row:
                    ans.append(matrix[row][s_col])
                    row -= 1
                s_col += 1

            print(ans)

        return ans
             