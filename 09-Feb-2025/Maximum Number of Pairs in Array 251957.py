# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0] * 2
        count = Counter(nums)
        for k, v in count.items():
            if v > 1:
                ans[0] += v // 2
                v -= (v // 2) * 2
            if v == 1:
                ans[1] += v
                print(k, v)
            # print(ans)
        return ans