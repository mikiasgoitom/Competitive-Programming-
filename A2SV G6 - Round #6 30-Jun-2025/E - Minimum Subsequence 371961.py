# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

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
    t = in_int()
    for _ in range(t):
        n = in_int()
        s = in_str()
        
        
        zeros = []
        ones = []
        
        for i, num in enumerate(s):
            if num == '0':
                if ones:
                    seq = ones.pop()   
                    seq.append(i) 
                    zeros.append(seq)
                else:
                    zeros.append([i])
            else:
                if zeros:
                    seq = zeros.pop()   
                    seq.append(i) 
                    ones.append(seq)
                else:
                    ones.append([i])
        
        subseqs = [0] + sorted(ones + zeros)
        
        no_seqs = len(subseqs) - 1
        ans = [0] * (len(s) + 0)
        
        # print(zeros, ones)
        # print(subseqs)
        # print(no_seqs)
        
        for i in range(1, len(subseqs)):
            for idx in subseqs[i]:
                ans[idx] = i
        print(no_seqs)
        print(" ".join(str(i) for i in ans))
                
def main():
    solve()

if __name__ == "__main__":
    main()
