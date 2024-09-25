from collections import defaultdict as dd
n = int(input())
shop = dd(int)
for _ in range(n):
    temp = input().split()
    productName = ' '.join(word for word in temp if word.isalpha())
    price = int(''.join(word for word in temp if word.isnumeric()))
    shop[productName] += price
for item in shop:
    print('{} {}'.format(item, shop[item]))