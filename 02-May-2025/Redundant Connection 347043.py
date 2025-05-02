# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rep_a = find(x)
            rep_b = find(y)

            if rep_a != rep_b:
                if size[rep_a] > size[rep_b]:
                    parent[rep_b] = parent[rep_a]
                    size[rep_a] += size[rep_b]
                else:
                    parent[rep_a] = parent[rep_b]
                    size[rep_b] += size[rep_a]
                return True
            else:
                return False

        n = len(edges) + 1
        parent = [i for i in range(n)]
        size = [1] * n

        ans = None
        for u, v in edges:
            if not union(u, v):
                ans = [u, v]
        
        return ans
                
        