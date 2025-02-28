# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            x1, y1 = firstList[i]
            x2, y2 = secondList[j]

            if x1 <= y2 and x2 <= y1:
                ans.append([max(x1,x2), min(y1,y2)])
            elif x1 == y2:
                ans.append([x1,y2])
            elif x2 == y1:
                ans.append([x2,y1])

            if y2 > y1:
                i += 1
            else:
                j += 1

            # if y2 > y1 and i + 1 < len(firstList) :
            #     x3, y3 = firstList[i + 1]
            #     if y2 == x3:
            #         ans.append([y2,x3])
            # elif y1 > y2 and i + 1 < len(secondList) :
            #     x3, y3 = secondList[i + 1]
            #     if y1 == x3:
            #         ans.append([y1,x3])

        return ans
