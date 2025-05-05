# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        size = defaultdict(lambda: 1)
        equations.sort(key=lambda x: x[1] == '!')
        print(equations)

        def find(x):
            parent.setdefault(x, x)
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            fx = find(x)
            fy = find(y)
            if fx != fy:
                if size[fx] > size[fy]:
                    parent[fy] = parent[fx]
                    size[fx] += size[fy]
                else:
                    parent[fx] = parent[fy]
                    size[fy] += size[fx]
        
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0]) == find(eq[-1]):
                    return False
            else:
                union(eq[0], eq[-1])
        # print(parent)
        return True
