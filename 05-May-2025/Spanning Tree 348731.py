# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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

res = 0
def find(x, par):
    while x != par[x]:
        par[x] = par[par[x]]
        x = par[x]
    return x

def union(x, y, w, par, sz, ):
    global res
    fx, fy = find(x, par), find(y, par)
    
    if fx != fy:
        res += w
        if sz[fy] > sz[fx]:
            par[fx] = par[fy]
            sz[fy] += sz[fx]
        else:
            par[fy] = par[fx]
            sz[fx] += sz[fy]

def solve():
    global res
    v, e = in_integers()
    par = [i for i in range(v)]
    sz = [1] * v
    edges = []
    for _ in range(e):
        eg = tuple(in_integers())
        edges.append(eg)
    edges.sort(key=lambda x: x[2])
    for eg in edges:
        u1, u2, w = eg
        union(u1 - 1, u2 - 1, w, par, sz)
    # print(edges)
    result = res
    sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
