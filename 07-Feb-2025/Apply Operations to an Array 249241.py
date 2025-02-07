# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        prv = 0
        nex = 1
        while nex <= len(nums) -1:
            if nums[prv] == 0:
                while nex <= len(nums) -1:
                    if nums[nex] > 0:
                        nums[prv], nums[nex] = nums[nex], nums[prv]
                        break
                    nex += 1
            prv += 1
            nex = prv + 1
        return nums
        


