# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        r = len(nums) - 1
        count = 0
        
        for i in range(len(nums)):
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1)
            count += right - left
        return count

                
                

                
        