
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    
    i, j, k = m-1, n-1, m+n - 1
    
    while i > -1 and j > -1:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1
    while j > -1:
        nums1[k] = nums2[j]
        j-=1
        k-=1
nums1, m = [1,2,3,0,1,0], 3
nums2, n = [2,5,6], 3

merge(nums1,m, nums2,n)
print(nums1)