# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        trav = head
        while l1 or l2:
            temp = ListNode()
            if l1 and l2:
                summed = l1.val + l2.val + carry
                if summed > 9:
                    carry = 1
                    summed %= 10
                else:
                    carry = 0
                temp.val = summed
                trav.next = temp
                trav = trav.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                summed = l1.val + carry
                if summed > 9:
                    carry = 1
                    summed %= 10
                else:
                    carry = 0
                temp.val = summed
                trav.next = temp
                trav = trav.next
                l1 = l1.next
            else:
                summed = l2.val + carry
                if summed > 9:
                    carry = 1
                    summed %= 10
                else:
                    carry = 0
                temp.val = summed
                trav.next = temp
                trav = trav.next
                l2 = l2.next
        if carry:
            temp = ListNode(carry)
            trav.next = temp

        return head.next
        
