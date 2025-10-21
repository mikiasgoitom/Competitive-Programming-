# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = {'#':True}
        candi = ['']
        # candi
        for w in words:
            invalid = False
            node = trie

            for ch in w:
                if '#' not in node:
                    invalid = True
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = True
            if not invalid:
                if len(candi[0]) < len(w):
                    candi[0] = w
        
        return candi[0]

