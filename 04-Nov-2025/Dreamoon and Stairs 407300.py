# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

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
    n, k = in_integers()
    
    if n < k:
        print(-1)
        return
    
    valid = False
    steps = (n // 2) if n % 2 == 0 else (n // 2) + 1
    cycle = steps if n % 2 == 0 else steps - 1
    # print(cycle)
    for _ in range(cycle):
        if steps % k == 0:
            valid = True
            break
        steps += 1
    
    if valid or steps % k == 0:
        print(steps)
    else:
        print(-1)

def main():
    solve()

if __name__ == "__main__":
    main()
