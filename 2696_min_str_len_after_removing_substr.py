from collections import deque
def minLength(s: str) -> int:
        s_list = []
        
        for c in s:
            if s_list and c == "B":
                if s_list[-1] == "A":
                    s_list.pop()
                    continue
            if s_list and c == "D":
                if s_list[-1] == "C":
                    s_list.pop()
                    continue
            s_list.append(c)
        return len(s_list)
    
s = "ABFCACDB"
n = minLength(s)
print(n)