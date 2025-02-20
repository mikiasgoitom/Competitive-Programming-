# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        trav = head

        while trav:
            ans.append(trav.val)
            trav = trav.next
        
        # ans = "".join(str(c) for c in ans)
        
        if ans == list(reversed(ans)):
            return True
        else:
            return False
        