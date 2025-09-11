# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

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
    for t in range(t):
        n = in_int()
        arr = in_str() + '0'
        target = in_str() + '0'
        
        count = 0
        invalid = False
        for i in range(n):
            if arr[i] == '1':
                count += 1
            else:
                count -= 1
            
            if count != 0:
                if arr[i] == target[i] and arr[i + 1] != target[i + 1]:
                    invalid = True
                    break
                elif arr[i] != target[i] and arr[i + 1] == target[i + 1]:
                    invalid = True
                    break
        
        if invalid:
            print("NO")
        else:
            print("YES")
        
        

def main():
    solve()

if __name__ == "__main__":
    main()
