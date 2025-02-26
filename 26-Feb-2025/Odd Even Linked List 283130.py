# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        odd = ListNode()

        traverse_even = even
        traverse_odd = odd
        i = 1

        while head:
            if i % 2 == 0:
                traverse_even.next = head
                traverse_even = traverse_even.next
            else:
                traverse_odd.next = head
                traverse_odd = traverse_odd.next

            i += 1
            head = head.next
        traverse_even.next = None
        traverse_odd.next = even.next
        return odd.next