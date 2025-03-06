# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        temp = target

        while temp > 1 and maxDoubles > 0:
            if temp % 2:
                count += 1
            temp //= 2
            maxDoubles -= 1
            count += 1
        if maxDoubles == 0:
            count += temp - 1
        return count