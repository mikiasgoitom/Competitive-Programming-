# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        arr = []

        while trav:
            arr.append(trav.val)
            trav = trav.next
        
        arr.sort()

        s_trav = head

        i = 0
        while s_trav:
            s_trav.val = arr[i]
            s_trav = s_trav.next
            i += 1
        return head