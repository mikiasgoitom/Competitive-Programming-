# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict


t  = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    pri_dia = defaultdict(int)
    sec_dia = defaultdict(int)
    for row in range(n):
        for col in range(m):  
            diag1 = row - col
            diag2 = row + col
            
            val = mat[row][col]
            
            pri_dia[diag1] += val
            sec_dia[diag2] += val
    max_sum = 0
    for row in range(n):
        for col in range(m):
            sums = pri_dia[row - col] + sec_dia[row + col] - mat[row][col]
            max_sum = max(max_sum, sums)
        
    print(max_sum)