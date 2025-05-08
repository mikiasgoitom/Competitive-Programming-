# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter

def in_str() -> str: return sys.stdin.readline().strip()
def in_int() -> int: return int(sys.stdin.readline().strip())
def in_integers(): return map(int, sys.stdin.readline().strip().split())
def in_list() -> list: return list(map(int, sys.stdin.readline().strip().split()))
def in_strings(): return sys.stdin.readline().strip().split()
def in_string_list() -> list: return list(sys.stdin.readline().strip())
def in_matrix(n: int) -> list: return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def find(x, par):
    while x != par[x]:
        x = par[x]
    return x

def union(x, y, par, size):
    x, y = find(x, par), find(y, par)
    
    if x != y:
        if size[x] > size[y]:
            par[y] = par[x]
            size[x] += size[y]
        else:
            par[x] = par[y]
            size[y] += size[x]


def solve():
    n, m, qrs = in_integers()
    par = [i for i in range(n + 1)]
    size = [1] * (n + 1)
    queries = []
    
    for _ in range(m):
        in_integers()
        
    for _ in range(qrs):
        queries.append(in_strings())
    ans = []
    for i in range(qrs - 1, -1, -1):
        oper, u, v = queries[i]
        u = int(u)
        v = int(v)
        if oper == 'ask':
            if find(u, par) == find(v, par):
                ans.append('YES')
            else:
                ans.append('NO')
        else:
            union(u, v, par, size)
    
    for i in range(len(ans)-1 , -1, -1):
        print(ans[i])
    

def main():
    solve()

if __name__ == "__main__":
    main()
