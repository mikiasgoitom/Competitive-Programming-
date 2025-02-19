# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def checker(mel, note):
    min_note = 0
    left, right = 0, size - 1
    
    while left < right:
        if mel[left] != mel[right]:
            if mel[left] == note:
                left += 1
            elif mel[right] == note:
                right -= 1
            else:
                return -1
            min_note += 1
        else:
            left += 1
            right -= 1

    return min_note

t = int(input())

for _ in range(t):
    size = int(input())
    mel = list(input())
    
    left, right = 0, size - 1
    
    del_note = []
    
    while left < right:
        if mel[left] != mel[right]:
            del_note.append(mel[left])
            del_note.append(mel[right])
            break
        left += 1
        right -= 1
    
    if len(del_note) == 0:
        print('0')
    else:
        t1 = checker(mel, del_note[0])
        t2 = checker(mel, del_note[1])
        ans = 0
        if t1 == -1 and t2 == -1:
            print(-1)
        elif t1 == -1 or t2 == -1:
            print(max(t1, t2))
        else:
            print(min(t1, t2))
    