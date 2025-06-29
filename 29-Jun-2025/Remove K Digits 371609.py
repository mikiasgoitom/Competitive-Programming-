# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:       
        stk = [num[0]]
        i = 1

        while i < len(num):
            while stk and k > 0 and num[i] < stk[-1]:
                stk.pop()
                k -= 1
            stk.append(num[i])
            i += 1

        while stk and k > 0:
            stk.pop()
            k -= 1

        for i in range(len(stk)):
            if stk[i] != '0':
                return "".join(stk[i:])
        return '0'