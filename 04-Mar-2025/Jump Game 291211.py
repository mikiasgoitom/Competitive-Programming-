# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, far = 0, 0
        while i < len(nums):
            if far == len(nums)-1:
                return True
            elif i == far and nums[i] == 0:
                return False
            far = max(far, i + nums[i])
            i += 1
            
        return True
