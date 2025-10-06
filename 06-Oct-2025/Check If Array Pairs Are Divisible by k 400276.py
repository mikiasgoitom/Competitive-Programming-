# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_k_arr = [0] * (k + 1)
        for n in arr:
            mod_k_arr[n%k] += 1
        print(mod_k_arr)
        for i in range(k + 1):
            if i == 0 or mod_k_arr[i] == 0:
                continue
            if mod_k_arr[i] != mod_k_arr[k-i] or (k % 2 == 0  and mod_k_arr[k // 2] % 2 != 0):
                # print(mod_k_arr[i],i, mod_k_arr[k-i])
                return False
        
        return True