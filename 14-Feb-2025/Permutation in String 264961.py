# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set_s1 = Counter(s1)
        set_s2 = defaultdict(int)
        s1_sz, s2_sz = len(s1), len(s2)

        left, right = 0, s1_sz - 1
        if len(s1) > len(s2):
            return False

        for i in range(left, right+1):
            set_s2[s2[i]] += 1

        while right < s2_sz:
            if set_s1 == set_s2:
                return True

            if set_s2[s2[left]] == 1:
                del set_s2[s2[left]]
            else:
                set_s2[s2[left]] -= 1
                
            right += 1
            if right < s2_sz:
                set_s2[s2[right]] += 1

            left += 1
        return False