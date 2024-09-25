# import math
def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    x0 = x /2
    x1 = 0.5 * (x0 + (x / x0))
    
    while abs(x1-x0) > 1e-6:
        x0 = x1
        x1 = 0.5 * (x0 + (x / x0))
    
    return int(x1)

x = 25
r = mySqrt(x)
print(r)

