# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_peri = 0
        for i in range(2, len(nums)):
            if nums[i-2] < nums[i-1] + nums[i]:
                max_peri = nums[i-2] + nums[i-1] + nums[i]
                break
        return max_peri