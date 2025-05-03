# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    arr = in_list()
    
    temp = []
    for i in range(1, n):
        temp.append(arr[i-1] - arr[i])
    
    temp.sort()
    res = arr[0] - arr[-1]
    # print(temp, res)
    for i in range(k - 1):
        res -= temp[i]
    
    result = -res
    sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
