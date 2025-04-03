# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def cyclicSort():
            nonlocal nums
            i = 0
            n = len(nums)

            while i < n:
                corr_indx = nums[i]
                if 0 <= nums[i] < n and nums[i] != nums[corr_indx]:
                    temp = nums[i]
                    nums[i] = nums[corr_indx]
                    nums[corr_indx] = temp
                else:
                    i += 1

        cyclicSort()
        print(nums)
        ans = []

        for i in range(len(nums)):
            if nums[i] != i:
                ans.append(i)
        if ans:
            return ans[0]
        else:
            return len(nums)