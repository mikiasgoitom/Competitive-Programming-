# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict


arr_size, param = map(int, input().split())

arr = list(map(int, input().split()))
uniq = defaultdict(int)
left = 0
max_good_seg = 0
max_good_seg_l = 0
max_good_seg_r = 0
for right in range(arr_size):
    uniq[arr[right]] += 1
    while len(uniq) > param and left <= right:
        if uniq[arr[left]] > 1:
            uniq[arr[left]] -= 1
        else:
            del uniq[arr[left]]
        left += 1

    if max_good_seg < right - (left-1):
        max_good_seg_r = right + 1
        max_good_seg_l = left + 1
        max_good_seg = right - (left-1)
print(max_good_seg_l, max_good_seg_r)