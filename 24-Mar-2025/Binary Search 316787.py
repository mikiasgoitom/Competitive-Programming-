# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def bs(self, l, r, target, nums):
        mid = (l + r) // 2
        if l > r :
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bs(l, mid - 1, target, nums)
        else:
            return self.bs(mid + 1, r , target, nums)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums)-1, target, nums)