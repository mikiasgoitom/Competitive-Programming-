def alice_bob_chocolates(n, chocolates):
    alice_time = 0
    bob_time = 0
    alice_count = 0
    bob_count = 0
    left = 0
    right = n - 1
    while left <= right:
        if alice_time <= bob_time:
            alice_time += chocolates[left]
            alice_count += 1
            left += 1
        else:
            bob_time += chocolates[right]
            bob_count += 1
            right -= 1
    return alice_count, bob_count

n = int(input())  
chocolates = list(map(int, input().split()))  


a, b = alice_bob_chocolates(n, chocolates)


print(a, b)
