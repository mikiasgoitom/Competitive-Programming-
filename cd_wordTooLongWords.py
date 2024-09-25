j = int(input())
output = []
for i in range(j):
    s = input()   
    if len(s) <= 10:
        output.append(s)
    else:
        output.append(f"{s[0]}{len(s[1:-1])}{s[-1]}")
for i in range(j):
    print(output[i])