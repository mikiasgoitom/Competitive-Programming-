# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = [0] * len(nums)
        for i in range(len(nums)):
            idx = sorted_nums.index(nums[i])
            ans[i] = idx
        return ans 