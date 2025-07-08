# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def validator(sol):
            pfx_arr = [0] * len(nums)
            pfx_arr[0] = nums[0]
            subarr = 1
            for i in range(1, len(nums)):
                if pfx_arr[i - 1] + nums[i] > sol:
                    pfx_arr[i] = nums[i]
                    subarr += 1
                    continue
                pfx_arr[i] = pfx_arr[i - 1] + nums[i]
            # print(sol, subarr, pfx_arr)
            return subarr <= k
        
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if validator(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
        