class ListNode:
    def __init__(self, x = 0):
        self.val = x
        self.next = None

def hasCycle(head) -> bool:
   slow = head
   fast =head
   while fast and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
    return False