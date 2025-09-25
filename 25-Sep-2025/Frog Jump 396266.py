# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        exist = set([k for k in stones])
        # print(exist)
        memo = {}

        def dp(i, k):
            if i >= stones[-1]:
                return i == stones[-1]

            if (i, k) not in memo:
                opt = False
                if i + k in exist and not opt:
                    opt = dp(i + k, k)
                
                if i + (k + 1) in exist and not opt:
                    opt = dp(i + (k + 1), k + 1)
                
                if i + (k - 1) in exist and k >= 2 and not opt:
                    opt = dp(i + (k - 1), k - 1)

                # print((i, k), opt)
                memo[(i, k)] = opt

            return memo[(i, k)]
        
        return stones[1] == 1 and dp(stones[1], 1)
        # print(memo)