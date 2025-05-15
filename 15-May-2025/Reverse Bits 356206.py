# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        
        pow = 31
        res = 0

        while n > 0:
            modul = n % 2
            res += modul * 2 ** pow
            n //= 2
            pow -= 1
        
        return res 
