def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    maxRange = max(len(word1),len(word2))
    for i in range(maxRange):
        if(i <= (len(word1)-1)):
            result += (word1[i])
        if(i <= (len(word2)-1)):
            result += (word2[i])
    return result
word1 = 'ab'
word2 = 'xyz'
result = mergeAlternately(word1, word2)
print("result: " + result)