# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        # print(s)
        temp  = [0] * len(s)
        for i in range(len(indices)):
            temp[indices[i]] = str(s[i])
        return "".join(temp)