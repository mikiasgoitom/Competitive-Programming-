# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        target = nums_sum // 2
        memo = {}
        def dp(idx, target):
            if target <= 0:
                return target == 0
            elif idx > len(nums) - 1:
                return False
            
            if (idx, target) not in memo:
                memo[(idx, target)] = dp(idx + 1, target) or dp(idx + 1, target - nums[idx])
            return memo[(idx, target)]

        if nums_sum % 2 == 0:
            return dp(0, target)
        else:
            return False