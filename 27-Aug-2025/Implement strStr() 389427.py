# Problem: Implement strStr() - https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = haystack.find(needle)
        return idx