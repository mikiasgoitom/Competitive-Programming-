# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right =  bisect.bisect_right(nums, target)
        
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        return [left, right-1]