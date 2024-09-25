from collections import defaultdict as ddict
l = list(map(int, input().split()))
n = l[0]
m = l[1]
words = ddict(list)
words['a']
words['b']
for _ in range(n):
    temp = input()
    words['a'].append(temp)
for _ in range(m):
    temp = input()
    words['b'].append(temp)
for i in range(m):
    indexs = ''
    for j in range(n):
        if(words['a'][j] == words['b'][i]):
            indexs += " {}".format(j+1)
    print(indexs)
