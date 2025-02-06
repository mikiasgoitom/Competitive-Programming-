# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = []
        bar = Counter(chars)
        for w in words:
            flag = True
            count_w = Counter(w)
            for k, v in count_w.items():
                if bar[k] < v:
                    flag = False
                    break
            if flag:
                ans.append(w)
        return len("".join(ans))
