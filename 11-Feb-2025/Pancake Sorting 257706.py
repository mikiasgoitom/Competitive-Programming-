# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        sorted_arr = sorted(arr, reverse=True)
        unsorted_ns = len(arr)
        for i in range(len(sorted_arr)):
            max_n = sorted_arr[i]
            # print("---", max_n, arr)
            idx = arr.index(max_n)
            # print(max_n, idx)

            left = list(reversed(arr[:idx+1]))
            right = arr[idx+1:] if idx + 1 < len(arr) else []
            left.extend(right)
            # print(left, right)
            arr = left

            left = list(reversed(arr[:unsorted_ns]))
            right = arr[unsorted_ns:] if unsorted_ns < len(arr) else []
            # print(left, right, unsorted_ns)
            left.extend(right)
            arr = left

            print(idx, unsorted_ns, ans)
            ans.append(idx+1)
            ans.append(unsorted_ns)
            unsorted_ns -= 1
        return ans
            
