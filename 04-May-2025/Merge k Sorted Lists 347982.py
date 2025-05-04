# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        heapify(heap)

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        trav = dummy
        # print(heap)
        while heap:
            min_num, idx, node = heappop(heap)
            trav.next = node
            trav = trav.next
            nxt_node = node.next

            if nxt_node:
                heappush(heap, (nxt_node.val, idx, nxt_node))
        # print(heap)
        return dummy.next