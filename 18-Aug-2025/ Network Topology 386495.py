# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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
    n, m = in_integers()
    graph = defaultdict(list)
    indeg = defaultdict(lambda:0)
    for _ in range(m):
        u, v = in_integers()
        graph[u].append(v)
        graph[v].append(u)
        indeg[u] += 1
        indeg[v] += 1
    source = []
    for k in indeg:
        if indeg[k] == 1:
            source.append(k)
    
    if not source:
        if n == m:
            print("ring topology")
            return
    star_pos = False
    bus_pos = False
    if len(source) == n-1:
        star_pos = True
    if len(source) == 2:
        bus_pos = True
    
    
    qu = deque(source)
    visited = set()
    
    valid = False
    while qu:
        sz = len(qu)
        for _ in range(sz):
            u = qu.popleft()
            visited.add(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 1 and v not in visited:
                    qu.append(v)
        if len(visited) == n:
            valid = True
    
    if valid:
        if star_pos:
            print("star topology")
            return
        elif bus_pos:
            print("bus topology")
            return
    print("unknown topology")
    

def main():
    solve()

if __name__ == "__main__":
    main()
