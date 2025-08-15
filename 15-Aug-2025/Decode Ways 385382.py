# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        checker = {str(k):chr(k + 64) for k in range(1, 27)}
        # print(checker)
        # ans = 0
        candi = ""
        memo = defaultdict(int)

        def btk(candi, idx):
            if checker.get(candi, 0) == 0:
                return 0
            if idx == len(s):
                return 1

            # print(ans, idx)

            candi = s[idx]
            ans = 0
            # print(memo)

            if (candi, idx) in memo:
                ans += memo[(candi, idx)]
            else:
                val = btk(candi, idx + 1)
                memo[(candi, idx)] = val
                ans += val
            
            if idx + 1 < len(s):
                candi = s[idx] + s[idx + 1]

                if (candi, idx) in memo:
                    ans += memo[(candi, idx)]
                else:
                    val = btk(candi, idx + 2)
                    memo[(candi, idx)] = val
                    ans += val
                    # print(val, ans)
            # print(ans)
            return ans
        
        ans = btk(s[0], 0)

        return ans
