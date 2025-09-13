# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        no_rows, no_cols = len(board), len(board[0])
        # calculates possible valid moves
        def calc_moves(row, col):
            movs = []
            # possible directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for row_move, col_move in directions:
                new_row, new_col = row + row_move, col + col_move
                if 0 <= new_row < no_rows and 0 <= new_col < no_cols:
                    movs.append((new_row, new_col))
            return movs
        #check if word exists
        def check_for_word(row, col, visited, index):
            if index == len(word):
                return True
            visited.add((row, col))
            movs = calc_moves(row, col)

            for next_row, next_col in movs:
                # print("rout", sorted(visited), index, len(word), word[index], board[next_row][next_col])
                if (next_row, next_col) not in visited and word[index] == board[next_row][next_col]:
                    res = check_for_word(next_row, next_col, visited, index + 1)
                    # print(res, index, next_row, next_col, word[index], board[next_row][next_col])
                    if res:
                        return True
            visited.remove((row, col))
            return False
                

        # start from all the character
        for row in range(len(board)):
            for col in range(len(board[0])):
                if word[0] == board[row][col]:
                    # print(index, word[index], board[row][col], visited)
                    if check_for_word(row, col, set(), 1):
                        return True
        
        return False
    
    """
    [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]]
    """
    "ABCESEEEFS"