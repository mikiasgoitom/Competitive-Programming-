# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min, last_max, left_bound = -1, -1 , -1
        ans = 0
        for i in range(len(nums)):
            if nums[i] == minK:
                last_min = i
            
            if nums[i] == maxK:
                last_max = i
            
            if minK > nums[i] or maxK < nums[i]:
                left_bound = i
            
            ans += max(0, min(last_min, last_max) - left_bound) 
            # print(ans, last_min, last_max)
        return ans