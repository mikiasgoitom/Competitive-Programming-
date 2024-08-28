distinct_char = set(list(input().lower()))
strNum = len(distinct_char)
if(strNum % 2 != 0):
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")