# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    arr_size = int(input())
    arr = list(map(int, input().split()))
    sums = 0
    
    maxi = arr[0]
    left = arr[0]
    for right in arr[1:]:
        if right * left < 0 :
            sums += maxi          
            maxi = right                
        else: 
            maxi = max(maxi, right)
        left = right
    sums += maxi
    print(sums)