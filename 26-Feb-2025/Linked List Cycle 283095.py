# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy

        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if fast == slow:
                return True
        return False