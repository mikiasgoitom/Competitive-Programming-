# height = [1,2,4,3]
height = [1,8,6,2,5,4,8,25,7]
first = 0
end = len(height) - 1
max_volume = 0
while(first < end):
    temp = (end-first) * min(height[first], height[end])
    if(temp > max_volume):
        max_volume = temp
    if(height[end] > height[first]):
        first += 1
    else:
        end -= 1
print(max_volume)