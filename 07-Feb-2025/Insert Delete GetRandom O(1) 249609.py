# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.rand = set()

    def insert(self, val: int) -> bool:
        self.rand.add(val)

    def remove(self, val: int) -> bool:
        if val in self.rand:
            self.rand.remove(val)
            return True
        else:
            return False            

    def getRandom(self) -> int:
        return random.choice(list(self.rand))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()