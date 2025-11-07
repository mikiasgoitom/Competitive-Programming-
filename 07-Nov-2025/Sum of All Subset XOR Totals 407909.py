# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        hold = []
        for i in range(1, len(nums) + 1):
            for comb in combinations(nums, i):
                accum = comb[0]
                for j in range(1, len(comb)):
                    accum ^= comb[j]
                hold.append(accum)
        
        # print(hold)
        return sum(hold)