# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter

def in_str() -> str:
    return sys.stdin.readline().strip()

def in_int() -> int:
    return int(sys.stdin.readline().strip())

def in_integers():
    return map(int, sys.stdin.readline().strip().split())

def in_list() -> list:
    return list(map(int, sys.stdin.readline().strip().split()))

def in_strings():
    return sys.stdin.readline().strip().split()

def in_string_list() -> list:
    return list(sys.stdin.readline().strip().split())

def in_matrix(n: int) -> list:
    return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Main problem solving function
def solve():
    t = in_int()
    for _ in range(t):
        r_n = in_int()
        r = in_list()
        b_n = in_int()
        b = in_list()
        
        pre_r = []
        accum = 0
        for i in range(r_n):
            accum += r[i]
            pre_r.append(accum)
        
        pre_b = []
        accum = 0
        for i in range(b_n):
            accum += b[i]
            pre_b.append(accum)
        
        max_r = max(0, max(pre_r))
        max_b = max(0, max(pre_b))
        
        result = max_r + max_b
        sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
