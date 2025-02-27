# Problem: Books - https://codeforces.com/contest/279/problem/B

num_book, time = map(int, input().split())


books = list(map(int, input().split()))

accum = 0
max_book = 0

pre_t = [0]
accum = 0

for i in range(num_book):
    accum += books[i]
    pre_t.append(accum)

pre_t_size = len(pre_t)
left = 0
right = 1
accum_t = 0

while right < pre_t_size:
    accum_t = pre_t[right] - pre_t[left]
    
    if accum_t <= time:
        max_book = max(max_book, (right - left))
        right += 1
    else:
        left += 1
        
print(max_book)