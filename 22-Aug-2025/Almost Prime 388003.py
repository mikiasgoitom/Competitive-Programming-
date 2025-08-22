# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

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

def is_prime_enough(n):
    div = 2
    count = set()
    while div * div <= n:
        if n % div == 0:
            count.add(div)
            while n % div == 0:
                n //= div
        else:
            div += 1
    # print(count)
    if n > 1:
        count.add(n)
    if len(count) == 2:
        return True
    return False
def solve():
    n = in_int()
    ans= 0
    for i in range(1, n+1):
        if is_prime_enough(i):
            ans += 1
            
    print(ans)
    

def main():
    solve()

if __name__ == "__main__":
    main()
