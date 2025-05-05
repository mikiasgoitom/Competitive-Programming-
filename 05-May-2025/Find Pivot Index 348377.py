# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lr_arr = [0] * len(nums)

        accum = 0
        for i in range(len(nums)):
            accum += nums[i]
            lr_arr[i] = accum
        
        rl_arr = [0] * len(nums)

        accum = 0
        for i in range(len(nums) -1, -1, -1):
            accum += nums[i]
            rl_arr[i] = accum
        
        # print(lr_arr)
        # print(rl_arr)
        for i in range(len(nums)):
            left = lr_arr[i - 1] if i > 0 else 0
            right = rl_arr[i + 1] if i < len(nums) - 1 else 0
            if left == right:
                return i
        return -1