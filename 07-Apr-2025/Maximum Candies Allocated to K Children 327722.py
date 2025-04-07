# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, c: List[int], k: int) -> int:
        c.sort()

        def validator(pile):
            nonlocal c, k
            i = 0
            ck = k
            while i < len(c):
                if c[i] == pile:
                    ck -= 1
                else:
                    ck -= c[i] // pile
                i +=1
            return ck <= 0

        def bst():
            low, high = 1, 1e7

            while low <= high:
                mid = (high + low) // 2
                if validator(mid):
                    low = mid + 1
                else:
                    high = mid - 1
            
            return high
        
        return int(bst())

        