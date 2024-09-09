def findTheDifference(s: str, t: str) -> str:
    for c in t:
        if(t.count(c) > s.count(c)):
            return c
    return -1
    
s = 'ae'
t = 'aea'
ordered = findTheDifference(s,t)
print(ordered)