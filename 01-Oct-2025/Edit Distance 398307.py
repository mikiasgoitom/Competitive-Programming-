# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        # i,   
        def dfs(i, j):
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i
            
            if (i, j) in  memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                opt1 = dfs(i, j + 1) + 1
                opt2 = dfs(i + 1, j) + 1
                opt3 = dfs(i + 1, j + 1) + 1
                memo[(i, j)] = min(float('inf'), opt1, opt2, opt3)

            return memo[(i, j)]
        
        return dfs(0, 0)
      
            