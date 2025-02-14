# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

from collections import defaultdict
 
t  = int(input())
 
for _ in range(t):
    n =int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, list(input()))))
    # print(mat)
    num_oper = 0
    for row in range(n):
        for col in range(n):
            count = defaultdict(int)
            count[mat[row][col]] += 1
            count[mat[col][n - row - 1]] += 1
            count[mat[n - row - 1][n - col - 1]] += 1
            count[mat[n - col - 1][row]] += 1
            
            oper = min(count[0], count[1])
            
            num_oper += oper
    print(num_oper//4)