# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                ans += (i + 1) * (len(word) - i)
        return ans