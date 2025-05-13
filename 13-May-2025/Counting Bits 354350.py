# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            count = 0
            while i > 0:
                if i % 2 != 0:
                    count += 1
                i //= 2
            ans.append(count) 
        return ans