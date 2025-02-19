# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode()
            dummy.next = head
            trav_r = dummy
            while n > 0:
                trav_r = trav_r.next
                n -= 1

            print("right", trav_r.val)
            
            trav_l = dummy
            while trav_r.next:
                print("in l",trav_l.val)
                print("in r",trav_r.val)
                trav_l = trav_l.next
                trav_r = trav_r.next
            
            temp = trav_l.next
            print(trav_l, trav_r)
            if trav_l.next and trav_l.next.next:
                trav_l.next = trav_l.next.next
            else:
                trav_l.next = None
            if trav_l == trav_r:
                return trav_l.next
            if temp:
                temp.next = None

            return dummy.next
            