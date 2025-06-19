# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

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
    arr =  in_list()
    
    weeks = n - k + 1
    cur = 0
    sums = 0
    
    for i in range(k):
        sums += arr[i]
    
    cur =  sums
    l, r = 0, k
    while r < n:
        cur += arr[r]
        cur -= arr[l]
        
        sums += cur
        r += 1
        l += 1
    print(sums / weeks)

def main():
    solve()

if __name__ == "__main__":
    main()
