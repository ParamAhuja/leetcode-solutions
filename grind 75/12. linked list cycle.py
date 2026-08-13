"""
slow fast method
other method is Floyd’s cycle-finding algorithm # todo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hist = []

        # while(head):
        #     if head in hist:
        #         return True
        #     hist.append(head)
        #     head = head.next
        # return False

        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow!=fast:
                slow=slow.next
                fast = fast.next.next
            else:
                return True
        return False


