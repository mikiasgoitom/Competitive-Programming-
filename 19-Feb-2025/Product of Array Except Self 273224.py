# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        size_nums = len(nums)
        accum = 1
        for i in range(size_nums):
            accum *= nums[i]
            pre.append(accum)
        
        suf = []
        accum = 1

        for i in range(size_nums-1, -1, -1):
            accum *= nums[i]
            suf.append(accum)

        suf = suf[::-1]

        ans = []

        for i in range(size_nums):
            multi = 1
            if  i - 1 > -1:
                multi *= pre[i-1]
            if i + 1 < size_nums:
                multi *= suf[i+1]
            
            ans.append(multi)
        return ans