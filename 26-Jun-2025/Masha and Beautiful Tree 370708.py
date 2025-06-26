# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque

def in_str() -> str: return sys.stdin.readline().strip()
def in_int() -> int: return int(sys.stdin.readline().strip())
def in_integers(): return map(int, sys.stdin.readline().strip().split())
def in_list() -> list: return list(map(int, sys.stdin.readline().strip().split()))
def in_strings(): return sys.stdin.readline().strip().split()
def in_string_list() -> list: return list(sys.stdin.readline().strip())
def in_matrix(n: int) -> list: return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]



def merge_sort_w_count(arr):
    ans = 0
    
    def merge(lft, rgt): 
        nonlocal ans
        res = []
        i, j = 0, 0
        if lft[0] > rgt[0]:
            res.extend(rgt)
            res.extend(lft)
            ans += 1
        else:
            res.extend(lft)
            res.extend(rgt)
        return res
    
    def merge_sort(left, right):
        if left == right:
            return [arr[left]]
        
        mid = (right + left) // 2
        
        larr = merge_sort(left, mid)
        
        rarr = merge_sort(mid + 1, right)
        
        return merge(larr, rarr)
    
    temp = merge_sort(0, len(arr) - 1)
    return [temp, ans]

def solve():
    t = in_int()
    for _ in range(t):
        n = in_int()
        arr = in_list()
        sarr = sorted(arr)
        temp, ans = merge_sort_w_count(arr)
        # print(temp, sarr, temp == sarr)
        if temp != sarr:
            print(-1)
        else:
            print(ans)

def main():
    solve()

if __name__ == "__main__":
    main()
