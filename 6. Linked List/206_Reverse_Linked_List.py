'''
Description
LeetCode solution to 206. Reverse Linked List

@author: Jw
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None

        # When cur reach end of linked list and becomes None, break
        while cur:
            # Set a temp variable
            tmp = cur.next
            # Let Node point backwards to reverse list
            cur.next = prev
            # Update cur and prev values
            prev = cur
            cur = tmp

        return prev 