# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        last = {c : i for i, c in enumerate(s)}
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last[char])
            
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        
        return ans