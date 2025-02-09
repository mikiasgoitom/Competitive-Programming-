# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        # histogram
        temp = [0] * len(nums)
        for num in nums:
            i = num - 1
            if temp[i] == 1:
                ans.append(num)
            else:
                temp[i] = 1
        return ans
