# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
binary = list(map(int, input().strip()))
# print(binary)


def atmost(k):
    if k == -1:
        return 0
    
    left = 0
    windw = 0
    num_substr = 0
    
    for right in range(len(binary)):
        windw += binary[right]
        while windw > k:
            windw -= binary[left]
            left += 1
                        
        num_substr += (right - left) + 1
    return num_substr


    

print(atmost(k) - atmost(k-1))