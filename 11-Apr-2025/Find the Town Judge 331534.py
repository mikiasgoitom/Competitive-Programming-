# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        freq = [0] * (n + 1)
        if not trust and n < 2:
            return n
        for a, b in trust:
            graph[a].append(b)
            freq[b] += 1
            graph[b]
        # print(graph)
        ans = -1
        for k in graph:
            if len(graph[k]) == 0 and freq[k] == (len(freq) - 2):
                ans= k

        
        print(freq)
        return ans