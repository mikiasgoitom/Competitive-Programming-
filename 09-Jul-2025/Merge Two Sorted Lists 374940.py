# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = ListNode()
        merged_head = merged
        trav1 = list1
        trav2 = list2

        while trav1 or trav2:
            if trav1 and trav2 and trav1.val <= trav2.val:
                # print(merged)
                merged.next = trav1
                trav1 = trav1.next
            elif trav1 and trav2 and trav1.val > trav2.val:    
                # print(merged)

                merged.next = trav2
                trav2 = trav2.next
            elif trav1:
                # print(merged)
                # temp
                merged.next = trav1
                trav1 = trav1.next
            else:
                # print(merged)
                merged.next = trav2
                trav2 = trav2.next
            merged = merged.next
        
        return merged_head.next

