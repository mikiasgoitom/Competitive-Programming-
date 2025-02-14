# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter, defaultdict
 
 
t  = int(input())
 
for z in range(t):
    n = int(input())
    s = input()
    
    set_a = defaultdict(int)
    set_b = Counter(s)
    
    max_substr = 0
    for i in range(n-1):
        chr = s[i]
        set_b[chr] -= 1
        set_a[chr] += 1
        
        if set_b[chr] == 0:
            set_b.pop(chr)
        
        max_substr = max(len(set_a) + len(set_b) , max_substr)
 
        
    print(max_substr)