# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

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
    b_n, qry = in_integers()
    temp = in_list()
    bs = [0]
    bs.extend(temp)
    lr_pre = [0 ] * (b_n + 1)
    accum = 0
    for i in range(1, b_n + 1):
        accum += -(bs[i] - bs[i - 1]) if bs[i] - bs[i - 1] < 0 else 0
        lr_pre[i] = accum
    
    rl_pre = [0 ] * (b_n + 1)
    accum = 0
    for i in range(b_n - 1, 0, -1):
        accum += -(bs[i] - bs[i + 1]) if bs[i] - bs[i + 1] < 0 else 0
        rl_pre[i] = accum
    
    # print(lr_pre, rl_pre)
    for _ in range(qry):
        q1, q2 = in_integers()
        ans = 0
        if q1 > q2:
            ans = rl_pre[q2] - rl_pre[q1]
        else:
            ans = lr_pre[q2] - lr_pre[q1]
        result = ans
        sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
