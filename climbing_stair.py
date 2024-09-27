def climbStairs(n: int) -> int:
    if n == 0:
        return 0 
    if n == 1:
        return 1
    if n == 2:
        return 2
    priv1, priv2 = 2, 1
    for _ in range(3, n + 1):
         current = priv1 + priv2
         priv2 = priv1
         priv1 = current
    return priv1

r = climbStairs(0)
print(r)