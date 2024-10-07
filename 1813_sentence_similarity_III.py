def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    w1 = sentence1.split()
    w2 = sentence2.split()
    
    len1 = len(w1)
    len2 = len(w2)
    
    i, j = 0, 0
    
    while i < len1 and i < len2 and w1[i] == w2[i]:
        i+=1
    while j < (len1-i) and j < (len2-i) and w1[len1-1-j] == w2[len2-1-j]:
        j+=1
    return len1 == i+j or len2== i+j