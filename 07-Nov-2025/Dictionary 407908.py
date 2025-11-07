# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

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
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dictionary = {}
    count = 1
    for frt in alphabets:
        for sec in alphabets:
            if frt == sec:
                continue
            dictionary[frt + sec] = count
            count += 1
    t = in_int()
    for _ in range(t):
        check = in_str()
        print(dictionary[check])
        

def main():
    solve()

if __name__ == "__main__":
    main()
