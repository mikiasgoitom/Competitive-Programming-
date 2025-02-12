# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_v = 0
        while i < j:
            if height[i] <= height[j]:
                v = height[i] * (j - i)
                i += 1
            elif height[i] > height[j]:
                v = height[j] * (j - i)
                j -= 1
            max_v = max(max_v, v)
        return max_v