from collections import deque

def addBinary(a: str, b: str) -> str:
    i, j = len(a)-1, len(b)-1
    c = 0
    r = []
    while i > -1 or j > -1 or c:
        digit_a = int(a[i]) if i > -1 else 0
        digit_b = int(b[j]) if j > -1 else 0
        
        bit_sum = digit_a + digit_b + c
        c = bit_sum // 2
        r.append(str(bit_sum%2))
        
        i-=1
        j-=1
                
    # print(str)
    return "".join(reversed(r))
s1 = "101"
s2 = "1"
r = addBinary(s1,s2)
print(r)
                
            