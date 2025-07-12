# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.is_end = True

    def search(self, word: str, node = None, idx = 0) -> bool:
        if not node:
            node = self.root

        if idx == len(word):
            return node.is_end
        
        if word[idx] == ".":
            for ch in node.children:
                if self.search(word, node.children[ch], idx + 1):
                    return True
            return False
        else:
            if word[idx] not in node.children:
                return False
            return self.search(word, node.children[word[idx]], idx + 1)

"""
["W","add","addddd","addd","addd","ssss","ssss","addddd","ssss","sssss","ssssss","ssss","sssss","s"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
[null,null,ndddddull,nuddll,nudll,fadlse,fddalse,nudddll,faaalse,trdddue,faldddse,falddse,false,false]
[null,null,ndddddull,ndddull,nsull,false,fddalse,nudddll,trrrrue,tdddrue,faldddse,fddalse,true,false]
"""

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)