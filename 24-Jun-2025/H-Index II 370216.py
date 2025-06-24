# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        def valid(mid):
            i = 0
            while i < len(citations) and citations[i] < mid:
                i += 1
            # print(i, mid)
            if len(citations) - (i) >= mid:
                # print("ans", mid)
                return True
            return False

        def bs():
            high, low = len(citations), 0
            while low <= high:
                mid = (high + low) // 2
                if valid(mid):
                    low = mid + 1
                else:
                    high = mid - 1
                # print("bd", low, high)
            return high
        return bs()