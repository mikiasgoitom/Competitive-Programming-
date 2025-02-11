# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    i = n - 1
    temp = arr[i]
    while arr[i - 1] > arr[i] and i > 0:
        # print("++++", i, i-1, arr[i], arr[i-1])
        if arr[i - 1] > arr[i]:
            hold = arr[i]
            arr[i] = arr[i - 1]
            print(" ".join(str(a) for a in arr))
            arr[i], arr[i-1] = arr[i-1], hold
        i -= 1
    arr[i] = temp
    print(" ".join(str(a) for a in arr))
