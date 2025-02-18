# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        ans = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            
            ans += prefix[diff]

            prefix[curr_sum] += 1
            # print(n, curr_sum, diff, prefix)
        return ans 