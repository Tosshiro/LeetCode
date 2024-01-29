'''
Description
LeetCode solution to 21. Merge Two Sorted Lists

@author: Jw
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a tmp node to avoid edge case
        tmp = ListNode()
        cur = tmp

        while list1 and list2:
            if list1.val < list2.val:
                # Add the smaller node value to the tmp linked list
                cur.next = list1
                # Update linked list(Move to next node)
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            # Update tail
            cur = cur.next

        # The while loop can break when one list is empty while the other list still has nodes
        # Check if list 1 is empty or not
        if list1:
            # If not empty, append remaining nodes
            cur.next = list1

        # Same for list 2
        if list2:
            cur.next = list2

        return tmp.next  # .next to avoid the tmp node