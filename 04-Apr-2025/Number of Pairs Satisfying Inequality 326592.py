# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0
        def merger(left, right):
            nonlocal ans
            s_arr = []

            i, j = 0, 0
            while i < len(left):
                while j < len(right) and left[i] > right[j] + diff:
                    j += 1
                ans += len(right) - j
                i += 1


            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    s_arr.append(left[i])
                    i += 1
                else:
                    s_arr.append(right[j])
                    j += 1

            while i < len(left):
                s_arr.append(left[i])
                i += 1
            
            while j < len(right):
                s_arr.append(right[j])
                j += 1
            
            return s_arr
                
        def mergeSort(l, r, arr):
            if l >= r:
                return [arr[l]]

            mid = (r + l) // 2

            left = mergeSort(l, mid, arr)
            right = mergeSort(mid + 1, r, arr)

            return merger(left, right)


        new_arr = [0] * len(nums1)

        for i in range(len(nums1)):
            new_arr[i] = nums1[i] - nums2[i]
        mergeSort(0, len(new_arr) - 1, new_arr)
        return ans


