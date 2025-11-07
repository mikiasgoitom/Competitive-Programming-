# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ev_idx = ceil(n / 2)
        od_idx = n // 2
            
        MOD = (10 ** 9) + 7
        
        def mod_pow(base, exp):
            res = 1
            while exp > 0 :
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        # print(pow(5,ev_idx, MOD), pow(4, od_idx, MOD), ev_idx, od_idx)
        return (mod_pow(5,ev_idx) * mod_pow(4, od_idx)) % MOD
