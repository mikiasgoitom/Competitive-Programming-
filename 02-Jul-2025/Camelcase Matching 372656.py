# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        count = Counter([ch for ch in pattern])
        ans = []
        for i in range(len(queries)):
            j = 0
            p_i = 0
            exited = False
            ptrn = count.copy()
            while j < len(queries[i]):
                if (ord(queries[i][j]) < ord('a')) and ptrn[queries[i][j]] < 1:
                    ans.append(False)
                    exited = True
                    break
                elif (ord(queries[i][j]) < ord('a')) and ptrn[queries[i][j]] > 0:
                    ptrn[queries[i][j]] -= 1
                
                if p_i < len(pattern) and (queries[i][j] == pattern[p_i]):
                    p_i += 1
                j += 1

            if not exited:
                if p_i < len(pattern):
                    ans.append(False)
                else:
                    ans.append(True)
        
        return ans