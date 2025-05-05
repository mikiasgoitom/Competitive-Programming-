# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count  = Counter(word)
        freq_dist = Counter(count.values())
        
        if len(freq_dist) == 1:
            ky, vals = list(freq_dist.items())[0]
            return ky == 1 or vals == 1
        elif len(freq_dist) == 2:
            (ky1, val1), (ky2, val2) = freq_dist.items()
        
            if (ky1 == 1 and val1 == 1) or (ky2 == 1 and val2 == 1):
                return True
            
            if abs(ky1 - ky2) == 1:
                if (ky1 > ky2 and val1 == 1) or (ky2 > ky1 and val2 == 1):
                    return True
        return False
