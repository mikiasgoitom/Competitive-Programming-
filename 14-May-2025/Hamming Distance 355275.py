# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        abit = bin(x)[2:]
        bbit = bin(y)[2:]

        abit = abit.zfill(len(bbit))
        bbit = bbit.zfill(len(abit))
        
        i = 0
        count = 0
        while i < len(bbit):
            # print(abit, bbit, i)
            if abit[i] != bbit[i]:
                count += 1
            i += 1
        
        
        return count