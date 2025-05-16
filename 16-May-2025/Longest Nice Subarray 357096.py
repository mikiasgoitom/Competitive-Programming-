# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        count = 0
        ans = 1
        running = 0

        i_holder = 0
        i, j = 0, 0

        while j < len(nums):
            while i < j and (running & nums[j]) != 0:
                running = running ^ nums[i]
                i += 1
            
            running = running | nums[j]
            
            ans = max(ans, j - i + 1)
            j += 1
        # print(pr)
        return ans

        