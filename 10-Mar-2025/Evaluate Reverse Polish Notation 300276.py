# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        oper = set(['+', '-', '/', '*'])
        ans = 0
        for smb in tokens:
            if smb.lstrip('-').isdigit():
                stk.append(int(smb))
            elif smb in oper:
                num2 = stk.pop()
                num1 = stk.pop()
                if smb == '+':
                    stk.append(num1 + num2)  
                elif smb == '-':
                    stk.append(num1 - num2)  
                elif smb == '/':
                    divided = num1 / num2
                    if divided > 0:
                        divided = floor(divided)
                    else:
                        divided = ceil(divided)
                    stk.append(divided)  
                elif smb == '*':
                    stk.append(num1 * num2)  
        return stk.pop()

