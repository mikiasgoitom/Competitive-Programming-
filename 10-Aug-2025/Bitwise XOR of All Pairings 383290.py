# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num3 = 0
        m = len(nums2)
        n = len(nums1)

        if m % 2 == 0 and n % 2 != 0:
            for num in nums2:
                num3 ^= num
        elif n % 2 == 0 and m % 2 != 0:
            for num in nums1:
                num3 ^= num
        elif n % 2 != 0 and m % 2 != 0:
            for num in nums1:
                num3 ^= num
            for num in nums2:
                num3 ^= num
        return num3