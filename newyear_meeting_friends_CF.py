points = list(map(int, input().split())).sort()
min_distance = (abs(points[0]-points[1])+abs(points[1]-points[2]))
print (min_distance)