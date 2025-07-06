# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intval = []
        for st, end in intervals:
            intval.append((st, 1))
            intval.append((end + 1, -1))
        intval.sort()
        ans = 1
        curr = 0
        for gabg, val in intval:
            curr += val
            # print(curr)
            ans = max(curr, ans)
        return ans