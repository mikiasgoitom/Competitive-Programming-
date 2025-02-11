# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        if min_num < 0:
            freq = [0] * (max(nums) + abs(min_num) + 1)
        else:
            freq = [0] * (max(nums) + 1)
            min_num = 0
        print(min_num, len(freq))
        for i in range(len(nums)):
            freq[nums[i] + abs(min_num)] += 1
        
        ans = []
        for i in range(len(freq)):
            print
            if freq[i] > 0:
                iter = freq[i]
                while iter > 0:
                    ans.append(i + min_num)        
                    iter -= 1
        return ans