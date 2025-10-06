# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(questions):
                return 0
            
            if i not in memo:
                memo[i] = max(dfs(i + 1), dfs(i + questions[i][1] + 1) + questions[i][0])
            return memo[i]
        
        return dfs(0)