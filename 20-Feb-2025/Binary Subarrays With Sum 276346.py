# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr_sum = 0
        pre = defaultdict(int)
        pre[0] = 1
        ans = 0
        for n in nums:
            curr_sum += n
            diff = curr_sum - goal
            ans += pre[diff]
            pre[curr_sum] += 1
        return ans