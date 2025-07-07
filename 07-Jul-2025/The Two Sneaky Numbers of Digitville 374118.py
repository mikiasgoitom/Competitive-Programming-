# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:
                ans.append(nums[i])
        return ans