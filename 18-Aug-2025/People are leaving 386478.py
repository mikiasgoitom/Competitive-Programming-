# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

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

class UnionFind:
    def __init__(self, n:int = 0):
        self.root = [0] + [i for i in range(1, n + 1)] + [-1]
        
    def find(self, X):
        root = X
        # Find the root
        while root != self.root[root]:
            root = self.root[root]
        # Path compression
        while X != root:
            parent = self.root[X]
            self.root[X] = root
            X = parent
        return root
    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)
        if rootX != rootY:
            self.root[rootX] = rootY

def solve():
    n, q = in_integers()
    uf = UnionFind(n)
    # ans = []
    for _ in range(q):
        op, idx = in_strings()
        idx = int(idx)
        if op == "?":
            print(uf.find(idx))
        else:
            uf.union(idx, idx+1)
            # uf.find(idx)
    # print(ans)
            
    
    
    
    

def main():
    solve()

if __name__ == "__main__":
    main()
