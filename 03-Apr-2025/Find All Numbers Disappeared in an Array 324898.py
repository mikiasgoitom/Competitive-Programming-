# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def cyclicSort():
            nonlocal nums
            i = 0
            n = len(nums)
            while i < n:
                corr_indx = nums[i] - 1
                if nums[i] != nums[corr_indx]:
                    temp = nums[i]
                    nums[i] = nums[corr_indx]
                    nums[corr_indx] = temp
                else:
                    i += 1
        cyclicSort()
        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)
        
        return ans