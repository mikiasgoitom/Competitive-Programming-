# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.qu = deque()

    def push(self, x: int) -> None:
        self.qu.append(x)

    def pop(self) -> int:
        return self.qu.pop()

    def top(self) -> int:
        return self.qu[-1]

    def empty(self) -> bool:
        if self.qu:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()