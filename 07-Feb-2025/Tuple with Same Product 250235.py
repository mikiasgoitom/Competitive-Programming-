# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                products[nums[i]*nums[j]].append(tuple([i, j]))
        ans = 0
        for k, v in products.items():
            if len(v) >= 2:
                s = len(v) * 2
                ans += s * (s-2)
        return ans
