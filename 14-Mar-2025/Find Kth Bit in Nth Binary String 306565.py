# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def binaryConstruction(self, n, k):
        if n == 1:
            return "0"

        s_len = (1 << n) - 1
        mid = (s_len // 2) + 1

        if k == mid:
            return "1"
        elif k <  s_len // 2:
            return self.binaryConstruction(n - 1, k)
        else:
            bit = self.binaryConstruction(n - 1, s_len - k - 1)
            return "0" if bit == '1' else "1"
        
    def findKthBit(self, n: int, k: int) -> str:
        return self.binaryConstruction(n, k-1)
        # print(s)
        # return s[k-1]
