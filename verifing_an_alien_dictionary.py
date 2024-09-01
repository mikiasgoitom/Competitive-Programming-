from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    j = 1
    i = 0
    index = 0
    while j < (len(words)):
        if (index >= len(words[i]) or index >= len(words[j])):
            if index >= len(words[i]):
                i+=1
                j+=1
                index = 0
            else:
                return False
        elif(order.index(words[i][index]) <  order.index(words[j][index]) or words[i] == words[j]):
            i+=1
            j+=1
            index = 0
        elif(order.index(words[i][index]) ==  order.index(words[j][index])):
            index +=1
        else:
            return False
    return True
found = isAlienSorted(["app","apple"],"abcdefghijklmnopqrstuvwxyz")
print(found)