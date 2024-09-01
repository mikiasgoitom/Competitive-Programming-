import collections
from typing import List

def similarPairs(words: List[str]) -> int:
    frequency = collections.defaultdict(int)
    pairs = 0
    for word in words:
        temp = frozenset(word)
       
        pairs += frequency[temp]
        frequency[temp] +=1
    return pairs


# x = 'cbaad'
# x = sorted(set(x))
# x = ''.join(x)
# print(x)

x = ["aba","aabb","abcd","bac","aabc"]
num  = similarPairs(x)
print(num)