def can_defeat_dragons(s, dragons):
    dragons.sort()
    for dragon in dragons:
        xi, yi = dragon
        if s > xi:
            s += yi  
        else:
            return "NO"  
    return "YES"  

s, n = map(int, input().split())  
dragons = [tuple(map(int, input().split())) for _ in range(n)]  
print(can_defeat_dragons(s, dragons))
