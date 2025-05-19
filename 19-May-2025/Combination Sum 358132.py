# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        sln = []
        def bkt():
            total = sum(sln)
            if total == target:
                res.add(tuple(sorted(sln.copy())))
                return
            if total > target:
                return

            for candi in candidates:
                sln.append(candi)
                bkt()
                sln.pop()
        
        bkt()
        return list(res)