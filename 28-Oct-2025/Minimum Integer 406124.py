# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

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
    t = in_int()
    for _ in range(t):
        l, r, d = in_integers()
        if d >= l:
            if r % d == 0:
                s = (r // d) + 1
            else: 
                s = ceil(r / d)
            print(s * d)
            continue
        else:
            print(d)
            

def main():
    solve()

if __name__ == "__main__":
    main()
