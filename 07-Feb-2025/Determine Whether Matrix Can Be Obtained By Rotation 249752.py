# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        next = mat
        for i in range(4):
            if next == target:
                return True
            trans_mat = 0
            if i == 0:
                trans_mat = [[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
                for row in range(len(next)):
                    for col in range(len(next[0])):
                        trans_mat[row][col] = next[col][row]
                    trans_mat[row] = trans_mat[row][::-1] 
                next = trans_mat
            elif i == 1:
                trans_mat = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
                for row in range(len(next[0])):
                    for col in range(len(next)):
                        trans_mat[row][col] = next[col][row]
                    trans_mat[row] = trans_mat[row][::-1] 
                next = trans_mat
            elif i == 2:
                trans_mat = [[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
                for row in range(len(next)):
                    for col in range(len(next[0])):
                        trans_mat[row][col] = next[col][row]
                    trans_mat[row] = trans_mat[row][::-1] 
                next = trans_mat
            print(next)
        return False
        