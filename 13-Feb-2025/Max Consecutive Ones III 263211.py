# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeros = 0
        max_wind = 0
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            w = right - left + 1
            max_wind = max(max_wind, w)
        return max_wind