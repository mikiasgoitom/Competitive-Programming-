# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow

        while cur:
            next_node  = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        trav1 = head
        trav2 = prev
        max_sum = 0

        while trav1 and trav2:
            max_sum = max(max_sum, trav1.val + trav2.val)
            trav1 = trav1.next
            trav2 = trav2.next
        
        return max_sum