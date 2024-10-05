from typing import List


def minSubarray(nums: List[int], p: int) -> int:
    total_sum = sum(nums)
    r = total_sum % p
    
    if r == 0:
        return 0
    prefix_sum = 0
    prefix_map = {0:-1}
    min_len = len(nums)
    for i, num in enumerate(nums):
        prefix_sum = (prefix_sum + num) % p
        target = (prefix_sum - r) % p
        if target in prefix_map:
            min_len = min(min_len, i - prefix_map[target])
        prefix_map[prefix_sum] = i
    return min_len if min_len < len(nums) else -1


a = [3,1,4,2]
print(minSubarray(a, 6))