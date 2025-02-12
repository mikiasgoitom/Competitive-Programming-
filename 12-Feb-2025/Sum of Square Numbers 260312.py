# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = list(range(isqrt(c) + 1))
        i, j = 0, len(nums) - 1
        while i <= j:
            potential_c = nums[i]**2 + nums[j]**2
            if potential_c == c:
                return True
            elif potential_c > c:
                j -= 1
            elif potential_c < c:
                i += 1
        return False