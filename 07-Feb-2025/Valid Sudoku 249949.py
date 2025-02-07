# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic_row = defaultdict(list)
        dic_col = defaultdict(list)
        dic_con = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    if board[row][col] in dic_row[row]:
                        print("row", row, board[row][col])
                        return False
                    else:
                        dic_row[row].append(board[row][col])
                    if board[row][col] in dic_col[col]:
                        print("col", col)
                        return False
                    else:
                        dic_col[col].append(board[row][col])
                    if board[row][col] in dic_con[tuple([row//3, col//3])]:
                        print("con", tuple([row//3, col//3]))
                        return False
                    else:
                        dic_con[tuple([row//3, col//3])].append(board[row][col])
                    
        return True