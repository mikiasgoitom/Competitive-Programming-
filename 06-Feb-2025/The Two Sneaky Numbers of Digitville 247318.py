# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_n = Counter(nums)
        ans = []
        for k, v in count_n.items():
            if count_n[k] >= 2:
                ans.append(k)
        return ans