# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(n):
            if n == len(nums) - 1:
                return nums[n]
            elif n == len(nums) - 2:
                return max(nums[n], nums[n + 1])
            else:
                if n in memo:
                    return memo[n]
                else:
                    memo[n] = max(dp(n + 1), dp(n + 2) + nums[n])
                    return memo[n]

        return dp(0)
