# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def bkt(i, candi):
            if len(candi) == len(s):
                temp= "".join(candi[:])
                res.append(temp)
                return
            if i >= len(s):
                return
            
            if s[i].isdigit():
                candi.append(s[i])
                bkt(i + 1, candi)
                candi.pop()
            else:
                sm, cap = s[i].lower(), s[i].upper()
                candi.append(sm)
                bkt(i + 1, candi)
                candi.pop()
                candi.append(cap)
                bkt(i + 1, candi)
                candi.pop()
        bkt(0, [])
        return res