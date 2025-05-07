# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

#  not to future self, check if your size[1] not size[0]

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

def union(x, y, par, xp, size):
    x, y = find(x, par), find(y, par)
    
    if x != y:
        if size[x] > size[y]:
            par[y] = par[x]
            size[x] += size[y]
            xp[y] += -xp[x]
        else:
            par[x] = par[y]
            size[y] += size[x]
            xp[x] += -xp[y]

def solve():
    n, qrs = in_integers()
    par = [i for i in range(n + 1)]
    size = [1] * (n + 1)
    xp = [0] * (n + 1)
    
    for _ in range(qrs):
        input = in_strings()
        if len(input) > 2:
            opr, x, y = input
            x = int(x)
            y = int(y)
            
            if opr == 'add':
                xp[find(x, par)] += y
            else:
                union(x, y, par, xp, size)
        else:
            x = int(input[-1])
            result = xp[x]
            
            while x != par[x]:
                x = par[x]
                result += xp[x]
            sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
