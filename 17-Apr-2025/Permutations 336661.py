# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)

            temp = self.permute(nums)

            for perm in temp:
                perm.append(n)
            nums.append(n)
            res.extend(temp)

        return res