# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            prev = nums[i]
            for j in range(i, len(nums)):
                prev = math.gcd(prev, nums[j])
                if prev == k:
                    ans += 1
                    
        return ans
    
    """ 
    [3,12,9,6]
    [0, 0, 0, 0]
    """