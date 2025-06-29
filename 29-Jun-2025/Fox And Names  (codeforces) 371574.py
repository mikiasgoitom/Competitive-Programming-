# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

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
    n = in_int()
    graph = defaultdict(list)
    possible = True
    wrds = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for ch in alphabet:
        graph[ch]
    
    for _ in range(n):
        wrds.append(in_str())
    
    for i in range(1, n):
        wrd1 = wrds[i - 1]
        wrd2 = wrds[i]
        min_len = min(len(wrd1), len(wrd2))
        
        idx = 0
        while idx < min_len and wrd1[idx] == wrd2[idx]:
            idx += 1
        
        if idx == min_len:
            if len(wrd1) > len(wrd2):
                possible = False
                break
            else:
                continue
        else:
            graph[wrd1[idx]].append(wrd2[idx])
    
    indegree = defaultdict(int)
    # print(graph)
    for node in graph:
        indegree[node]
        for neb in graph[node]:
            indegree[neb] += 1
    
    qu = deque()
    
    for node in indegree:
        if indegree[node] == 0:
            qu.append(node)
            break
    
    order = []
    
    
    while qu:
        sz = len(qu)
        
        for i in range(sz):
            node = qu.popleft()
            
            for neb in graph[node]:
                indegree[neb] -= 1
                
                if indegree[neb] == 0:
                    qu.append(neb)
                    
            order.append(node)
            indegree[node] -= 1
            
        if not qu:
            
            for node in indegree:
                
                if indegree[node] == 0:
                    qu.append(node)
                    break
            
    order = "".join(order)
    
    if not possible:
        result = 'Impossible'
    else:
        if len(order) < 26:
            result = 'Impossible'
        else:
            result = order
    
    sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
