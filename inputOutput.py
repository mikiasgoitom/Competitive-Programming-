if __name__ == '__main__':
    N = int(input())
    arr1 = [None] * N
    for i in range(N):
        arr1[i] = input()
    arr2 = [None] * N
    for i in range(N):
        arr_reciver = arr1[i].split()
        print(arr1[i].split())
        if( arr_reciver[0]== 'insert'):
            arr2[int(arr_reciver[1])] = int(arr_reciver[2])
        elif(arr_reciver[0] == 'print'):
            print(arr2)
        elif(arr_reciver[0] == 'remove'):
            arr2.remove(int(arr_reciver[1]))
        elif(arr_reciver[0] == 'append'):
            arr2.append(arr_reciver[1])
        elif(arr_reciver[0] == 'sort'):
            arr2.sort()
        elif(arr_reciver[0] == 'pop'):
            arr2.pop()
        elif(arr_reciver[0] == 'print'):
            arr2.reverse()
        else:
            print("Error in strings")