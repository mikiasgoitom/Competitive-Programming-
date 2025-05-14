# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sumed = sum(nums)
        temp = 0
        for i in range(len(nums)):
            temp = temp ^ nums[i]
        return temp     