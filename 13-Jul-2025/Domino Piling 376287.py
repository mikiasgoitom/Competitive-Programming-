# Problem: Domino Piling - https://codeforces.com/problemset/problem/50/A

import math
 
m, n = list(map(int, input().split()))
maxDomino =  math.floor((m * n) / 2)
 
print(maxDomino)