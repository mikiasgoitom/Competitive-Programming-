# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        s = path.split('/')
        for i in range(len(s)):
            if s[i] == '..' and stk:
                stk.pop()
            elif s[i] != '..' and s[i] != '.' and s[i] != '':
                stk.append(s[i])
        return "/" + "/".join(dir for dir in stk)
                