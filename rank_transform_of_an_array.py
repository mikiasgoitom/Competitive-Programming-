from typing import List


def arrayRankTransform(arr: List[int]) -> List[int]:
    sorted_arr = sorted(set(arr))
    
    rank = {val: i+1 for i, val in enumerate(sorted_arr)}
    
    return [rank[num] for num in arr]