# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        size = len("".join(s.split()))
        # print(size)
        s = s.split(" ")
        max_size = 0
        for i in range(len(s)):
            max_size = max(max_size, len(s[i]))
        # print(s)
        for i in range(len(s)):
            if len(s[i]) < max_size:
                space = max_size - len(s[i])
                s[i] += "".join([' ' for _ in range(space)])
        ans = []
        # print(s)
        for i in range(max_size):
            buff = []
            for j in range(len(s)):
                # print(len(s[j]))
                buff.append(s[j][i])
            ans.append("".join(buff).rstrip())
        return ans