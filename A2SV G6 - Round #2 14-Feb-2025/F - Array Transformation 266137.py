# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
from math import inf
 
 
t  = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = Counter(arr)
    f_count = Counter(count.values())
    
    max_f = max(f_count)
    lower_b = 0
    min_oper = inf
    
    for k in range(1, max_f+1):
        
        if k in f_count:
            v = f_count[k]
            oper = 0
            z = 1
            
            for i in range(k+1, max_f+1):
                if i in f_count and i > z:
                    oper += f_count[i] * z
                    
                z += 1
                
            min_oper = min(oper + lower_b, min_oper)
            lower_b += k * v
            
    print(min_oper)