# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk_1 = []
        stk_2 = []

        for c in s:
            if c == '#' and stk_1:
                stk_1.pop()
            elif c != '#':
                stk_1.append(c)
        for c in t:
            if c == '#' and stk_2:
                stk_2.pop()
            elif c != '#':
                stk_2.append(c)
        return stk_1 == stk_2
        