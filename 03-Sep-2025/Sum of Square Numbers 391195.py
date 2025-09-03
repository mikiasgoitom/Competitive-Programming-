# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = list(range(isqrt(c) + 1))
        i, j = 0, len(nums) - 1
        while i <= j:
            x, y = pow(i, 2), pow(j, 2)
            if x + y == c:
                return True
            
            if x + y < c:
                i += 1
            else:
                j -= 1

        return False