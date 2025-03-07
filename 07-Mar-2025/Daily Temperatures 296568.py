# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stk = []  
        size_temper = len(temperatures)
        ans = [0] * size_temper

        for i in range(size_temper):
            if not mono_stk:
                mono_stk.append(i)
            elif mono_stk:
                while mono_stk and temperatures[mono_stk[-1]] < temperatures[i]:
                    ans[mono_stk[-1]] = i - mono_stk[-1]
                    mono_stk.pop()
                mono_stk.append(i)
        return ans 