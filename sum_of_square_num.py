c = 2
end = round(c**0.5)
start = 0
while(start <= end):
    if(end**2 + start**2 == c):
        print( True)
    elif(end**2 + start**2 > c):
        end -= 1
    else:
        start += 1
print(False)