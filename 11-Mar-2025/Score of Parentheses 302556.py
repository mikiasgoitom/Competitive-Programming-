# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        i = 0
        while i < len(s): 
            if not stk:
                stk.append(s[i])
                i += 1
            else:
                if stk[-1] == '(' and s[i] == ')':
                    stk.pop()
                    if stk and isinstance(stk[-1], int):
                        num = stk.pop()
                        num += 1
                        stk.append(num)
                    else:
                        stk.append(1)
                elif len(stk) >= 2 and isinstance(stk[-1], int) and s[i] == ')':
                    num = stk.pop()
                    while len(stk) >= 2 and isinstance(stk[-1], int):
                        num += stk.pop()
                    num *= 2
                    stk.pop()
                    stk.append(num)
                else:
                    stk.append(s[i])
                i += 1

        ans = 0
        while stk:
            ans += stk.pop()
        return ans
                
                