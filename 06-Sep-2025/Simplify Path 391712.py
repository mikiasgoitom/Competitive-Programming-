# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        npath = path.split('/')
        # print(npath)
        stk = []
        ans = []
        for c in npath:
            if c == '/' or c == '':
                continue
            if not stk:
                # print("sdf", c )
                if c != '..' and c != '.':
                    stk.append(c)
            elif c == '..':
                stk.pop()
            elif c == '.':
                continue
            else:
                # print(c)
                if c != '..' and c != '.':
                    stk.append(c)
        # print(stk)
        return "/" + ("/".join(stk))
            
