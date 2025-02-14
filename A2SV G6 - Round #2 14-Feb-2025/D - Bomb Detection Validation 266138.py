# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def check_bomb(mat):
    eight_dir = [(-1, -1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    r_size = len(mat)
    c_size = len(mat[0])
    for row in range(r_size):
        for col in range(c_size):
            bomb_count = 0
            for i, j in eight_dir:
                if 0 <= (row + i) < r_size and 0 <= (col + j) < c_size:
                    # print(row + i, col+j)
                    if mat[row + i][col+j] == '*':
                        bomb_count += 1
                    else:
                        continue
            if mat[row][col] == '.' and bomb_count != 0:
                return "NO"
            elif mat[row][col] == '*':
                continue
            elif mat[row][col] == '.' and bomb_count == 0:
                continue
            elif int(mat[row][col]) != bomb_count:
                return "NO"
    return "YES"
        
 
n, m = map(int, input().split())
mat = []
 
for i in range(n):
    mat.append(list(input()))      
    
print(check_bomb(mat))