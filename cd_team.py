c = int(input())
tot = 0

for i in range(c):
    s = list(map(int, input().split()))
    if sum(s) > 1:
        tot += 1
print(tot)