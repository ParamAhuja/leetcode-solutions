# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""can be done iteratively or recursively

iterative method given:
update next pointer to point backwards
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev = None
        ahead = head.next


        while(ahead):
            head.next = prev
            prev = head
            head = ahead
            ahead = head.next
        head.next = prev


        return head
