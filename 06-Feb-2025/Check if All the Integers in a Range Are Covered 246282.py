# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # create a list of all the items in the interval from left to right then check it with another set created based in the actual elements in the 2d arr
        checker = set(x for x in range(left,right+1))
        res = set()
        for i in range(len(ranges)):
            res.update(i for i in range(ranges[i][0], ranges[i][-1]+1))
        return checker.issubset(res)