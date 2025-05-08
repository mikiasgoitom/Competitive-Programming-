# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        count = n
        def find(x):
            while x != par[x]:
                x = par[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            nonlocal count
            if x != y:
                if size[x] > size[y]:
                    par[y] = par[x]
                    size[x] += size[y]
                else:
                    par[x] = par[y]
                    size[y] += size[x]
                count -= 1

        par = [i for i in range(n)]
        size = [1] * (n)

        for i in range(n):
            for j in range(i, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        
        return n - count