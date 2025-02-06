# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        ans = []
        # check if the str has @
        if "@" in s:
            s = s.lower()
            ans.append(s[:1])
            index = s.index('@')
            stars = ('*****')
            ans.append(stars)
            ans.append(s[index-1])
            ans.append(s[index:])
        # remove filter out only '+' and num if num
        else:
            num = "".join(c for c in s if c.isdigit())
            if len(num) == 10:
                ans.append('***-***-')
            elif len(num) == 11:
                ans.append('+*-***-***-')
            elif len(num) == 12:
                ans.append('+**-***-***-')
            elif len(num) == 13:
                ans.append('+***-***-***-')
            ans.append(num[-4:])                
        return "".join(ans)
            
            