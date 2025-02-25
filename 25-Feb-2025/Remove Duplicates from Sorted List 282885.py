# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        trav = head
        count = defaultdict(int)
        while trav:
            count[trav.val] += 1

            if count[trav.val] > 1:
                print("touched")
                prev.next = trav.next
            else:
                print("cctouched")
                prev.next = trav
                prev = prev.next
            trav = trav.next
        return dummy.next
        
