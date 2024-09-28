class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.deque = [0]*(k+1)
        self.front = 0
        self.rear = 0
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % len(self.deque)
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % len(self.deque)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.deque)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % len(self.deque)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return
        return self.deque[self.front]       
    def getRear(self) -> int:
        if self.isEmpty():
            return
        return self.deque[self.rear - 1]       

    def isEmpty(self) -> bool:
       return self.front == self.rear

    def isFull(self) -> bool:
       return (self.rear + 1) == self.front


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(4)
param_1 = obj.insertFront(2)
param_2 = obj.insertLast(4)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
param_5 = obj.getFront()
# param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()
print(param_1, param_2, param_5, param_7, param_8)