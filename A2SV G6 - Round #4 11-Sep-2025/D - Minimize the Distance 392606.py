# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

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
    n = in_int()
    arr = in_list()
    arr.sort()
    
    suml = 0
    sumr = sum(arr)
    
    min_dis = float('inf')
    ans = 0
    
    for i, x in enumerate(arr):
        left_side = (x * i) - suml
        right_side = sumr - ((n - i) * x)
        
        cur_dis = left_side + right_side
        
        if cur_dis < min_dis:
            min_dis = cur_dis
            ans = i
        
        suml += x
        sumr -= x
    
    print(arr[ans])
    
    

def main():
    solve()

if __name__ == "__main__":
    main()
