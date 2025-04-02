# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        def cyclicSort():
            nonlocal nums
            n = len(nums)
            i = 0
            while i < n:
                corr_index = nums[i] - 1
                if nums[i] != nums[corr_index]:
                    temp = nums[i]
                    nums[i] = nums[temp - 1]
                    nums[temp - 1] = temp
                else:
                    i += 1
        cyclicSort()
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.append(nums[i])
        return ans
        