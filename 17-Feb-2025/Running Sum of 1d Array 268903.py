# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        accum = 0
        for i in range(0, n):
            accum += nums[i]
            nums[i] = accum
        return nums