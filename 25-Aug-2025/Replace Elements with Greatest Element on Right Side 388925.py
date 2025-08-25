# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        comp = [0] * len(arr)
        comp[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            comp[i] = max(arr[i + 1], comp[i + 1])

        return comp