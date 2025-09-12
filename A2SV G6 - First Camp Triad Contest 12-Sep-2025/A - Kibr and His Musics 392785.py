# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

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
    n, m = in_integers()
    
    cur_sum = 0
    songs_range = []
    for _ in range(n):
        c, t = in_integers()
        duration = c * t
        songs_range.append(duration + cur_sum)
        
        cur_sum += duration
    moments = in_list()
    # print(songs_range)
    cur_song = 0
    ans = []
    for i in range(m):
        while cur_song < n and songs_range[cur_song] < moments[i]:
            cur_song += 1
        print(cur_song + 1) 
       
def main():
    solve()

if __name__ == "__main__":
    main()
