# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0
        for n in nums:
            curr_sum += n
            rem = curr_sum % k

            ans += prefix[rem]
            prefix[rem] += 1
            # print(ans, prefix, curr_sum)
        return ans
            