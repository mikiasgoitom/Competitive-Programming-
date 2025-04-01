# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        def merger( left_arr, right_arr):
            nonlocal ans
            s_arr = []
            i, j = 0, 0
            # print("b", left_arr, right_arr)
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i][0] <= right_arr[j][0]:
                    ans[left_arr[i][1]] += j
                    s_arr.append(left_arr[i])
                    i += 1
                else:
                    s_arr.append(right_arr[j])
                    j += 1

            while i < len(left_arr):
                ans[left_arr[i][1]] += j
                s_arr.append(left_arr[i])
                i += 1
            
            s_arr.extend(right_arr[j:])

            # print(s_arr, ans)
            return s_arr

        def mergeSort(l, r, arr):
            if l >= r:
                return [arr[l]]

            mid = (r + l) // 2

            left_arr = mergeSort(l, mid, arr)
            right_arr = mergeSort(mid + 1, r, arr)

            return merger(left_arr, right_arr)
        
        new_arr = []

        for i in range(len(nums)):
            new_arr.append((nums[i], i))

        s_arr = mergeSort(0, len(nums) - 1, new_arr)

        return ans
        

        