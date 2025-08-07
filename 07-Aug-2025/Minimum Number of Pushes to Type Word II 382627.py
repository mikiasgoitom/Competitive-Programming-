# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        
        i = 1
        ans = 0

        max_vals = sorted(count.values(), reverse=True)
        # print(count)
        for v in max_vals:
            if i < 9:
                ans += 1 * v
            else:
                ans += (ceil(i / 8) * v)
                # print(ceil(i / 8), v, ans, i)
            i += 1
        return ans
                