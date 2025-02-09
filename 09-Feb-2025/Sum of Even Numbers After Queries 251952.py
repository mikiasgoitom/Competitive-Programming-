# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        count = sum( n for n in nums if n % 2 == 0)
        for val, idx in queries:
            temp = nums[idx]

            if temp % 2 == 0:
                count -= temp
            
            nums[idx] += val
            if nums[idx] % 2 == 0:
                count += nums[idx] 

            ans.append(count)    
            
        return ans