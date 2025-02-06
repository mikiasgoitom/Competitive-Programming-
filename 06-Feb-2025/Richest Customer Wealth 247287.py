# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for row in range(len(accounts)):
            temp = 0
            for col in range(len(accounts[row])):
                temp += accounts[row][col]
            max_wealth = max(max_wealth, temp)
        return max_wealth