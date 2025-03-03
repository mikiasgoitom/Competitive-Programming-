# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = defaultdict(int)
        flag = True
        for n in bills:
            if n == 5:
                register[5] += 1
            elif n == 10:
                register[10] += 1
                if register[5] > 0:
                    register[5] -= 1
                else:
                    flag = False
                    break
            elif n == 20:
                if register[5] > 0:
                    register[5] -= 1
                else:
                    flag = False
                    break
                if register[10] > 0:
                    register[10] -= 1
                else:
                    if register[5] > 1:
                        register[5] -= 2
                    else:
                        flag = False
                        break
        return flag
