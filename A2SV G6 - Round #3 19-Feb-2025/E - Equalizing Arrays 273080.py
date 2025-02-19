# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())

a = list(map(int, input().split()))
# a.sort()
m = int(input())

b = list(map(int, input().split()))
# b.sort()
prefix_a = []
accum = 0
for i in range(n):
    accum += a[i]
    prefix_a.append(accum)

prefix_b = []
accum = 0
for i in range(m):
    accum += b[i]
    prefix_b.append(accum)

ans = 0 

f, s = 0, 0

while f < n and s < m:
    if prefix_a[f] == prefix_b[s]:
        ans += 1
        f += 1
        s += 1
    elif prefix_a[f] < prefix_b[s]:
        f += 1
    elif prefix_a[f] > prefix_b[s]:
        s += 1

if f != n or s != m:
    print(-1)
else:
    print(ans)