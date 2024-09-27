from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyList:
    def __init__(self) -> None:
        self.root = ListNode()
    def insert(self, value):
        temp = ListNode(value)
        if self.root is None:
            self.root = temp
        else: 
            node = self.root
            while node.next is not None:
                node = node.next
            node.next = temp

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    values = set()
    node = head
    while node is not None:
        if node.val not in values:
              values.add(node.val)
        node = node.next

    sorted_values = sorted(values)
    sorted_head = ListNode(sorted_values[0])
    current = sorted_head
    for value in sorted_values[1:]:
            current.next = ListNode(value)
            current = current.next
    return sorted_head
def printList(head: ListNode):
    if head is None:
        print("None")
    node = head
    while node is not None:
        print(node.val,end="->")
        node = node.next
a = MyList()
b = [1,3,4,5,7,7,7,5,3,2,9]
for value in b:
    a.insert(value)
d = deleteDuplicates(a.root)
printList(d)
    