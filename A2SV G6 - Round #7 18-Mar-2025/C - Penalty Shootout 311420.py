# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter

def in_str() -> str:
    return sys.stdin.readline().strip()

def in_int() -> int:
    return int(sys.stdin.readline().strip())

def in_integers():
    return map(int, sys.stdin.readline().strip().split())

def in_list() -> list:
    return list(map(int, sys.stdin.readline().strip().split()))

def in_strings():
    return sys.stdin.readline().strip().split()

def in_string_list() -> list:
    return list(sys.stdin.readline().strip())

def in_matrix(n: int) -> list:
    return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def solve():
    t = in_int()
    for _ in range(t):
        kicks = in_str()
        min1 = float('inf')
        goal1, goal2 = 0, 0
        
        for i in range(len(kicks)):

            if i % 2 == 0:
                if kicks[i] != '0':
                    goal1 += 1
            else:
                if kicks[i] == '1':
                    goal2 += 1
            rem1 = (10 - i - 1) // 2
            rem2 = (10 - i) // 2
            
            # print("gh",goal1, goal2, i, "r1", rem1, "r2", rem2)
            
            if goal1 > goal2 + rem2 or goal2 > goal1 + rem1 or i == 9:
                min1 = i+1
                break
            
    
        min2 = float('inf')
        goal1, goal2 = 0, 0
        
        for i in range(len(kicks)):

            if i % 2 != 0:
                if kicks[i] != '0':
                    goal2 += 1
            else:
                if kicks[i] == '1':
                    goal1 += 1
                    
            rem1 = (10 - i - 1) // 2
            rem2 = (10 - i) // 2
            
            # print("gh",goal1, goal2, i, "r1", rem1, "r2", rem2)
            
            if goal1 > goal2 + rem2 or goal2 > goal1 + rem1 or i == 9:
                min2 = i + 1
                break
        
                                
        result = min(min1, min2)
        sys.stdout.write(str(result) + "\n")

def main():
    solve()

if __name__ == "__main__":
    main()
