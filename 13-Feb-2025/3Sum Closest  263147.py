# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)-2):
            second, third = i + 1, len(nums) - 1
            while second < third:
                curr_sum = nums[i] + nums[second] + nums[third]
                if curr_sum == target:
                    return curr_sum
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum
                if curr_sum > target:
                    third -= 1
                else:
                    second += 1
        return closest_sum
