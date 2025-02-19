# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        accum = 0
        max_subarr = float('-inf')
        for i in range(len(nums)):
            if prefix < 0:
                prefix = 0
            prefix += nums[i]
            max_subarr = max(max_subarr, prefix)

        return max_subarr
