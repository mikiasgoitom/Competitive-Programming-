# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class LinkedNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = 0
        self.max_capacity = k
        self.head = None

    def insertFront(self, value: int) -> bool:
        new_node = LinkedNode(value)
        if self.capacity < self.max_capacity:
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.capacity +=1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        new_node = LinkedNode(value)
        if self.capacity < self.max_capacity:
            if not self.head:
                self.head = new_node
            else:
                trav = self.head
                while trav and trav.next:
                    trav = trav.next
                new_node.prev = trav
                trav.next = new_node
            self.capacity +=1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        
        if not self.head:
            return False
        else:
            self.head
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next                
            else:
                self.head = None
            self.capacity -=1
            return True

    def deleteLast(self) -> bool:
        if not self.head:
            return False
        else:
            trav = self.head

            while trav and trav.next:
                trav = trav.next

            if trav.prev:
                trav.prev.next = None
                trav.prev = None
            else:
                self.head = None
            self.capacity -=1
            return True

    def getFront(self) -> int:
        # self.display()
        if not self.head:
            return -1
        else:
            return self.head.val

    def getRear(self) -> int:
        trav = self.head

        while trav and trav.next:
            trav = trav.next
        if not self.head:
            # self.display()
            return -1
        else:
            return trav.val

    def isEmpty(self) -> bool:
        if self.capacity == 0:
            return True
        else:
            return False
    def display(self):
        trav = self.head

        while trav:
            print(trav.val)
            trav = trav.next
        
    def isFull(self) -> bool:
        if self.capacity == self.max_capacity:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()