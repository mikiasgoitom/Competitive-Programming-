# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        n_set = set(nums)
        for i in range(size+1):
            if i not in n_set:
                return i
