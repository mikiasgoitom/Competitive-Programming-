# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x : (x[1]))
        # print(points)
        count = 1
        i, j = 0, 1
        while j < len(points) and i < len(points):
            # print("b", i, j, count)
            if points[j][1] >= points[i][0] and points[j][0] <= points[i][1]:
                j += 1
            else:
                j += 1
                i  = j - 1
                count += 1
            # print("a", i, j, count)
            
        return count