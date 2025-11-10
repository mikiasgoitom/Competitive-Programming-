# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

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

def solve():
    n, k = in_integers()
    arr = [0] + in_list()
    
    ans = 0
    
    inc_qu = deque()
    dec_qu = deque()
    # print(arr)
    l, r = 1, 1
    while r < n + 1:        
        while inc_qu and inc_qu[-1] > arr[r]:
            inc_qu.pop()
        inc_qu.append(arr[r])   
        
        while dec_qu and dec_qu[-1] < arr[r]:
            dec_qu.pop()
        dec_qu.append(arr[r])
        
        while k < abs(dec_qu[0] - inc_qu[0]):            
            if inc_qu[0] == arr[l]:
                inc_qu.popleft()
            elif dec_qu[0] == arr[l]:
                dec_qu.popleft()
            l += 1

        ans += r - l + 1
        r += 1
    print(int(ans))
            
                
                
    
    
    
        
            
def main():
    solve()

if __name__ == "__main__":
    main()
