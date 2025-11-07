# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C(x):
            return math.comb(x + 2, 2) if x >= 0 else 0
        universe = C(n)
        sub1 = 3 * C(n - limit - 1)
        add2 = 3 * C(n - 2 * (limit + 1))
        sub3 = C(n - 3 * (limit + 1))
        # print(universe, sub1, add2, sub3)
        return universe - sub1 + add2 - sub3