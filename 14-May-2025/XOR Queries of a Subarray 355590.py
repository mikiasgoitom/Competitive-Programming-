# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorpre = [0]
        for i in range(len(arr)):
            xorpre.append(xorpre[-1] ^ arr[i])
        
        ans = []
        
        for l, r in queries:
            ans.append(xorpre[r+1] ^ xorpre[l])
        
        return ans