# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        ugly = {1, 2, 3, 5}
        while n > 1:
            possible_prime_num = floor(n ** 0.5)
            # print(n, possible_prime_num)

            if possible_prime_num < 2:
                break
            
            if n in ugly:
                return True

            found_ugly = False

            for i in range(2, possible_prime_num + 1):
                if (n % i == 0) and (i in ugly):
                    n //= i
                    found_ugly = True
                    break

            if not found_ugly:
                return False
        return True
