# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        if count_s.keys() != count_t.keys():
            return False
        for k, v in count_s.items():
            if count_t[k] != v :
                return False
        else:
            return True