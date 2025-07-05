# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newHead = ListNode()
        trav = newHead
        trav1, trav2 = l1, l2

        while trav1 and trav2:
            temp = ListNode()
            num = trav1.val + trav2.val
            
            if carry == 1:
                num += 1
                carry = 0

            if num > 9:
                carry = 1

            num = num % 10
            trav1 = trav1.next
            trav2 = trav2.next

            temp.val = num
            trav.next = temp
            trav = trav.next
        
        while trav1:
            temp = ListNode()
            num = trav1.val
            if carry == 1:
                num += 1
                carry = 0

            if num > 9:
                carry = 1
                
            num = num % 10
            trav1 = trav1.next

            temp.val = num
            trav.next = temp
            trav = trav.next
        
        while trav2:
            temp = ListNode()
            num = trav2.val
            if carry == 1:
                num += 1
                carry = 0

            if num > 9:
                carry = 1
                
            num = num % 10

            trav2 = trav2.next

            temp.val = num
            trav.next = temp
            trav = trav.next
        if carry == 1:
            trav.next = ListNode(1)
        return newHead.next
