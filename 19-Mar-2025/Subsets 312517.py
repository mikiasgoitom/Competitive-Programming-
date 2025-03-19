# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if n == i:
                res.append(sol[:])
                return
            
            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        backtrack(0)
        return res