# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans