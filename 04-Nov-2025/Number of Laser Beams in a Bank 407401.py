# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        i = 0
        while i < len(bank):
            num_1 = bank[i].count('1')
            if num_1 >= 1:
                for j in range(i + 1, len(bank)):
                    num_j_1 = bank[j].count('1')
                    if num_j_1 >= 1:
                        ans += (num_1 * num_j_1)
                        # print(ans)
                        i = j - 1
                        break
                    j += 1
            i += 1
        return ans
