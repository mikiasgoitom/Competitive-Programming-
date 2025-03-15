# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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
    n = in_int()
    stones = in_list()
    sorted_stones = sorted(stones)
    pre_s = [0]
    accum = 0
    for i in range(n):
        accum += stones[i]
        pre_s.append(accum)
        
    pre_s_s = [0]  
    accum = 0
    for i in range(n):
        accum += sorted_stones[i]
        pre_s_s.append(accum)
  
    
    queries = in_int()
    
    for _ in range(queries):
        # n = in_int()
        t, l, r = in_integers()
        result = 0
        if t == 2:
            result = pre_s_s[r] - pre_s_s[l-1]
        else:
            result = pre_s[r] - pre_s[l-1]
        sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
