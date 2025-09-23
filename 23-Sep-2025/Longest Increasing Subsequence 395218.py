# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    sys.setrecursionlimit(10**7)
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums))
        def dp(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]
            memo[i] = 1

            # exclude = dp(i + 1)
            for j in range(i + 1, len(nums)):
                include = 0
                if nums[j] > nums[i]:
                    include = 1 + dp(j)
                    
                memo[i] = max(include, memo[i])
                # print("memo", i, memo[i])

            return memo[i]
        
        ans = float('-inf')

        for i in range(len(nums)):
            ans = max(ans, dp(i))
            # print(ans, i, memo)
        return ans