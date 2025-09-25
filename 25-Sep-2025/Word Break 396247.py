# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        mx = max(len(word) for word in wordDict)

        def dp(idx):
            if idx == len(s):
                return True

            if idx not in memo:
                # temp = ''
                # for i in range(idx, len(s)):
                #     temp += s[i]
                #     if len(temp) > 20:
                #         return False 
                #     if temp in wordDict:
                #         memo[i] = dp(i + 1)

                for j in range(idx, len(s)):
                    if s[idx : j + 1] in wordDict:
                        if dp(j + 1):
                            memo[idx] = True
                            break
                if idx not in memo:
                    memo[idx] = False
            
            return memo[idx]
        
        return dp(0)
            
            
                
            