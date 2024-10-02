from collections import defaultdict as dd
from typing import List


def canArrange(arr: List[int], k: int) -> bool:
        remainder_count = dd(int)
        for num in arr:
            r = num % k
            remainder_count[r] += 1
        for r in range(k):
            if r == 0:
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k-r]:
                    return False
        return True