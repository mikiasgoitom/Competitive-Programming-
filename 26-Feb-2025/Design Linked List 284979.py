# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val = -1):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        traverse = self.head
        i = 0
        while traverse and i < index:
            traverse = traverse.next
            i += 1
        if i == index and traverse:
            return traverse.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            traverse = self.head
            while traverse.next:
                traverse = traverse.next
            traverse.next = new_node
            

    def addAtIndex(self, index: int, val: int) -> None:
        inserted_node = Node(val)

        if self.head is None and index == 0:
            self.head = inserted_node
            return
        
        dummy = Node()
        dummy.next = self.head
        d2 = dummy
        while d2:
            print("cal", d2.val)
            d2 = d2.next
        
        traverse = dummy
        
        i = 0
        while traverse.next and i < index:
            traverse = traverse.next
            i += 1

        if i < index:
            return
        elif traverse.next and i == index:
            inserted_node.next = traverse.next
            traverse.next = inserted_node
        else:
            traverse.next = inserted_node
            inserted_node.next = None

        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:

        # if 

        dummy = Node()
        dummy.next = self.head
        traverse = dummy
        i = 0
        while traverse.next and i < index:
            traverse = traverse.next
            i += 1

        if i != index or not traverse.next:
            return

        if i == index:
            if traverse.next and traverse.next.next:
                # [d, 1, 2]
                #  l  n  nn
                print(traverse.val, traverse.next.val, traverse.next.next.val)
                temp = traverse.next
                traverse.next = traverse.next.next
                temp.next = None
            elif traverse.next:
                traverse.next = None
            self.head = dummy.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)