# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def pascalTriangle(self, arr, row):
        if row == 0:
            return arr
        nxt_arr = [1]
        for i in range(len(arr) -1 ):
            nxt_arr.append(arr[i] + arr[i+1])
        nxt_arr.append(1)
        return self.pascalTriangle(nxt_arr, row-1)

            

    def getRow(self, rowIndex: int) -> List[int]:
        return self.pascalTriangle([1], rowIndex)