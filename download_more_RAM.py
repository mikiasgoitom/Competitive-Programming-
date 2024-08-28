test = int(input())
ram = []
for i in range(test):
    n = int(input())
    k = int(input())
    ram.append(k)
    a = map(int, input().split())
    b = map(int, input().split())
    unsorted_c = {**a, **b}
    sorted_c = dict(sorted(unsorted_c.items()))
    ram[i] = sum(value for key, value in sorted_c.items() if key <= k)
    print(ram[i])