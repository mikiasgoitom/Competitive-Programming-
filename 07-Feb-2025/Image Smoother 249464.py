# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_img = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        row_size = len(img) -1 
        col_size = len(img[0]) - 1
        for row in range(row_size + 1):
            for col in range(col_size + 1):
                avg = 0
                surrounding_num = 0
                if col - 1 <= col_size and col - 1 >= 0 and row - 1 <= row_size and row - 1 >= 0:
                    avg += img[row-1][col-1]
                    surrounding_num += 1
                if row - 1 <= row_size and row - 1 >= 0:
                    avg += img[row-1][col]
                    surrounding_num += 1
                if col + 1 <= col_size and col + 1 >= 0 and row - 1 <= row_size and row - 1 >= 0:
                    avg += img[row-1][col+1]
                    surrounding_num += 1
                if col - 1 <= col_size and col - 1 >= 0:
                    avg += img[row][col-1]
                    surrounding_num += 1
                if col + 1 <= col_size and col + 1 >= 0:
                    avg += img[row][col+1]
                    surrounding_num += 1
                if col - 1 <= col_size and col - 1 >= 0  and row + 1 <= row_size and row + 1 >= 0:
                    avg += img[row+1][col-1]
                    surrounding_num += 1
                if row + 1 <= row_size:
                    avg += img[row+1][col]
                    surrounding_num += 1
                if col + 1 <= col_size and col + 1 >= 0 and row + 1 <= row_size:
                    avg += img[row+1][col+1]
                    surrounding_num += 1
                avg += img[row][col]
                surrounding_num += 1
                new_img[row][col] = avg // surrounding_num
                # print(avg, surrounding_num)
        return new_img

