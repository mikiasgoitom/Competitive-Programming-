# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mapper = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mapper[r+c].append(mat[r][c])
        ans = []
        for k, v in mapper.items():
            if k % 2 == 0:
                ans.extend(reversed(v))
            else:
                ans.extend(v)
        return ans