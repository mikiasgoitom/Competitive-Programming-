# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

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

def solve():
    mtx = in_matrix(5)
    r1, c1 = 1, 1
    for r in range(5):
        for c in range(5):
            if mtx[r][c] == 1:
                r1 += r
                c1 += c
    ans = abs(3 - r1) + abs(3 - c1)
    print(ans)

def main():
    solve()

if __name__ == "__main__":
    main()
