# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()

        left_trav = left
        right_trav = right

        while head:
            if head.val < x:
                left_trav.next = head
                left_trav = left_trav.next
            else:
                right_trav.next = head
                right_trav = right_trav.next

            head = head.next
        
        left_trav.next = right.next
        right_trav.next = None

        return left.next