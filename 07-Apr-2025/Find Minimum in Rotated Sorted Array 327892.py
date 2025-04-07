# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr_size = len(nums)
        def bst():
            l, h = 0 , arr_size - 1

            while l <= h:
                mid = (h + l) // 2
                # print(mid, l, h)
                if nums[mid - 1] > nums[mid] < nums[(mid + 1) % arr_size]:
                    return nums[mid]
                elif nums[mid] >= nums[-1]:
                    l = mid + 1
                else:
                    h = mid - 1
        if arr_size == 1:
            return nums[0]
        elif arr_size == 2:
            if nums[0] <= nums[1]:
                return nums[0]
            else:
                return nums[1]
        ans = bst()
        return ans