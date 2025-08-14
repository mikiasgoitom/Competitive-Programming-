# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

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
        a = int(in_str())
        a =  "0" + bin(a)[2:]  # Convert to binary string
        a = a[::-1]

        f1 = a.index('1')
        count1 = a.count('1')
        count0 = a.count('0')
        if count1 == 1:
            if count0 == 0:
                print((1 << f1) + (1 << (f1 + 1)))
            else:
                f0 = a.index('0')
                print((1 << f1) + (1 << f0))
        else:
            print((1 << f1))
        # print(ans)
        # y = 1
        # while a == y or a & y == 0:
        #     y += 1
        # print(y)

def main():
    solve()

if __name__ == "__main__":
    main()
