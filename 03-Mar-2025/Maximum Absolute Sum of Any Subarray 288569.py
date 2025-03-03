# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        max_pre = 0
        arr_size = len(nums)
        for i in range(arr_size):
            if max_pre < 0:
                max_pre = 0
            max_pre += nums[i]
            max_sum = max(max_sum, max_pre)

        min_pre = 0
        min_sum = float('inf')

        for i in range(arr_size):
            if min_pre > 0:
                min_pre = 0
            min_pre += nums[i]
            min_sum = min(min_sum, min_pre)
        
        return max(abs(max_sum), abs(min_sum))