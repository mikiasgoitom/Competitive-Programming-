# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0  
        oper = 0   
        
        for char in s:
            if char == '1':
                ones += 1  
            else:
                oper += ones
        
        return oper