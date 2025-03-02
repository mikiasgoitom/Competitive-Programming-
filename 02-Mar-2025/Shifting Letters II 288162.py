# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
       
        prefix_shifts = [0] * (len(s) + 1)

        for l, r, d in shifts:
            if d == 0:
                prefix_shifts[l] -= 1
                prefix_shifts[r+1] += 1
            elif d == 1:
                prefix_shifts[l] += 1
                prefix_shifts[r+1] -= 1
        
        for i in range(1, len(prefix_shifts)):
            prefix_shifts[i] += prefix_shifts[i-1]
        s_arr = list(s)
        # print(prefix_shifts, s_arr)
        for i in range(len(prefix_shifts)-1):
            # accum += prefix_shifts[i]
            s_arr[i] = chr(( (ord(s_arr[i]) - 97 + prefix_shifts[i]) % 26 ) + 97)

        return "".join(s_arr)


