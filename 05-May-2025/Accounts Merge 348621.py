# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent = {}

        def find(x):
            parent.setdefault(x, x)
            root = x
            while root != parent[root]:
                root = parent[root]

            while root != x:
                nxt_x = parent[x]
                parent[x] = root
                x = nxt_x
            return x

        def union(x, y):
            parent[find(y)] = find(x)


        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                union(i, accounts[i][j])
    

        temp = defaultdict(list)
        
        for node in parent:
            if not isinstance(node, int):
                temp[parent[find(node)]].append(node)
        
        ans = [[accounts[key][0]] + sorted(temp[key]) for key in temp]
        
        return ans
        