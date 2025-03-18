# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

def calc(l, r, c):
    if l == r:
        if s[l] == c:
            return 0
        return 1
    
    mid = (r + l) // 2
    
    left_change = (mid - l + 1) - s[l:mid+1].count(c)
    left_result = left_change + calc(mid + 1, r, chr(ord(c)+1))
    
    right_change = (r - mid) - s[mid+1:r+1].count(c)
    right_result = right_change + calc(l, mid, chr(ord(c)+1))
    
    return min(left_result, right_result)
        
t  = int(input())

for _ in range(t):
    s_size = int(input())
    s = input()
    print(calc(0, s_size - 1, 'a'))
