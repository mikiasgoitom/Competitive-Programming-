# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list = [float('inf')] * len(nums)
        min_so_far = float('inf')

        for i in range(len(nums)):
            min_so_far = min(min_so_far, min(min_list[i], nums[i]))
            min_list[i] = min_so_far
        

        mono_stk = []
        for i in range(len(nums)-1, 0, -1):
            if not mono_stk:
                mono_stk.append(nums[i])
            else:
                while mono_stk and min_list[i-1] >= mono_stk[-1]:
                    mono_stk.pop()

                if mono_stk and mono_stk[-1] < nums[i] and min_list[i-1] < mono_stk[-1]:
                    return True
                
                while mono_stk and mono_stk[-1] < nums[i]:
                    mono_stk.pop()
                mono_stk.append(nums[i])
        print()
        return False                    
