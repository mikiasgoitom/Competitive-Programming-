# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for l in logs:
            if l == "../" and stk:
                stk.pop()
            elif l != "./" and l != "../":
                stk.append(l)
        return len(stk)