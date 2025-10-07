# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        i = 2

        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            
            i += 1
        
        ans = 0

        for i in range(n):
            if is_prime[i]:
                ans += 1
                
        return ans