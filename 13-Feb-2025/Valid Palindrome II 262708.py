# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        new_s = ''
        while l <= r:
            if s[l] != s[r]:
                n_l, n_r = s[l+1:r+1], s[l:r]
                return n_l == n_l[::-1] or n_r == n_r[::-1]
            l += 1
            r -= 1
        return True