# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def __search_first(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) //  2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low
    def __search_last(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) //  2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high  
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.__search_first(nums, target), self.__search_last(nums, target)
        if left > right:
            return [-1, -1]
        return [left, right]