# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        prefix1 = []
        accum = 0

        for i in range(len(s)-1, 0, -1):
            if s[i] == '1':
                accum += 1
                prefix1.append(accum)
            else:
                prefix1.append(accum)
        prefix1 = prefix1[::-1]
        max_sum = 0
        num_zero = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                num_zero += 1
            max_sum = max(max_sum, num_zero + prefix1[i])

        return max_sum