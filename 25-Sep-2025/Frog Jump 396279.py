# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        exist = set([k for k in stones])
        # print(exist)
        memo = {}

        def dfs(pos, last_jmp):
            if pos >= stones[-1]:
                return pos == stones[-1]

            if (pos, last_jmp) not in memo:
                can_jmp = False
                if pos + last_jmp in exist and not can_jmp:
                    can_jmp = dfs(pos + last_jmp, last_jmp)
                
                if pos + (last_jmp + 1) in exist and not can_jmp:
                    can_jmp = dfs(pos + (last_jmp + 1), last_jmp + 1)
                
                if pos + (last_jmp - 1) in exist and last_jmp >= 2 and not can_jmp:
                    can_jmp = dfs(pos + (last_jmp - 1), last_jmp - 1)

                # print((i, last_jmp), can_jmp)
                memo[(pos, last_jmp)] = can_jmp

            return memo[(pos, last_jmp)]
        
        return stones[1] == 1 and dfs(stones[1], 1)
        # print(memo)