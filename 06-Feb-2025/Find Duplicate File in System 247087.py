# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dp = defaultdict(list)       
        for path in paths:
            val = path.split()
            dir = val[0]
            files = val[1:]
            for file in files:
                open_p = file.index('(')
                content = file[open_p+1:-1]
                value = dir + '/' + file[:open_p]
                dp[content].append(value)
        # print(dp)
        ans = []
        for key, val in dp.items():
            if len(val) >= 2:
                ans.append(val)
        return ans