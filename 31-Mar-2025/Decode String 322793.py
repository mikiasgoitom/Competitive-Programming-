# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        s_size = len(s)
        
        stk = []

        for i in range(s_size):
            if s[i] != ']':
                stk.append(s[i])
            else:
                temp = []
                segment = []
                digit = []

                while stk and stk[-1] != '[':
                    segment.append(stk.pop())

                stk.pop()
                str_segment = "".join(list(reversed(segment)))
                
                while stk and stk[-1].isdigit():
                    digit.append(stk.pop())

                num = "".join(list(reversed(digit)))
                loop = int(num)

                for _ in range(loop):
                    temp.append(str_segment)
                
                stk.append("".join(temp))
                segment.clear()
                digit.clear()
                temp.clear()

        return "".join(stk)
