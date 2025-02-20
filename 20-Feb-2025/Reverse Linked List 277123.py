# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        trav1 = head

        while trav1:
            temp.append(trav1.val)
            trav1 = trav1.next
        
        temp = temp[::-1]
        trav2 = head
        for i in range(len(temp)):
            trav2.val = temp[i]
            trav2 = trav2.next
        
        return head