# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, trgt):
            # if trgt == 0 and len():
            #     print("DFDF")
            #     return 1

            if i >= len(nums):
                return 1 if trgt == target else 0

            
            if (i, trgt) not in memo:
                memo[(i, trgt)] = dfs(i + 1, trgt - nums[i]) + dfs(i + 1, trgt + nums[i])
                    # print("asdfgh")

            return memo[(i, trgt)]
        return (dfs(0, 0))
        print(memo)