# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        alph = {chr(97 + i): i for i in range(26)}
        btmap = []

        # temp = sorted(words, key=lambda x: len(x))
        for i in range(len(words)):
            bt = [0] * 26
            for j in range(len(words[i])):
                bt[alph[words[i][j]]] = 1
            btmap.append(bt)            
        # print(btmap)
        # print(temp)
        ans = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                invalid = False
                for k in range(26):
                    if btmap[i][k]  == 1 and btmap[j][k] == 1:
                        # print("hhasdf")
                        invalid = True
                        break
                if not invalid:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans