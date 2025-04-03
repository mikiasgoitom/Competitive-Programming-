# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        def cyclicSort():
            nonlocal nums
            i = 0
            n = len(nums)
            while i < n:
                corr_index = nums[i] - 1
                if nums[i] != nums[corr_index]:
                    temp = nums[i]
                    nums[i] = nums[corr_index]
                    nums[corr_index] = temp
                else:
                    i += 1
        
        ans = []
        cyclicSort()
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                ans.append(nums[i])
                ans.append(i + 1)
        return ans