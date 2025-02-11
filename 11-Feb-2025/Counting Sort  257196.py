# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    max_range = 100
    freq = [0] * max_range
    for i in range(len(arr)):
        freq[arr[i]] += 1
    ans = []
    
    for i in range(len(freq)):
        ans.append(freq[i])
    return ans