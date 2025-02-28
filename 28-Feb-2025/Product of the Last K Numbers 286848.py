# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prd = 1

    def add(self, num: int) -> None:
        if self.prd == 0:
            size_stream = len(self.stream)
            self.stream = [0] * size_stream
            self.prd = 1
        self.prd *= num
        self.stream.append(self.prd)        

    def getProduct(self, k: int) -> int:
        reversed_stream = list(reversed(self.stream))
        # print(reversed_stream)
        if reversed_stream[k-1] == 0:
            return 0
        if k >= 0 and k < len(reversed_stream) and reversed_stream[k] > 0:
            return reversed_stream[0] // reversed_stream[k]
        else:
            return reversed_stream[0]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)