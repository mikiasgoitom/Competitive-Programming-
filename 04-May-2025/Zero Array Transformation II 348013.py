# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0:
            return 0
        def helper(index):
            arr = [0] * (len(nums) + 1)

            for i in range(index + 1):
                l, r, v = queries[i]
                arr[l] += v
                arr[r + 1] -= v
            pre = arr[:]
            for i in range(1, len(arr)):
                pre[i] += pre[i-1]
            for i in range(len(nums)):
                if nums[i] > pre[i]:
                    return False

            return True
        
        low, high = 0, len(queries) - 1

        while low <= high:
            mid = (high + low) // 2
            if helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        if low < len(queries):
            return low + 1
        else:
            return -1