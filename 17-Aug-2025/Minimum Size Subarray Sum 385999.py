# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        seg = 0
        ans = len(nums)
        found = False
        for r in range(len(nums)):
            seg += nums[r]
            while seg - nums[l] >= target:
                seg -= nums[l]
                l += 1
            if seg >= target:
                ans = min(ans, r - l + 1)
                found = True
        if found:
            return ans
        else:
            return 0
            
