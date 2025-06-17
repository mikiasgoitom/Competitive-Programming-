# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.v = value
        self.qu = deque()

    def consec(self, num: int) -> bool:
        if not self.qu:
            self.qu.append(num)
            return False
        
        if len(self.qu) == self.k:
            self.qu.popleft()

        while self.qu and self.qu[-1] > num:
            self.qu.pop()
        self.qu.append(num)

        if len(self.qu) == self.k and self.qu[0] == self.qu[-1] and self.qu[0] == self.v:
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)