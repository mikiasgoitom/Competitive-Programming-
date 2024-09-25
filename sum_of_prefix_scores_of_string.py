from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word) -> None:
        node  = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count+=1
    def get_prefix_score(self, word) -> int:
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.count
        return score
def sumPrefixScores(words) -> List[int]:
    trie = Trie()
    result = []
    for word in words:
        trie.insert(word)
        
    for word in words:
        result.append(trie.get_prefix_score(word))
    return result


words = ["abc","ab","bc","b"]
result = sumPrefixScores(words)
print(result)
            