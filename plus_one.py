from collections import deque
def plusOne(digits):
        n = len(digits) - 1
        s = deque(digits)
        while n > -1:
            if(digits[n] < 9):
                s[n] += 1
                return list(s)
            else:
                s[n] = 0
                if n - 1 < 0:
                    s.appendleft(1)
            n -= 1
        return list(s)

digits = [9,9,9,9]
d = plusOne(digits)
print(d)