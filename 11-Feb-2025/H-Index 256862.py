# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        ans = 0

        for i in range(n):
            curr = min(citations[i], n - i)
            if curr > ans:
                ans = curr
        return ans