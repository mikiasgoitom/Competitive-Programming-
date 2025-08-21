# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

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
sys.setrecursionlimit(10**6)
def solve():
    n, m = in_integers()
    graph = defaultdict(list)
    
    indegree = defaultdict(int)
    for _ in range(m):
        u, v = in_integers()
        graph[u].append(v)        
        graph[v].append(u)
    
    # print(graph)
    """
    5 11
    11 9
    9 15
    15 5
    _____
    4 13
    3 13
    4 3
    14 3 
    14 4
    _____
    7 10
    16 7
    10 16
    
    visited = set()
    # visited_bfs = set()
    # def bfs(node):
    #     qu = deque([node])
    #     node_count = 0
    #     edge_count = 0
    #     while qu:
    #         cur = qu.popleft()
    #         if cur in visited_bfs:
    #             continue
    #         visited_bfs.add(cur)
    #         node_count += 1
    #         for neb in graph[cur]:
    #             edge_count += 1
    #             if neb not in visited_bfs:
    #                 qu.append(neb)
    #     return node_count, edge_count // 2
    """
    
    visited = set()      
    def dfs(node, parent, entry):
        visited.add(node)
        
        if len(graph[node]) != 2:
            return False
        if node != parent and node == entry:
            # print(node, entry, graph[node])
            return True
        
        
        for neb in graph[node]:
            if neb not in visited:
                if neb != parent:
                    return dfs(neb, node, entry)
        return False
        
    count = 0
    
    for i in graph:
        if i not in visited:
            # print(i, graph[i])
            if dfs(graph[i][-1], i, i):
                count += 1

    print(count)


def main():
    solve()

if __name__ == "__main__":
    main()
