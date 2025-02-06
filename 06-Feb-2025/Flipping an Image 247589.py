# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            image[row] = image[row][::-1]
            for col in range(len(image)):
                if image[row][col] == 0:
                    image[row][col] = 1
                elif image[row][col] == 1:
                    image[row][col] = 0
        return image