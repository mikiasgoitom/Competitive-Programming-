# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0] * len(nums)

        for i,j in requests:
            pre[i] += 1
            if j + 1 < len(nums):
                pre[j+1] -= 1
            
        accum = 0

        for i in range(len(pre)):
            accum += pre[i]
            pre[i] = accum

        pre.sort(reverse=True)

        nums.sort(reverse = True)
        summed = 0
        i = 0

        while i < len(pre):
            summed += nums[i] * pre[i]
            i += 1

        return summed % (10**9 + 7)

