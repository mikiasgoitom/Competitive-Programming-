# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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
        n = in_int()
        arr = in_list()
        count = 0
        i = 0
        while i < n - 1:
            if arr[i] > arr[i + 1]:
                count += 1
                i += 1
            i += 1
        result = count
        sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
