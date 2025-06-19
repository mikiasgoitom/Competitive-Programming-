# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        sln = []
        def bkt():
            if (len(sln) >= 2) and (sln[-1] == '0' and sln[-2] == '0'):
                return
            
            if len(sln) == n:
                ans.append("".join(sln[:]))
                return
            if len(sln) > n:
                return

            for candi in ['0', '1']:
                sln.append(candi)
                bkt()
                sln.pop()

        bkt()
        return ans
                