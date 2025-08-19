# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(list)
        uf = {}
        # print(uf)
        for i in range(len(s1)):
            graph[s1[i]].append(s2[i])
            graph[s2[i]].append(s1[i])
        
        def find(x):
            root = x

            if x not in uf:
                uf[x] = x
                return x
            
            while root != uf[root]:
                root = uf[root]
            
            while x != root:
                parent = uf[x]
                uf[x] = root
                x = parent
            return root
                
        def union(x, y):
            rx, ry = find(x), find(y)
            if ord(rx) != ord(ry):
                if ord(rx) > ord(ry):
                    uf[rx] = ry
                else:
                    uf[ry] = rx

        for i in range(len(s1)):
            for ch in graph[s1[i]]:
                union(s1[i], ch)
        ans = []
        # print("as", uf)
        # print("jjkh", find("p"), uf.get('m', '0'))
        for i in range(len(baseStr)):
            ans.append(uf[find(baseStr[i])])
            # print(ans, baseStr[i],uf[baseStr[i]])
        
        return "".join(ans)