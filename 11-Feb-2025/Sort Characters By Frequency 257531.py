# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        # s = list(s)
        s = sorted(count.items(), key = lambda item: item[1],reverse = True)
        ans = [key for key, value in s for _ in range(value)]
        
        return "".join(ans)
