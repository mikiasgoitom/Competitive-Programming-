# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def _find_pse():
            stk = []
            res = [-1] * len(arr)

            for i in range(len(arr)):
                while stk and arr[stk[-1]] > arr[i]:
                    stk.pop()
                if stk:
                    res[i] = stk[-1]
                else:
                    res[i] = -1
                stk.append(i)
            return res
        
        def _find_nse():
            stk = []
            res = [len(arr)] * len(arr)

            for i in range(len(arr) - 1, -1, -1):
                while stk and arr[stk[-1]] >= arr[i]:
                    stk.pop()
                if stk:
                    res[i] = stk[-1]
                else:
                    res[i] = len(arr)
                stk.append(i)
            return res
            
        def calc_total():
            nse = _find_nse()
            pse = _find_pse()
            total, MOD = 0, 10**9 + 7

            for i in range(len(arr)):
                left = i - pse[i]
                right = nse[i] - i
                total = (total + (left * right * arr[i]) % MOD) % MOD
            return total

        return calc_total()
        