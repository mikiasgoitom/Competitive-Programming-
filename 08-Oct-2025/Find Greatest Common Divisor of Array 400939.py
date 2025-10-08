# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1, num2 = max(nums), min(nums)
        
        def factorize(num):
            d = 2
            factors = defaultdict(int)
            factors[1] = 1
            while d * d <= num:
                while num % d == 0:
                    num //= d
                    factors[d] += 1
                d += 1
            
            if num > 1:
                factors[num] += 1

            return factors
        
        f1 = factorize(num1)
        f2 = factorize(num2)

        gcd = 1
        # print(f1, f2, num1, num2)
        for k in f1:
            if f1[k] != 0 and f2[k] != 0:
                gcd *= k ** min(f1[k], f2[k])
        
        return gcd