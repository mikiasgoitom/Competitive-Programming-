# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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


def validator(i_a, i_b, a, b, ans_arr):
    if b[i_b] - a[i_a] >= ans_arr[-1]:
        return True
    return False
    
def bst(i_a, a, b, ans_arr):
    low, high = 0, len(b) - 1
    while low <= high:
        mid = (high + low) // 2
        if validator(i_a, mid, a, b, ans_arr):
            high = mid - 1
        else:
            low = mid + 1
    return low

def solve():
    t = in_int()
    for _ in range(t):
        a_n, b_n = in_integers()
        a = in_list()
        b = in_list()       
        b.sort()
        ans_arr = [min(a[0], b[0] - a[0])]
        for i in range(1, len(a)):
            min_b_i =  bst(i, a, b, ans_arr)
            if min_b_i >= len(b):
                ans_arr.append(a[i])
            else:
                ans_arr.append(min(a[i],b[min_b_i] - a[i]))
        result = ""
        # print(ans_arr)
        if ans_arr == sorted(ans_arr):
            result = "YES"
        else:
            result = "NO"
        sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
